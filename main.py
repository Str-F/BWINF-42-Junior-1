def readline(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines

lines = readline("data/wundertuete0.txt")

print(lines)

lines