with open("input1.txt","r") as f:
	lines = f.readlines()

drawn_numbers = [int(x) for x in lines[0].split(",")]
grids = []


class Grid:
	def __init__(self):
		self.numbers = []
		self.bingo_numbers = [[False for i in range(5)] for j in range(5)]
		self.complete_time = 0
	def add_row(self,row):
		self.numbers.append(row)

	def bingo_number(self,number):
		for i,row in enumerate(self.numbers):
			for j,numb in enumerate(row):
				if numb == number:
					self.bingo_numbers[i][j] = True


	def calc_score(self):
		sum = 0
		for i,row in enumerate(self.bingo_numbers):
			for j,numb in enumerate(row):
				if not numb:
					sum += self.numbers[i][j]
		return sum

	def check_bingo(self):
		#check rows
		for i in range(len(self.bingo_numbers)):
			bingo = True
			for j in range(len(self.bingo_numbers[0])):
				if not self.bingo_numbers[i][j]:
					bingo = False
					break
			if bingo:
				return True
		#check Columns
		for j in range(len(self.bingo_numbers[0])):
			bingo = True
			for i in range(len(self.bingo_numbers)):
				 if not self.bingo_numbers[i][j]:
				 	bingo = False
				 	break
			if bingo:
				return True
		#check diagonals
		"""
		bingo = True
		for i in range(len(self.bingo_numbers)):
			if not self.bingo_numbers[i][i]:
				bingo = False
				break
		if bingo:
			return True

		bingo = True
		for i in range(len(self.bingo_numbers)):
			if not self.bingo_numbers[len(self.bingo_numbers) -1 - i][i]:
				bingo = False
				break
		if bingo:
			return True
		"""

		return False


for line in lines[1:]:
	if line =="\n":
		grids.append(Grid())
	else:
		inp = [int(x) for x in line.split()]
		grids[-1].add_row(inp)

def run_bingo():
	completed_bingos = 0

	for time,numb in enumerate(drawn_numbers):
		for i,grid in enumerate(grids):
			if(grid.complete_time == 0):
				grid.bingo_number(numb)
				if grid.check_bingo():
					if completed_bingos < len(grids)-1:
						completed_bingos += 1
						grid.complete_time = time
					else:
						print(numb*grid.calc_score())
						return
			
run_bingo()