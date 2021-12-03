
def binarray_to_dec(bin_array):
	sum = 0
	for i,digit in enumerate(reversed(bin_array)):
		sum += digit * pow(2,i)
	return sum


with open("input1.txt","r") as f:
	lines = f.readlines()

width = len(lines[0].strip())


length = len(lines)
digits = [0]*width

for line in lines:
	for i,digit in enumerate(line.strip()):
		digits[i] += int(digit)


gamma_rate = [0]*width
epsilon_rate = [0]*width

for i,digit in enumerate(digits):
	if(length/2 < digit):
		gamma_rate[i] = 1
		epsilon_rate[i] = 0
	else:
		gamma_rate[i] = 0
		epsilon_rate[i] = 1


print(binarray_to_dec(gamma_rate) * binarray_to_dec(epsilon_rate))