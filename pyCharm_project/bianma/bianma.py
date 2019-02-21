#coding:utf-8
with open('gbk编码.txt','r',encoding='gbk') as gbk, open('utf8编码.txt','r',encoding='utf8') as utf, open('T.txt','w',encoding='utf8') as T:
    g = gbk.read()
    u = utf.read()
    # print(g)
    # print(u+g)
    T.write(g+'\n'+u)

