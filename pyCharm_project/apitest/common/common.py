#utf-8
import requests

class Base():
    def __init__(self,c_host = 'localhost',c_port = '8066'):
        self.c_host = c_host
        self.c_port = c_port
        self.domain_name = 'http://' + c_host + ':' + c_port

    def userlogin(self,username,passwd):
        # log.logging.info('INFO:')
        login_path = '/api/mgr/loginReq'
        login_url =  self.domain_name+login_path
        logindata = {
            'username': username,
            'password': passwd
            }
        reponse = requests.post(login_url,data=logindata)
        self.sessionid = reponse.cookies['sessionid']
        return reponse.json()

    def userlogout(self):
        logout_path = '/api/mgr/logoutreq'
        logout_url = self.domain_name + logout_path
        reponse = requests.get(logout_url,cookies={'sessionid': self.sessionid})
        return reponse.json()

    def list_course(self):
        list_course_path = '/api/mgr/sq_mgr/'
        list_course_url = self.domain_name + list_course_path
        list_course_paramters = {
                                    'action':'list_course',
                                    'pagenum':'1',
                                    'pagesize':22
                                 }
        reponse = requests.get(list_course_url,params=list_course_paramters,cookies={'sessionid': self.sessionid})
        return reponse.json()

    def add_course(self,c_name,c_desc,c_displayidx):
        add_course_path = '/api/mgr/sq_mgr/'
        add_course_url =  self.domain_name + add_course_path
        add_course_data = {
            'action': 'add_course',
            'data': '''
                        {{
                          "name":"{}",
                          "desc":"{}",
                          "display_idx":"{}"
                        }}
                '''.format(c_name, c_desc, c_displayidx)
        }
        reponse = requests.post(add_course_url,data=add_course_data,cookies={'sessionid': self.sessionid})
        return reponse.json()

    def modify_course(self,m_id,m_name,m_desc,m_index):
        modify_course_path = '/api/mgr/sq_mgr/'
        modify_course_url = self.domain_name + modify_course_path
        modify_course_data = {
            'action': 'modify_course',
            'id': m_id,
            'newdata': '''
                        {{
                            "name":"{}",
                            "desc":"{}",
                            "display_idx":"{}"
                        }}
            '''.format(m_name,m_desc,m_index)
        }
        reponse = requests.put(modify_course_url,data=modify_course_data,cookies = {'sessionid':self.sessionid})
        return reponse.json()

    def delete_course(self,d_id):
        delete_course_path = '/api/mgr/sq_mgr/'
        delete_course_url = self.domain_name + delete_course_path
        delete_course_data = {
                                'action': 'delete_course',
                                'id': d_id,
                              }
        reponse = requests.delete(delete_course_url,data = delete_course_data,cookies = {'sessionid':self.sessionid})
        return reponse.json()

    # def findCourseNameById(self,ids):
    #     res = self.list_course()['retlist']
    #     course_data = []
    #     for re in res:
    #         if re['id'] == id:
    #             dic = {}
    #             dic["id"] = id
    #             # dic["name"] = re["name"]
    #             course_data.append(dic)
    #     return course_data

    def addTeacher(self,username,passwd,realname,desc,display_idx):
        add_teacher_path = '/api/mgr/sq_mgr/'
        add_teacher_url = self.domain_name + add_teacher_path
        # courses_data = [{'course_id': course_id}]
        add_teacher_data = {
            'action': 'add_teacher',
            'data': '''
                                {{
                                  "username":"{}",
                                  "password":"{}",
                                  "realname":"{}",
                                  "desc":"{}",
                                  "courses":[],
                                  "display_idx":{}
                                }}
                        '''.format(username, passwd, realname, desc, display_idx)
        }
        reponse = requests.post(add_teacher_url, data=add_teacher_data, cookies={'sessionid': self.sessionid})
        return reponse.json()

    def listTeacher(self,pagenum=1,pagesize=20):
        list_teacher_path = '/api/mgr/sq_mgr/'
        list_teacher_url = self.domain_name + list_teacher_path
        list_teacher_paramters = {
            'action': 'list_teacher',
            'pagenum': pagenum,
            'pagesize': pagesize
        }
        reponse = requests.get(list_teacher_url, params=list_teacher_paramters, cookies={'sessionid': self.sessionid})
        # print(reponse.json())
        # print(1)
        return reponse.json()

    def modTeacher(self,t_id,username,passwd,realname,desc,display_idx):
        modify_teacher_path = '/api/mgr/sq_mgr/'
        modify_teacher_url = self.domain_name + modify_teacher_path
        # courses_data = [{'course_id': zcourse_id}]
        modify_teacher_data = {
            'action': 'modify_teacher',
            'id': t_id,
            'newdata': '''
                                {{
                                    "username":"{}",
                                    "password":"{}",
                                    "realname":"{}",
                                    "desc":"{}",
                                    "courses":[],
                                    "display_idx":{}
                                }}
                    '''.format(username, passwd, realname, desc, display_idx)
        }
        reponse = requests.put(modify_teacher_url, data=modify_teacher_data, cookies={'sessionid': self.sessionid})
        return reponse.json()

    def deleteTeacher(self,d_id):
        delete_teacher_path = '/api/mgr/sq_mgr/'
        delete_teacher_url = self.domain_name + delete_teacher_path
        delete_teacher_data = {
                                'action': 'delete_teacher',
                                'id': d_id,
                              }
        reponse = requests.delete(delete_teacher_url,data = delete_teacher_data,cookies = {'sessionid':self.sessionid})
        return reponse.json()
if __name__ == "__main__":
    import pprint
    test = Base()
    test.userlogin('auto','sdfsdfsdf')
    # pprint.pprint( test.list_course())
    # pprint.pprint(test.list_course())


    # res = test.listTeacher()
    # pprint.pprint(res)
    res1 = test.addTeacher('fefae','zzzzj','zzztht','zzzzfjstee',31)
    print(1)
    pprint.pprint(res1)