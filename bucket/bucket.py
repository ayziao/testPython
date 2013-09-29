import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../bucket')

from pprint import pprint
import bucket2

print(__name__)


def ccc():
  x = 2
  bucket2.aaa()


ccc()

if __name__ == '__main__a':
  a = {}
  a['a'] = 2
  m = a.get('b')
  print(a)
  print(globals())
  print(locals())
  pprint(a)
  pprint(globals())
  pprint(locals())
