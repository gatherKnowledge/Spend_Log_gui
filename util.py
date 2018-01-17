def check_input(value):
	try:
		i = int(value)
		return i
	except ValueError as vError:
		return 0
	# return void : int
	#        except :