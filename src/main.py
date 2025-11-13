from power import factorial_easy
from power import factorial_tree
from power import factorial_recursive
from power import fibonaci
from power import fibonaci_recursive
from power import bubble_sort
from power import quick_sort
from power import counting_sort

from power import radix_sort
from power import bucket_sort
from power import heap_sort


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
    print(radix_sort(mas))
if __name__ == "__main__":
    main()
