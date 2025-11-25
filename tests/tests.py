import unittest
from symtable import Class

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

class FibonacciAndFactorial(unittest.TestCase):
    def test_fibonacci(self):
        """Тест базовых случаев фибоначи"""
        self.assertEqual(fibonaci(5), 5)
        self.assertEqual(fibonaci(1), 1)
        self.assertEqual(fibonaci(0), 0)
        self.assertEqual(fibonaci(10), 55)
        self.assertEqual(fibonaci(100),  354224848179261915075)
    def test_fibonacci_recursive(self):
        """Тест базовых случаев фибоначи"""
        self.assertEqual(fibonaci_recursive(6), 8)
        self.assertEqual(fibonaci_recursive(1), 1)
        self.assertEqual(fibonaci_recursive(0), 0)
        self.assertEqual(fibonaci_recursive(10), 55)
    def test_fibonacci_negative(self):
        """Тест на отрицательные числа"""
        with self.assertRaises(ValueError):
            factorial_easy(-1)
        with self.assertRaises(ValueError):
            factorial_tree(-100)
    def test_fibonacci_recursive_negative(self):
        """Тест на отрицательные числа"""
        with self.assertRaises(ValueError):
            fibonaci(-1)
        with self.assertRaises(ValueError):
            fibonaci(-5)

    def test_factorial_easy(self):
        """Тест базовых случаев факториала"""
        self.assertEqual(factorial_easy(5), 120)
        self.assertEqual(factorial_easy(20), 2432902008176640000)
        self.assertEqual(factorial_easy(0), 1)
        self.assertEqual(factorial_easy(1), 1)

    def test_factorial_recursive(self):
        """Тест базовых случаев факториала c рекурсией"""

        self.assertEqual(factorial_easy(5), 120)
        self.assertEqual(factorial_easy(20), 2432902008176640000)
        self.assertEqual(factorial_recursive(1), 1)
        self.assertEqual(factorial_recursive(1), 1)

    def test_factorial_tree(self):
        """Тест базовых случаев факториала методом деревьев"""

        self.assertEqual(factorial_tree(5), 120)
        self.assertEqual(factorial_tree(20), 2432902008176640000)
        self.assertEqual(factorial_tree(1), 1)
        self.assertEqual(factorial_tree(1), 1)

    def test_factorial_recursive_negative(self):
        """Тест на отрицательные числа"""
        with self.assertRaises(ValueError):
            factorial_recursive(-1)
        with self.assertRaises(ValueError):
            factorial_recursive(-5)
    def test_factorial_negative(self):
        """Тест на отрицательные числа"""
        with self.assertRaises(ValueError):
            factorial_easy(-1)
        with self.assertRaises(ValueError):
            factorial_easy(-5)
    def test_factorial_tree_negative(self):
        """Тест на отрицательные числа"""
        with self.assertRaises(ValueError):
            factorial_tree(-1)
        with self.assertRaises(ValueError):
            factorial_tree(-5)
