import heapq


def factorial_easy(number: int) -> int:
    f = 1
    while number > 1:
        f = f * number
        number = number - 1
    return f
def factorial_tree(n:int):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1 or n == 2:
        print("Aaa")
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
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)
def fibonaci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
def fibonaci_recursive(n: int) -> int:
    if n == 0:
        return 0
    if n < 0:
        return "нет такого члена последовательности",n
    if n == 1 or n == 2:  
        return 1
    else:  
        return (fibonaci_recursive(n-1) + fibonaci_recursive(n-2))  
def bubble_sort(a):
    for i in range(len(a)):
        for j in range(i,len(a)):
            if(a[i] > a[j]):
                c = a[i]
                a[i] = a[j]
                a[j] = c
    return a

def quick_sort(a):
    if len(a) <= 1:  
        return a  
    pivot = a[-1]
    left = [x for x in a[:-1] if x < pivot]  
    right = [x for x in a[:-1] if x >= pivot]  
    return quick_sort(left) + [pivot] + quick_sort(right)  

def counting_sort(a):
    count_mas = [0] * (max(a) + 1)
    for i in a:
        count_mas[i] += 1
    res = []
    for i in range(len(count_mas)):
        res.extend([i] * count_mas[i])
    return res
def radix_sort(arr):
    max_digits = max(arr)
    bins = [[] for _ in range(10)]
    for i in range(0, max_digits):
        for x in arr:
            digit = (x // 10 ** i) % 10
            bins[digit].append(x)
        arr = [x for queue in bins for x in queue]
        bins = [[] for _ in range(10)]
    return arr


def bucket_sort(a,buckets):
    if not a:
        return []
    if len(a) == 1:
        return a
    if buckets is None:
        buckets = len(a)
    min_val = min(a)
    max_val = max(a)
    if min_val == max_val:
        return a
    bucket_list = [[] for _ in range(buckets)]
    range_val = max_val - min_val
    for num in a:
        normalized = (num - min_val) / range_val
        bucket_index = int(normalized * buckets)
        bucket_index = min(bucket_index, buckets - 1)
        bucket_list[bucket_index].append(num)
    result = []
    for bucket in bucket_list:
        if bucket:  # Сортируем только непустые корзины
            result.extend(sorted(bucket))
    return result
def heap_sort(a):
    heapq.heapify(a)
    sorted_list = []
    while a:
        sorted_list.append(heapq.heappop(a))
    return sorted_list

    
