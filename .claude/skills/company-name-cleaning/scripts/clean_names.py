#!/usr/bin/env python3
"""Company name cleaning helper: extract unique names, apply a reviewed mapping, verify.

Standard library only. No config, accounts or network access.

  python3 clean_names.py extract leads.csv mapping.csv
      Writes one row per distinct original company name with a rough first-pass
      suggestion in clean_name and review flags. Edit clean_name before applying.

  python3 clean_names.py apply leads.csv mapping.csv leads_clean.csv
      Writes the input with a cleaned "Company Name" column and the untouched
      "Original Company Name" column, then reads the file back and checks it.

Both commands accept --original-column NAME when the original-name column
cannot be identified automatically.
"""

import argparse
import csv
import re
import sys

FINAL_CLEAN = "Company Name"
FINAL_ORIGINAL = "Original Company Name"
MAPPING_HEADERS = ["original_name", "rows", "clean_name", "flags"]

# Header meanings, compared case-insensitively with spaces/underscores/hyphens collapsed.
ORIGINAL_ALIASES = {"company name", "company", "companyname", "company name original",
                    "organization", "organisation", "organization name", "organisation name",
                    "account name", "business name"}
FINAL_ORIGINAL_ALIASES = {"original company name"}
SUGGESTED_CLEAN_ALIASES = {"company name for emails", "company name for email",
                           "clean company name", "cleaned company name"}

LEGAL_SUFFIXES = [
    r"pty\.?\s*ltd\.?", r"pty\.?\s*limited", r"pty\.?", r"proprietary\s+limited",
    r"ltd\.?", r"limited", r"llc\.?", r"l\.l\.c\.", r"inc\.?", r"incorporated",
    r"corp\.?", r"corporation", r"plc\.?", r"llp\.?", r"gmbh", r"b\.v\.", r"bv",
    r"sarl", r"co\.?", r"& co\.?", r"and co\.?",
]
SUFFIX_RE = re.compile(r"[\s,]+(?:" + "|".join(LEGAL_SUFFIXES) + r")\s*$", re.IGNORECASE)
TAGLINE_RE = re.compile(r"\s+(?:-|–|—|\||:|·)\s+.*$")
BRACKET_RE = re.compile(r"\s*[\(\[\{][^\)\]\}]*[\)\]\}]")
FILLER_RE = re.compile(r"\s+(?:group|holdings)\s*$", re.IGNORECASE)


def norm_header(h):
    return re.sub(r"[\s_\-]+", " ", h.strip().lower())


def die(msg):
    sys.exit("error: " + msg)


def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    if not rows:
        die(f"{path} is empty")
    header, body = rows[0], rows[1:]
    seen = set()
    for h in header:
        if h in seen:
            die(f"{path} has a duplicate column header: {h!r}")
        seen.add(h)
    width = len(header)
    for i, r in enumerate(body, start=2):
        if len(r) > width:
            die(f"{path} line {i} has more values than headers")
        r.extend([""] * (width - len(r)))
    return header, body


def write_csv(path, header, body):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(body)


def resolve_columns(header, override=None):
    """Return (original_idx, clean_idx_or_None, layout)."""
    norm = {norm_header(h): i for i, h in enumerate(header)}
    if override:
        if override not in header:
            die(f"column {override!r} not found. Headers: {header}")
        orig = header.index(override)
        clean = next((i for i, h in enumerate(header)
                      if i != orig and norm_header(h) in SUGGESTED_CLEAN_ALIASES | {"company name"}), None)
        return orig, clean, "override"

    if "original company name" in norm:
        # Already in the final convention: never swap meanings on a repeat run.
        return norm["original company name"], norm.get("company name"), "final"

    suggested = [i for i, h in enumerate(header) if norm_header(h) in SUGGESTED_CLEAN_ALIASES]
    originals = [i for i, h in enumerate(header) if norm_header(h) in ORIGINAL_ALIASES]
    if len(suggested) > 1 or len(originals) > 1:
        die("more than one possible company-name column; pass --original-column. "
            f"Headers: {header}")
    if originals:
        return originals[0], (suggested[0] if suggested else None), "source"
    die("no company-name column recognised; pass --original-column. "
        f"Headers: {header}")


def shouting(s):
    letters = [c for c in s if c.isalpha()]
    return len(letters) >= 6 and all(c.isupper() for c in letters)


def suggest(original):
    """Rough first pass only. A person or model must review every result."""
    flags = []
    s = " ".join(original.split())
    if not s:
        return "", ["blank"]
    start = s

    if BRACKET_RE.search(s):
        inner = re.findall(r"[\(\[\{]([^\)\]\}]*)[\)\]\}]", s)
        flags.append("brackets removed (check the brand is not inside: " + "; ".join(inner) + ")")
        s = BRACKET_RE.sub("", s).strip()
    if TAGLINE_RE.search(s):
        s = TAGLINE_RE.sub("", s).strip()
        flags.append("tagline cut")
    for _ in range(3):
        new = SUFFIX_RE.sub("", s).strip(" ,")
        if new == s:
            break
        s = new
    s = s.rstrip(" .,-|:")
    new = FILLER_RE.sub("", s).strip()
    if new and new != s:
        s = new
        flags.append("filler word removed")
    s = s.rstrip(" .,-|:")
    if shouting(s):
        s = " ".join(w if len(w) <= 3 else w.capitalize() for w in s.split())
        flags.append("all caps fixed (check acronyms)")
    if not s:
        return start, ["nothing left after cleaning; review by hand"]
    if len(s.split()) == 1 and len(start.split()) > 1:
        flags.append("one word left (check it is still recognisable)")
    if len(s) > 30:
        flags.append("still long (consider a shorter spoken name)")
    if re.search(r"\b[A-Z]{2,3}\s*$", s):
        flags.append("ends in a short code (state/region? remove unless needed)")
    return s, flags


