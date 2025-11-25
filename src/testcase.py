import random

def rand_int_array(n: int, lo: int, hi: int,seed: int) -> list[int]:
    """
        Генерирует массив случайных целых чисел и возвращает его
        Получ
    """
    random_list = []
    if seed:
        random.seed(seed)
        for i in range(n):
            random_list.append(random.randint(lo, hi))
    else:
        for i in range(n):
            random_list.append(random.randint(lo, hi))
    return random_list

def nearly_sorted(n: int,swaps: int,seed: int):
    """
        Генерирует почти отсортированный массив и возвращает его
    """
    sort_list = [x for x in range(n)]
    if seed:
        random.seed(seed)
        for i in range(swaps):
            el_1 = random.randint(1, n - 1)
            el_2 = random.randint(1,  n - 1)
            while el_1 == el_2:
                el_2 = random.randint(1, n)
            sort_list[el_1], sort_list[el_2] = sort_list[el_2], sort_list[el_1]
    else:
        for i in range(swaps):
            el_1 = random.randint(1, n)
            el_2 = random.randint(1, n)
            while el_1 == el_2:
                el_2 = random.randint(1, n)
            sort_list[el_1], sort_list[el_2] = sort_list[el_2], sort_list[el_1]
    return sort_list

def many_duplicates(n: int, k_unique: int, seed=None):
    """
        Генерирует массив с определенным количеством дупликатов и возвращает его
    """
    if seed :
        random.seed(seed)
    if k_unique <= 0:
        raise ValueError("k_unique должен быть натуральным")
    unique_values = list(range(1, k_unique + 1))

    return [random.choice(unique_values) for n in range(n)]

def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None):
    """
        Генерирует массив случайных дробных чисел и возвращает его
    """
    random_list = []
    if seed:
        random.seed(seed)
        for i in range(n):
            random_list.append(random.uniform(lo, hi))
    else:
        for i in range(n):
            random_list.append(random.uniform(lo, hi))
    return random_list

def reverse_sorted(n: int):
    """
    Генерирует обратно отсортированный массив и возвращает его
    """
    return list(range(n, 0, -1))