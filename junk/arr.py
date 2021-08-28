
def extract(val):
    return list(map(int, val.split(":")))

def canGo(charge, arr_v):
    return charge + arr_v[0] - arr_v[1]

def tryGo(charge, s_pos, arr, n_left):
    # print(charge, s_pos, arr, n_left)
    
    if n_left == 0:
        return True
    charge = canGo(charge, arr[s_pos])
    if charge < 0:
        return False
    else:
        return tryGo(charge, (s_pos + 1) % len(arr), arr, n_left - 1)
    return None

def ArrayChallenge(strArr):
    n = int(strArr[0])
    i =0 
    arr = list(map(extract, strArr[1:]))
    while i < n:
        if tryGo(0, i, arr, n):
            return i+1
        i+=1

    return "impossible" 


if __name__ == "__main__":
        
    inp2 = ["4", "0:1", "2:2", "1:2", "3:1"]
    out2 = 4 
    res2 = ArrayChallenge(inp2)
    assert res2 == out2

    inp1 = ["4", "1:1", "2:2", "1:2", "0:1"]
    out1 = "impossible"
    res1 = ArrayChallenge(inp1)
    assert res1 == out1

