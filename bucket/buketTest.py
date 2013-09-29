import unittest
import bucket.hoge


class MyTestCase(unittest.TestCase):
	def test_something(self):
		self.assertEqual(True, True)
		self.assertEqual(False, False)

	def test_piyo(self):
		self.assertEqual(bucket.hoge.piyo(), 'piyo')


if __name__ == '__main__':
	unittest.main()
