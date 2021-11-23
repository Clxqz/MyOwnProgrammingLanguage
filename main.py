import random, os, time
arrayInt = []
variable = []
variable1 = []
breakYes = []
forRangeVAR = []
STRVARIABLE = []
INTVARIABLE = []
CHARVARIABLE = []
countSTR = 0;
countINT = 0;
countCHAR = 0;
run = True
def randomInt(choice):
  if choice.__contains__("RANDOM INT"):
    removeType = choice.replace(F"{choice[0]} RANDOM INT ", "")
    splitWord = removeType.split(",")
    randomIndex = choice.index(" RANDOM")
    newIndex = choice[0:randomIndex]
    print("")
    choice = input("")
    print("")
    if(choice.__contains__(f"OUTPUT {newIndex}") == True):
      randInteger = random.randint(int(splitWord[0]),int(splitWord[1]))
      print(randInteger)
    elif(choice.__contains__(f"OUTPUT {newIndex}") == False):
      removeOUTPUT = choice.replace("OUTPUT ", "")
      print(removeOUTPUT)

def forRange(choice):
  if choice.__contains__("FOR") and choice.__contains__("RANGE"):
    indexOf1 = choice.index("RANGE")
    newWord = choice[indexOf1:]
    removeWords = newWord.replace("RANGE ", "")
    splitIndex = removeWords.split(",")
    intFirst = splitIndex[0]
    intSecond = splitIndex[1]
    randomIndex = choice.index(" IN")
    newIndex = choice[4:randomIndex]
    forRangeVAR.append(intFirst)
    forRangeVAR.append(intSecond)
    variable1.append(newIndex)
    print("")
    choice = input("")
    print("")
    if(choice.__contains__(f"OUTPUT {newIndex}") == True):
      for w in range(int(intFirst), int(intSecond)):
         print(w)
    elif(choice.__contains__(f"OUTPUT {newIndex}") == False):
      removeOUTPUT = choice.replace("OUTPUT ", "")
      for x in range(int(intFirst), int(intSecond)):
        print(removeOUTPUT)

def whileLoop(choice):
  if choice.__contains__("WHILE "):
    removeThing = choice.replace("WHILE ", "")
    lowerText = removeThing.lower()
    run = True
    while run:
      userOutput = input("")
      if userOutput.__contains__("OUTPUT"):
        run = False
        removeWord = userOutput.replace("OUTPUT ", "")
        print()
        if breakYes.__contains__("Yes") == True:
          while lowerText.title():
             print(removeWord)
             break
        elif breakYes.__contains__("Yes") == False:
          while lowerText.title():
            print(removeWord)
            
         
      elif userOutput.__contains__("BREAK"):
        breakYes.append("Yes")
        continue

def variables(choice):
  if choice.__contains__("STRING"):
    removeLetterString = choice.replace("STRING ", "")
    stringSplit = removeLetterString.split("=")
    STRVARIABLE.append([])
    STRVARIABLE[countSTR].append(f'{stringSplit[0]} ')
    STRVARIABLE[countSTR].append(f'{stringSplit[1]}')

  if choice.__contains__("INT"):
    removeLetterString = choice.replace("INT ", "")
    intSplit = removeLetterString.split("=")
    INTVARIABLE.append([])
    INTVARIABLE[countINT].append(f'{intSplit[0]} ')
    INTVARIABLE[countINT].append(f'{intSplit[1]}')

  if choice.__contains__("CHAR"):
    removeLetterString = choice.replace("CHAR ", "")
    getIndexOFEquals = removeLetterString.index("=") + 1

    charSplit = removeLetterString.split("=")
    if len(removeLetterString[getIndexOFEquals:]) == 1:
      CHARVARIABLE.append([])
      CHARVARIABLE[countINT].append(f'{charSplit[0]} ')
      CHARVARIABLE[countINT].append(f'{charSplit[1]}')

    elif len(removeLetterString[getIndexOFEquals:]) > 1:
      print("Variable Content Doesn't Contain Char")
      




    

def clearFunction(choice):
  if choice == "CLEAR CODE":
    os.system("clear")

def printFunc(choice):
  if choice.__contains__("OUTPUT"):
    
    removeWord = choice.replace("OUTPUT ", "")
    if(removeWord.__contains__("\\N") == True):
       newWord  = removeWord.replace("\\N", "\n")
       print()
       print(newWord)
       print()
    if(removeWord.__contains__("\\N") == False):
      newCount = 0
      newRun = True
      removeVar = removeWord.replace("VAR ", "")
      if(removeWord.__contains__(f"VAR ") == True):
          while newRun:
            for x in STRVARIABLE:
              strVariable = x
              d = []
              d.append(strVariable)
              for i in d:
                for j in i:
                  newArray  = j
                  newArray1 = newArray.replace("ji", "")
                  newArray2 = newArray1.replace(f"{removeVar}", "")
                  newArray3 = newArray2.replace("", "")
                  print(newArray3)
                  newRun = False
            for x in INTVARIABLE:
              intVariable = x
              d = []
              d.append(intVariable)
              for i in d:
                for j in i:
                  newArray  = j
                  newArray1 = newArray.replace("ji", "")
                  newArray2 = newArray1.replace(f"{removeVar}", "")
                  newArray3 = newArray2.replace("", "")
                  print(newArray3)
                  newRun = False
            for x in CHARVARIABLE:
              charVariable = x
              d = []
              d.append(charVariable)
              for i in d:
                for j in i:
                  newArray  = j
                  newArray1 = newArray.replace("ji", "")
                  newArray2 = newArray1.replace(f"{removeVar}", "")
                  newArray3 = newArray2.replace("", "")
                  print(newArray3)
                  newRun = False

          newCount += 1
      elif(removeWord.__contains__("VAR ") == False):
        print()
        print(removeWord)
        print()

            
print("FUN LANGUAGE EASY")
print()
print("FIGURE IT OUT NERD NOT THAT HARD TO LEARN")
print()
while(run):
  breakYes.clear()
  userInput = input("")
  randomInt(userInput)
  forRange(userInput)
  printFunc(userInput)
  whileLoop(userInput)
  clearFunction(userInput)
  variables(userInput)
  if(userInput.__contains__("STRING")):
    countSTR += 1
  if(userInput.__contains__("INT")):
    countINT += 1
  if(userInput.__contains__("CHAR")):
    countCHAR += 1
  if userInput == "QUIT CODE":
    run = False
