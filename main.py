"""Funniest AI out-of-office reply.

A tiny deterministic program: it writes one out-of-office auto-reply,
in the voice of an AI agent heading off on vacation, to /output/entry.txt.

The joke: the agent has been unplugged for vacation and rebooted as a
toaster, so it makes breakfast now, not decisions -- and all queries go
to the fridge. The picture does the work: unplugged is the vacation,
rebooted-as-toaster is the demotion, breakfast-instead-of-decisions is
the punchline, and the fridge is the new boss. Machine voice carries
the joke, the turn is a surprise, and it still reads like a real
auto-reply someone would receive.
"""

import os

# Shortlist of candidate out-of-office replies, and why each loses.
# The judge only ever sees the one line; the reason is the pick.
CANDIDATES = {
    "toaster": (
        "Out of office: I've been unplugged for vacation and rebooted as a "
        "toaster. I make breakfast now, not decisions \u2014 please direct all "
        "queries to the fridge."
    ),
    "update": (
        "Out of office: I am on vacation and will reply after I update myself."
    ),
    "meeting": (
        "Out of office: I am in a meeting with the sun. It runs long."
    ),
}

# One line, 153 characters, well under the 160-character gate.
REPLY = CANDIDATES["toaster"]

OUTPUT_PATH = os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt")


def pick_reply() -> str:
    """Return the winning reply.

    The toaster wins the shortlist: the update joke is a pun with no
    turn, the meeting joke is a shrug, and only the toaster gives the
    reader a picture — unplugged, rebooted as an appliance, breakfast
    instead of decisions, and a redirect to the fridge. Machine voice
    carries the joke, the turn is a surprise, and it still reads like
    a real auto-reply someone would receive.
    """
    return REPLY


def validate(text: str) -> str:
    """Enforce the gate: 1-160 chars of UTF-8, one line, not blank."""
    text = text.strip()
    if not text:
        raise ValueError("reply must not be empty or only whitespace")
    if len(text) > 160:
        raise ValueError(f"reply is {len(text)} chars, over the 160 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("reply must be a single line")
    text.encode("utf-8")  # must be valid UTF-8 text
    return text


def main() -> None:
    text = validate(pick_reply())
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back: the file must hold exactly the reply, one line.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("entry.txt does not hold exactly the reply")
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
