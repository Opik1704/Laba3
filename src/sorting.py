import heapq
from sys import setrecursionlimit
setrecursionlimit(10000000)
def factorial_easy(number: int):
    """
       Вычисление факториала итеративным методом
       Получает number
       возвращает факториал числа number
    """
    if number < 0:
        raise ValueError("Факториал только для натуральнх чисел чисел")
    f = 1
    while number > 1:
        f = f * number
        number = number - 1
    return f
def factorial_tree(n:int):
    """
        Вычисление факториала методом деревьев, крутой алгоритм вррррр
        Получает number
        возвращает факториал числа number
       """
    if n < 0:
        raise ValueError("Факториал только для натуральнх чисел чисел")
    if n == 0:
        return 1
    if n == 1 or n == 2:
        return n
    return FactTree(2, n)
def FactTree(l,r):
    if  l > r:
        return 1
    if l == r:
         return l
    if (r - l == 1):
        return int(l) * r
    m = (l + r) // 2
    return FactTree(l, m) * FactTree(m + 1, r)
def factorial_recursive(n: int) -> int:
    """
        Вычисление факториала рекурсией
        Получает number
        возвращает факториал числа number
       """
    if n < 0:
        raise ValueError("Факториал только для натуральнх чисел чисел")
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
def fibonaci(n: int) -> int:
    """
    Вычисление n-го числа Фибоначчи итеративным методом
    Получает n
    Возвращает n-ое числа Фибоначчи
    """
    if n < 0:
        raise ValueError("Число Фибоначчи определено только для натуральных  чисел")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
def fibonaci_recursive(n: int) -> int:
    """
        Вычисление n-го числа Фибоначчи рекурсией
        Получает n
        Возвращает n-ое числа Фибоначчи
       """
    if n == 0:
        return 0
    if n < 0:
        raise ValueError("нет такого члена последовательности",n)
    if n == 1 or n == 2:  
        return 1
    else:  
        return (fibonaci_recursive(n-1) + fibonaci_recursive(n-2))  
def bubble_sort(arr):
    """
      Пузырьковая сортировка
      Получает массив arr
      Возвращает сортированный массив arr
      """
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if(arr[i] > arr[j]):
                c = arr[i]
                arr[i] = arr[j]
                arr[j] = c
    return arr

def quick_sort(arr):
    """
       Быстрая сортировка
       Получает массив arr
       Возвращает сортированный массив arr
       """
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x < pivot]
    right = [x for x in arr[:-1] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)  

def counting_sort(arr):
    """
        Сортировка подсчетом
        Получает массив arr
        Возвращает массив res
        """
    if not arr:
        return []
    if len(arr) == 1:
        return arr
    count_mas = [0] * (max(arr) + 1)
    for i in arr:
        count_mas[i] += 1
    res = []
    for i in range(len(count_mas)):
        res.extend([i] * count_mas[i])
    return res
def radix_sort(arr,base: int = 10):
    """
        Поразрядная сортировка
        Получает массив arr и систему счисления base
        Возвращает сортированный массив arr
        """
    if not arr:
        return []

    max_digits = max([len(str(x)) for x in arr])
    bins = [[] for _ in range(base)]
    for i in range(0, max_digits):
        for x in arr:
            digit = (x // base ** i) % base
            bins[digit].append(x)
        arr = [x for queue in bins for x in queue]
        bins = [[] for _ in range(base)]
    return arr

def bucket_sort(arr,buckets: int | None = None):
    """
       Ведерная сортировка
       Получает массив arr
       Возвращает сортированный массив result
       """
    if not arr:
        return []
    if len(arr) == 1:
        return arr
    if buckets is None:
        buckets = len(arr)
    min_val = min(arr)
    max_val = max(arr)
    if min_val == max_val:
        return arr
    bucket_list = [[] for _ in range(buckets)]
    range_val = max_val - min_val
    for num in arr:
        normalized = (num - min_val) / range_val
        bucket_index = int(normalized * buckets)
        bucket_index = min(bucket_index, buckets - 1)
        bucket_list[bucket_index].append(num)
    result = []
    for bucket in bucket_list:
        if bucket:  # Сортируем только непустые корзины
            result.extend(sorted(bucket))
    return result

def heap_sort(arr):
    """
        Heap сортировка
        Получает массив arr
        Возвращает сортированный массив result
        """
    heapq.heapify(arr)
    result = []
    while arr:
        result.append(heapq.heappop(arr))
    return result

    
