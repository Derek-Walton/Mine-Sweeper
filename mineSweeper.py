from graphics import *
from random import *
from time import *

def drawRectangle(win, Point1, Point2):
    square = Rectangle(Point1, Point2)
    square.setFill("lightGreen")
    square.setOutline("black")
    square.draw(win)
    return square

def drawRectangleBottom(win, Point1, Point2, colour):
    square = Rectangle(Point1, Point2)
    square.setFill(colour)
    square.setOutline("black")
    square.draw(win)
    return square

def button(win, x, y, buttonText, buttonColour, buttonWidth):
    buttonBox = Rectangle(Point(x, y), Point(x + buttonWidth, y + 50))
    buttonBox.setFill(buttonColour)
    buttonBox.setOutline("black")
    buttonBox.draw(win)

    buttonTextBuild = Text(Point(x + buttonWidth/2, y + 50/2), buttonText)
    buttonTextBuild.draw(win)

    return buttonBox

def drawNumberOfMines(win, PointX, PointY, text):
    numberOfMines = Text(Point(PointX, PointY), text)
    numberOfMines.draw(win)


def buttonDeselector(buttonDictionary, x, y, colour):
    buttonDictionary[f"button{x}{y}"][0].setFill(colour)
    buttonDictionary[f"button{x}{y}"][1] = False

def buttonSelector(buttonDictionary, x, y):
    selectorColour = "grey"
    buttonDictionary[f"button{x}{y}"][0].setFill(selectorColour)
    buttonDictionary[f"button{x}{y}"][1] = True

def flagDrawing(win, x, y, squareSize):
    pole = Rectangle(Point((x + squareSize/2) - squareSize * 1/10, y + (squareSize* 2/10)), Point((x + squareSize/2), y + (squareSize * 8 / 10)))
    pole.setFill("black")

    triangle = Polygon(Point((x + squareSize/2), y + (squareSize* 2/10)), Point((x + squareSize/2) + squareSize * 3/10, y + (squareSize* 3/10)), Point((x + squareSize/2), y + (squareSize* 4/10)))
    triangle.setFill("red")

    return [pole, triangle]

def flagsPlaced(mapSizeLength, squareSize, numberOfFlagsPlaced):
    numberOfFlagsPlaced = Text(Point(mapSizeLength*3/4, mapSizeLength + squareSize*3/2), f"You've placed {numberOfFlagsPlaced} Flags")
    return numberOfFlagsPlaced



