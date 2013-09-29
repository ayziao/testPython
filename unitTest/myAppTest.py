#タスク書き方
#TODO やること
#PENDING 考えること

#タスク
#PENDING	全体的な進め方
#PENDING	準備
#PENDING		webサーバどうにかする
#PENDING		ストレージ検討 KVS RDB
#PENDING		プラグインディレクトリ構成
#PENDING		TwitterAPI関連調べる
#PENDING	設計
#PENDING	単体テスト
#PENDING	実装
#PENDING	結合テスト
#PENDING
#PENDING
#PENDING
#PENDING

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../myApp')

import unittest
import MyApp
#from MyApp import MyApp


class MyTestCase(unittest.TestCase):
	def test_something(self):
		self.assertEqual(False, False)
		self.assertEqual(True, True)

	def test_main(self):
		app = MyApp.MyApp()
		f = app.main
		f()

		self.assertEqual(app.main(), True)

	#		self.assertEqual(MyApp.main(), True)


