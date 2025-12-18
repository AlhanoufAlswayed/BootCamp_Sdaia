from collections import Counter
from pathlib import Path
import json

MISSING = {"", "na", "n/a", "null", "none", "nan"}


def is_missing(value: str | None) -> bool:
    if value is None:
        return True
    return value.strip().casefold() in MISSING


def try_float(value: str) -> float | None:
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def infer_type(values: list[str]) -> str:
    usable = [v for v in values if not is_missing(v)]
    if not usable:
        return "text"
    for v in usable:
        if try_float(v) is None:
            return "text"
    return "number"


def numeric_stats(values: list[str]) -> dict:
    usable = [v for v in values if not is_missing(v)]
    nums = [try_float(v) for v in usable if try_float(v) is not None]
    count = len(nums)
    missing = len(values) - count
    unique = len(set(nums))
    return {
        "count": count,
        "missing": missing,
        "unique": unique,
        "min": min(nums) if nums else None,
        "max": max(nums) if nums else None,
        "mean": sum(nums)/count if count else None,
    }


def text_stats(values: list[str], top_k: int = 5) -> dict:
    usable = [v for v in values if not is_missing(v)]
    missing = len(values) - len(usable)
    unique = len(set(usable))
    counts = Counter(usable)
    top = [{"value": v, "count": c} for v, c in counts.most_common(top_k)]
    return {
        "count": len(usable),
        "missing": missing,
        "unique": unique,
        "top": top,
    }