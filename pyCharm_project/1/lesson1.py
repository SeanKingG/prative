logs = ['A old lady come in, the name is Mary, level 94454',\
        'A pretty boy come in, the name is Patrick, level 194']


def GetName(a):
    b = a.split(',')
    print(b)
    print(b[1][12:])
for log in logs:
    GetName(log)