# Suppose up/down limitation (1) & [7]
def compTone(ta,tb):
    import re
    pattern = re.compile(r'(.*)(\d)(.*)')
    # get dig
    dta = int(pattern.match(ta).group(2))
    dtb = int(pattern.match(tb).group(2))
    if ta[0] != tb[0]:
        if ta[0] == "[" or tb[0] == "(":
            return True
        elif ta[0] == "(" or tb[0] == "[":
            return False
        else:
            if dta == dtb:
                return len(ta) >= len(tb)
            else:
                return dta >= dtb
    else:
        if dta == dtb:
            return len(ta) >= len(tb)
        else:
            return dta >= dtb
    return dta >= dtb

def fetchInput(fpath):
    # 打开文件
    toneArr = []
    fo = open(fpath, "r+")
    print("Read File: ", fo.name)
    line = fo.read(-1)
    # Break element into array
    cnt = 0
    ##
    upL = "(1)"
    downL = "[7]"
    for i in range(0, len(line)):
        if i<cnt:
            continue
        curt = line[i]
        pt = ""
        # () []
        if (curt == "(" or curt == "[") and line[i + 1] != "#":
            pt = line[i :i + 3]
            cnt=i+3
        elif (curt == "(" or curt == "[") and line[i + 1] == "#":
            pt = line[i :i + 4]
            cnt=i+4
        elif curt == "#":
            pt = line[i :i + 2]
            cnt=i+2
        else:
            pt = line[i]
            cnt = i+1
        # Done: to sort the order before insert
        try:
            if compTone(pt,upL):
                upL = pt
            if compTone(downL, pt):
                downL = pt
        except:
        # Do nothing
            pass
        toneArr.append(pt)
    print(toneArr)
    print("Highest Tone is: " + upL)
    print("Lowest Tone is: " + downL)
    # Todo: Analyze the space for adjustment based on up/down limitation

    # 关闭文件
    fo.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Load note file
    fetchInput("input.txt")
