
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

import time


def main():
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    Return: Данная функция ничего не возвращает
    """
    flag = 0
    while True:
        if flag == 0:
            flag = 1
            print("Help","Для выхода break")
            print("Использование факториала: factorial   число   easy/tree/recursive")
            print("Использование фибоначи : fibonacci   число   iterative/recursive")
            print("Использование сортировок: sort алгоритм числа через пробел")
            print("Доступные сортировки: bubble, quick, counting, radix, bucket, heap")
            print("Использование cтека : stack   действиe   действие   действие (stack push 7 pop push 8 pop) ")
            print("Доступные действия: push число, pop, peek, min")
            print("Использование очереди: queue  действиe   действие   действие")
            print("Доступные действия: enqueue число, dequeue, front")
        command = input("Введите команду: ").strip()
        if not command:
            continue
        if command == "break":
            break
        parts = command.split()
        command = parts[0].lower()
        try:
            if command == "help":
                print("Help:")
                print("Для выхода break")
                print("Использование факториала: factorial   число   easy/tree/recursive")
                print("Использование фибоначи : fibonacci   число   iterative/recursive")
                print("Использование сортировок: sort алгоритм числа через пробел")
                print("Доступные сортировки: bubble, quick, counting, radix, bucket, heap")
                print("Использование cтека : stack   действиe   действие   действие (stack push 7 pop  push 8 pop)")
                print("Доступные действия: push число, pop, peek, min")
                print("Использование: queue   действие   действие   действие ")
                print("Доступные действия: enqueue X, dequeue, front")
            if command == "factorial":
                num = int(parts[1])
                method = parts[2] if len(parts) > 2 else "easy"
                if method == "easy":
                    result = factorial_easy(num)
                elif method == "tree":
                    result = factorial_tree(num)
                elif method == "recursive":
                    result = factorial_recursive(num)
                else:
                    print("Неизвестный метод")
                    continue
                print(f"Факториал {num} = {result}")
            elif command == "fibonacci":
                if len(parts) < 2:
                    print("Введите число")
                    continue
                num = int(parts[1])
                method = parts[2] if len(parts) > 2 else "iterative"

                if method == "iterative":
                    result = fibonaci(num)
                elif method == "recursive":
                    result = fibonaci_recursive(num)
                else:
                    print(f"Неизвестный метод {parts[2]}")
                    continue
                print(f"Число Фибоначчи F({num}) = {result}")

            elif command == "sort":
                if len(parts) < 3:
                    print("Использование: sort <алгоритм> <числа через пробел>")
                    print("Алгоритмы: bubble, quick, counting, radix, bucket, heap")
                    continue
                sort = parts[1]
                arr = [int(x) for x in parts[2:]]
                sorts = {
                    "bubble": bubble_sort,
                    "quick": quick_sort,
                    "counting": counting_sort,
                    "radix": radix_sort,
                    "bucket": bucket_sort,
                    "heap": heap_sort
                }
                if sort not in sorts:
                    print("Неизвестный алгоритм")
                    continue
                print(f"Исходный массив {arr}")
                start_time = time.time()
                result = sorts[sort](arr.copy())
                finish_time = time.time()
                print(f"Отсортированный массив {result}")
                print(f"Время: {finish_time - start_time:.6f} сек")

            elif command == "stack":
                if len(parts) < 2:
                    print("ВВедите команду")
                    continue
                stack = StackOnList()
                i = 1
                while i < len(parts):
                    action = parts[i]
                    if action == "push":
                        if i + 1 >= len(parts):
                            print("Ошибка: для push нужно число")
                            break
                        try:
                            push_num = int(parts[i + 1])
                            stack.push(push_num)
                            print(f"push({push_num})")
                            i += 2
                        except ValueError:
                            print(f"Ошибка: '{parts[i + 1]}' не является целым числом")
                            i += 2  # все равно пропускаем

                    elif action == "pop":
                        try:
                            del_el = stack.pop()
                            print(f"pop = {del_el}")
                        except Exception as e:
                            print(f"Ошибка pop: {e}")
                        i += 1

                    elif action == "peek":
                        try:
                            peek_el = stack.peek()
                            print(f"peek = {peek_el}")
                        except Exception as e:
                            print(f"Ошибка peek: {e}")
                        i += 1

                    elif action == "min":
                        try:
                            min_el = stack.getMin()
                            print(f"min = {min_el}")
                        except Exception as e:
                            print(f"Ошибка min: {e}")
                        i += 1
                    else:
                        print(f"Неизвестное действие: {action}")
                        i += 1

            elif command == "queue":
                if len(parts) < 2:
                    print("Использование: queue <действия>")
                    print("Действия: enqueue X, dequeue, front")
                    continue

                queue = QueueOnList()
                i = 1
                while i < len(parts):
                    action = parts[i]

                    if action == "enqueue":
                        if i + 1 >= len(parts):
                            print("Ошибка: для enqueue нужно число")
                            break
                        enqueue_el = int(parts[i + 1])
                        queue.enqueue(enqueue_el)
                        print(f"enqueue({enqueue_el})")
                        i += 2

                    elif action == "dequeue":
                        try:
                            dequeue_el = queue.dequeue()
                            print(f"dequeue() = {dequeue_el}")
                        except Exception as e:
                            print(f"Ошибка dequeue: {e}")
                        i += 1

                    elif action == "front":
                        try:
                            front_el = queue.front()
                            print(f"front() = {front_el}")
                        except Exception as e:
                            print(f"Ошибка front: {e}")
                        i += 1
                    else:
                        print(f"Неизвестное действие: {action}")
                        i += 1
            else:
                print("Неизвестная команда")

        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
# def main() -> None:
#извините что оставил тут такие непотребства
#     """
#     Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
#     :return: Данная функция ничего не возвращает
#     """
#     mas = [9,7,11,10,13,12,14,15,1488,156,5]
#
#     #не подходит для больших чисел
#     print(factorial_easy(5))
#
#     #не подходит для больших чисел
#     print(factorial_recursive(5))
#
#     #подходит для больших чисел
#     print(factorial_tree(5))
#
#     print(fibonaci(10))
#
#     print(fibonaci_recursive(10))
#     print(bubble_sort(mas))
#     mas = [9,7,11,10,13,12,14,15,1488,156,5]
#     print(quick_sort(mas))
#     mas = [9,7,11,10,13,12,14,15,1488,156,5]
#     print(counting_sort(mas))
#     mas = [9,7,11,10,13,12,14,15,1488,156,5]
#     print(radix_sort(mas,2))
#     mas = [9.0,7.0,11.0,10.0,13.0,12.0,14.0,15.0,1488.0,156.0,5.0]
#     print(bucket_sort(mas,3))
#     mas = [9,7,11,10,13,12,14,15,1488,156,5]
#     print(heap_sort(mas))
#
#     stack = StackOnList()
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)
#
#     print(f"Вершина: {stack.peek()}")
#     print(f"Размер: {stack.__len__()}")
#     print(f"Удален: {stack.pop()}")
#     print(f"Размер: {stack.__len__()}")
#     print(f"min:{stack.getMin()}")
#     print(f"Удален: {stack.pop()}")
#     print(f"Стек после удалений: {stack}")
#
#     queue = QueueOnList()
#     queue.enqueue(1)
#     queue.enqueue(2)
#     queue.enqueue(3)
#     print(f"Очередь: {queue}")
#     print(f"Начало: {queue.front()}")
#     print(f"Размер: {queue.__len__()}")
#     print(f"Удален: {queue.dequeue()}")
#     print(f"Удален: {queue.dequeue()}")
#     print(f"Очередь после удалений: {queue}")
#
#     print(rand_float_array(15,2,10))
#     print("   \n")
#     print(rand_int_array(15,2,10,1))
#     print("   \n")
#     print(nearly_sorted(15,5,1488))
#     print("   \n")
#     print(many_duplicates(15,5,12 ))
#     print("   \n")
#     print(reverse_sorted(15))
#
# if __name__ == "__main__":
#     main()
