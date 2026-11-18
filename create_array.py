import random


def create_random_array(last_index, seed):
    first_index=1
    data = list(range(first_index, last_index + 1))
    rng = random.Random(seed)
    rng.shuffle(data)
    return data


def create_sorted_array(first_index, last_index):
    return list(range(first_index, last_index + 1))


def create_reverse_sorted_array(first_index, last_index):
    return list(range(last_index, first_index - 1, -1))


def create_equal_array(first_index, last_index):
    return [1] * (last_index - first_index + 1)


def create_nearly_sorted_array(first_index, last_index, seed):
    data = create_sorted_array(first_index, last_index)
    rng = random.Random(seed)
    number_of_swaps = len(data) // 20

    possible_positions = list(range(len(data) - 1))
    rng.shuffle(possible_positions)

    used_positions = set()
    swap_positions = []

    # Choose non-overlapping positions.
    for left in possible_positions:
        if len(swap_positions) == number_of_swaps:
            break

        right = left + 1

        if left in used_positions or right in used_positions:
            continue

        swap_positions.append(left)
        used_positions.add(left)
        used_positions.add(right)

    # Swap the chosen  pairs.
    for left in swap_positions:
        right = left + 1
        data[left], data[right] = data[right], data[left]

    return data
