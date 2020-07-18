import random

#list of swapping choices, would be made larger for a real password generator
def swapChar(char):
    if char == 'a':
        swaps = ['A','@']
        return random.choice(swaps)
    elif char == 'b':
        swaps = ['B','&']
        return random.choice(swaps)
    elif char == 'c':
        swaps = ['C','(']
        return random.choice(swaps)
    elif char == 'd':
        swaps = ['D','>']
        return random.choice(swaps)
    elif char == 'e':
        swaps = ['E','3']
        return random.choice(swaps)
    elif char == 'f':
        swaps = ['F','4']
        return random.choice(swaps)
    elif char == 'g':
        swaps = ['G','6']
        return random.choice(swaps)
    elif char == 'h':
        swaps = ['H','#']
        return random.choice(swaps)
    elif char == 'i':
        swaps = ['I','1']
        return random.choice(swaps)
    elif char == 'j':
        swaps = ['J','%']
        return random.choice(swaps)
    elif char == 'k':
        swaps = ['K','{']
        return random.choice(swaps)
    elif char == 'l':
        swaps = ['L','[']
        return random.choice(swaps)
    elif char == 'm':
        swaps = ['M','/']
        return random.choice(swaps)
    elif char == 'n':
        swaps = ['N','^']
        return random.choice(swaps)
    elif char == 'o':
        swaps = ['O','0']
        return random.choice(swaps)
    elif char == 'p':
        swaps = ['P','~']
        return random.choice(swaps)
    elif char == 'q':
        swaps = ['Q','9']
        return random.choice(swaps)
    elif char == 'r':
        swaps = ['R','}']
        return random.choice(swaps)
    elif char == 's':
        swaps = ['S','$']
        return random.choice(swaps)
    elif char == 't':
        swaps = ['T','+']
        return random.choice(swaps)
    elif char == 'u':
        swaps = ['U','_']
        return random.choice(swaps)
    elif char == 'v':
        swaps = ['V','!']
        return random.choice(swaps)
    elif char == 'w':
        swaps = ['W','/']
        return random.choice(swaps)
    elif char == 'x':
        swaps = ['X','*']
        return random.choice(swaps)
    elif char == 'y':
        swaps = ['Y','+']
        return random.choice(swaps)
    elif char == 'z':
        swaps = ['Z','5']
        return random.choice(swaps)
    return char

#Updates the word with the swapped character in the position    
def updateWord(word,index):
    newWord = word[0:index] + swapChar(word[index]) + word[index+1:len(word)]
    return newWord

#In practice this would be the entire dictionary, but that would take too much space for this small proof of concept
words_list = ["enteric", "ingenuity", "unrefining", "epistolic", "godiva", "stegodont", "armagnac", "pourable", "norw", "instigator", "reequipped", "pricker", "adel", "shortly", "tailband", "unfawning", "deadwood", "pinguid", "americanised", "bister"]

passLength = -1

while (passLength < 8):
    try:
        passLength = int(input("Enter a length for password (>= 8): "))
    except ValueError:
        print("Not an integer value...")

valid_words = []

for WORD in words_list:
    if len(WORD) <= passLength:
        valid_words.append(WORD)

startWord = random.choice(valid_words)
swappedWord = startWord
#for i in range(0,len(startWord)):
  #  x = random.randint(0, len(startWord)-1)
 #   newWord = startWord[0:x] + swapChar(startWord[x]) + startWord[x+1:len(startWord)]

for i in range(0,int(len(startWord)/2)):
    x = random.randint(0, len(startWord)-1)
    swappedWord = updateWord(swappedWord,x)

numbers = ['0','1','2','3','4','5','6','7','8','9']
upperC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowerC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ["`","~","!","@","#","$","%","^","&","*","(",")","_","-","+","=","]","}","[","{","|",";",":","|","<",">","/","?"]

needCheck = True

while needCheck == True:
    containsNum = False
    containsUpC = False
    containsLwrC = False
    containsSmbl = False
    
    for x in numbers:
        if x in swappedWord:
            containsNum = True
    for x in upperC:
        if x in swappedWord:
            containsUpC = True
    for x in lowerC:
        if x in swappedWord:
            containsLwrC = True
    for x in symbols:
        if x in swappedWord:
            containsSmbl = True
    
    if containsNum == False:
        swappedWord+=(random.choice(numbers))
        containsNum = True
    if containsUpC == False:
        swappedWord+=(random.choice(upperC))
        containsUpC = True
    if containsLwrC == False:
        swappedWord+=(random.choice(lowerC))
        containsLwrC = True
    if containsSmbl == False:
        swappedWord+=(random.choice(symbols))
        containsSmbl = True
    
    needCheck = False
    
    while len(swappedWord) < passLength:   
        swappedWord += random.choice([random.choice(numbers),random.choice(upperC),random.choice(lowerC),random.choice(symbols)])
    
    while len(swappedWord) > passLength:
        swappedWord = swappedWord.replace(swappedWord[random.randint(0,len(swappedWord)-1)], "")
        needCheck = True
    
print (startWord)
print (swappedWord)

