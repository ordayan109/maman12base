"""Section D4: sorted input compared with one adjacent swap."""

import csv
from datetime import datetime
from pathlib import Path

from black_box import run
from create_array import create_sorted_array
from starter import ARRAY_SIZES
#

def run_and_check(algorithm, data, position, left_index, sorted_cost=None):
    result = run(algorithm, data.copy())

    if result.values != sorted(data):
        raise ValueError(
            f"Output check failed: {algorithm}, n={len(data)}, position={position}"
        )

    cost = result.comparisons + result.writes
    if sorted_cost is None:
        sorted_cost = cost

    # List indexes start at 0. Positions in the CSV start at 1.
    return {
        "algorithm": algorithm,
        "array_type": "sorted" if left_index is None else "single_swap",
        "n": len(data),
        "position": position,
        "swap_first": "" if left_index is None else left_index + 1,
        "swap_second": "" if left_index is None else left_index + 2,
        "comparisons": result.comparisons,
        "writes": result.writes,
        "cost": cost,
        "nanoseconds": result.nanoseconds,
        "sorted_cost": sorted_cost,
        "cost_change": cost - sorted_cost,
        "cost_ratio": cost / sorted_cost,
    }


def run_single_swap_experiment(array_sizes):
    results = []

    for size in array_sizes:
        if size < 2:
            raise ValueError("A single swap needs at least two elements.")

        positions = {
            "start": 0,
            "middle": (size - 1) // 2,
            "end": size - 2,
        }

        for algorithm in ["A", "B", "C", "D"]:
            sorted_data = create_sorted_array(1, size)
            baseline = run_and_check(algorithm, sorted_data, "none", None)
            results.append(baseline)

            for position, left_index in positions.items():
                data = sorted_data.copy()
                data[left_index], data[left_index + 1] = (
                    data[left_index + 1], data[left_index]
                )

                row = run_and_check(
                    algorithm, data, position, left_index, baseline["cost"]
                )
                results.append(row)

    return results


def save_results(results, folder):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = Path(folder) / f"section_d_results_{timestamp}.csv"

    # "x" creates a new file and never overwrites an existing file.
    with filename.open("x", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=list(results[0]))
        writer.writeheader()
        writer.writerows(results)

    return filename


def main():
    results = run_single_swap_experiment(ARRAY_SIZES)
    filename = save_results(results, Path(__file__).parent)

    print("Completed runs:", len(results))
    print("All output checks passed.")
    print("Results saved to:", filename)
    return results


if __name__ == "__main__":
    results = main()
