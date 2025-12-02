

def RotateLeft(currentstate = int, clicks = int): return (currentstate - clicks)%100

def RotateRight(currentstate = int, clicks = int): return (currentstate + clicks)%100

def main():
    countedzero = 0
    currentstate = 50

    for move in open("./1_input.txt"):

        if move.startswith('L'):
            currentstate = RotateLeft(currentstate, int(move[1:].strip()))
        elif move.startswith('R'):
            currentstate = RotateRight(currentstate, int(move[1:].strip()))

        if currentstate == 0:
            countedzero += 1

    print(countedzero)



main()