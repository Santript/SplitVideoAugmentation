def LOG_INFO(*msg):
	print("[INFO] ", end=' ')
	for message in msg:
		print(message, end=' ')
	print()

def LOG_ERR(*err):
	print("[ERR] ", end=' ')
	for error in err:
		print(error, end=' ')
	print()