def inputMenu():
    win = GraphWin("Mine Sweeper Menu", 500, 500)

    titleText = Text(Point(250, 80), "Mine Sweeper")
    titleText.setSize(35)
    titleText.draw(win)

    difficultyText = Text(Point(250, 155), "Choose your Difficulty")
    difficultyText.setSize(15)
    difficultyText.draw(win)
    
    mapSizeText = Text(Point(250, 255), "Choose the Size")
    mapSizeText.setSize(15)
    mapSizeText.draw(win)

    tryAgainText = Text(Point(250, 410), "Choose your Difficulty and Size")
    tryAgainText.setSize(15)
    tryAgainText.setTextColor("red")

    buttonText = ["Easy", "Medium", "Hard", "Small", "Medium", "Large"]
    buttonColours = ["lightGreen", "orange", "red", "lightGreen", "orange", "red"]

    buttonDictionary = {}

    runningTotal = 0

    for y in range(175, 375, 100):
        for x in range(125, 425, 100):
            buttonDictionary[f"button{x}{y}"] = [button(win, x, y, buttonText[runningTotal], buttonColours[runningTotal], 50), False]
            runningTotal = runningTotal + 1

    submitButton = button(win, 200, 375, "Play", "lightblue", 100)
    # submitButton

    buttonSize = 50

    menuFlag = True

    alreadyDrawn = False

    selectedMapSize = ""
    selectedDifficulty = ""

    while menuFlag:
        userClick = win.getMouse()

        xClick = userClick.getX()
        yClick = userClick.getY()

        if xClick >= 200 and xClick <= 300 and yClick >= 375 and yClick <= 425:
            if buttonDictionary[f"button{325}{175}"][1] == True or buttonDictionary[f"button{225}{175}"][1] == True or buttonDictionary[f"button{125}{175}"][1] == True and buttonDictionary[f"button{325}{275}"][1] == True or buttonDictionary[f"button{225}{275}"][1] == True or buttonDictionary[f"button{125}{275}"][1] == True:
                menuFlag = False

                if buttonDictionary[f"button{125}{175}"][1] == True:
                    selectedDifficulty = "easy"
                elif buttonDictionary[f"button{225}{175}"][1] == True:
                    selectedDifficulty = "medium"
                elif buttonDictionary[f"button{325}{175}"][1] == True:
                    selectedDifficulty = "hard"

                if buttonDictionary[f"button{125}{275}"][1] == True:
                    selectedMapSize = "small"
                elif buttonDictionary[f"button{225}{275}"][1] == True:
                    selectedMapSize = "medium"
                elif buttonDictionary[f"button{325}{275}"][1] == True:
                    selectedMapSize = "large"

                win.close()
                return selectedMapSize, selectedDifficulty
            




            else:
                if alreadyDrawn:
                    pass
                else:
                    tryAgainText.draw(win)
                    alreadyDrawn = True

        elif xClick > 125 and xClick < 125 + buttonSize:
            if yClick > 175 and yClick < 175 + buttonSize:                  #Top Left
                if buttonDictionary[f"button{125}{175}"][1] == True:
                    buttonDeselector(buttonDictionary, 125, 175, "lightgreen")
                else:
                    buttonSelector(buttonDictionary, 125, 175)
                    buttonDeselector(buttonDictionary, 225, 175, "orange")
                    buttonDeselector(buttonDictionary, 325, 175, "red")
            elif yClick > 275 and yClick < 275 + buttonSize:                  #bottom Left
                if buttonDictionary[f"button{125}{275}"][1] == True:
                    buttonDeselector(buttonDictionary, 125, 275, "lightGreen")
                else:
                    buttonSelector(buttonDictionary, 125, 275)
                    buttonDeselector(buttonDictionary, 225, 275, "orange")
                    buttonDeselector(buttonDictionary, 325, 275, "red")


        elif xClick > 225 and xClick < 225 + buttonSize:
            if yClick > 175 and yClick < 175 + buttonSize:                  #Top middle
                if buttonDictionary[f"button{225}{175}"][1] == True:
                    buttonDeselector(buttonDictionary, 225, 175, "orange")
                else:
                    buttonSelector(buttonDictionary, 225, 175)
                    buttonDeselector(buttonDictionary, 125, 175, "lightgreen")
                    buttonDeselector(buttonDictionary, 325, 175, "red")
            elif yClick > 275 and yClick < 275 + buttonSize:                  #bottom middle
                if buttonDictionary[f"button{225}{275}"][1] == True:
                    buttonDeselector(buttonDictionary, 225, 275, "orange")
                else:
                    buttonSelector(buttonDictionary, 225, 275)
                    buttonDeselector(buttonDictionary, 325, 275, "red")
                    buttonDeselector(buttonDictionary, 125, 275, "lightGreen")


        elif xClick > 325 and xClick < 325 + buttonSize:
            if yClick > 175 and yClick < 175 + buttonSize:                  #Top right
                if buttonDictionary[f"button{325}{175}"][1] == True:
                    buttonDeselector(buttonDictionary, 325, 175, "red")
                else:
                    buttonSelector(buttonDictionary, 325, 175)
                    buttonDeselector(buttonDictionary, 225, 175, "orange")
                    buttonDeselector(buttonDictionary, 125, 175, "lightgreen")
            elif yClick > 275 and yClick < 275 + buttonSize:                  #bottom right
                if buttonDictionary[f"button{325}{275}"][1] == True:
                    buttonDeselector(buttonDictionary, 325, 275, "red")
                else:
                    buttonSelector(buttonDictionary, 325, 275)
                    buttonDeselector(buttonDictionary, 225, 275, "orange")
                    buttonDeselector(buttonDictionary, 125, 275, "lightGreen")

    





