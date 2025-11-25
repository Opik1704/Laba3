import time
from Laba3.src.sorting import factorial_easy
from Laba3.src.sorting import factorial_tree
from Laba3.src.sorting import factorial_recursive
from Laba3.src.sorting import fibonaci
from Laba3.src.sorting import fibonaci_recursive

from Laba3.src.sorting import bubble_sort
from Laba3.src.sorting import quick_sort
from Laba3.src.sorting import counting_sort
from Laba3.src.sorting import radix_sort
from Laba3.src.sorting import bucket_sort
from Laba3.src.sorting import heap_sort

from Laba3.src.testcase import rand_int_array
from Laba3.src.testcase import nearly_sorted
from Laba3.src.testcase import many_duplicates
from Laba3.src.testcase import rand_float_array
from Laba3.src.testcase import reverse_sorted


def timeit_once(func, *args, **kwargs):
    """Измеряет время функции """
    start = time.perf_counter()
    func(*args, **kwargs)
    finish = time.perf_counter()
    return finish - start


def benchmark_sorts(arrays, algorithms):
    """Запускает бенчмарк"""
    results = {}
    for array_name, array in arrays.items():
        results[array_name] = {}
        for algorithm_name, algorithm_function in algorithms.items():
            array = array.copy()
            if algorithm_name == "Radix Sort":
                time_taken = timeit_once(algorithm_function, array, 10)
            elif algorithm_name == "Bucket Sort":
                time_taken = timeit_once(algorithm_function, array, 10)
            else:
                time_taken = timeit_once(algorithm_function, array)
            results[array_name][algorithm_name] = time_taken
    return results

def print_results(results):
    """Выводит результаты """
    alg_names = list(next(iter(results.values())))
    print()
    print(f"{'Тип массива':<25}", end="")
    for alg in alg_names:
        print(f"{alg:<10}", end="")
    print(12 * len(alg_names),"AA")

    for array_name, algo_times in results.items():
        print(f"{array_name:<25}", end="")
        for alg_name in alg_names:
            time = algo_times[alg_name]
            print(f"{time:.6f}  ", end="")
        print()

def main():
    arrays_small = {
        "Случайные": rand_int_array(100, 1, 100, seed=42),
        "Почти отсортированный ": nearly_sorted(100, 10, seed=42),
        "Дубликаты ": many_duplicates(100, 5, seed=42),
        "Обратные ": reverse_sorted(100),
    }
    arrays_medium = {
        "Случайные": rand_int_array(1000, 1, 100, seed=42),
        "Почти отсортированный ": nearly_sorted(100, 25, seed=42),
        "Дубликаты ": many_duplicates(1000, 55, seed=42),
        "Обратные ": reverse_sorted(1000),
    }
    arrays_big = {
        "Случайные": rand_int_array(5000, 1, 100, seed=42),
        "Почти отсортированный ": nearly_sorted(5000, 52, seed=42),
        "Дубликаты ": many_duplicates(5000, 250, seed=42),
        "Обратные ": reverse_sorted(5000),
    }
    alg = {
        "Bubble": bubble_sort,
        "Quick": quick_sort,
        "Counting": counting_sort,
        "Radix": radix_sort,
        "Bucket": bucket_sort,
        "Heap": heap_sort,
    }

    results_small = benchmark_sorts(arrays_small, alg)
    results_medium = benchmark_sorts(arrays_medium, alg)
    results_big = benchmark_sorts(arrays_big, alg)

    print_results(results_small)
    print_results(results_medium)
    print_results(results_big)

if __name__ == "__main__":
    main()