import random

def shufflePass(string):
    tempList = list(string)
    random.shuffle(tempList)
    string = ''.join(tempList)
    print(string)

upperCaseLetter1 = chr(random.randint(65, 90))
upperCaseLetter2 = chr(random.randint(65, 90))
numberOne = chr(random.randint(0, 9))
numberTwo = chr(random.randint(0, 9))
lowerCaseLetter1 = chr(random.randint(97, 122))
lowerCaseLetter2 = chr(random.randint(97, 122))
specialSign1 = chr(random.randint(33, 47))
specialSign2 = chr(random.randint(33, 47))
password = upperCaseLetter1 + upperCaseLetter2 + specialSign1 + specialSign2 + numberOne + numberTwo + lowerCaseLetter1 + lowerCaseLetter2
shufflePass(password)