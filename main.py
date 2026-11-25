#!/usr/bin/env python3
"""The Best Meal You Ever Had — one sentence about the best meal.

The sentence is one memory, told in one breath. It names the dish
(soto ayam), the place (a street cart in Yogyakarta), the hour (2 a.m.)
and two sensory details that only someone who was there would remember:
broth hot enough to fog glasses, a tongue burned on the first spoon.
The ending is the turn — the burn did not stop anything, a second bowl
was ordered anyway — which is how the reader knows, without being told,
that this was the best meal. No general praise, no cliche, just the
moment itself.

Deterministic: the same sentence is written on every run.
"""

import os

SENTENCE = (
    "The best meal I ever had was soto ayam from a street cart "
    "in Yogyakarta at 2 a.m., the broth so hot it fogged my glasses, "
    "and I burned my tongue and ordered another bowl anyway."
)


# The gate only accepts 1-200 characters: fail loudly here instead of
# shipping an invalid entry.
assert 1 <= len(SENTENCE) <= 200, (
    f"entry is {len(SENTENCE)} chars, gate wants 1-200")


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(f"Wrote {len(SENTENCE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
