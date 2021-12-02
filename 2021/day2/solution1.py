with open("input.txt","r") as f:
 	lines = f.readlines()


horizontal_position = 0
depth = 0

commands = [line.split() for line in lines]
for line in commands:
	if line[0] == "forward":
		horizontal_position += int(line[1])
	elif line[0] == "down":
		depth += int(line[1])
	elif line[0] == "up":
		depth -= int(line[1])

print(horizontal_position * depth