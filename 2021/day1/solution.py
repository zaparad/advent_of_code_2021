
with open("input.txt" ,"r") as f:
	lines = f.readlines()


readings = [int(x) for x in lines]

increase_count = 0
prev_reading = 9999999
for reading in readings:
	if(reading > prev_reading):
		increase_count += 1
	prev_reading = reading

print(increase_count)