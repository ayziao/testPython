from pprint import pprint

if __name__ == '__main__':
	a = {}
	a['a'] = 2
	m = a.get('b')
	print(a)
	print(globals())
	print(locals())
	pprint(a)
	pprint(globals())
	pprint(locals())
