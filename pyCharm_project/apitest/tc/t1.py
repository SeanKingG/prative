from apitest.common.common import Base
import pprint


lesson_manager = Base()
username = 'auto'
passwd = 'sdfsdfsdf'
login_res = lesson_manager.userlogin(username,passwd)
pprint.pprint(login_res)


list_course_res = lesson_manager.list_course()
pprint.pprint(list_course_res)


add_course_res = lesson_manager.add_course('php2','fphp语言','22')
pprint.pprint(add_course_res)

modify_course_res = lesson_manager.modify_course(1018,'python','G_python','888')
pprint.pprint(modify_course_res)

delete_course_res = lesson_manager.delete_course(1019)
pprint.pprint(delete_course_res)
