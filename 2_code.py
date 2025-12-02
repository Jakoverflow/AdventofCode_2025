def main():
    sum = 0
    input = open("./2_input.txt").read().split(',')
    for idrange in input:
        for id in range(int(idrange.split('-')[0]), int(idrange.split('-')[1])+1):
            id1 = str(id)[:int((len(str(id))/2))]
            id2 = str(id)[int((len(str(id))/2)):]
            if id1 == id2:
                sum += id
                print('got one: ', id)

    print(sum)

main()