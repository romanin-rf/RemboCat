import sys

def check_prefix():
	if sys.platform == "win32":
		return "\\"
	elif sys.platform == "linux":
		return "/"
	else:
		return None