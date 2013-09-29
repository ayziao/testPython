'''
afefefef
'''

import bucket2.bucket2

exit()
import sys

#sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../bucket')
#sys.path.append(os.pardir)

from pprint import pprint
#import bucket.bucket2
#from . import bucket2

import bucket2.bucket2

print(__name__)


def ccc() -> object:
	'''
	' aaaaaaa
	@rtype : object
	'''
	x = 2
	bucket2.bucket2.aaa()
	return x


ccc()

if __name__ == '__main__':
	a = {}
	a['a'] = 2
	m = a.get('b')
	n = None
	#	print(a)
	#	print(globals())
	#	print(locals())
	pprint(a)
	pprint(globals())
	pprint(locals())

	pprint(dir())

	pprint(sys.path)