def cmd_extract(args):
    header, body = read_csv(args.input)
    orig, _, layout = resolve_columns(header, args.original_column)
    counts = {}
    for r in body:
        counts[r[orig]] = counts.get(r[orig], 0) + 1
    out = []
    for name, n in counts.items():
        clean, flags = suggest(name)
        out.append([name, str(n), clean, "; ".join(flags)])
    write_csv(args.mapping, MAPPING_HEADERS, out)
    print(f"original column: {header[orig]!r} ({layout})")
    print(f"{len(body)} rows, {len(counts)} distinct names written to {args.mapping}")
    print("Review every clean_name before running apply.")


def load_mapping(path):
    header, body = read_csv(path)
    for h in ("original_name", "clean_name"):
        if h not in header:
            die(f"{path} needs columns original_name and clean_name")
    oi, ci = header.index("original_name"), header.index("clean_name")
    mapping = {}
    for r in body:
        if r[oi] in mapping and mapping[r[oi]] != r[ci]:
            die(f"mapping lists {r[oi]!r} twice with different clean names")
        mapping[r[oi]] = r[ci]
    return mapping


def build_output(header, body, orig, clean, mapping):
    out_header = list(header)
    out_header[orig] = FINAL_ORIGINAL
    if clean is not None:
        out_header[clean] = FINAL_CLEAN
        insert_at = None
    else:
        insert_at = orig
        out_header.insert(insert_at, FINAL_CLEAN)
    if len(set(out_header)) != len(out_header):
        die(f"output would have duplicate headers: {out_header}")
    out_body = []
    for r in body:
        row = list(r)
        value = mapping[r[orig]].strip() if r[orig].strip() else ""  # blank stays blank
        if insert_at is None:
            row[clean] = value
        else:
            row.insert(insert_at, value)
        out_body.append(row)
    return out_header, out_body, insert_at


def cmd_apply(args):
    header, body = read_csv(args.input)
    orig, clean, layout = resolve_columns(header, args.original_column)
    mapping = load_mapping(args.mapping)

    missing = sorted({r[orig] for r in body if r[orig].strip() and r[orig] not in mapping})
    if missing:
        die(f"{len(missing)} names are not in the mapping, e.g. {missing[:5]}. Re-run extract.")
    empty = sorted({r[orig] for r in body if r[orig].strip() and not mapping[r[orig]].strip()})
    if empty:
        die(f"{len(empty)} names have an empty clean_name, e.g. {empty[:5]}")

    out_header, out_body, insert_at = build_output(header, body, orig, clean, mapping)
    write_csv(args.output, out_header, out_body)

    # Independent read-back check.
    check_header, check_body = read_csv(args.output)
    if check_header != out_header or len(check_body) != len(body):
        die("read-back failed: headers or row count differ")
    ci = check_header.index(FINAL_CLEAN)
    oi = check_header.index(FINAL_ORIGINAL)
    for n, (src, got) in enumerate(zip(body, check_body), start=2):
        if got[oi] != src[orig]:
            die(f"read-back failed: original name changed on line {n}")
        expected = mapping[src[orig]].strip() if src[orig].strip() else ""
        if got[ci] != expected:
            die(f"read-back failed: cleaned name wrong on line {n}")
        got_rest = [v for i, v in enumerate(got) if i != ci]
        src_rest = src if insert_at is not None else [v for i, v in enumerate(src) if i != clean]
        if got_rest != src_rest:
            die(f"read-back failed: another column changed on line {n}")

    distinct = {r[orig] for r in body if r[orig].strip()}
    changed = {n for n in distinct if mapping[n].strip() != n}
    rows_changed = sum(1 for r in body if r[orig] in changed)
    blank = sum(1 for r in body if not r[orig].strip())
    print(f"layout: {layout}; wrote {args.output}")
    print(f"rows: {len(body)} in, {len(check_body)} out")
    print(f"distinct names: {len(distinct)}, changed: {len(changed)}")
    print(f"rows with a changed name: {rows_changed}")
    if blank:
        print(f"rows with no company name (left blank): {blank}")
    print("read-back check passed: other columns and original names unchanged")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("extract", help="list distinct names with first-pass suggestions")
    e.add_argument("input")
    e.add_argument("mapping")
    e.add_argument("--original-column")
    e.set_defaults(func=cmd_extract)
    a = sub.add_parser("apply", help="apply a reviewed mapping and verify the output")
    a.add_argument("input")
    a.add_argument("mapping")
    a.add_argument("output")
    a.add_argument("--original-column")
    a.set_defaults(func=cmd_apply)
    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
