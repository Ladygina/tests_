import unittest
from defs import solve, solve_list, discriminant, solution


class Test_task1(unittest.TestCase):
    def test_discriminant(self):  # тест с параметрами
        # arrange
        for i, (a,b,c, expected) in enumerate((

                (1, -4, 4, 2),
                (1,2,14,'корней нет'),
                (1,5,6,(-2,-3))
            )):

            with self.subTest(i): # номер теста
                actual = solution(a, b, c)
                self.assertEqual(expected, actual)

    def test_worktime(self):

        todo_list = [
            ["Разобрать почту", 1],
            ["Обзвонить клиентов", 2],
            ["Запланировать дела на завтра", 0.6],
            ["Сделать презентацию", 3],
            ["Созвон с командой", 0.5]
        ]
        expected = 0.9
        actual = round(solve_list(todo_list, 8),1)
        self.assertEqual(expected, actual)

    def test_animal_solve(self):    # тест с параметрами
        for i, (hare_distance, turtle_distance, expected) in enumerate((

                ([1,2,3],[3,1,2],'одинаково'),
                ([1,2,10],[3,1,2], 'заяц'),
                ([1,2,3],[3,1,10],'черепаха')
            )):

            with self.subTest(i): # номер теста
                actual = solve(hare_distance, turtle_distance)
                self.assertEqual(expected, actual)
