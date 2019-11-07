from random import randint,choice

answer = []
possibles = []

def generateAnswer():
    while len(answer)<4:
        a = randint(1,9)
        if str(a) not in answer:
            answer.append(str(a))

def isValid(num):
    num = str(num)
    for n in num:
        if n == '0':
            return False
    n1,n2,n3,n4 = num[0],num[1],num[2],num[3]
    if n1!=n2 and n1!=n3 and n2!=n3 and n3!=n4 and n2!=n4 and n1!=n4:
        return True
    else:
        return False

def generatePossibles():
    for i in range(1234,9877):
        if isValid(i):
            possibles.append(str(i))

def checkAnswer(guess,ans):
    a_num = 0
    b_num = 0
    for i in range(4):
        if guess[i] in ans:
            b_num += 1
        if guess[i] == ans[i]:
            a_num += 1
            b_num -= 1
    return (a_num,b_num)
    
gameMode = input('1: player mode ; others: AI mode  ')

if gameMode == '1':
    generateAnswer()
    while True:
        player = input()
        print(checkAnswer(player,answer)[0],'A',checkAnswer(player,answer)[1],'B')
        if checkAnswer(player,answer)[0] == 4:
            break
else:
    generatePossibles()
    while True:
        print(len(possibles),'left')
        ai = str(choice(possibles))
        n = []
        print(ai)
        comp = input().split()
        if int(comp[0]) != 4:
            for possible in possibles:
                if checkAnswer(ai,possible)[0]==int(comp[0]) and checkAnswer(ai,possible)[1]==int(comp[1]):
                    # ~ print(ai,possible,checkAnswer(ai,possible))
                    n.append(possible)
                # ~ else:
                    # ~ possibles.remove(possible)
            possibles = n
        else:
            break