def recursion(win, x, y, mineDict, clearedBoxColour1 , clearedBoxColour2, mapSizeLength):


    if mineDict[f"mineDict{x}{y}"][0]:
        print("game over")

        mineDict[f"mineDict{x}{y}"][1].setFill("red")
    
    elif mineDict[f"mineDict{x}{y}"][3] > 0:
        if x % 60 == 0 and y % 60 == 0 or (x + 30) % 60 == 0 and (y + 30) % 60 == 0:
            clearedBoxColour = clearedBoxColour1
        else:
            clearedBoxColour = clearedBoxColour2
        mineDict[f"mineDict{x}{y}"][1].setFill(clearedBoxColour)
        drawNumberOfMines(win, x + 15, y + 15, mineDict[f"mineDict{x}{y}"][3])
        

    elif mineDict[f"mineDict{x}{y}"][3] == 0:
        for y2 in range(y - 30, y + 60, 30):
            for x2 in range(x - 30, x + 60, 30):

                if x2 % 60 == 0 and y2 % 60 == 0 or (x2 + 30) % 60 == 0 and (y2 + 30) % 60 == 0:
                    clearedBoxColour = clearedBoxColour1
                else:
                    clearedBoxColour = clearedBoxColour2
                if x2 < 0 or x2 >= mapSizeLength or y2 < 0 or y2 >=mapSizeLength:
                    pass
                else:
                    mineDict[f"mineDict{x2}{y2}"][1].setFill(clearedBoxColour)
                if mineDict[f"mineDict{x2}{y2}"][3] != 0:
                    if x2 < 0 or x2 >= mapSizeLength or y2 < 0 or y2 >= mapSizeLength:
                        pass
                    else:
                        drawNumberOfMines(win, x2 + 15, y2 + 15, mineDict[f"mineDict{x2}{y2}"][3])
                

                if y2 == y and x2 == x:
                    mineDict[f"mineDict{x}{y}"][2] = True
                    
                elif mineDict[f"mineDict{x2}{y2}"][3] == 0 and mineDict[f"mineDict{x2}{y2}"][2] == False:
                    mineDict[f"mineDict{x}{y}"][2] = True
                    recursion(win, x2, y2, mineDict, clearedBoxColour1, clearedBoxColour2, mapSizeLength)
                else:
                    pass




