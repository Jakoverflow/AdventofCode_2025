
# countedzero = 0

def RotateLeft(currentstate = int, clicks = int): 
    # print(currentstate, clicks)
    # print(currentstate - clicks)
    # print(int((currentstate - clicks)), (currentstate - clicks) / 100)
    # print()
    res = currentstate - clicks
    zeros = 0
    print(res)
    if (res) < 0:
        if currentstate != 0:
            zeros = 1
        if -int((res)/100) >= 1:
            zeros +=  -int((res)/100)
            zeros += 1
            print('links zero', zeros)
        # elif currentstate != 0:
        #     zeros = 1
        # # zeros = 1 + -int((res)/100)
        # elif currentstate > (res)%100:
        #     zeros += 1
        # print((res) / 100)
        # print(zeros)
    elif res == 0:
        zeros = 1

    return (res)%100, zeros

def RotateRight(currentstate = int, clicks = int): 

    return (currentstate + clicks)%100, int((currentstate + clicks) / 100)

def main():
    countedzero = 0
    currentstate = 50

    for move in open("./1_input.txt"):
        print('-------- new ---------', move.strip())
        print("Current", currentstate)
        print("Zeros", countedzero)

        if move.startswith('L'):
            currentstate, zeros = RotateLeft(currentstate, int(move[1:].strip()))
        elif move.startswith('R'):
            currentstate, zeros = RotateRight(currentstate, int(move[1:].strip()))
            print('rechts',zeros)
        countedzero += zeros
        # if currentstate == 0:
        #     countedzero += 1
        print("Zeros", countedzero, "cur", currentstate)


    print(countedzero)



main()