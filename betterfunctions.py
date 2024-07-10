import numpy as np

# function to read the variables in from a file at path 'filename'
def read_file(filename):
    with open(filename, "r") as f:
        bagcount = int(f.readline())
        gamescount = int(f.readline())
        games = []
        for _ in range(2, gamescount+2):
            games.append(int(f.readline()))

    return bagcount, gamescount, games


# function to compute how many games are in each bag
def processing_data(bagcount, gamescount, games):

    fullgames = []
    überbleiblesgames= []

    for i in range(len(games)):
        fullgames.append(games[i]//bagcount)
        überbleiblesgames.append(games[i] % bagcount)

    fullgames = int(np.sum(fullgames))

    # initialize list
    result = np.full((bagcount, gamescount),fullgames , np.uint16)

    # distribute games
    b = 0
    
    for i in range(gamescount):
        for e in range(überbleiblesgames[i]):
            result[b, i] += 1
            if b == bagcount - 1:
                b = 0
            else:
                b += 1

    return result


def processing_numpy():
    return