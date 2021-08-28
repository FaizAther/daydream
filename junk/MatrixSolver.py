"""
MATRIX
"""

AXIS = [
    (-1,-1),(+0,-1),(+1,-1),
    (-1,+0),        (+1,+0),
    (-1,+1),(+0,+1),(+1,+1)
]

def letter_find(matrix, X, Y, start, letter):
    if start == None:
        return False, []
    coordinates = []
    found = False
    for a in AXIS:
        x,y = start
        _x, _y = a
        x += _x
        y += _y
        if ((not (x >= X or x < 0 or y >= Y or y < 0)) and letter == matrix[y][x]):
            coordinates.append((x,y))
            found = True

    return found, coordinates

def word_find(matrix, X, Y, data, word, starts):
    if len(word) == 1 or word == "":
        return True
    if starts == None:
        return False

    for start in starts:
        found, coordinates = letter_find(matrix, X, Y, start, word[1])
        if found and word_find(matrix, X,Y,data,word[1:], coordinates):
            return True
            
    return False

def construct_matrix(words):
    matrix = []
    data = {}
    x, y = (0,0)
    for word in words.split(", "):
        row = []
        x = 0
        for letter in word:
            row.append(letter)
            var = data.get(letter)
            if var == None:
                data[letter] = [(x, y)]
            else:
                data[letter].append((x,y))
            x += 1
        matrix.append(row)
        y += 1
    return matrix, data

def run(words, check):
    matrix, data = construct_matrix(words)
    cannot = []
    X = len(matrix[0])
    Y = len(matrix)
    for word in check.split(","):
        if not (word_find(matrix, X, Y, data, word, data.get(word[0]))):
            cannot.append(word)
    return cannot

def main():
    TESTS = []
    TESTS.append([["aaey, rrum, tgmn, ball", "all,ball,mur,raeymnl,tall,true,trum"], []])
    TESTS.append([["aaey, rrum, tgmn, ball", "all,ball,mur,raeymnl,rumk,tall,true,trum,yes"], ['rumk', 'yes']])

    for test in TESTS:
        print("TEST:\t", test)
        res = run(test[0][0], test[0][1])
        assert(res == test[1])
        print("PASSED")

if __name__ == "__main__":
	main()