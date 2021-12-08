import random
import string


letters = string.ascii_lowercase
digits = string.digits

length = 100
password = ''
for i in range(length):
	if i > 3:
		text = random.choice(digits)
	else:
		text = random.choice(letters)
	password+=text
print(password)	
