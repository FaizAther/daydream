from datetime import datetime, timedelta

def StringChallenge(strParam):
    strFormat = '%I:%M%p'
    st, en = strParam.split("-")
    st_d = datetime.strptime(st, strFormat)
    en_d = datetime.strptime(en, strFormat)
    res = st_d - en_d
    if (st_d > en_d):
        res = en_d - st_d
    res = res.__str__().split(" ")[2]
    arr = res.split(":")
    return str(int(arr[0]) * 60 + int(arr[1]))


if __name__ == "__main__":
    inp1 = "12:30pm-12:00am"
    res1 = StringChallenge(inp1)
    assert res1 == "690"
    inp2 = "1:23am-1:08am"
    res2 = StringChallenge(inp2)
    assert res2 == "1425"
