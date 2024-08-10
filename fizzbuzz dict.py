fizzbuzz_dict = {3: 'Fizz', 5: 'Buzz'}

def fizzbuzz(int):
	result = ''
	for num, word in fizzbuzz_dict.items():
		if int % num  == 0:
			result = result + word
	
	return result

for i in range(1, 101):
	result = fizzbuzz(i)
	if result != '':
		print(str(i) + ' result: ' + result)