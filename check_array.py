import create_array
from black_box import run


# Internal helper for this file only.
def _check_result(input_data, output_data):
    if len(input_data) != len(output_data):
        raise ValueError("Output length is different. Experiment stopped.")

    for i in range(1, len(output_data)):
        if output_data[i - 1] > output_data[i]:
            raise ValueError("Output is not sorted. Experiment stopped.")

    if sorted(input_data) != output_data:
        raise ValueError("Output does not contain exactly the input values. Experiment stopped.")


def create_and_check_array(algorithm, array_type, last_index, seed):
    if array_type == "random":
        data = create_array.create_random_array(last_index, seed)
    elif array_type == "sorted":
        data = create_array.create_sorted_array(1, last_index)
    elif array_type == "reverse_sorted":
        data = create_array.create_reverse_sorted_array(1, last_index)
    elif array_type == "equal":
        data = create_array.create_equal_array(1, last_index)
    elif array_type == "nearly_sorted":
        data = create_array.create_nearly_sorted_array(1, last_index, seed)
    else:
        raise ValueError("Unknown array type.")

    original_data = data.copy()
    result = run(algorithm, data)
    _check_result(original_data, result.values)
    return original_data, result


def print_summary(results, averages, error=None):
    print("algorithm", "array_type", "n", "seed", "comparisons", "writes", "cost", "nanoseconds", sep="\t")
    for row in results:
        print(row["algorithm"], row["array_type"], row["n"], row["seed"],
              row["comparisons"], row["writes"], row["cost"], row["nanoseconds"], sep="\t")

    if averages:
        print()
        print("Random averages")
        print("algorithm", "array_type", "n", "runs", "comparisons", "writes", "cost", "nanoseconds", sep="\t")
        for row in averages:
            print(row["algorithm"], row["array_type"], row["n"], row["runs"],
                  row["comparisons"], row["writes"], row["cost"], row["nanoseconds"], sep="\t")

    if error is not None:
        print("Error:", error)


def main():
    results = []
    error = None
    try:
        data, result = create_and_check_array("A", "random", 128, 1)
        cost = result.comparisons + result.writes
        results.append({
            "algorithm": "A",
            "array_type": "random",
            "n": 128,
            "seed": 1,
            "comparisons": result.comparisons,
            "writes": result.writes,
            "cost": cost,
            "nanoseconds": result.nanoseconds,
        })
    except Exception as exception:
        error = str(exception)
        raise
    finally:
        print_summary(results, [], error)
    return results


if __name__ == "__main__":
    results = main()
