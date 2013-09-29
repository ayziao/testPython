import unittest
import bucket3.hoge


class MyTestCase(unittest.TestCase):
	def test_something(self):
		self.assertEqual(True, True)
		self.assertEqual(False, False)

	def test_piyo(self):
		self.assertEqual(bucket3.hoge.piyo(), 'piyo')


if __name__ == '__main__':
	unittest.main()
