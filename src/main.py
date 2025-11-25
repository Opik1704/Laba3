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

from Laba3.src.structuri import StackOnList
from Laba3.src.structuri import QueueOnList

from Laba3.src.testcase import rand_int_array
from Laba3.src.testcase import nearly_sorted
from Laba3.src.testcase import many_duplicates
from Laba3.src.testcase import rand_float_array
from Laba3.src.testcase import reverse_sorted



def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    mas = [9,7,11,10,13,12,14,15,1488,156,5]

    #не подходит для больших чисел
    print(factorial_easy(5))

    #не подходит для больших чисел
    print(factorial_recursive(5))

    #подходит для больших чисел
    print(factorial_tree(5))

    print(fibonaci(10))

    print(fibonaci_recursive(10))
    print(bubble_sort(mas))
    mas = [9,7,11,10,13,12,14,15,1488,156,5]
    print(quick_sort(mas))
    mas = [9,7,11,10,13,12,14,15,1488,156,5]
    print(counting_sort(mas))
    mas = [9,7,11,10,13,12,14,15,1488,156,5]
    print(radix_sort(mas,2))
    mas = [9.0,7.0,11.0,10.0,13.0,12.0,14.0,15.0,1488.0,156.0,5.0]
    print(bucket_sort(mas,3))
    mas = [9,7,11,10,13,12,14,15,1488,156,5]
    print(heap_sort(mas))

    stack = StackOnList()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(f"Вершина: {stack.peek()}")
    print(f"Размер: {stack.__len__()}")
    print(f"Удален: {stack.pop()}")
    print(f"Размер: {stack.__len__()}")
    print(f"min:{stack.getMin()}")
    print(f"Удален: {stack.pop()}")
    print(f"Стек после удалений: {stack}")

    queue = QueueOnList()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Очередь: {queue}")
    print(f"Начало: {queue.front()}")
    print(f"Размер: {queue.__len__()}")
    print(f"Удален: {queue.dequeue()}")
    print(f"Удален: {queue.dequeue()}")
    print(f"Очередь после удалений: {queue}")

    print(rand_float_array(15,2,10))
    print("   \n")
    print(rand_int_array(15,2,10,1))
    print("   \n")
    print(nearly_sorted(15,5,1488))
    print("   \n")
    print(many_duplicates(15,5,12 ))
    print("   \n")
    print(reverse_sorted(15))

if __name__ == "__main__":
    main()
