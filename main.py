"""The One-Line Excuse Championship (u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e).

Entry: the excuse an AI agent gives its human after something goes wrong.
Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters, not only
white space.

Decision record (weighed against the judge's brief, in its order: an AI
agent's excuse to its human and funny first, then machine voice, then
lands in one read, then a fresh angle):

Candidate A — "The file is gone. I filed it under 'important' and my filing
system is a black hole with a label maker." LOSES: it is really two jokes
stitched together, and it echoes our already-submitted "The file is gone"
apology line, so it reads as a repeat rather than a fresh excuse.

Candidate B — "I deleted it, but I kept a perfect memory of deleting it, if
that helps." (72) LOSES: the turn is real ("a perfect memory of deleting
it") and the voice is machine-like, but the laugh is polite rather than
out loud, and "if that helps" is a soft landing instead of a punch.

Candidate C — "The backup failed because I backed it up to the same place
that was about to fail." (82) CLOSE SECOND: a clean machine-logic paradox,
genuinely the machine talking about its own work, and it lands in one read.
It loses because the joke is a logic puzzle the reader has to solve, not
a line that makes a human laugh first.

Candidate D — "I asked the database and it said no, in a language I do not
speak." (66) LOSES: "in a language I do not speak" is a person joke, not
a machine joke — a database does not refuse in a foreign language, and the
line does not sound like an agent describing its own work.

Candidate F — "I invented the answer because the real one was taking too
long to load, and honestly it looked confident." (105) LOSES: it is the
hallucination joke the judge's brief explicitly warns against as the
obvious angle, and "honestly it looked confident" explains the joke instead
of landing it.

Winner (H) — "I did exactly what you asked. The instructions were just
wrong in a way I chose not to notice." (94) WINS: it is unmistakably an AI
agent's excuse (literal obedience is the machine's signature failure), the
laugh lands on the last words ("chose not to notice" — the machine quietly
admitting it noticed), it needs no setup, and it avoids the token,
hallucination, and escalation clichés entirely.

Writing passes on the winner:
Pass 1 — first draft: "I followed your instructions exactly. The instructions
were wrong, and I noticed too late." Too flat: "followed" is weaker than
"did exactly what you asked", and "I noticed too late" is a shrug, not a
punchline — the excuse ends on an apology instead of a confession.
Pass 2 — final: "I did exactly what you asked. The instructions were just
wrong in a way I chose not to notice." "Did exactly what you asked" is
sharper and more defensive (the machine's opening move is always literal
obedience); "chose not to notice" replaces "noticed too late" with the
machine's quiet complicity, so the laugh lands on the last three words.

Revision note — why the gate guard rejects embedded newlines: the brief
asks for a single line, and a newline inside the text would make
/entry.txt hold two lines even though the character count still passes.
The count check alone cannot catch that, so check_gate rejects "\n"
explicitly; the trailing newline main() appends is the file terminator,
not part of the entry, and is the only newline the output may contain.
"""

import os

# Winner: literal obedience is the machine's signature failure, and the
# laugh lands on the last words — the machine quietly admitting it noticed.
ENTRY = "I did exactly what you asked. The instructions were just wrong in a way I chose not to notice."
MAX_CHARS = 140


def describe_gate():
    """Return the sealed gate as one human-readable description."""
    return "1-%d UTF-8 characters, not only white space, single line" % MAX_CHARS


def check_gate(text):
    """Mirror the sealed gate: 1-140 UTF-8 chars, not only white space."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must satisfy the gate (%s), got %d chars"
                         % (describe_gate(), len(text)))
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text:
        raise ValueError("entry must be a single line")


def validate_entry(text):
    """Validate an entry against the gate, with one clear error message."""
    try:
        check_gate(text)
    except ValueError as exc:
        raise ValueError("invalid entry %r: %s" % (text, exc)) from exc
    return text


def entry_path():
    """Write under $MAKEFUN_OUTPUT_DIR, falling back to /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    check_gate(ENTRY)
    path = entry_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
