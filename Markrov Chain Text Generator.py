import re
import random


finallist = []
text = str(input("Write your text: "))
n = 0
text = re.sub('[^A-Za-z ]', '', text)
text = re.sub(' +', ' ', text)
text = text.lower()
text = text.capitalize()
if text[0].isspace():
    text = text[1:]
if text[len(text)-1].isspace():
    text = text[:-1]
length = input("Input the Markrov chain length: ")
listtext = list(text.split(" "))
if len(listtext)>=5:
    finallist.append(listtext[n])
    for i in range(0, len(listtext)-1):
        appearancelist = []
        o = 0
        for m in listtext:
            if listtext[o] == finallist[n]:
                if o+1 != len(listtext):
                    appearancelist.append(listtext[o+1])
                else:
                    appearancelist.append(listtext[random.randrange(len(listtext)-2)])
            o = o + 1
        t = random.randint(0,len(appearancelist)-1)
        finallist.append(appearancelist[t])
        if n != len(listtext)-1:
            n = n+1
    if int(length) <= len(finallist)-2:
        l = random.randint(0,len(finallist)-1-int(length))
        del finallist[l + int(length):len(finallist)]
        del finallist[0:l]
        finaltext = ' '.join(finallist)
        finaltext = finaltext.capitalize()
        print(finaltext)
    else:
        print("The length you gave is too big")
else:
    print('Your text must be at least 5 words long')
xD = input()


