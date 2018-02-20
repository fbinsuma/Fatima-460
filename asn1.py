"""This program is the 8 puzzle solver from assignment 1 the program takes in a puzzle from the user tries to solve it
in the fast way using A* manhatan distance. Since the cost of each step is the same the counter is not used.
Student Name: Fatima Bin Sumait
Student ID:1552510
Date: 2018-02-19
Version: 5
"""

##This class is where most of the logic happens##
class Puzzle():

    #This function is where the initialization takes place
    def __init__(self, copy, copyone, copyTwo, copyThree, zeroPosition):
        self.copy = copy
        self.copyone = copyone
        self.copyTwo = copyTwo
        self.copyThree = copyThree
        self.zeroPosition = zeroPosition
        self.counter = 0
        self.children = []
        self.numOfMisplaced = 0
        self.moveUp()
        self.moveDown()
        self.moveRight()
        self.moveLeft()
        self.childrenGetter()
        self.goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.childOne = self.children[0]
        self.childTwo = self.children[1]
        self.childThree = self.children[2]
        self.childThree = self.children[3]
        self.value = 0
        self.childChooser()
        self.childGetter()

    # This function moves the zero to the up
    def moveUp(self):
        row = self.zeroPosition[0]
        col = self.zeroPosition[1]
        if row - 1 < 0:
            self.copy = None
        else:
            newNum = self.copy[row][col]
            oldNum = self.copy[row - 1][col]
            self.copy[row - 1][col] = newNum
            self.copy[row][col] = oldNum
            self.counter = self.counter + 1
        self.children.append(self.copy)

    # This function moves the zero to the down
    def moveDown(self):
        row = self.zeroPosition[0]
        col = self.zeroPosition[1]
        if row + 1 > 2:
            self.copyone = None
        else:
            newNum = self.copyone[row][col]
            oldNum = self.copyone[row + 1][col]
            self.copyone[row + 1][col] = newNum
            self.copyone[row][col] = oldNum
            self.counter = self.counter + 1
        self.children.append(self.copyone)

    # This function moves the zero to the right
    def moveRight(self):
        row = self.zeroPosition[0]
        col = self.zeroPosition[1]
        if col + 1 > 2:
            self.copyTwo = None
        else:
            newNum = self.copyTwo[row][col]
            oldNum = self.copyTwo[row][col + 1]
            self.copyTwo[row][col + 1] = newNum
            self.copyTwo[row][col] = oldNum
            self.counter = self.counter + 1
        self.children.append(self.copyTwo)

    # This function moves the zero to the left
    def moveLeft(self):
        row = self.zeroPosition[0]
        col = self.zeroPosition[1]
        if col - 1 < 0:
            self.copyThree = None
        else:
            newNum = self.copyThree[row][col]
            oldNum = self.copyThree[row][col - 1]
            self.copyThree[row][col - 1] = newNum
            self.copyThree[row][col] = oldNum
            self.counter = self.counter + 1
        self.children.append(self.copyThree)


    #Assigns matrix values to lists
    def valueAssigner(self, child):
        board = child
        values = {}

        for i in range(3):
            for j in range(3):
                key = board[i][j]
                values[key] = [i, j]

        return values

    #calculates manhatan using martix cooridnate values
    def manhantanCalc(self, other, goal):
        sumOfAll = 0
        sum = 0
        for i in range(0, 9):
            if other[i] == goal[i]:
                sum = sum + 0
            else:
                first = (other[i][0]) - (goal[i][1])
                second = (goal[i][0]) - (other[i][1])
                sum = abs(first) + abs(second)
                sumOfAll = sumOfAll + sum
        return (sumOfAll)

    #chooses which way it will proceeds based on minimum value
    def childChooser(self):

        goalBoard = self.goal
        goal = self.valueAssigner(goalBoard)

        """These if statements makes sure you are not choocsing a none possible solution"""
        if self.children[0] == None:
            valueForUp = 20000000000000000000000000000000000
        else:
            up = self.valueAssigner(self.children[0])
            valueForUp = self.manhantanCalc(up, goal)


        if self.children[1] == None:
            valueForDown = 20000000000000000000000000000000000
        else:
            down = self.valueAssigner(self.children[1])
            valueForDown = self.manhantanCalc(down, goal)


        if self.children[2] == None:
            valueForRight = 20000000000000000000000000000000000
        else:
            right = self.valueAssigner(self.children[2])
            valueForRight = self.manhantanCalc(right, goal)


        if self.children[3] == None:
            valueForLeft = 20000000000000000000000000000000000
        else:
            left = self.valueAssigner(self.children[3])
            valueForLeft = self.manhantanCalc(left, goal)

        """gets the minimum value and compares it to the values that it chooses the lowest number"""
        minimum = min(valueForUp, valueForDown, valueForRight, valueForLeft)

        "Chooses the puzzle index with the minimum value"
        if valueForUp == minimum:
            self.value = 0
        if valueForDown == minimum:
            self.value = 1
        if valueForRight == minimum:
            self.value = 2
        if valueForLeft == minimum:
            self.value = 3

    #This function gets the list after the zero is moved
    #@Retun: self.child
    def childGetter(self):
        return self.children[self.value]


    #This function gets the counter decided not to use since all costs are equal
    #@Retun: self.counter
    def counterGetter(self):
        return self.counter


    #This function gets the list of children if needed --> used for testing
    #@Retun: self.children
    def childrenGetter(self):
        return self.children

    def __str__(self):
        print(self.puzzle)

#This fuction is the goal state checker
def isGoal(initial):
    goal = [[0,1,2],[3,4,5],[6,7,8]]

    if initial == goal:
        stopper = True
    else:
        stopper = False
    return stopper

#This fuction finds the zeroPostion and returs it
def findingTheZero(puzzle):
    zeroPosition = [0,0]

    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                zeroPosition[0] = i
                zeroPosition[1] = j
    return zeroPosition

#This fuction prints the list in proper form
def printing(list):
    for i in range(len(list)):
        print(list[i], '\n')

#This fuction is where everything will run
def solution(initialPuzzle, counter):
    print('Puzzle: \n')
    printing(initialPuzzle)
    puzzle = initialPuzzle
    copy = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    copyone = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    copyTwo = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    copyThree = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            copy[i][j] = puzzle[i][j]
            copyone[i][j] = puzzle[i][j]
            copyTwo[i][j] = puzzle[i][j]
            copyThree[i][j] = puzzle[i][j]

    """This if statement checks if users puzzle matches the goal or not if not it solves it """
    if isGoal(initialPuzzle) == True:
        print('The solved Puzzle: \n')
        printing(initialPuzzle)
        print('Totol Number of steps: ', counter)
        return initialPuzzle
    else:
        counter = counter + 1
        puzz = Puzzle(copy, copyone, copyTwo, copyThree, findingTheZero(initialPuzzle))
        if isGoal(puzz.childGetter()) == True:
            print('The Puzzle is solved: \n')
            printing(puzz.childGetter())


            return puzz.childGetter()
        else:
            solution(puzz.childGetter(), counter + 1)
            counter = counter + 1
        print('Totol Number of steps: ', counter)

#This fuction prompts user for input
def userPrompt():
    initialPuzzle = [[0,0,0],[0,0,0],[0,0,0]]

    for i in range(3):
        for j in range(3):
            print('[', i,' ', j, ']')
            userInput = int(input('Please enter the number in the above position remember to include a zero: '))
            initialPuzzle[i][j] = userInput

    return (initialPuzzle)


#Calls to start the program
counter = 0
initialPuzz = userPrompt()
solution(initialPuzz, counter)