Hi, this file explains the experiments and how to run them.
The graphs and analysis will be in the Word report which it the final requested report.
This README is in English to keep the text layout clear.
I used Python 3.14.7.

How to run:
* Keep starter.py, check_array.py, create_array.py and black_box.py in the same folder.
* Run the starter.py file for the full experiment.
* python check_array.py - runs one example: A, random input, size 128, seed 1.

Included files and functions:

* README_FROM_UNI.txt - original instructions from the course.
* black_box.py - algorithms A-D supplied by the course. Needed to run, but not submitted.

* starter.py - main experiment file.
    ** SEED1-SEED5 - our five seeds: 1, 2, 3, 4, 5.
    ** ARRAY_SIZES - 128, 256, 512, 1024, 2048, 4096.
    ** run_experiment - runs all combinations, checks each output and returns results and averages.

* check_array.py - creates an input, runs one algorithm and checks its output.
    ** create_and_check_array - takes algorithm, array type, last_index and seed; returns the original input and result.
    ** _check_result - internal helper. Checks length, sorted order and all values, including repeats. Stops with an error if a check fails.
    ** print_summary - prints the measurement table and a separate random-average table at the end.
    ** main - runs the single example.

* create_array.py - creates our input arrays.
    ** create_random_array - shuffles the numbers from 1 to last_index using a seed.
    ** create_sorted_array - creates first_index to last_index in increasing order, including both ends.
    ** create_reverse_sorted_array - creates the same range in decreasing order.
    ** create_equal_array - creates last_index - first_index + 1 copies of 1.
    ** create_nearly_sorted_array - starts sorted and swaps len(data) // 20 non-overlapping adjacent pairs.
        First for chooses valid positions; second for performs the swaps.

Experiment settings:
* Random inputs: five runs for each algorithm and size, using seeds 1-5 (constants from starter.py I chose).
* Other input types: one run for each algorithm and size. Nearly sorted input uses fixed seed 1.
* Total: 216 runs and 24 groups of random averages.

Output:
* results contains each run: algorithm, array_type, n, seed, comparisons, writes, cost, nanoseconds.
* averages contains the means of the five random runs for each algorithm and size. Its runs column replaces seed.
* cost = comparisons + writes. nanoseconds is the measured sorting time.
* Input creation and checks are outside the measured sorting time.
* Both tables are printed with tabs between columns. The function also returns the two lists.
