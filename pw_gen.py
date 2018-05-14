from string import ascii_letters, digits
from random import choice

lst = list(ascii_letters + digits)

def pw_gen(pw_len):
	return ''.join([choice(lst) for n in range(0, pw_len)])
