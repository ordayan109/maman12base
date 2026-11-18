from check_array import create_and_check_array, print_summary

SEED1 = 1
SEED2 = 2
SEED3 = 3
SEED4 = 4
SEED5 = 5
ARRAY_SIZES = [128,256,512,1024,2048,4096]

"""
run() returns a result with 4 fields:
values - the sorted array
comparisons - number of comparisons between array values
writes - number of writes to the array and helper arrays
nanoseconds - sorting time in nanoseconds
"""


def run_experiment():
    algorithms = ["A", "B", "C", "D"]
    array_types = ["random", "sorted", "reverse_sorted", "equal", "nearly_sorted"]
    seeds = [SEED1, SEED2, SEED3, SEED4, SEED5]
    results = []
    averages = []
    error = None

    try:
        for array_type in array_types:
            if array_type == "random":
                run_seeds = seeds
            else:
                run_seeds = [SEED1]

            for size in ARRAY_SIZES:
                for algorithm in algorithms:
                    total_comparisons = 0
                    total_writes = 0
                    total_cost = 0
                    total_nanoseconds = 0

                    for seed in run_seeds:
                        data, result = create_and_check_array(algorithm, array_type, size, seed)
                        cost = result.comparisons + result.writes

                        results.append({
                            "algorithm": algorithm,
                            "array_type": array_type,
                            "n": size,
                            "seed": seed,
                            "comparisons": result.comparisons,
                            "writes": result.writes,
                            "cost": cost,
                            "nanoseconds": result.nanoseconds,
                        })

                        total_comparisons += result.comparisons
                        total_writes += result.writes
                        total_cost += cost
                        total_nanoseconds += result.nanoseconds

                    if array_type == "random":
                        average = {
                            "algorithm": algorithm,
                            "array_type": array_type,
                            "n": size,
                            "runs": len(run_seeds),
                            "comparisons": total_comparisons / len(run_seeds),
                            "writes": total_writes / len(run_seeds),
                            "cost": total_cost / len(run_seeds),
                            "nanoseconds": total_nanoseconds / len(run_seeds),
                        }
                        averages.append(average)
    except Exception as exception:
        error = f"{algorithm}, {array_type}, n={size}, seed={seed}: {exception}"
        raise
    finally:
        print_summary(results, averages, error)

    return results, averages


if __name__ == "__main__":
    results, averages = run_experiment()
