from timeit import timeit

# function to read the variables in from a file at path 'filename'
def read_file(filename):
    with open(filename, "r") as f:
        bagcount = int(f.readline())
        gamescount = int(f.readline())
        games = []
        for i in range(2, gamescount+2):
            games.append(int(f.readline()))

    return bagcount, gamescount, games
# measure the time taken for 50 repetitions
print(timeit('read_file("data/wundertuete0.txt")', number=50, globals={'read_file': analys_file}))


# test with wundertuete0
bagcount, gamescount, games = read_file('data/wundertuete0.txt')

print(bagcount, gamescount, games)
