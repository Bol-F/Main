def add(a, b, *args, **kwargs):
	return sum(list(a, b, *args, **kwargs.values))


def is_odd(a):
	if a % 2 == 0:
		return 'this num is even'
	elif a % 2 != 0:
		return 'this num is odd'
	else:
		return 'Bruh !'
