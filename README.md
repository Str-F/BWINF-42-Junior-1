# BWINF-42-Junior-1
#### The first Junior Task of Bwinf 42
---
# Quick start guide
* Download the latest Version [here](https://github.com/Str-F/BWINF-42-Junior-1/releases) and unpack it on your drive
* Alternatively you can clone the Repository with Git
* Open the folder with your favorite code editor
* You can run `main.py` to see the resault
* You can change the zero in 'data/wundertuete0.txt' to a number you like, available numbers are in `data/*`
* The files in `data/*` have a scheme:
## Input
##### Each file describes a donation to the kindergarten and contains
```
- in the first line the number n of goody bags,

- in the second line the number k of game types

- and in the following k lines the number of games per game type.
```
---
* The output of `main.py` you saw earlier has this structure:

## Output
##### Example
```
DEBUG:
3 3 [7, 5, 13] # Debug Informations (Number of Bags, Number of Game Types, Number of games per Game Type)

RESULT  
[3, 1, 5] # First bag contains: 3 times first game, 1 time second game, 5 times third game  
[2, 2, 4] # Second bag...
[2, 2, 4]
```

## Testing
You may have already noticed the `testing.py` file. This file becomes interesting as soon as you modify the code. It checks whether the result of the code is correct.
* The test checks whether there is a maximum difference of 1 value in each column (Game) and each sums of the rows (Bag)
* The test also checks whether all games have been distributed

The file also compares the new (`betterfunctions.py`) and the old (`functions.py`) and determines which one is faster. In one of our tests `betterfunctions.py` was 43000x faster (wow, amazing).

© Str-F 2024
