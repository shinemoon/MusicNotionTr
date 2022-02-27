# Suppose up/down limitation (1) & [7]
def demapTone(ta):
    ret = ""
    if ta == -1:
        ret = "\n"
        return ret
    absT = ta%12
    if absT <5:
        ret = "%d"%(int(absT/2) + 1)
        if absT%2 == 1:
            ret = "#" + ret
    else:
        ret = "%d"%(int((absT+1)/2) + 1)
        if absT%2 == 0:
            ret = "#" + ret
    if ta <= 11:
        ret = "("+ret+")"
    elif ta > 23:
        ret = "[" + ret + "]"
    return ret

def mapTone(ta):
    ret = 0
    #map Tone to real number steps
    # (1) = 0
    # [#7] = 30
    import re
    pattern = re.compile(r'(.*)(\d)(.*)')
    # get dig
    try:
        dta = int(pattern.match(ta).group(2))
        # Number
        if dta < 4:
            ret = (dta-1) * 2
        else:
            ret = (dta-4)*2 + 5
        #  [/)
        if re.match(r'.*\[.*', ta) is not None:
            ret = ret + 24
        elif re.match(r'.*\(.*', ta) is not None:
            ret = ret
        else:
            ret = ret + 12
        # \#
        if re.match(r'.*#.*', ta) is not None:
            ret = ret + 1
    except:
        ret = -1
    return ret
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
    toneNArr = []
    toneArr = []
    fo = open(fpath, "r+",encoding='UTF-8')
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
        toneNArr.append(mapTone(pt))
    # Analyze the space for adjustment based on up/down limitation
    leftS = 0-mapTone(downL)
    rightS = 35-mapTone(upL)
    # 关闭文件
    fo.close()
    return [toneArr, toneNArr,[leftS,rightS]]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Load note file
    t = fetchInput("input.txt")
    print(t[0])
    print(t[1])
    name = int(input("Tell me how many steps to shift (%d ~ %d) :"%(t[2][0],t[2][1])))
    while name < t[2][0] or name > t[2][1]:
        name = int(input("Please input right number in (%d ~ %d) :" % (t[2][0], t[2][1])))
    # ToDo: To handle the shifted number list!
    sArr = []
    nArr = []
    for i in range(0,len(t[0])):
        cur=[t[0][i],t[1][i]]
        if cur[1]>=0 and cur[1] <=35:
            nArr.append(cur[1]+name)
            sArr.append(demapTone(cur[1]+name))
        else:
            nArr.append(cur[1])
            sArr.append(cur[0])
    print(nArr)
    outP = ""
    for i in sArr:
        outP = outP + i
    print(outP)
    fo = open("output.txt", "w",encoding='UTF-8')
    print(outP, file=fo)
    fo.close()
