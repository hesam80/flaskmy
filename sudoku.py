#
# Sudoku solver with python
# --------------------------------------
# programmer: Mohsen Safari
# Mobile phone : +989355071859
# email: safari.tafreshi@gmail.com
# --------------------------------------
#
# Sorry for my bad english (Lo siento mucho por mi ingles!)
#
import sys
import fileinput
 
class Sudoku:
	# number of moves for resolving this sudoku
	__count = 0
 
	# self.__table is a dictionary and contains values or
	# possibilidades of each entry
	__table = {}
 
	# self.__move keeps track of each move
	#is neccessary for Rollback!
	__moves = []
 
	# a sample sudoku. no has any role in problem solving!
	__sampleSudoku = "52...6.........7.13...........4..8..6......5...........418.........3..2...87....."
 
	# define (and after in codes: set)	row indexes, column indexes, grid indexes
	__rindexes = [[], [], [], [], [], [], [], [], []]
	__cindexes = [[], [], [], [], [], [], [], [], []]
	__gindexes = [[], [], [], [], [], [], [], [], []]
 
	# variable for keep entries adjacents of each entry
	__adjacents = []
 
	def __init__(self, table = None):
		# create one list for each entry. contents of each list will be adjacents
		# of that entry
		for i in range(81):
			self.__adjacents.append([])
 
		# set values: row indexes, column indexes, grid indexes, adjacents
		self.__setRIndexes()
		self.__setCIndexes()
		self.__setGIndexes()
		self.__setAdjacents()
 
		# create sudoku table with information provided in table
		if table is not None:
			try:
				self.setTable(table)
			except SyntaxError:
				print("Sudoku is not valid")
				print("Try something like: ", self.getSampleSudoku())
 
	# create sudoku table 
	def setTable(self, table):
		self.__count = 0
		self.__moves = []
		self.__table = {}
 
		if len(str(table)) != 81:
			raise SyntaxError
 
		# read sudoku table and set in self.table
		for i in range(len(table)):
			# if value is not specified fill its place with
			# empty list. this list will be filled with
			# all numbers possible
			if table[i] == ".":
				self.__table[i] = []
			else :
				self.__table[i] = int(table[i])
 
		# update possible values for each entry which no has value
		self.__updatePossibleTable(fullUpdate = True)
 
	# set row indexes for each row. key is row number and values are
	# number of each entry inside that row
	# Example:
	# self.__rindexes[0] = [0,1,2,3,4,5,6,7,8] ,
	# self.__rindexes[1] = [9,10,11,12,13,14,15,16,17]
	def __setRIndexes(self):
		for i in range(9):
			s = i * 9
			for j in range(9):
				self.__rindexes[i].append(s + j)
 
	# set column indexes for each column. key is column number and values are
	# number of each each entry inside that column
	# example:
	# self.__cindexes[0] = [0,9,18,27,36,45,54,63,72]
	def __setCIndexes(self):
		for i in range(9):
			c = i % 9
			self.__cindexes[i].append(c)
			for j in range(8):
				c = c + 9
				self.__cindexes[i].append(c)
 
	# set grid indexes for each grid. key is grid number and values are
	# number of each entry inside that grid
	# example:
	# self.__gindexs[0] = [0,1,2,9,10,11,18,19,20]
	def __setGIndexes(self):
		gStartIndexes = [0, 3, 6, 27, 30, 33, 54, 57, 60]
 
		for i in range(9):
			s = gStartIndexes[i]
			self.__gindexes[i].append(s)
			self.__gindexes[i].append(s + 1)
			self.__gindexes[i].append(s + 2)
			self.__gindexes[i].append(s + 9)
			self.__gindexes[i].append(s + 10)
			self.__gindexes[i].append(s + 11)
			self.__gindexes[i].append(s + 18)
			self.__gindexes[i].append(s + 19)
			self.__gindexes[i].append(s + 20)
 
	# set all neighbors for each entry. key is number of entry
	# and values are numbers of each entry in this row and this
	# column and this grid
	# example:
	# self.__adjacents[0] = [0,1,2,3,4,5,6,7,8,9,18,27,36,45,54,63,72,10,11,19,20]
	def __setAdjacents(self):
		for i in range(81):
			tmp = self.__entry2RCG(i)
			self.__adjacents[i] = list(set(self.__rindexes[tmp["r"]] + self.__cindexes[tmp["c"]] + self.__gindexes[tmp["g"]]))
 
 
	# get i'th row indexes of __rindexes.
	# just is a getter and no has any role in problem solving
	def getRIndexes(self, i):
		return self.__rindexes[int(i)]
 
	# get i'th column indexes of __cindexes
	# just a getter and no has any role in problem solving
	def getCIndexes(self, i):
		return self.__cindexes[int(i)]
 
	# get i'th grid indexes of __gindexes
	# just a getter and no has any role in problem solving
	def getGIndexes(self, i):
		return self.__gindexes[int(i)]
 
	# get all adjacents of one index
	# just a getter and no has any role in problem solving
	def getAdjacents(self, i):
		return self.__adjacents[int(i)]
 
 
	# return a sample sudoku.
	# this sample is just forpresentation of input format and no has 
	# and role in problem solving
	def getSampleSudoku(self):
		return self.__sampleSudoku
 
 
	# get entry and find its row, its column and its grid
	# example: entry2RCG(11)--->row:1, column:2, grid:0
	# Already only used inside the "setAdjacents" methos
	def __entry2RCG(self, entry):
		r = int(entry / 9)
		c = entry % 9
 
		if r <= 2 :
			g = 0 if c <= 2 else 1 if c <= 5 else 2
		elif r <= 5:
			g = 3 if c <= 2 else 4 if c <= 5 else 5
		else :
			g = 6 if c <= 2 else 7 if c <= 5 else 8
 
		return {'c':c, 'r':r, 'g':g}
 
 
	# prepare variable self.table for print on screen
	def __prepareForPrint(self, removeList = True, space = 1):
		tmp = {}
		for i in range(len(self.__table)):
			if type(self.__table[i]) == list and removeList:
				tmp[i] = "."
			elif type(self.__table[i]) == list:
				tmp[i] = (''.join(str(x) for x in self.__table[i]) + "*").center(space)
			else:
				tmp[i] = str(self.__table[i]).center(space)
 
		return tmp
 
 
	# print sudoko table. those entries that no have value will be displayed with a "."
	# Example:
	# We have this sudoko:
	# ..53.....8......2..7..1.5..4....53...1..7...6..32...8..6.5....9..4....3......97..
	#
	# method "printTable" will have this output:
	# +---+---+---+
	# |..5|3..|...|
	# |8..|...|.2.|
	# |.7.|.1.|5..|
	# +---+---+---+
	# |4..|..5|3..|
	# |.1.|.7.|..6|
	# |..3|2..|.8.|
	# +---+---+---+
	# |.6.|5..|..9|
	# |..4|...|.3.|
	# |...|..9|7..|
	# +---+---+---+
	def printTable(self):
		tmp = self.__prepareForPrint()
 
		for i in list(map(lambda x: x[0], self.__rindexes)):
			if i % 27 == 0:
				print("+---+---+---+")
 
			print(
					"|" + tmp[i+0] + tmp[i+1] + tmp[i+2] + \
					"|" + tmp[i+3] + tmp[i+4] + tmp[i+5] + \
					"|" + tmp[i+6] + tmp[i+7] + tmp[i+8] + "|"
			)
 
		print("+---+---+---+")
 
 
	# print possible table
	# for above sudoku output the printPossibleTable will be:
	# +---------------------------+---------------------------+---------------------------+
	# |  1269*	   924*		 5	  |    3	  24689*   24678* |  14689*   14679*   8147*  |
	# |    8	   934*		169*  |  9467*	  9456*		467*  |  1469*		2	   1347*  |
	# |  9236*		7		926*  |  8946*		1	   8246*  |    5	   946*		834*  |
	# +---------------------------+---------------------------+---------------------------+
	# |    4	   892*    26789* |  8169*	   896*		 5	  |    3	   197*		127*  |
	# |   925*		1		892*  |   894*		7		834*  |   924*	   945*		 6	  |
	# |  9567*	   95*		 3	  |    2	   946*		146*  |   149*		8	   1457*  |
	# +---------------------------+---------------------------+---------------------------+
	# |  1237*		6	   8127*  |    5	  8234*   123478* |  8124*	   14*		 9	  |
	# |  12579*   8925*		 4	  |  8167*	   826*    12678* |  8126*		3	   8125*  |
	# |  1235*	  8235*		812*  |  8146*	  23468*	 9	  |    7	  1456*    12458* |
	# +---------------------------+---------------------------+---------------------------+
	def printPossibleTable(self):
		space = 9
		tmp = self.__prepareForPrint(False, space)
 
		for i in list(map(lambda x: x[0], self.__rindexes)):
			if i % 27 == 0:
				print( ("+" + ("-" * space) * 3) * 3 + "+")
 
			print(
					"|" + tmp[i+0] + tmp[i+1] + tmp[i+2] + \
					"|" + tmp[i+3] + tmp[i+4] + tmp[i+5] + \
					"|" + tmp[i+6] + tmp[i+7] + tmp[i+8] + "|"
			)
 
		print( ("+" + ("-" * space) * 3) * 3 + "+")
 
 
	# only find next best move. return entry and its finded value.
	# if variable "entry" is set then find best move for that entry
	# when no more move is possible return [-1, -1]
	# this value means that we have to RollBACK!
	# if each entry has its value return [1000, 1000]
	# this value means that sudoku is already solved.
	def findNextMove(self, entry = -1):
		count, minLength, entry, value = 0, 1000, -1, -1
 
		if [] in self.__table.values():
			return [-1, -1]
 
		if entry != -1:
			tmp = sorted(self.__table[entry])
			if not len(tmp):
				return [-1, -1]
			return [entry, tmp[0]]
 
 
		for k, v in self.__table.items():
			if type(v) == list :
				count = count + 1
				if len(v) < minLength:
					minLength = len(v)
					entry = k
 
 
		if count == 0:
			return [1000, 1000]
 
		tmp = sorted(self.__table[entry])
		value = tmp[0]
		return [entry, value]
 
 
	# delete last move and call "updatepossibleTable()"
	def rollback(self):
		move = self.__moves.pop()
		entry, value = move[0], move[1]
		self.move(entry, [], value)
		return entry 
 
	# a getter for __count variable
	# no has any role in problem solving
	def getCount(self):
		return self.__count
 
	# get entry and value and set value in that entry
	def move(self, entry, value, onRollBackValueGreaterThan = -1):
		self.__table[entry] = value
		self.__count = self.__count + 1
 
		if type(value) != list:
			self.__moves.append([entry, value])
 
		if value == []:
			self.__updatePossibleTable(entry, onRollBackValueGreaterThan, fullUpdate = True)
		else:
			self.__updatePossibleTable(entry, onRollBackValueGreaterThan)
 
 
	# get moves variable
	# just a getter. no has any role in problem solving
	def getMoves(self):
		return self.__moves
 
	# update possible table
	# normally we call this function after each move and each rollback
	def __updatePossibleTable(self, entry = -1, valueGreaterThan = -1, fullUpdate = False):
		values = set()
 
		if fullUpdate == True:
			check = range(81)
		elif entry != -1:
			check = self.__adjacents[entry]
		else:
			print("Unknown update policy")
			sys.exit(1)
 
		for i in check:
			if type(self.__table[i]) != list:
				continue
 
			values.clear()
			for j in self.__adjacents[i]:
				if type(self.__table[j]) == list:
					continue
				values.add(self.__table[j])
 
			possibles = list({1,2,3,4,5,6,7,8,9} - values)
			if i == entry:
				possibles = list(filter(lambda x: x > valueGreaterThan, possibles))
 
			self.__table[i] = possibles
 
	def markEntries(self, indexes):
		for i in range(9):
			start = i * 9
 
			if i % 3 == 0:
				print("+---+---+---+")
 
			for j in range(9):
				if j % 3 == 0:
					print("|", end="")
				if (start + j) in indexes:
					print("x", end="")
				else:
					print(" ", end="")
			print("|")
 
		print("+---+---+---+")
 
	# solve sudoku by repeating these steps
	# 1- find best move or roll back last move
	# 2- move
	# go to step 1 
	def solve(self):
		# reset number of tries for resolving this sudoku
		self.__count = 0
 
		entry = -1
		# while true ...
		while(True):
			# find next move. if entry is set "findNextMove" will find next
			# value for specified entry
			entry, value = self.findNextMove(entry)
 
			# if we have no more moves and sudoku is solved then break
			if entry == 1000 and value == 1000:
				return	
 
			# last move is incorrect. Rollback!
			if entry == -1:
				entry = self.rollback()
				continue
 
			# set finded value in its entry
			self.move(entry, value)
			entry = -1
 
 
	def __repr__(self):
		return "another sudoku solver with python!"
 
 
if __name__ == "__main__" :
	# create object of sudoku with sudoku of user
	obj = Sudoku()
 
	# read sudoku from standard input or file
	# format of sudoku has to be similar:
	# ..53.....8......2..7..1.5..4....53...1..7...6..32...8..6.5....9..4....3......97..
	for line in fileinput.input():
		string = line.rstrip()
 
		try:
			obj.setTable(string)
		except SyntaxError:
			print("Sudoku is not valid")
			print("Try something like: ", obj.getSampleSudoku())
			continue
 
		# print sudoku on screen
		obj.printTable()
 
		# solve sudoku
		obj.solve()
 
		# Already sudoku is solved
		print("Solved with ", obj.getCount(), " moves")
 
		# Display solved sudoku
		obj.printTable()
		print("@@@@@@@@@@@@@")