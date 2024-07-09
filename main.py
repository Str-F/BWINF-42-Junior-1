from timeit import timeit

# function to read the variables in from a file
def analys_file(filename):
    with open(filename, "r") as f:
        bagcount = int(f.readline())
        gamescount = int(f.readline())
        games = []
        for i in range(2, gamescount+2):
            games.append(int(f.readline()))

    return bagcount, gamescount, games

bagcount, gamescount, games = analys_file('data/wundertuete0.txt')
print(timeit('analys_file("data/wundertuete0.txt")', number=50, globals={'analys_file': analys_file}))

print(bagcount, gamescount, games)
