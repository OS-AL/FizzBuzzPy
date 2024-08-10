numbers = [3, 5]
words = ['Fizz', 'Buzz']

def fizzbuzz(int):
	result = ''
	for i, num in enumerate(numbers):
		if int % num  == 0:
			result = result + words[i]
	
	return result

for i in range(1, 101):
	result = fizzbuzz(i)
	if result != '':
		print(str(i) + ' result: ' + result)