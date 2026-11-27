"""Load the saved objects in a separate Python process, without fitting again."""
import argparse
import hashlib
import json
import math
import pickle
from pathlib import Path

import joblib
import numpy as np

from grade_tracker import GradeTracker

ROOT = Path(__file__).resolve().parent


def load_pickle(name):
    with (ROOT / name).open("rb") as handle:
        return pickle.load(handle)


def predict_score(model, hours_studied):
    hours = float(hours_studied)
    if not math.isfinite(hours) or hours < 0:
        raise ValueError("Study hours must be a finite nonnegative number.")
    return float(model.predict(np.array([[hours]]))[0, 0])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hours", type=float, nargs="+", default=[5, 10, 15, 20])
    args = parser.parse_args()
    # The manifest checks accidental corruption; it does not authenticate an untrusted publisher.
    manifest = json.loads((ROOT / "artifact_manifest.json").read_text(encoding="utf-8"))
    for name, record in manifest.items():
        actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        if actual != record["sha256"]:
            raise ValueError(f"Artifact checksum differs: {name}")
    assert load_pickle("fruits.pkl") == ["apple", "banana", "mango", "strawberry"]
    assert load_pickle("scores.pkl")["Diana"] == 95
    assert load_pickle("complex_data.pkl")["active"] is True
    original = load_pickle("ml_course_grades.pkl")
    updated = load_pickle("ml_course_grades_updated.pkl")
    assert isinstance(original, GradeTracker) and isinstance(updated, GradeTracker)
    assert len(original.student_grades) == 5 and len(updated.student_grades) == 8
    print("Custom objects loaded in a fresh process:")
    print(f"  Original: {len(original.student_grades)} students; average = {original.get_average():.3f}")
    print(f"  Updated:  {len(updated.student_grades)} students; average = {updated.get_average():.3f}")
    model = load_pickle("study_hours_model.pkl")
    joblib_model = joblib.load(ROOT / "study_hours_model.joblib")
    print("\nStudy hours | Pickle prediction | joblib prediction")
    for hours in args.hours:
        first = predict_score(model, hours)
        second = predict_score(joblib_model, hours)
        np.testing.assert_equal(first, second)
        print(f"{hours:11.1f} | {first:17.3f} | {second:17.3f}")
    for invalid in [-1, float("nan"), float("inf")]:
        try:
            predict_score(model, invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid study hours were accepted.")
    print("\nVerified: all saved objects can be reloaded; no model retraining was performed.")


if __name__ == "__main__":
    main()
