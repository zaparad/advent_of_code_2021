
import numpy as np

def binarray_to_dec(bin_array):
	sum = 0
	for i,digit in enumerate(reversed(bin_array)):
		sum += int(digit) * pow(2,i)
	return sum





def get_oxygen_rating(data):
	pos = 0
	while(True):
		length = len(data)
		if(length <= 1):
			return data[0]
			break

		count = 0
		ones = []
		zeros = []

		for i,line in enumerate(data):
			if line[pos] == '1':
				ones.append(i)
				count += 1
			else:
				zeros.append(i)

		if count >= length / 2:
			for index in reversed(zeros):
				data.pop(index)
		else:
			for index in reversed(ones):
				data.pop(index)
		pos += 1


def get_co2_rating(data):
	pos = 0
	while(True):
		length = len(data)
		if(length <= 1):
			return data[0]
			break

		count = 0
		ones = []
		zeros = []

		for i,line in enumerate(data):
			if line[pos] == '1':
				ones.append(i)
				count += 1
			else:
				zeros.append(i)

		if count >= length / 2:
			for index in reversed(ones):
				data.pop(index)
		else:
			for index in reversed(zeros):
				data.pop(index)

		pos += 1
with open("input1.txt","r") as f:
	lines = f.readlines()



print(binarray_to_dec(get_oxygen_rating([x.strip() for x in lines]))*binarray_to_dec(get_co2_rating([x.strip() for x in lines])))

