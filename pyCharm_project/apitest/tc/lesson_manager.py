#coding:utf-8
from apitest.common.common import Base
import unittest


username = 'auto'
passwd = 'sdfsdfsdf'
c_name1 = '1zyf40'
c_desc1 = '1zyf40'
c_displayidx1 = 144
c_name2 = '2zyf40'
c_desc2 = '2zyf20'
c_displayidx2 = 244

class ApiLessonManagerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lesson_manager = Base()
        cls.lesson_manager.userlogin(username, passwd)

    def setUp(self):
        self.flag = 1
        # pprint.pprint(login_res)
    @classmethod
    def tearDownClass(cls):
        cls.lesson_manager.userlogout()

    def test_AddNewLesson(self):
        '''测试添加不存在的课程'''
        #添加列出课程
        add_course_res = self.lesson_manager.add_course(c_name1, c_desc1, c_displayidx1)
        list_course_res = self.lesson_manager.list_course()


        #判断添加课程的返回结果
        if add_course_res['retcode'] != 0:
            # pprint.pprint(add_course_res)
            flag == 0
        #判断列出课程中是否包含添加的课程信息
        for course in list_course_res['retlist']:
            if course['id'] == add_course_res['id']:
                if course['desc'] != c_desc1 or course['display_idx'] != c_displayidx1 or course['name'] != c_name1:
                    pprint.pprint(course)
                    self.flag = 0

        #删除添加课程
        self.lesson_manager.delete_course(add_course_res['id'])
        #断言
        self.assertEqual(1,self.flag)

    def test_AddExistingLesson(self):
        '''测试添加已存在课程'''
        #添加已存在课程
        add_course_res1 = self.lesson_manager.add_course(c_name1, c_desc1, c_displayidx1)
        add_course_res2 = self.lesson_manager.add_course(c_name1, c_desc2, c_displayidx2)
        list_course_res = self.lesson_manager.list_course()
        self.lesson_manager.delete_course(add_course_res1['id'])
        #判断添加已存在课程的返回结果是否符合预期
        if add_course_res2['retcode'] != 2 or add_course_res2['reason'] != '同名课程存在':
            pprint.pprint(add_course_res2)
            self.flag = 0
        #判断是否存在重复的课程&已存在的课程是否被改变
        for course in list_course_res['retlist']:
            if course['name'] == c_name1:
                # pprint.pprint(course)
                if course['desc'] == c_desc2 or course['display_idx'] == c_displayidx2 :
                    self.flag = 0

        self.assertEqual(1,self.flag)

    def test_moidfyLesson(self):
        '''测试修改课程'''
        #修改课程
        add_course_res1 = self.lesson_manager.add_course(c_name1, c_desc1, c_displayidx1)
        modify_course_res2 = self.lesson_manager.modify_course(add_course_res1['id'],c_name2, c_desc2, c_displayidx2)
        list_course_res = self.lesson_manager.list_course()
        self.lesson_manager.delete_course(add_course_res1['id'])
        #判断添加已存在课程的返回结果是否符合预期
        if modify_course_res2['retcode'] != 0 :
            pprint.pprint(add_course_res2)
            self.flag = 0
        #判断课程信息是否修改成功
        for course in list_course_res['retlist']:
            if course['name'] == add_course_res1['id']:
                # pprint.pprint(course)
                if course['desc'] != c_desc2 or course['display_idx'] != c_displayidx2  or course['name'] != c_name12 :
                    self.flag = 0

        self.assertEqual(1,self.flag)

    def test_deleteLesson(self):
        '''测试删除课程'''
        #修改课程
        add_course_res = self.lesson_manager.add_course(c_name1, c_desc1, c_displayidx1)
        delete_course_res = self.lesson_manager.delete_course(add_course_res['id'])
        list_course_res = self.lesson_manager.list_course()
        self.lesson_manager.delete_course(add_course_res['id'])
        #判断添加已存在课程的返回结果是否符合预期
        if delete_course_res['retcode'] != 0 :
            pprint.pprint(add_course_res2)
            self.flag = 0
        #根据是否存在已删除的课程id来判断是否删除成功
        for course in list_course_res['retlist']:
            if course['name'] == add_course_res['id']:
                # pprint.pprint(course)
                self.flag = 0

        self.assertEqual(1,self.flag)


if __name__ == '__main__':
    lesson_manager_test = ApiLessonManagerTest()