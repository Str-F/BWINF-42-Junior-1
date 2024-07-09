from functions import *


if __name__=='__main__':
    # test with wundertuete0
    bagcount, gamescount, games = read_file('data/wundertuete0.txt')
    result = processing_data(bagcount, gamescount, games)
    print("DEBUG:")
    print(bagcount, gamescount, games)
    print("")
    print("RESULT")
    [print(a) for a in result]