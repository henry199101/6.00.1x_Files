def divide(x, y):
	try:
		result = x / y
	except ZeroDivisionError, e:
		print "division by zero!" + str(e)
	else:
		print "result is", result
	finally:
		print "executing finally clause"