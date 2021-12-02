
with open("input2.txt" ,"r") as f:
	lines = f.readlines()


readings = [int(x) for x in lines]

increase_count = 0
prev_reading = 9999999

fifo_buffer = readings[0:3]
old_value = sum(fifo_buffer)

print(readings[3:][0])


for reading in readings[3:]:
	fifo_buffer.pop(0)
	fifo_buffer.append(reading)
	new_value = sum(fifo_buffer)

	if(new_value > old_value):
		increase_count += 1

	old_value = new_value

print(increase_count)