class Sorting(unittest.TestCase):
    def test_sort_single(self):
        """Тест сортировок массива из одного элемента"""
        arr = [5]
        self.assertEqual(bubble_sort(arr), [5])
        self.assertEqual(quick_sort(arr), [5])
        self.assertEqual(counting_sort(arr), [5])
        self.assertEqual(radix_sort(arr, 10), [5])
        self.assertEqual(bucket_sort(arr, 5), [5])
        self.assertEqual(heap_sort(arr), [5])

    def test_sort_random_int(self):
        """Тест сортировки случайного массива"""
        arr = rand_int_array(15,2,10,1)
        expected = sorted(arr)
        self.assertEqual(bubble_sort(arr.copy()), expected)
        self.assertEqual(quick_sort(arr.copy()), expected)
        self.assertEqual(counting_sort(arr.copy()), expected)
        self.assertEqual(radix_sort(arr.copy(), 10), expected)
        self.assertEqual(bucket_sort(arr.copy(), 5), expected)
        self.assertEqual(heap_sort(arr.copy()), expected)
    def test_sort_random_float(self):
        """Тест сортировки случайного массива с float"""
        arr = rand_float_array(15,2,10)
        expected = sorted(arr)
        self.assertEqual(bubble_sort(arr.copy()), expected)
        self.assertEqual(quick_sort(arr.copy()), expected)

        self.assertEqual(bucket_sort(arr.copy(), 5), expected)
        self.assertEqual(heap_sort(arr.copy()), expected)
    def test_sort_random_nearly_sorted(self):
        """Тест сортировки случайного массива с nearly sorted"""

        arr = nearly_sorted(15,5,1478)
        expected = sorted(arr)
        print("AAAAAAAAAAAAAAAAAAAAAAAAAA")
        print("AAAAAAAAA",expected)

        self.assertEqual(bubble_sort(arr.copy()), expected)
        self.assertEqual(quick_sort(arr.copy()), expected)
        self.assertEqual(counting_sort(arr.copy()), expected)
        self.assertEqual(radix_sort(arr.copy(), 10), expected)
        self.assertEqual(bucket_sort(arr.copy(), 5), expected)
        self.assertEqual(heap_sort(arr.copy()), expected)
    def test_sort_random_many_duplicates(self):
        """Тест сортировки случайного массива с дубликатами"""
        arr = many_duplicates(15,5,12 )
        expected = sorted(arr)
        self.assertEqual(bubble_sort(arr.copy()), expected)
        self.assertEqual(quick_sort(arr.copy()), expected)
        self.assertEqual(counting_sort(arr.copy()), expected)
        self.assertEqual(radix_sort(arr.copy(), 10), expected)
        self.assertEqual(bucket_sort(arr.copy(), 5), expected)
        self.assertEqual(heap_sort(arr.copy()), expected)
    def test_sort_random_nearly_sorted(self):
        """Тест сортировки развернутого массива"""
        arr = reverse_sorted(15)
        expected = sorted(arr)

        self.assertEqual(bubble_sort(arr.copy()), expected)
        self.assertEqual(quick_sort(arr.copy()), expected)
        self.assertEqual(counting_sort(arr.copy()), expected)
        self.assertEqual(radix_sort(arr.copy(), 10), expected)
        self.assertEqual(bucket_sort(arr.copy(), 5), expected)
        self.assertEqual(heap_sort(arr.copy()), expected)
class TestStack(unittest.TestCase):
    """Тесты для реализации стека"""
    def setUp(self):
        """Создание"""
        self.stack = StackOnList()

    def test_push_single(self):
        """Тест добавления элемента"""
        self.stack.push(42)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.__len__(), 1)
        self.assertEqual(len(self.stack), 1)

    def test_push_multiple(self):
        """Тест добавления нескольких элементов"""
        test_chisla = [1, 2, 3, 4, 5]
        for i in test_chisla:
            self.stack.push(i)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.__len__(), 5)
        self.assertEqual(len(self.stack), 5)

    def test_pop_single(self):
        """Тест извлечения элемента"""
        self.stack.push(42)
        popped = self.stack.pop()

        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.__len__(), 0)

    def test_pop_empty(self):
        """Тест извлечения из пустого стека"""
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek(self):
        """Тест просмотра вершины стека"""
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.peek(), 20)

    def test_getMin_empty_stack(self):
        """Тест getMin на пустом стеке"""
        with self.assertRaises(IndexError):
            self.stack.getMin()

    def test_getMin_(self):
        """Тест getMin """
        for i in range(2, 6):
            self.stack.push(i)
            self.assertEqual(self.stack.getMin(), 2)
class Queue(unittest.TestCase):
    """Тесты для реализации очереди"""
    def setUp(self):
        """Создание"""
        self.queue = QueueOnList()

    def test_enqueue_single(self):
        """Тест добавления одного элемента"""
        self.queue.enqueue(42)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.__len__(), 1)
        self.assertEqual(len(self.queue), 1)

    def test_enqueue_multiple(self):
        """Тест добавления нескольких элементов"""
        test_chisla = [1, 2, 3, 4, 5]
        for i in test_chisla:
            self.queue.enqueue(i)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.__len__(), 5)
        self.assertEqual(len(self.queue), 5)

    def test_dequeue_single(self):
        """Тест извлечения элемента"""
        self.queue.enqueue(42)
        dequeued = self.queue.dequeue()

        self.assertEqual(dequeued, 42)
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.__len__(), 0)

    def test_dequeue_empty(self):
        """Тест извлечения из пустой очереди"""
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_front(self):
        """Тест просмотра начала очереди"""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.front(), 10)
if __name__ == '__main__':
    unittest.main()