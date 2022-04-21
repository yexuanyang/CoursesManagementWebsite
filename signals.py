'''
一个用于定义信号的文件 用于日志文件的书写
'''
from flask import request, g
from blinker import Namespace

space = Namespace()  # 创建命名空间
# 用户登录信号
login_space = space.signal('登录')

# 用户进入课程管理系统信号
in_course = space.signal('进入课程管理')
# 用户进入课程管理系统进行删除信号
in_course_delete = space.signal('删除了课程')
# 用户进入课程管理系统进行增加信号
in_course_add = space.signal('增加了课程')
# 用户进入课程管理系统进行更改信号
in_course_change = space.signal('更改了课程')
# 用户进入课程管理排序信号
in_course_sort = space.signal('排序了课程')

# 用户进入课外管理系统信号
out_activity = space.signal('进入了课外管理系统')
# 用户进入课外管理系统设置信号
out_activity_set = space.signal('设置了课外活动')
# 用户进入课外管理系统删除信号
out_activity_delete = space.signal('删除了课外活动')
# 用户进入课外管理系统更改信号
out_activity_in = space.signal('更改了课外活动')
# 用户进入课外管理系统排序信号
out_activity_sort = space.signal('对课外活动进行了排序')

# 用户进入导航系统信号
route_in = space.signal('进入了导航系统')
# 用户导航系统进行路径规划信号
route_in = space.signal('进行了路线规划')

# 用户进入日志系统信号
logging_in = space.signal('访问了日志系统')


def logging_into(sender):  # 访问日志系统信号
    info = f'{g.uname}访问了日志系统'
    with open('logging.log', 'a', encoding='utf-8') as f:  # 打开日志文件然后写入
        f.write(info + "\n")  # 写入日志信息


def login_space_into(sender):  # 登录信号
    info = f'{g.uname}登录了系统'
    with open('logging.log', 'a', encoding='utf-8') as f:  # 打开日志然后写如
        f.write(info + "\n")  # 写入日志信息


def in_course_into(sender):
    info = f'{g.uname}进入了课程管理系统'
    with open('logging.log', 'a', encoding='utf-8') as f:  # 打开日志然后写如
        f.write(info + "\n")  # 写入日志信息


def in_course_add_into(sender):
    info = f'{g.uname}增加了课程'
    with open('logging.log', 'a', encoding='utf-8') as f:  # 打开日志然后写如
        f.write(info + "\n")  # 写入日志信息


def in_course_delete_into(sender):
    info = f'{g.uname}删除了课程'
    with open('logging.log', 'a', encoding='utf-8') as f:  # 打开日志然后写如
        f.write(info + "\n")  # 写入日志信息


def in_course_change_into(sender):
    info = f'{g.uname}更新了课程'
    with open('logging.log', 'a', encoding='utf-8') as f:  # 打开日志然后写如
        f.write(info + "\n")  # 写入日志信息


def out_activity_into(sender):
    info = f'{g.uname}进入了课外管理系统'
    with open('logging.log', 'a', encoding='utf-8') as f:  # 打开日志然后写如
        f.write(info + "\n")  # 写入日志信息


def out_activity_set_into(sender):
    info = f'{g.uname}设置了课外活动'
    with open('logging.log', 'a', encoding='utf-8') as f:  # 打开日志然后写如
        f.write(info + "\n")  # 写入日志信息


def route_in_into(sender):
    info = f'{g.uname}进入了导航系统'
    with open('logging.log', 'a', encoding='utf-8') as f:  # 打开日志然后写如
        f.write(info + "\n")  # 写入日志信息


logging_in.connect(logging_into)  # 注册这个日志信号
login_space.connect(login_space_into)  # 注册信号
in_course.connect(in_course_into)  # 进入了课内信息管理系统
in_course_add.connect(in_course_add_into)  # 增加了课程
in_course_delete.connect(in_course_delete_into)  # 删除了课程
in_course_change.connect(in_course_change_into)  # 更新了课程
route_in.connect(route_in_into)  # 进入了导航系统
out_activity.connect(out_activity_into)  # 进入了课外管理系统
out_activity_set.connect(out_activity_set_into)  # 设置了课外活动
