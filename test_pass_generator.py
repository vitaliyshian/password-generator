import unittest
from pass_generator import PassGenerator


class TestPassGenerator(unittest.TestCase):
    def setUp(self):
        self.pass_generator = PassGenerator()

    def test_random_generator(self):
        self.assertEqual(len(self.pass_generator.random_generator('10')), 10)
        self.assertEqual(len(self.pass_generator.random_generator('5')), 5)
        self.assertEqual(len(self.pass_generator.random_generator('1000')), 1000)
        self.assertEqual(self.pass_generator.random_generator('0'), 'Invalid')
        self.assertEqual(self.pass_generator.random_generator('abc'), 'Invalid')
        self.assertEqual(self.pass_generator.random_generator(''), 'Invalid')
        self.assertEqual(self.pass_generator.random_generator('-3'), 'Invalid')


if __name__ == '__main__':
    unittest.main()
