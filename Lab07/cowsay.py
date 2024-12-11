import sys
from heifer_generator import HeiferGenerator
def list_cows(cows):
    print('Cows available: ', end='')
    for cow in cows:
        print(cow.name, end=' ')
def find_cow(cows, name):
    for cow in cows:
        if cow.name == name:
            return cow
    return None

if __name__ == '__main__':
    cows = HeiferGenerator.get_cows()
    if sys.argv[1] == '-l':
        list_cows(cows)
        pass
    elif sys.argv[1] == '-n':
        cow = find_cow(cows, sys.argv[2])
        if cow == None:
            print('Could not find', sys.argv[2], 'cow!')
            pass
        else:
            print()
            for word in sys.argv[3:]:
                print(word, end=' ')
            print()
            print(cow.image)
            pass
    else:
        for word in sys.argv[1:]:
            print(word, end=' ')
        print()
        print(cows[0].image)
        pass