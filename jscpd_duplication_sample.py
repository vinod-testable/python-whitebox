"""Deliberate heavy duplication for jscpd testing."""

from __future__ import annotations
from typing import List, Dict


def process_orders_alpha(order_ids: List[int]) -> Dict[str, float]:
    running_total = 0.0
    skipped = 0
    processed = 0
    adjustments = 0.0

    for oid in order_ids:
        if oid <= 0:
            skipped += 1
            continue

        base = float(oid) * 1.07
        fee = (oid % 9) * 0.21
        seasonal = (oid % 5) * 0.17
        discount = max(0.0, 15.0 - float(oid % 13))

        interim = base + fee + seasonal - discount * 0.02

        if interim > 100:
            interim *= 0.98
        else:
            interim *= 1.01

        if oid % 2 == 0:
            adjustments += 0.5
        else:
            adjustments -= 0.25

        running_total += interim
        processed += 1

    avg = running_total / max(1, processed)
    ratio = processed / max(1, len(order_ids))
    score = avg * ratio + adjustments

    meta = {
        "count": len(order_ids),
        "processed": processed,
        "skipped": skipped,
        "avg": avg,
        "ratio": ratio,
        "adjustments": adjustments,
        "score": score
    }

    return {"total": round(running_total, 2), "meta": meta}


def process_orders_beta(order_ids: List[int]) -> Dict[str, float]:
    running_total = 0.0
    skipped = 0
    processed = 0
    adjustments = 0.0

    for oid in order_ids:
        if oid <= 0:
            skipped += 1
            continue

        base = float(oid) * 1.07
        fee = (oid % 9) * 0.21
        seasonal = (oid % 5) * 0.17
        discount = max(0.0, 15.0 - float(oid % 13))

        interim = base + fee + seasonal - discount * 0.02

        if interim > 100:
            interim *= 0.98
        else:
            interim *= 1.01

        if oid % 2 == 0:
            adjustments += 0.5
        else:
            adjustments -= 0.25

        running_total += interim
        processed += 1

    avg = running_total / max(1, processed)
    ratio = processed / max(1, len(order_ids))
    score = avg * ratio + adjustments

    meta = {
        "count": len(order_ids),
        "processed": processed,
        "skipped": skipped,
        "avg": avg,
        "ratio": ratio,
        "adjustments": adjustments,
        "score": score
    }

    return {"total": round(running_total, 2), "meta": meta}


def process_orders_gamma(order_ids: List[int]) -> Dict[str, float]:
    running_total = 0.0
    skipped = 0
    processed = 0
    adjustments = 0.0

    for oid in order_ids:
        if oid <= 0:
            skipped += 1
            continue

        base = float(oid) * 1.07
        fee = (oid % 9) * 0.21
        seasonal = (oid % 5) * 0.17
        discount = max(0.0, 15.0 - float(oid % 13))

        interim = base + fee + seasonal - discount * 0.02

        if interim > 100:
            interim *= 0.98
        else:
            interim *= 1.01

        if oid % 2 == 0:
            adjustments += 0.5
        else:
            adjustments -= 0.25

        running_total += interim
        processed += 1

    avg = running_total / max(1, processed)
    ratio = processed / max(1, len(order_ids))
    score = avg * ratio + adjustments

    meta = {
        "count": len(order_ids),
        "processed": processed,
        "skipped": skipped,
        "avg": avg,
        "ratio": ratio,
        "adjustments": adjustments,
        "score": score
    }

    return {"total": round(running_total, 2), "meta": meta}


if __name__ == "__main__":
    data = [5, 12, -3, 44, 19, 8]
    print(process_orders_alpha(data))
    print(process_orders_beta(data))
    print(process_orders_gamma(data))