#Patrick Devine
#C.S. in action
#10-4-19


def printTable(inputList):
    # initialize the list "colWidths" with zeroes equal to the length of the input list
    colWidths = [0] * len(inputList)

    # iterate over the input list to find the longest word in each inner list
    # if its larger than the current value, set it as the new value
    for i in range(len(inputList)):
	    for j in range(len(inputList[i])):
		    if len(inputList[i][j]) > colWidths[i]:      #Compares lenght of input list and column list
			    colWidths[i] = len(inputList[i][j])

    # assuming each inner list is the same length as the first, iterate over the input list
    # printing the x value from each inner list, right justifed to its corresponding value
    #getting right justified was most difficult part for me
    # in colWidths
    for x in range(len(inputList[0])):
	    for y in range(len(inputList)):
		    print(inputList[y][x].rjust(colWidths[y]), end = ' ') # justifies proper elements
	    print('')

printTable([['ACDC', 'TomPetty', 'Thewho', 'queen'],
             ['AliceInChains', 'BobSeger', 'Carolking', 'Davidbowie'],
             ['EricClapton', 'RollingStones', 'Ledzeppelin', 'TheKinks']])	
