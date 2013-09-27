# -*- coding: UTF-8 -*-

#タスク書き方
#TODO やること
#PENDING 考えること

#タスク
#PENDING	全体的な進め方
#PENDING	準備
#PENDING		Python3調べる
#PENDING		コーディング規約調べる
#PENDING		webサーバどうにかする
#PENDING		ディレクトリ構成
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

import myApp
import unittest

class MyTestCase(unittest.TestCase):
	def test_something(self):
		self.assertEqual(False, False)
		self.assertEqual(True, True)

	def test_main(self):
		app = myApp.myApp()
		self.assertEqual(app.main(), True)


if __name__ == '__main__':
	unittest.main()