def mineSweeperCreation(mapSize, difficulty):
    if mapSize == "small":
        mapSize = 10
    elif mapSize == "medium":
        mapSize = 20
    elif mapSize == "large":
        mapSize = 30
    
    if difficulty == "easy":
        difficulty = 15
    elif difficulty == "medium":
        difficulty = 20
    elif difficulty == "hard":
        difficulty = 25

    squareSize = 30             # the size of the squares
    chanceOfMine = difficulty   # difficulty is the % of mines out of the total

    win = GraphWin("Mine Sweeper", mapSize * squareSize, (mapSize * squareSize) + 60)
    mapSizeLength = mapSize * squareSize

    mineDict = {}           #dictornary that tells wether theres are mine at the coordinate [0] and stores the draw as [1]

    flagDict = {}           #Flag dictionary to keep track of the flags

    clearedBoxColour1 = "white"
    clearedBoxColour2 = "beige"

    numberOfMinesTotal = 0

    for y in range(0, mapSizeLength, squareSize):
        for x in range(0, mapSizeLength, squareSize):

            randomNumber = randint(1, 101)
            if randomNumber <= chanceOfMine:
                mineDict[f"mineDict{x}{y}"] = [True, drawRectangle(win, Point(x, y), Point(x + squareSize, y + squareSize)), False]
                flagDict[f"flagDict{x}{y}"] = [flagDrawing(win, x, y, squareSize), False]
                numberOfMinesTotal = numberOfMinesTotal + 1
            else:
                mineDict[f"mineDict{x}{y}"] = [False, drawRectangle(win, Point(x, y), Point(x + squareSize, y + squareSize)), False]
                flagDict[f"flagDict{x}{y}"] = [flagDrawing(win, x, y, squareSize), False]

    # creates the edge border of empty boxes
    for y in range(- squareSize, mapSizeLength + squareSize, squareSize):
        for x in range(- squareSize, mapSizeLength + squareSize, squareSize):
            if y < 0 or y >= mapSizeLength or x < 0 or x >= mapSizeLength:
                mineDict[f"mineDict{x}{y}"] = [False, "drawRectangle(win, Point(x, y), Point(x + squareSize, y + squareSize))", False, -1]



    for y in range(0, mapSizeLength, squareSize):
        for x in range(0, mapSizeLength, squareSize):

        # visibley Draws the mines for testing purposes
            # if mineDict[f"mineDict{x}{y}"][0]:
            #     mineDict[f"mineDict{x}{y}"][1].setFill("red")
            
            numberOfMinesAroundBox = 0

            for y2 in range(y - 30, y + 60, 30):
                for x2 in range(x - 30, x + 60, 30):
                    if mineDict[f"mineDict{x2}{y2}"][0]:
                        numberOfMinesAroundBox = numberOfMinesAroundBox + 1
                
            if not mineDict[f"mineDict{x}{y}"][0]:
                mineDict[f"mineDict{x}{y}"].append(numberOfMinesAroundBox)

            
    drawRectangleBottom(win, Point(0, mapSizeLength), Point((mapSizeLength), (mapSizeLength) + 60), "white")

    switchModeButton = button(win, 5, mapSizeLength + 5, "Flag Mode", "lightblue", (mapSizeLength/2) -5)

    numberOfMinesTotalText = Text(Point(mapSizeLength*3/4, mapSizeLength + squareSize/2), f"Total Number of Mines: {numberOfMinesTotal}")
    numberOfMinesTotalText.draw(win)

    numberOfFlagsPlaced = 0

    
            
    clearMode = True
    flagMode = False

    while True:
        while clearMode:
            userClick = win.getMouse()
            if userClick.getX() >=  5 and userClick.getX() <= (mapSize * squareSize)/2 - 5 and userClick.getY() >= (mapSize * squareSize) + 5 and userClick.getY() <= (mapSize * squareSize) + 55:
                clearMode = False
                flagMode = True
                switchModeButton.setFill("red")
            else:


                for y in range(0, mapSizeLength, squareSize):
                        for x in range(0, mapSizeLength, squareSize):
                            if userClick.getX() - x <= squareSize and userClick.getX() - x > 0 and userClick.getY() - y <= squareSize and userClick.getY() - y > 0:
                                
                                recursion(win, x, y, mineDict, clearedBoxColour1, clearedBoxColour2, mapSizeLength)
        while flagMode:
            mineFlag = flagsPlaced(mapSizeLength, squareSize, numberOfFlagsPlaced)
            mineFlag.draw(win)
            userClick = win.getMouse()
            if userClick.getX() >=  5 and userClick.getX() <= (mapSize * squareSize)/2 - 5 and userClick.getY() >= (mapSize * squareSize) + 5 and userClick.getY() <= (mapSize * squareSize) + 55:
                clearMode = True
                flagMode = False
                switchModeButton.setFill("lightblue")
            else:
                for y in range(0, mapSizeLength, squareSize):
                        for x in range(0, mapSizeLength, squareSize):
                            if userClick.getX() - x <= squareSize and userClick.getX() - x > 0 and userClick.getY() - y <= squareSize and userClick.getY() - y > 0 and flagDict[f"flagDict{x}{y}"][1] == False:
                                for i in range(0, 2):
                                    flagDict[f"flagDict{x}{y}"][0][i].draw(win)
                                flagDict[f"flagDict{x}{y}"].remove(False)
                                flagDict[f"flagDict{x}{y}"].append(True)
                                numberOfFlagsPlaced = numberOfFlagsPlaced + 1
                            elif userClick.getX() - x <= squareSize and userClick.getX() - x > 0 and userClick.getY() - y <= squareSize and userClick.getY() - y > 0 and flagDict[f"flagDict{x}{y}"][1] == True:
                                for i in range(0, 2):
                                    flagDict[f"flagDict{x}{y}"][0][i].undraw()
                                flagDict[f"flagDict{x}{y}"].remove(True)
                                flagDict[f"flagDict{x}{y}"].append(False)
                                numberOfFlagsPlaced = numberOfFlagsPlaced - 1
            mineFlag.undraw()





        
                                    








def main():
    mapSize, difficulty = inputMenu()
    mineSweeperCreation(mapSize, difficulty)
main()