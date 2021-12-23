import math
import os
import time
import keyboard

Turn = 1
PosList = ["0", "0", "0", "0", "0", "0", "0", "0", "0"]

YInc = 4
XInc = 4

SelectUnit = 0

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

Symbols = {
    0:" ",
    1:"O",
    2:"X",
    3:"#"
}

Players = {
    1:"O",
    2:"X"
}

Directions = {
    1:[-1,-1],
    2:[0,-1],
    3:[1,-1],
    4:[1, 0],
    5:[1, 1],
    6:[0, 1],
    7:[-1, 1],
    8:[-1, 0]
}

WinPatterns = [
    [0, 1, 2], [6, 7, 8], [0, 3, 6], [0, 4, 8], [2, 4, 6], [2, 5, 8], [3, 4, 5], [1, 4, 7]
]

def XYtoUnit(x, y):
    if x >= 0 and y >= 0:
        row = y*3
        return row + x
    else:
        return -1

def UnitToXY(Unit):
    Y = math.floor(Unit/3)
    X = Unit - Y
    return X, Y

def drawGame():
    cls()
    print("Current Turn: " + Players[Turn])
    for y in range(0, 3):
            for i in range(0, 3):
                Pos = i * y
                if i == 1:
                    Signs = []
                    for x in range(0, 3):
                        Pos = XYtoUnit(x, y)
                        PosValue = int(PosList[Pos])
                        if Pos == SelectUnit:
                            Signs.append(Symbols[3])
                        else:
                            Signs.append(Symbols[PosValue])

                    print(" {} | {} | {} \n".format(Signs[0], Signs[1], Signs[2]))
            if y < 2:
                print("-" * 12)

def winScreen(drawOrWin):
    drawGame()
    if drawOrWin == 'Draw':
        print("Draw!")
    else:
        print(drawOrWin + " won!")
    print("Enter to restart!")
    keyboard.wait('enter')
    time.sleep(1/15)

while True:
    Loop = True
    SelectUnit = max(min(SelectUnit, 8), 0)
    drawGame()
    print('Select Unit: ' + str(SelectUnit + 1))
    while Loop:
        for player in range(1, 3):
            for pattern in WinPatterns:
                Win = True
                for Space in pattern:
                    if int(PosList[Space]) != player:
                        Win = False
                if Win:
                    winScreen(Symbols[player])
                    Turn = 1
                    PosList = ["0", "0", "0", "0", "0", "0", "0", "0", "0"]
                    Loop = False
        IsFilled = True
        for i in range(len(PosList)):
            if int(PosList[i]) == 0:
                IsFilled = False
        if IsFilled:
            drawGame()
            winScreen("Draw")
            Turn = 1
            PosList = ["0", "0", "0", "0", "0", "0", "0", "0", "0"]
            Loop = False
        try:
            
            if keyboard.is_pressed('w'):
                print('Move Up')
                SelectUnit -= 3
                time.sleep(1/15)
                break  # finishing the loop
            elif keyboard.is_pressed('s'):
                print('Move Down')
                SelectUnit += 3
                time.sleep(1/15)
                break  # finishing the loop
            elif keyboard.is_pressed('a'):
                print('Move Left')
                SelectUnit -= 1
                time.sleep(1/15)
                break  # finishing the loop
            elif keyboard.is_pressed('d'):
                print('Move Right')
                SelectUnit += 1
                time.sleep(1/15)
                break  # finishing the loop
            elif keyboard.is_pressed('enter'):
                print('Enter')
                PValue = SelectUnit+1
                print(PValue)
                if PValue >= 1 and PValue <= 9:
                    if PosList[PValue - 1] == "0":
                        PosList[PValue - 1] = str(Turn)
                        if Turn == 1:
                            Turn = 2
                        else:
                            Turn = 1
                        Loop = False
                time.sleep(1/15)
        except:
            break
