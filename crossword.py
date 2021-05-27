# Crossword Puzzle

import sys

def possible_area(crossword, w):
    length=len(w)

    for i in range(10):
        for j in range(10):
            posH=True
            posV=True

            for k in range(length):
                if j<10-length+1:
                    if crossword[i][j+k] not in ['-', w[k]]:
                        posH=False
                if i<10-length+1:
                    if crossword[i+k][j] not in ['-', w[k]]:
                        posV=False

            if posH and j<10-length+1:
                yield(i,j,0)
            if posV and i<10-length+1:
                yield(i,j,1)

def fill(crossword,w,area):
    x,y,axis=area

    if axis==0: # Horizontal
        for i in range(len(w)):
            crossword[x][y+i]=w[i]
    else:
        for i in range(len(w)):
            crossword[x+i][y]=w[i]

def erase(crossword,w,area):
    x,y,axis=area

    if axis==0: # Horizontal
        for i in range(len(w)):
            crossword[x][y+i]='-'
    else:
        for i in range(len(w)):
            crossword[x+i][y]='-'

def crosswordPuzzle(crossword, word):
    global solved
    
    if len(word)==0:
        if not solved:
            for row in crossword:
                print(''.join(row))
            solved=True
            return

    w=word.pop()

    for area in possible_area(crossword,w):
        fill(crossword,w,area)
        crosswordPuzzle(crossword, word)
        erase(crossword,w,area)

    word.append(w)

if __name__=="__main__":
    crossword=list()

    for _ in range(10):
        crossword_item=list(sys.stdin.readline().rstrip())
        crossword.append(crossword_item)

    word=str(sys.stdin.readline().rstrip()).split(';')
    
    solved=False
    crosswordPuzzle(crossword, word)
    