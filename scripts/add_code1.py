"""
add_code1.py — First-cycle qualitative coding for thesis interview data
=======================================================================

Reads the source interview transcript CSV, applies inductive first-cycle
multi-label qualitative coding to the ``response_text`` column for all
meaningful rows (athletes and coaches), and writes a new coded CSV with an
appended ``code_1`` column.

Usage
-----
From the repository root::

    python scripts/add_code1.py

Requirements
------------
    pip install pandas

Inputs / outputs
----------------
* Input  : ``data/INTERVIEW_TRANSCRIPT_FINAL - INTERVIEW_TRANSCRIPT_2026.csv``
* Output : ``data/INTERVIEW_TRANSCRIPT_FINAL - INTERVIEW_TRANSCRIPT_2026_coded.csv``

The output file preserves **all** original columns and values in the same
order.  A new column ``code_1`` is appended as the last column.

Coding rules
------------
Codes are semicolon-separated (max 4 per row).  See
``reports/codebook_code_1.md`` for definitions and examples.

Blank separator rows (rows where all fields are empty) keep ``code_1``
blank.  Rows whose ``response_text`` is empty or exactly "no answer"
(case-insensitive) also receive a blank ``code_1``.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import pandas as pd

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
INPUT_CSV = REPO_ROOT / "data" / "INTERVIEW_TRANSCRIPT_FINAL - INTERVIEW_TRANSCRIPT_2026.csv"
OUTPUT_CSV = REPO_ROOT / "data" / "INTERVIEW_TRANSCRIPT_FINAL - INTERVIEW_TRANSCRIPT_2026_coded.csv"

# ---------------------------------------------------------------------------
# Code priority order (used to consistently order multi-label output)
# ---------------------------------------------------------------------------
CODE_PRIORITY: list[str] = [
    "motivation_reward",
    "cost_access_barrier",
    "inclusion_retention",
    "trust_safety",
    "scam_risk",
    "hygiene_quality_concern",
    "fairness_reciprocity",
    "app_preference",
    "face_to_face_preference",
    "social_comfort_team",
    "social_comfort_broad",
    "reuse_sustainability",
    "logistics_exchange",
    "competition_pressure",
    "community_support",
    "positive_acceptance",
    "negative_or_skeptical",
    "other_contextual",
]

# ---------------------------------------------------------------------------
# Keyword rules (applied to normalised response text)
# ---------------------------------------------------------------------------
# Each entry maps a code label to a list of substring patterns.
# Matching is case-insensitive after normalisation.
KEYWORD_RULES: dict[str, list[str]] = {
    "motivation_reward": [
        "motivat", "reward", "token", "points", "earn", "incentive",
        "encourage", "keep playing", "keep replying", "get good rewards",
        "excited to come", "come to training", "goal", "prize",
    ],
    "app_preference": [
        "through the app", "use the app", "use app", "via app",
        "platform", "digital platform", "welloop", "phone",
        "app makes", "app will", "app for", "app-",
    ],
    "face_to_face_preference": [
        "face to face", "in person", "at practice", "at training",
        "when we train", "during training", "physically meet",
        "at the game", "meet them", "meetup", "meet up",
    ],
    "trust_safety": [
        "trust", "safe", "safety", "secure", "bank id", "bankid",
        "verification", "verified", "phone number", "identity",
        "know the person", "know who", "anonymous", "private",
        "rely on", "relying on", "reliable",
    ],
    "scam_risk": [
        "scam", "fraud", "fake", "different picture", "not what",
        "lie about", "bug", "misuse", "abuse", "wrong item",
        "not as described", "deceiv",
    ],
    "hygiene_quality_concern": [
        "hygiene", "sanitary", "sanitation", "smell", "smells",
        "dirty", "quality", "condition", "too worn", "worn out",
        "washed", "wash", "clean", "not hygienic",
    ],
    "fairness_reciprocity": [
        "fair", "unfair", "give back", "contribute", "not contributing",
        "only take", "free rider", "free-rider", "everyone put in",
        "take without", "share equally", "not fair",
        "who does not give", "if they don't give",
    ],
    "social_comfort_team": [
        "same team", "my team", "teammate", "people i know",
        "know them", "friends", "comfortable with", "within the team",
        "inside the team", "my friends", "already know",
    ],
    "social_comfort_broad": [
        "other team", "other club", "anyone", "does not matter",
        "doesn't matter", "would not care", "wouldn't care",
        "both", "everyone", "all people", "don't care who",
        "i wouldn't mind", "i don't mind",
    ],
    "cost_access_barrier": [
        "money", "afford", "expensive", "cost", "financial",
        "economic", "can't buy", "cannot buy", "not enough money",
        "low income", "single parent", "hard life", "budget",
        "price", "training fee", "membership fee", "annual fee",
        "can't pay", "cannot pay",
        "struggling", "rents", "food", "less privilege",
    ],
    "inclusion_retention": [
        "stay", "quit", "drop", "dropout", "retention",
        "keep playing", "continue playing", "start sport", "start playing",
        "leave football", "leave basketball", "leave the sport",
        "stay in sport", "leave sport", "keep kids", "stop playing",
        "remains in", "gymnasium", "new school",
    ],
    "reuse_sustainability": [
        "reuse", "recycle", "second hand", "secondhand",
        "second-hand", "used product", "used item", "used shoe",
        "give away", "pass down", "not throw", "throw away",
        "environment", "sustainable", "selling used", "buy used",
        "old equipment", "old shoes",
    ],
    "logistics_exchange": [
        "delivery", "deliver", "post office", "shipping", "shipment",
        "size", "description", "rules", "communication", "how to exchange",
        "exchange process", "shoes", "boots", "chin pad", "shin guard",
        "shin pad", "glove", "hoodie", "clothes", "equipment",
        "gear", "items", "backpack",
    ],
    "competition_pressure": [
        "pressure", "pressuri", "competitive", "competition",
        "leaderboard", "compare", "comparison", "statistics",
        "ranking", "compare token", "who has more token",
        "healthy competition", "unhealthy competition",
        "compete with each other", "competi",
    ],
    "community_support": [
        "help", "support", "good cause", "community", "assist",
        "give to others", "help others", "solidarity", "welfare",
        "help the team", "united", "together", "give each other",
        "care about", "look out for", "check in",
    ],
    "negative_or_skeptical": [
        "don't know", "dont know", "not sure", "maybe not",
        "won't work", "would not work", "hard to", "difficult",
        "unnecessary", "no need", "no i don't", "probably not",
        "i doubt", "i'm not sure", "i'm skeptical", "unclear",
        "not confident", "not convinced", "too much app",
        "i cannot answer", "not in this team",
    ],
    "positive_acceptance": [
        "good idea", "great idea", "amazing", "of course",
        "sounds good", "would work", "i think it's good",
        "i think it is good", "good thing", "great thing",
        "makes sense", "very good", "really good", "cool idea",
        "works well", "comfortable with", "i'm comfortable",
        "i am comfortable", "i would be comfortable", "happy with",
        "that's good", "that is good",
    ],
}

# ---------------------------------------------------------------------------
# Question-aware fallback codes
# These are applied when keyword matching yields nothing meaningful.
# They represent the primary theme of each question in the interview guide.
# ---------------------------------------------------------------------------
QUESTION_FALLBACKS: dict[str, list[str]] = {
    # Kids questions
    "Q_Warmup":         ["other_contextual"],
    "Q1_Kids":          ["positive_acceptance"],
    "Q2_Kids":          ["motivation_reward"],
    "Q3_Kids":          ["reuse_sustainability", "social_comfort_team"],
    "Q4_Kids":          ["logistics_exchange"],
    "Q5_Kids":          ["logistics_exchange", "hygiene_quality_concern"],
    "Q6_Kids":          ["app_preference", "face_to_face_preference"],
    "Q7_Kids":          ["social_comfort_broad", "fairness_reciprocity"],
    "Q8_Kids":          ["social_comfort_team", "social_comfort_broad"],
    "Q9_Kids":          ["fairness_reciprocity", "community_support"],
    "Q10_Kids":         ["reuse_sustainability"],
    "Q11_Kids":         ["inclusion_retention", "cost_access_barrier"],
    "Q12_Kids":         ["inclusion_retention", "cost_access_barrier"],
    "Q13_Kids":         ["app_preference", "positive_acceptance"],
    "Additional_Q_Kids":["other_contextual"],
    # Coach questions
    "Q1_Coach":         ["inclusion_retention", "cost_access_barrier"],
    "Q2_Coach":         ["cost_access_barrier", "inclusion_retention"],
    "Q3_Coach":         ["community_support", "social_comfort_team"],
    "Q4_Coach":         ["logistics_exchange"],
    "Q5_Coach":         ["reuse_sustainability", "logistics_exchange"],
    "Q6_Coach":         ["logistics_exchange", "social_comfort_team"],
    "Q7_Coach":         ["app_preference", "community_support"],
    "Q8_Coach":         ["competition_pressure", "trust_safety"],
    "Q9_Coach":         ["motivation_reward", "fairness_reciprocity"],
    "Q10_Coach":        ["competition_pressure", "inclusion_retention"],
    "Q11_Coach":        ["trust_safety", "social_comfort_team"],
    "Q12_Coach":        ["negative_or_skeptical"],
    "Q13_Coach":        ["app_preference", "reuse_sustainability"],
    "Q14_Coach":        ["hygiene_quality_concern", "scam_risk"],
    "Q15_Coach":        ["inclusion_retention", "community_support"],
    "Q16_Coach":        ["logistics_exchange", "app_preference"],
}

# ---------------------------------------------------------------------------
# Short affirmative / negative patterns that override keyword rules
# ---------------------------------------------------------------------------
AFFIRMATIVE = {"yes", "yeah", "yep", "yup", "sure", "absolutely", "of course",
               "ofcourse", "yess", "yah"}
NEGATIVE = {"no", "nope", "not really", "i don't know", "dont know",
            "i dont know", "no idea"}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def normalise(text: str | float) -> str:
    """Lowercase, collapse whitespace, strip."""
    if pd.isna(text):
        return ""
    return re.sub(r"\s+", " ", str(text).strip().lower())


def is_blank_separator_row(row: pd.Series) -> bool:
    """Return True when the row is a blank separator (all fields empty)."""
    return all(str(v).strip() == "" for v in row)


def should_skip_coding(text_norm: str) -> bool:
    """Return True when response_text is empty or exactly 'no answer'."""
    return text_norm == "" or text_norm == "no answer"


def apply_keyword_rules(text_norm: str) -> set[str]:
    """Return the set of codes whose keywords appear in text_norm."""
    codes: set[str] = set()
    for code, keywords in KEYWORD_RULES.items():
        if any(kw in text_norm for kw in keywords):
            codes.add(code)
    return codes


def apply_short_reply_rules(text_norm: str) -> set[str]:
    """Handle very short affirmative/negative replies."""
    codes: set[str] = set()
    if text_norm in AFFIRMATIVE:
        codes.add("positive_acceptance")
    elif text_norm in NEGATIVE:
        codes.add("negative_or_skeptical")
    return codes


def build_code1(row: pd.Series) -> str:
    """
    Derive the ``code_1`` label string for a single data row.

    Returns a semicolon-separated string of 1–4 codes, or an empty string
    when the row should not be coded.
    """
    if is_blank_separator_row(row):
        return ""

    text_raw: str = str(row.get("response_text", "") or "")
    text_norm: str = normalise(text_raw)
    question_key: str = normalise(row.get("question_key", "") or "")

    if should_skip_coding(text_norm):
        return ""

    codes: set[str] = set()

    # 1) Keyword-based matching
    codes |= apply_keyword_rules(text_norm)

    # 2) Short reply override
    codes |= apply_short_reply_rules(text_norm)

    # 3) Question-aware fallback: if no codes found yet, use question theme
    if not codes and question_key:
        # Reconstruct original capitalisation for lookup
        qk_original = str(row.get("question_key", "") or "").strip()
        fallbacks = QUESTION_FALLBACKS.get(qk_original, [])
        codes.update(fallbacks)

    # 4) Ultimate fallback: generic label
    if not codes:
        codes.add("other_contextual")

    # 5) Suppress over-broad logistics code when more specific codes present
    # (logistics_exchange from shoe/gear keywords fires on Q4/Q5 by design,
    #  but elsewhere it should not dominate)
    specific_codes = codes - {"logistics_exchange", "other_contextual"}
    if specific_codes and "logistics_exchange" in codes:
        # Keep logistics only if it was triggered by a logistics keyword
        # *other* than bare gear/item names — heuristic: keep it alongside
        # other specific codes rather than removing it completely.
        pass  # keep both; priority ordering will limit to 4 anyway

    # 6) Order by priority and cap at 4 codes
    ordered = [c for c in CODE_PRIORITY if c in codes]
    # Any codes not in priority list (shouldn't happen, but safeguard)
    ordered += [c for c in sorted(codes) if c not in CODE_PRIORITY]
    ordered = ordered[:4]

    return "; ".join(ordered)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    if not INPUT_CSV.exists():
        print(f"ERROR: Input file not found: {INPUT_CSV}", file=sys.stderr)
        sys.exit(1)

    print(f"Reading: {INPUT_CSV}")
    df = pd.read_csv(INPUT_CSV, dtype=str, keep_default_na=False)

    print(f"  {len(df)} rows, {len(df.columns)} columns")
    print(f"  Columns: {list(df.columns)}")

    # Apply coding row by row
    df["code_1"] = df.apply(build_code1, axis=1)

    # Diagnostics
    coded_count = (df["code_1"].str.strip() != "").sum()
    blank_sep = (df.apply(is_blank_separator_row, axis=1)).sum()
    print(f"  Blank separator rows : {blank_sep}")
    print(f"  Rows with code_1     : {coded_count} / {len(df)}")

    print(f"Writing: {OUTPUT_CSV}")
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")

    # Sanity checks
    df_check = pd.read_csv(OUTPUT_CSV, dtype=str, keep_default_na=False)
    assert len(df_check) == len(df), "Row count mismatch after writing!"
    assert "code_1" in df_check.columns, "code_1 column missing in output!"
    print("  Sanity checks passed.")
    print("Done.")


if __name__ == "__main__":
    main()
