from timeit import timeit
from pprint import pprint

# function to read the variables in from a file at path 'filename'
def read_file(filename):
    with open(filename, "r") as f:
        bagcount = int(f.readline())
        gamescount = int(f.readline())
        games = []
        for _ in range(2, gamescount+2):
            games.append(int(f.readline()))

    return bagcount, gamescount, games
# measure the time taken for 50 repetitions
print(timeit('read_file("data/wundertuete0.txt")', number=50, globals={'read_file': read_file}))


# test with wundertuete0
bagcount, gamescount, games = read_file('data/wundertuete0.txt')

print(bagcount, gamescount, games)



def processing_data(bagcount, gamescount, games):
    # initialize list
    result = []
    for i in range(bagcount):
        result.append([0 for _ in range(gamescount)])

    # distribute games
    b = 0
    
    for i in range(gamescount):
        for e in range(games[i]):
            result[b][i] += 1
            if b == bagcount - 1:
                b = 0
            else:
                b += 1

    return result



result = processing_data(bagcount, gamescount, games)



pprint(result, width=30)