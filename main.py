def analys_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    bagcount = int(lines[0])
    gamescount = int(lines[1])
    games = []
    for i in range(2, gamescount+2):
        games.append(int(lines[i]))

    return bagcount, gamescount, games

bagcount, gamescount, games = analys_file("data/wundertuete0.txt")

print(bagcount, gamescount, games)