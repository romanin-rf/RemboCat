import string
import random

def line_break(text: str, max_char: int, chrr = "\n"):
	count = int(len(text) / max_char) + 1
	wag = 1
	done_list = []
	while count != 0:
		if (count - 1) != 0:
			done_list.append(text[(max_char * (wag - 1)):(max_char * wag)] + chrr)
		else:
			done_list.append((text[(max_char * (wag - 1)):]))
		count -= 1
		wag += 1
	return done_list

def generate_str(size):
	return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))