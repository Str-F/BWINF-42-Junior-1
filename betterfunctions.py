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
    games = np.array(games, dtype=np.uint64)

    fullgames, remaininggames = np.divmod(games, bagcount)

    e = np.array(fullgames).reshape(1, -1)
    f = np.ones(bagcount).reshape(-1, 1)

    result = e*f
    
    # distribute games
    b = 0

    def fill_between(array, column, start, end):
        if end == start:
            return
        elif end > start:
            array[start:end, column] += 1
        else:
            array[:, column] += 1
            array[end:start, column] -= 1
        # no return statement needed, since np-array is passed by reference

    start = 0

    for i, game in enumerate(remaininggames): # game = remainggames[i]
        end = (start+game)%bagcount
        fill_between(result, i, start, end)
        start = end
    
    return result


def processing_numpy():
    return


