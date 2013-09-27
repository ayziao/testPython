# -*- coding: UTF-8 -*-
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../myApp')

import myApp
import unittest


class MyTestCase(unittest.TestCase):
	def test_something(self):
		self.assertEqual(True, False)

	def test_main(self):
		app = myApp.myApp()
		self.assertEqual(app.main(), True)


if __name__ == '__main__':
	unittest.main()



#TODO やること
#PENDING やること考える
#PENDING Python3調べる
#PENDING webサーバどうにかする
#PENDING テストのやり方＞プロ版じゃないとなさげ＞コマンドラインでのやり方を探す
#PENDING ストレージ検討 KVS RDB
#PENDING TwitterAPI関連調べる
#PENDING コーディング規約調べる
#PENDING
#PENDING
#PENDING
#PENDING
#PENDING
