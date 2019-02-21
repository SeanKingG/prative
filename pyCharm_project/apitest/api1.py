import requests
import pprint

#列出课程
list_course = requests.get('http://localhost:8066/api/mgr/sq_mgr/'
             '?action=list_course&pagenum=1&pagesize=22')

pprint.pprint(list_course.json())

#添加课程
new_courseData = {
    'action':'add_course',
    'data':'''
        {
        "name":"qqq初中化学",
        "desc":"qqq中化学课程",
        "display_idx":"7"
        }
        '''
}
add_course = requests.post('http://localhost:8066/api/mgr/sq_mgr/',data=new_courseData)
pprint.pprint(add_course.json())

#修改课程
modify_data = {
    'action':'modify_course',
    'id':1014,
    'newdata':'{"name":"yyeee","desc":"yyeee","display_idx":"666"}'
     }
modify_course = requests.put('http://localhost:8066/api/mgr/sq_mgr/',data=modify_data)
pprint.pprint(modify_course.json())

#删除课程
deleteInfo ={
    'action':'delete_course',
    'id':1010
    }
delete_course = requests.delete('http://localhost:8066/api/mgr/sq_mgr/',data=deleteInfo)
pprint.pprint(delete_course.json())