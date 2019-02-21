#utf-8
from apitest.common.common import Base
import unittest,pprint

username1 = 'kakaxi'
password1 = 'kakaxi'
realname1 = '卡卡西'
desc1 = '木叶忍者'
display_idx1 = 2

username2 = 'SunWuKong'
password2 = 'SunWuKong'
realname2 = '孙悟空'
desc2 = '斗战胜佛'
display_idx2 = 3

username = 'auto'
passwd = 'sdfsdfsdf'

c_name1 = '1zyf40'
c_desc1 = '1zyf40'
c_displayidx1 = 144
c_name2 = '2zyf40'
c_desc2 = '2zyf20'
c_displayidx2 = 244
c_name3 = '3zyf40'
c_desc3 = '3zyf20'
c_displayidx3 = 344

class TeacherManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.teacher_manager = Base()
        cls.teacher_manager.userlogin(username,passwd)
        cls.course_id1 = cls.teacher_manager.add_course(c_name1, c_desc1, c_displayidx1)['id']
        cls.course_id2 = cls.teacher_manager.add_course(c_name2, c_desc2, c_displayidx2)['id']
        cls.course_id3 = cls.teacher_manager.add_course(c_name3, c_desc3, c_displayidx3)['id']
        cls.all_course_id = [cls.course_id1,cls.course_id2,cls.course_id3]

    def setUp(self):
        self.flag = 1
        self.res1 = self.teacher_manager.addTeacher(username1, password1, realname1, desc1, display_idx1)

    @classmethod
    def tearDownClass(cls):
        print(' ')
        # for course_id in cls.all_course_id:
        #     cls.teacher_manager.delete_course(course_id)

    def tearDown(self):
        self.teacher_manager.deleteTeacher(self.res1['id'])


    def test_addTeacher(self):
        '''测试新增已存在的老师'''
        res2 = self.teacher_manager.addTeacher(username1, password1, realname1, desc1, display_idx1)
        # pprint.pprint(res1)#登录名 kakaxi 已经存在
        except_reason = '登录名 kakaxi 已经存在'
        if res2['reason'] != except_reason or res2['retcode'] != 1:
            self.flag = 0
        self.assertEqual(1,self.flag)

    def test_modTeacher(self):
        '''测试修改老师'''
        self.teacher_manager.modTeacher(self.res1['id'],username2, password2, realname2, desc2, display_idx2)
        # pprint.pprint(res3)
        res2 = self.teacher_manager.listTeacher()
        for retlist1 in res2['retlist']:
            if retlist1['id'] == self.res1['id']:
                if retlist1['username'] != username2 or retlist1['realname'] != realname2 or retlist1['desc'] != desc2 or retlist1['display_idx'] != display_idx2 or res2['retcode'] != 0:
                    self.flag = 0
        self.assertEqual(1,self.flag)

    def test_deleteTeacher(self):
        '''测试删除老师'''
        res2 = self.teacher_manager.addTeacher(username2, password2, realname2, desc2, display_idx2)
        self.teacher_manager.deleteTeacher(res2['id'])
        res3 = self.teacher_manager.listTeacher()
        for retlist1 in res3['retlist']:
            if retlist1['id'] == res2['id']:
                self.flag = 0
        self.assertEqual(1,self.flag)
        pprint.pprint(self.teacher_manager.list_course())


if __name__ == '__mian__':
    teacher_maneger = TeacherManager()

