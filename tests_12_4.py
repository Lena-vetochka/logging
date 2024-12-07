import logging
import unittest
import rt_with_exceptions as rn


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner1 = rn.Runner('Mari', -5)
            for i in range(10):
                runner1.walk()
            logging.info('"test_run" выполнен успешно')
            self.assertEqual(runner1.distance, 50)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info= True)


    def test_run(self):
        try:
            runner2 = rn.Runner(4, 5)
            for i in range(10):
                runner2.run()
            logging.info('"test_run" выполнен успешно')
            self.assertEqual(runner2.distance, 100)
        except TypeError:
            logging.warning( "Неверный тип данных для объекта Runner", exc_info= True)



logging.basicConfig(level= logging.INFO, filemode= 'w', filename= 'runner_tests.log',
                        encoding= 'UTF-8', format= '%(asctime)s | %(levelname)s | %(message)s')
