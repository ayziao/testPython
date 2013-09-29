import pprint

if __name__ == '__main__':
	a = {}
	a['a'] = 2
	m = a.get('b')
	pprint.pprint(a)

#pprint.pprint(globals())
#pprint.pprint(locals())
