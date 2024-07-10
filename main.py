from betterfunctions import *


if __name__=='__main__':
    # test with wundertuete0
    bagcount, gamescount, games = read_file('data/wundertuete0.txt')
    result = np.array(processing_data(bagcount, gamescount, games), dtype=np.uint64)
    print("DEBUG:")
    print(bagcount, gamescount, games)
    print("")
    print("RESULT")
    [print(a.tolist()) for a in result]