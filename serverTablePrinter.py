#! python3
# serverTablePrinter.py - Create a table to show the waiters which area they will serve tonight

def tableData():
	# establish the constant, list of rows
	sectionNames= ['Row A', 'Row B', 'Row C', 'Row D', 'Row E', 'Row F', 'Row H']

	# figure out the number of servers working tonight
	while True:
		numberOfServers = input('How many servers are working tonight? ')
		if not numberOfServers.isdecimal():
			print('Please enter an integer.')
		else:
			break

	# figure out who will be serving tonight
	serverNames = []
	print("Which servers will be working tonight? Starting from first to clock in, to the last.")
	for i in range(int(numberOfServers)):
		serverNames.append(input(f'Server {i+1}: '))

	# create the tableData
	tableData = [serverNames, sectionNames]
	return tableData

def tablePrinter(tableData):
	# find the biggest width within the strings of data bc it will we be our columnn width
	colWidth = [0] * len(tableData)

	# we need to determine the size of the column for each column
	for y in range(len(tableData)):
		for x in tableData[y]:
			if colWidth[y] < len(x):
				colWidth[y] = len(x)

	# we need to create the table
	for x in range(len(tableData[0])): # 0,1,2,3
		for y in range(len(tableData)):  # 0,1,2
			print(tableData[y][x].rjust(colWidth[y]),end = ' ')
		print('')

# run the function to recieve the data and apply it to tablePrinter
tableData = tableData()
print('Here is the section map:')
tablePrinter(tableData)