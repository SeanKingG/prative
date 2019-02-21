#fileName1:签到源文件 fileName2：经处理按字典格式存储的文件，可用notepad++用Json格式查看
fileName1 = r'C:\Users\Administrator\Desktop\深圳-赵永福-20181221\0005_1.txt'
fileName2 = r'C:\Users\Administrator\Desktop\深圳-赵永福-20181221' \
            r'\未排序字典.txt'
fileName3 = r'C:\Users\Administrator\Desktop\深圳-赵永福-20181221' \
            r'\排序字典.txt'

def putInfoToDict(file):
    import json
    signList1 = {}#未排序字典
    signList2 = {}#按studentID排序的字典
    with open(fileName1, 'r') as infoFile, open(fileName2,'w') as noSortFile, open(fileName3,'w') as sortFile:
        signInfos = infoFile.readlines()
        for signInfo in signInfos:
            signInfoList = signInfo.split(',')#用，分割
            studentID = int(signInfoList[2][:-1].strip().replace(')',''))#提取studentID：去空格，处理结尾是）或）；的情况
            lessonID = int(signInfoList[1].strip())#提取lessonID，去空格
            checkInTime = signInfoList[0][-20:-1]#提取签到时间
           # print(str(studentID)+'  '+str(lessonID)+'  '+checkInTime)
            if studentID not in signList1.keys():#判断student ID对应在signList字典的key中是否存在
                signList1[studentID] = [{'lssonid':lessonID,'checkintime':checkInTime}]
            else:
                signList1[studentID].append({'lssonid':lessonID,'checkintime':checkInTime})

#对生成的字典排序
        studentIDs = []
        for studentID in signList1.keys():#生成studentid数组
            studentIDs.append(studentID)
        while studentIDs:#生成按studentID排序的新字典
            signList2[min(studentIDs)] = signList1[min(studentIDs)]
            studentIDs.remove(min(studentIDs))

#把生成的字典输出到文件
        noSortFile.write(json.dumps(signList1))
        sortFile.write(json.dumps(signList2))
        return signList1, signList2

putInfoToDict(fileName1)

