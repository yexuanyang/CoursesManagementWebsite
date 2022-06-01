from flask import Flask, render_template, request, redirect, g, session,send_from_directory
from compress import file_decode  # 解码函数
from compress import file_encode  # 编码函数
from compress import datatemp #引入记录文件名的
import os
import setting
import json
import datetime
from werkzeug.utils import secure_filename
from signals import logging_in, login_space, in_course, route_in, out_activity, in_course_add, in_course_delete, \
    in_course_change, out_activity_set, data,DataStore,direct_course_go,add_homework,upload_homework_signal,upload_material_signal,download_material_signal
from forms import OutCourseForms, InCourseForms
app = Flask(__name__)

app.config.from_object(setting)
app.config['SECRET_KEY'] = 'yyx'
app.config['JSON_AS_ASCII'] = False
admin_filePtr = open("./static/data/admin.json", "r", encoding='utf-8')
student_filePtr = open("./static/data/stu.json", "r", encoding='utf-8')
course_filePtr = open("./static/data/course.json", "r", encoding='utf-8')
out_course_filePtr = open("./static/data/out_course.json", "r", encoding='utf-8')
course_material_filePtr = open("./static/data/courses_material.json", "r", encoding='utf-8')
homework_filePtr = open("./static/data/homework.json", "r", encoding='utf-8')
# test_filePtr = open("./static/data/test.json", "r", encoding='utf-8')
admins = json.load(admin_filePtr)
student = json.load(student_filePtr)
courses = json.load(course_filePtr)
out_courses = json.load(out_course_filePtr)
courses_material = json.load(course_material_filePtr)
homework = json.load(homework_filePtr)
# test = json.load(test_filePtr)
chToint = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "日": 7}

data1=DataStore()


def sort_activity_time(e):
    return e['activity_time']


def strToWeekDay(str):
    str = str.split('-')
    time = datetime.datetime(int(str[0]), int(str[1]), int(str[2]))
    weekday = time.weekday() + 1
    data.initconflict()#初始化
    return weekday


@app.route('/')
def index():
    data.initconflict()#初始化
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    data.initconflict()#初始化
    no_found = False
    error_in_password = False
    usn = request.form.get('usn')
    pwd = request.form.get('pwd')
    if request.method == 'POST':

        for stu in student:
            if stu['usn'] == usn and stu['pwd'] == pwd:
                session['now_user'] = usn
                g.uname = session['now_user']
                if g.uname:  # 如果这个名称存在的话
                    login_space.send()
                return redirect("/index/" + 'student')
            elif stu['usn'] == usn and stu['pwd'] != pwd:
                error_in_username = True
                return render_template('login.html', error_in_password=error_in_password, no_found=no_found)

        for us in admins:
            if us['usn'] == usn and us['pwd'] == pwd:
                session['now_user'] = usn
                g.uname = session['now_user']
                if g.uname:  # 如果这个名称存在的话
                    login_space.send()
                return redirect('/index/' + 'admin')
            elif us['usn'] == usn and us['pwd'] != pwd:
                error_in_password = True
                return render_template('login.html', error_in_password=error_in_password, no_found=no_found)

        no_found = True
        return render_template('login.html', no_found=no_found, error_in_password=error_in_password)

    return render_template('login.html', no_found=no_found, error_in_password=error_in_password)


@app.route('/register', methods=['GET', 'POST'])
def register():
    data.initconflict()#初始化
    if request.method == 'POST':
        usn = request.form.get('usn')
        pwd = request.form.get('pwd')
        pwd1 = request.form.get('pwd1')

        for stu in student:
            if stu['usn'] == usn:
                return render_template('register.html', have_already=True)

        for us in admins:
            if us['usn'] == usn:
                return render_template('register.html', have_already=True)

        if pwd1 == pwd:
            student.append({'usn': usn, 'pwd': pwd})
            fp = open("./static/data/stu.json", "w", encoding='utf-8')
            json.dump(student, fp, ensure_ascii=False, separators=(',', ':'))
            fp.close()

        else:
            return render_template('register.html', error_in_password=True)

        print(type(usn))
        print(student)

    return render_template('register.html')


# 查看usn用户的密码，提供更新功能；若usn == 'admin' 那么显示所有的用户和密码并提供删除和更新功能
@app.route('/admin/<string:usn>', methods=['GET', 'POST'])
def admin(usn):
    data.initconflict()#初始化
    if request.method == 'POST':
        print(request.form.get('usn'))
        print(request.form.get('pwd'))
    return render_template('admin.html', student=student, admins=admins, usn=usn)


# 删除
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    data.initconflict()#初始化
    usn = request.args.get('usn')
    print(usn)
    print(request.method)
    for stu in student:
        print(stu['usn'])
        print(student)
        if usn == stu['usn']:
            student.remove(stu)
            print(student)
            fp = open("./static/data/stu.json", "w", encoding='utf-8')
            json.dump(student, fp, ensure_ascii=False, separators=(',', ':'))
            return redirect('/admin/admin')

    for ad in admins:
        print(ad['usn'])
        print(ad)
        if usn == ad['usn']:
            admins.remove(ad)
            print(ad)
            fp = open("./static/data/admin.json", "w", encoding='utf-8')
            json.dump(admins, fp, ensure_ascii=False, separators=(',', ':'))
            return redirect('/admin/admin')

    return render_template('admin.html', student=student, admins=admins)


# 更新
@app.route('/change', methods=['GET', 'POST'])
def change():
    data.initconflict()#初始化
    if request.method == 'POST':
        usn = request.form.get('usn')
        pwd = request.form.get('pwd')
        pwd1 = request.form.get('pwd1')

        if pwd == pwd1:
            print(pwd)
            for stu in student:
                if usn == stu['usn']:
                    stu['pwd'] = pwd
                    fp = open("./static/data/stu.json", "w", encoding='utf-8')
                    json.dump(student, fp, ensure_ascii=False, separators=(',', ':'))
                    print(stu)
        else:
            return '密码输入不一致'

        return redirect('/admin/' + usn)

    usn = request.args.get('usn')
    print(usn)
    for stu in student:
        if usn == stu['usn']:
            return render_template('change.html', usn=usn)

    for ad in admins:
        if usn == ad['usn']:
            return render_template('change.html', usn=usn)

    return '用户不存在'


# 忘记密码
@app.route('/forget', methods=['GET', 'POST'])
def forget():
    data.initconflict()#初始化
    print(request.method)
    if request.method == 'POST':
        usn = request.form.get('usn')
        print(usn)
        pwd = request.form.get('pwd')
        pwd1 = request.form.get('pwd1')
        if pwd == pwd1:
            for stu in student:
                if usn == stu['usn']:
                    stu['pwd'] = pwd
                    fp = open("./static/data/stu.json", "w", encoding='utf-8')
                    json.dump(student, fp, ensure_ascii=False, separators=(',', ':'))
                    return redirect('/admin/' + usn)
                else:
                    for ad in admins:
                        if usn == ad['usn']:
                            return render_template('forget.html', level_error=True)
            return render_template('forget.html', no_found=True)
        else:
            return render_template('forget.html', error_in_password=True)

    return render_template('forget.html')


# 学生课程信息管理首页
@app.route('/index/admin')
def admin_index():
    data.initconflict()#初始化
    return render_template('admin_new.html', cla1='active', time_que=data.time_list)


@app.route('/index/student')
def student_index():
    data.initconflict()#初始化
    return render_template('student_index.html', cla1='active', time_que=data.time_list)


@app.route('/in_course/student', methods=['POST', 'GET'])
def in_course_fun_stu():
    data.initconflict()#初始化
    g.uname = session.get('now_user')
    in_course.send()
    return render_template('student_course.html', cla2='active', posts=courses, time_que=data.time_list)


@app.route('/in_course/admin', methods=['POST', 'GET'])
def in_course_fun():
    data.initconflict()#初始化
    g.uname = session.get('now_user')
    in_course.send()
    return render_template('student_course_admin.html', cla2='active', posts=courses, time_que=data.time_list)


@app.route('/in_course/admin/add', methods=['POST', 'GET'])
def in_course_add_func():
    data.initconflict()#初始化
    form = InCourseForms()
    conflict = False
    conflict_course = {}

    if request.method == 'POST':
        g.uname = session.get('now_user')
        in_course_add.send()
        cause_name = request.form.get('cause_name')
        teacher = request.form.get('teacher')
        time = request.form.get('time')
        class_end_time = request.form.get('class_end_time')
        day = request.form.get('day')
        location = request.form.get('location')
        class_num = request.form.get('class_num')
        qq = request.form.get('qq')
        exam_time = request.form.get('exam_time').replace("T", " ")
        end_time = request.form.get('end_time').replace("T", " ")

        newcourse = {"cause_name": cause_name, "teacher": teacher, "time": day + time + '~' + class_end_time,
                     "location": location + ' ' + class_num,
                     "qq": qq, "exam_time": exam_time + '~~' + end_time}

        # 课程时间冲突检测
        in_course_temp = list(courses)
        weekday = chToint[day[2]]
        for one_in_course in in_course_temp:
            int_day = chToint[one_in_course["time"][2]]
            if weekday == int_day:
                course_begin_time = one_in_course['time'][3:8]
                course_end_time = one_in_course['time'][9:]
                if (course_begin_time < time < course_end_time) or (
                        course_begin_time < class_end_time < course_end_time):
                    conflict = True
                    conflict_course = one_in_course
                    break

        if not conflict:
            courses.append(newcourse)
            with open('./static/data/course.json', 'w', encoding='utf-8') as fp:
                json.dump(courses, fp, ensure_ascii=False, separators=('\n,', ':'))
            return redirect('/in_course/admin')

    return render_template('add_course.html', form=form, conflict=conflict, conflict_course=conflict_course)


@app.route('/in_course/admin/delete', methods=['POST', 'GET'])
def in_course_delete_fun():
    data.initconflict()#初始化
    g.uname = session.get('now_user')
    in_course_delete.send()
    delete_index = request.form.getlist('checklist')

    for i in delete_index:
        if int(i) - 1 == len(courses):
            courses.pop(-1)
        else:
            courses.pop(int(i) - 1)
    with open('./static/data/course.json', "w", encoding='utf-8') as fp:
        json.dump(courses, fp, ensure_ascii=False, separators=('\n,', ':'))
    return redirect('/in_course/admin')


@app.route('/in_course/admin/change', methods=['POST', 'GET'])
def in_course_change_fun():
    data.initconflict()#初始化
    form = InCourseForms()
    id1 = request.args.get('id1')
    cause_name = request.args.get('cause_name')
    teacher = request.args.get('teacher')
    time = request.args.get('time')
    location = request.args.get('location')
    qq = request.args.get('qq')
    exam_time = request.args.get('exam_time')
    conflict = False
    conflict_course = {}

    if request.method == 'GET':
        if len(courses) == int(id1) - 1:
            courses.pop()
        else:
            courses.pop(int(id1) - 1)

    if request.method == 'POST':
        g.uname = session.get('now_user')
        in_course_change.send()
        course_name = request.form.get('cause_name')
        teacher = request.form.get('teacher')
        time = request.form.get('time')
        class_end_time = request.form.get('class_end_time')
        day = request.form.get('day')
        location = request.form.get('location')
        class_num = request.form.get('class_num')
        qq = request.form.get('qq')
        exam_time = request.form.get('exam_time').replace('T', ' ')
        end_time = request.form.get('end_time').replace('T', ' ')
        newcourse = {"cause_name": course_name, "teacher": teacher, "time": day + time + '~' + class_end_time,
                     "location": location + ' ' + class_num,
                     "qq": qq, "exam_time": exam_time + "~~" + end_time}

        # 课程时间冲突检测
        in_course_temp = list(courses)
        weekday = chToint[day[2]]
        for one_in_course in in_course_temp:
            int_day = chToint[one_in_course["time"][2]]
            if weekday == int_day:
                course_begin_time = one_in_course['time'][3:8]
                course_end_time = one_in_course['time'][9:]
                if (course_begin_time < time < course_end_time) or (
                        course_begin_time < class_end_time < course_end_time):
                    conflict = True
                    conflict_course = one_in_course
                    break

        if not conflict:
            courses.insert(int(id1) - 1, newcourse)
            with open('./static/data/course.json', 'w', encoding='utf-8') as fp:
                json.dump(courses, fp, ensure_ascii=False, separators=('\n,', ':'))
            return redirect('/in_course/admin')

    return render_template('change_course.html', form=form, time=time, location=location, exam_time=exam_time,
                           cause_name=cause_name, qq=qq, teacher=teacher, conflict=conflict,
                           conflict_course=conflict_course)


@app.route('/out_course/admin', methods=['POST', 'GET'])
def out_course_fun():
    data.initconflict()#初始化
    g.uname = session.get('now_user')
    out_activity.send()
    return render_template('student_out_course_admin.html', cla3='active', posts=out_courses, time_que=data.time_list)


@app.route('/out_course/admin/add', methods=['POST', 'GET'])
def out_course_add_fun():
    data.initconflict()#初始化
    conflict = False
    conflict_activity = {}
    conflict_in_course = False
    conflict_which_course = {}
    form = OutCourseForms()

    if request.method == 'POST':
        g.uname = session.get('now_user')
        out_activity_set.send()
        activity_name = request.form.get('activity_name')
        activity_time = request.form.get('activity_time')
        begin_time = request.form.get('begin_time')
        end_time = request.form.get('end_time')
        persons_num = request.form.get('persons_num')
        location = request.form.get('location')
        new_out_course = {'activity_name': activity_name, 'activity_time': activity_time, 'begin_time': begin_time,
                          'end_time': end_time,
                          'persons_num': persons_num, 'location': location}
        # 活动时间冲突检测
        out_courses_temp = list(out_courses)
        out_courses_temp.sort(key=sort_activity_time)
        for out_courses_activity in out_courses_temp:
            if activity_time == out_courses_activity['activity_time']:
                #     进入活动时间的判断
                if (out_courses_activity['begin_time'] < begin_time < out_courses_activity['end_time']) \
                        or (
                        out_courses_activity['begin_time'] < end_time < out_courses_activity['end_time']):
                    conflict = True
                    conflict_activity = out_courses_activity
                    break
        # 课程时间冲突检测
        in_course_temp = list(courses)
        weekday = strToWeekDay(activity_time)
        for one_in_course in in_course_temp:
            int_day = chToint[one_in_course["time"][2]]
            if weekday == int_day:
                course_begin_time = one_in_course['time'][3:8]
                course_end_time = one_in_course['time'][9:]
                if (course_begin_time < begin_time < course_end_time) or (
                        course_begin_time < end_time < course_end_time):
                    conflict_in_course = True
                    conflict_which_course = one_in_course
                    break

        if not (conflict or conflict_in_course):
            out_courses.append(new_out_course)
            with open('./static/data/out_course.json', "w", encoding='utf-8') as fp:
                json.dump(out_courses, fp, ensure_ascii=False, separators=('\n,', ':'))
            return redirect('/out_course/admin')

    return render_template('add_out_course.html', cla3='active', posts=out_courses, time_que=time_list, form=form,
                           conflict=conflict, conflict_activity=conflict_activity,
                           conflict_in_course=conflict_in_course, conflict_which_course=conflict_which_course)


@app.route('/out_course/admin/delete', methods=['POST', 'GET'])
def out_course_del_fun():
    data.initconflict()#初始化
    global time_list
    g.uname = session.get('now_user')
    out_activity.send()
    delete_list = request.form.getlist('checklist')
    print(delete_list)
    for i in delete_list:
        if int(i) - 1 == len(delete_list):
            out_courses.pop(-1)
        else:
            out_courses.pop(int(i) - 1)
    with open('./static/data/out_course.json', "w", encoding='utf-8') as fp:
        json.dump(out_courses, fp, ensure_ascii=False, separators=('\n,', ':'))
    return redirect('/out_course/admin')


@app.route('/out_course/admin/change', methods=['POST', 'GET'])
def out_course_change_fun():
    data.initconflict()#初始化
    conflict = False
    conflict_activity = {}
    conflict_in_course = False
    conflict_which_course = {}
    form = OutCourseForms()
    id2 = request.args.get('id2')
    activity_name = request.args.get('activity_name')
    activity_time = request.args.get('activity_time')
    begin_time = request.args.get('begin_time')
    end_time = request.args.get('end_time')
    persons_num = request.args.get('persons_num')
    location = request.args.get('location')

    if request.method == 'GET':
        if int(id2) - 1 == len(out_courses):
            out_courses.pop(-1)
        else:
            out_courses.pop(int(id2) - 1)

    if request.method == 'POST':
        g.uname = session.get('now_user')
        out_activity_set.send()
        id1 = request.form.get('id1')
        activity_name = request.form.get('activity_name')
        activity_time = request.form.get('activity_time')
        begin_time = request.form.get('begin_time')
        end_time = request.form.get('end_time')
        persons_num = request.form.get('persons_num')
        location = request.form.get('location')
        new_out_course = {'activity_name': activity_name, 'activity_time': activity_time, 'begin_time': begin_time,
                          'end_time': end_time,
                          'persons_num': persons_num, 'location': location}
        # 活动时间冲突检测
        out_courses_temp = list(out_courses)
        out_courses_temp.sort(key=sort_activity_time)
        for out_courses_activity in out_courses_temp:
            if activity_time == out_courses_activity['activity_time']:
                #     进入活动时间的判断
                if (out_courses_activity['begin_time'] < begin_time < out_courses_activity['end_time']) \
                        or (
                        out_courses_activity['begin_time'] < end_time < out_courses_activity['end_time']):
                    conflict = True
                    conflict_activity = out_courses_activity
                    break

        # 课程时间冲突检测
        in_course_temp = list(courses)
        weekday = strToWeekDay(activity_time)
        for one_in_course in in_course_temp:
            int_day = chToint[one_in_course["time"][2]]
            if weekday == int_day:
                course_begin_time = one_in_course['time'][3:8]
                course_end_time = one_in_course['time'][9:]
                if (course_begin_time < begin_time < course_end_time) or (
                        course_begin_time < end_time < course_end_time):
                    conflict_in_course = True
                    conflict_which_course = one_in_course
                    break

        if not (conflict or conflict_in_course):
            out_courses.insert(int(id2) - 1, new_out_course)

            with open('./static/data/out_course.json', "w", encoding='utf-8') as fp:
                json.dump(out_courses, fp, ensure_ascii=False, separators=('\n,', ':'))
            return redirect('/out_course/admin')

    return render_template('change_out_course.html', activity_name=activity_name, activity_time=activity_time,
                           begin_time=begin_time,
                           end_time=end_time,
                           persons_num=persons_num, location=location, form=form, conflict=conflict,
                           conflict_activity=conflict_activity, conflict_in_course=conflict_in_course,
                           conflict_which_course=conflict_which_course)


@app.route('/out_course/student', methods=['POST', 'GET'])
def out_course_fun_stu():
    data.initconflict()#初始化
    g.uname = session.get('now_user')
    out_activity.send()
    return render_template('student_out_course.html', cla3='active', posts=out_courses, time_que=data.time_list)


@app.route('/out_course/student/add', methods=['POST', 'GET'])
def out_course_add_fun_stu():
    data.initconflict()#初始化
    form = OutCourseForms()
    conflict = False
    conflict_activity = {}
    conflict_in_course = False
    conflict_which_course = {}
    global time_list
    if request.method == 'POST':
        g.uname = session.get('now_user')
        out_activity_set.send()
        activity_name = request.form.get('activity_name')
        activity_time = request.form.get('activity_time')
        begin_time = request.form.get('begin_time')
        end_time = request.form.get('end_time')
        persons_num = request.form.get('persons_num')
        location = request.form.get('location')
        new_out_course = {'activity_name': activity_name, 'activity_time': activity_time, 'begin_time': begin_time,
                          'end_time': end_time,
                          'persons_num': persons_num, 'location': location}
        # 活动时间冲突检测
        out_courses_temp = list(out_courses)
        out_courses_temp.sort(key=sort_activity_time)
        for out_courses_activity in out_courses_temp:
            if activity_time == out_courses_activity['activity_time']:
                #     进入活动时间的判断
                if (out_courses_activity['begin_time'] < begin_time < out_courses_activity['end_time']) \
                        or (
                        out_courses_activity['begin_time'] < end_time < out_courses_activity['end_time']):
                    conflict = True
                    conflict_activity = out_courses_activity
                    break

        # 课程时间冲突检测
        in_course_temp = list(courses)
        weekday = strToWeekDay(activity_time)
        for one_in_course in in_course_temp:
            int_day = chToint[one_in_course["time"][2]]
            if weekday == int_day:
                course_begin_time = one_in_course['time'][3:8]
                course_end_time = one_in_course['time'][9:]
                if (course_begin_time < begin_time < course_end_time) or (
                        course_begin_time < end_time < course_end_time):
                    conflict_in_course = True
                    conflict_which_course = one_in_course
                    break

        if not (conflict or conflict_in_course):
            out_courses.append(new_out_course)
            with open('./static/data/out_course.json', "w", encoding='utf-8') as fp:
                json.dump(out_courses, fp, ensure_ascii=False, separators=('\n,', ':'))
            return redirect('/out_course/student')

    return render_template('add_out_course.html', cla3='activate', posts=out_courses, time_que=time_list, form=form,
                           conflict=conflict, conflict_activity=conflict_activity,
                           conflict_in_course=conflict_in_course, conflict_which_course=conflict_which_course)


@app.route('/out_course/student/delete', methods=['POST', 'GET'])
def out_course_del_fun_stu():
    data.initconflict()#初始化
    g.uname = session.get('now_user')
    out_activity_set.send()
    delete_list = request.form.getlist('checklist')
    for i in delete_list:
        if int(i) - 1 == len(delete_list):
            out_courses.pop(-1)
        else:
            out_courses.pop(int(i) - 1)
    with open('./static/data/out_course.json', "w", encoding='utf-8') as fp:
        json.dump(out_courses, fp, ensure_ascii=False, separators=('\n,', ':'))
    return redirect('/out_course/student')


@app.route('/out_course/student/change', methods=['POST', 'GET'])
def out_course_change_fun_stu():
    data.initconflict()#初始化
    global time_list
    form = OutCourseForms()
    id1 = request.args.get('id1')
    activity_name = request.args.get('activity_name')
    activity_time = request.args.get('activity_time')
    begin_time = request.args.get('begin_time')
    end_time = request.args.get('end_time')
    persons_num = request.args.get('persons_num')
    location = request.args.get('location')
    conflict = False
    conflict_activity = {}
    conflict_in_course = False
    conflict_which_course = {}
    if request.method == 'GET':
        if int(id1) - 1 == len(out_courses):
            out_courses.pop(-1)
        else:
            out_courses.pop(int(id1) - 1)

    if request.method == 'POST':
        g.uname = session.get('now_user')
        out_activity_set.send()
        activity_name = request.form.get('activity_name')
        activity_time = request.form.get('activity_time')
        begin_time = request.form.get('begin_time')
        end_time = request.form.get('end_time')
        persons_num = request.form.get('persons_num')
        location = request.form.get('location')
        new_out_course = {'activity_name': activity_name, 'activity_time': activity_time, 'begin_time': begin_time,
                          'end_time': end_time,
                          'persons_num': persons_num, 'location': location}
        # 活动时间冲突检测
        out_courses_temp = list(out_courses)
        out_courses_temp.sort(key=sort_activity_time)
        for out_courses_activity in out_courses_temp:
            if activity_time == out_courses_activity['activity_time']:
                #     进入活动时间的判断
                if (out_courses_activity['begin_time'] < begin_time < out_courses_activity['end_time']) \
                        or (
                        out_courses_activity['begin_time'] < end_time < out_courses_activity['end_time']):
                    conflict = True
                    conflict_activity = out_courses_activity
                    break

        # 课程时间冲突检测
        in_course_temp = list(courses)
        weekday = strToWeekDay(activity_time)
        for one_in_course in in_course_temp:
            int_day = chToint[one_in_course["time"][2]]
            if weekday == int_day:
                course_begin_time = one_in_course['time'][3:8]
                course_end_time = one_in_course['time'][9:]
                if (course_begin_time < begin_time < course_end_time) or (
                        course_begin_time < end_time < course_end_time):
                    conflict_in_course = True
                    conflict_which_course = one_in_course
                    break

        if not (conflict or conflict_in_course):
            out_courses.insert(int(id1) - 1, new_out_course)

            with open('./static/data/out_course.json', "w", encoding='utf-8') as fp:
                json.dump(out_courses, fp, ensure_ascii=False, separators=('\n,', ':'))
            return redirect('/out_course/student')

    return render_template('change_out_course.html', activity_name=activity_name, activity_time=activity_time,
                           begin_time=begin_time,
                           end_time=end_time,
                           persons_num=persons_num, location=location, form=form, conflict=conflict,
                           conflict_activity=conflict_activity, conflict_in_course=conflict_in_course,
                           conflict_which_course=conflict_which_course)


@app.route('/route/admin', methods=['POST', 'GET'])
def route():
    data.initconflict()#初始化
    global time_list
    g.uname = session.get('now_user')
    str_all = ["/static/js/qustmap_shahe.js", "/static/js/qustmap_headquarter.js"]
    str_choose = "/static/js/qustmap_shahe.js"
    template_chose = "qustmap_admin.html"
    route_in.send()
    if request.method == 'POST':  # 此时如果是提交
        way = request.form.get('way')
        if way == '010':  # 此时是沙河
            template_chose = "qustmap_admin.html"
            str_choose = str_all[0]
        elif way == '001':  # 此时为本部
            template_chose = "qustmap_admin.html"
            str_choose = str_all[1]
        elif way == '100':  # 此时是两地跨越
            template_chose = "one_to_one_admin.html"
    if (template_chose == "qustmap_admin.html"):
        return render_template(template_chose, ways=str_choose, cla4="active", usn="admin", time_que=data.time_list)
    else:
        return render_template(template_chose, cla4="active", usn="admin", time_que=data.time_list)


@app.route('/route/student', methods=['POST', 'GET'])
def route_stu():
    data.initconflict()#初始化
    global time_list
    g.uname = session.get('now_user')
    str_all = ["/static/js/qustmap_shahe.js", "/static/js/qustmap_headquarter.js"]
    str_choose = "/static/js/qustmap_shahe.js"
    template_chose = "qustmap_student.html"
    route_in.send()
    if request.method == 'POST':  # 此时如果是提交
        way = request.form.get('way')
        if way == '010':  # 此时是沙河
            template_chose = "qustmap_student.html"
            str_choose = str_all[0]
        elif way == '001':  # 此时为本部
            template_chose = "qustmap_student.html"
            str_choose = str_all[1]
        elif way == '100':  # 此时为两地的跨越
            template_chose = "one_to_one_admin.html"
    if template_chose == "qustmap_student.html":
        return render_template(template_chose, ways=str_choose, cla4="active", usn="student", time_que=data.time_list)
    else:
        return render_template(template_chose, cla4="active", usn="student", time_que=data.time_list)


@app.route('/logging/admin', methods=['POST', 'GET'])
def logging_fun():
    data.initconflict()#初始化
    global time_list
    g.uname = session.get('now_user')
    if request.method == 'POST':
        with open('logging.log', 'r+', encoding='utf-8') as f:
            f.seek(0)
            f.truncate()
            contents = f.read()
            a = contents.split('\n')
            a.reverse()
        return render_template('logging.html', posts=a, time_que=data.time_list, cla5='active')
    else:
        logging_in.send()
        with open('logging.log', 'r', encoding='utf-8') as f:
            contents = f.read()
            contents.split('\n')
            a = contents.split('\n')
            a.reverse()
        return render_template('logging.html', posts=a, time_que=data.time_list, cla5='active')


@app.route('/direct_course/<course>/')
def direct_course(course):
    display="" #init
    g.uname=session.get('now_user')
    if g.uname=="master":
        display="block"
    else:
        display="none"
    direct_course_go.send()
    global homework
    global coursename
    material = None
    test1 = None
    homework1 = None
    flag = -1
    flag1 = -1  # 不存在课程资料
    flag2 = -1  # 不存在作业
    homework_length=0 #作业的个数
    material_length=0 #资料的个数
    post = None
    for a in courses:
        if a.get("cause_name") == course:
            flag = 1
            post = a
    if flag == -1:
        return render_template("NotFound.html")
    else:
        data.coursename = course
        for i in range(0, len(courses_material)):
            if courses_material[i]["coursename"] == course:
                flag1 = i
                break
        if flag1 == -1:  # 如果其不存在
            material = None
            material_length=0
        else:  # 如果存在的话
            material = courses_material[flag1]
            material_length = len(material["material_name"])

        for j in range(0, len(homework)): #这里获得的大小
            if homework[j]["coursename"] == course:
                flag2 = j
                break
        if flag2 == -1:  # 如果不存在
            homework1 = None
            homework_length=0
        else:  # 如果存在
            homework1 = homework[flag2]
            homework_length = len(homework1["homework"])
            #最后的变量是标志是否发生了冲突
        return render_template("causes_page.html", post=post, mat=material, hw=homework1,hw_length=homework_length,mat_length=material_length,ifdisplay=display,con=data.material_conflict,back=g.uname)

'''
课程资料提交位置:
实现功能：提交，压缩，下载，删除
'''
@app.route('/direct_course/materials/<coursename_temp>', methods=['POST'])
def materials_submit(coursename_temp):
    data.initconflict()#初始化
    if request.method == "POST":
        UPLOAD_PATH = os.path.join(os.path.dirname(__file__), data.coursename)  # 当前的文件路径
        if not os.path.exists(UPLOAD_PATH):  # 如果文件夹不存在则创建文件夹
            os.mkdir(UPLOAD_PATH)  # 创建文件夹
        material_file = request.files.get("course-file")
        # 保存文件
        filename = material_file.filename
        file_name = secure_filename(filename)  # 文件名的安全转换
        file_path = os.path.join(UPLOAD_PATH, file_name)
        material_file.save(file_path) #保存文件
        flag = -1  # 还是标志是否存在这个课程的名称 如果不存在则增加
        for i in range(0, len(courses_material)):
            if courses_material[i]["coursename"] == data.coursename:
                flag = i
                break
        if request.form.get('compress') == "yes":
            file_encode(file_path)
            os.remove(file_path) # 删除源文件 然后生成一个新的名字
            file_name=file_name.split(".")[0]+".ys" #生成一个新的名字
        for i in range(0,len(courses_material[flag]["material_name"])):
            if courses_material[flag]["material_name"][i].split(".")[0]==file_name.split(".")[0]:
                data.material_conflict=1#发生了冲突
                return redirect("/direct_course/" + coursename_temp) #如果发生了冲突则直接返回
            else:
                data.material_conflict=0
        if flag == -1:  # 如果不存在
            length = len(courses_material)
            temp = {"coursename": data.coursename, "material_name": [file_name]}
            courses_material.append(temp)
            with open('./static/data/courses_material.json', "w", encoding="utf-8") as fp:
                json.dump(courses_material, fp, ensure_ascii=False, separators=('\n,', ':'))
        else:
            courses_material[flag]["material_name"].append(file_name)  # 如果存在则增加名字
        data.upload_material_name=file_name
        upload_material_signal.send() #发送信号
        with open('./static/data/courses_material.json', "w", encoding="utf-8") as fp:#最后重新写入
            json.dump(courses_material, fp, ensure_ascii=False, separators=('\n,', ':'))
        return redirect("/direct_course/"+coursename_temp)

@app.route('/course/download/',methods=['POST']) #实现下载的路由
def download_material():
    data.initconflict()#初始化
    g.uname=session.get('now_user')
    DOWNLOAD_PATH = os.path.join(os.path.dirname(__file__), data.coursename)  # 当前的文件路径
    #得到文件名
    download_name=request.form.get("downloadmaterial")
    #将文件名拆分

    if download_name.split(".")[1]=="ys": #如果是一个压缩文件
        DOWNLOAD_PATH_YS = os.path.join(DOWNLOAD_PATH, download_name)  # 将字符串进行连接
        file_decode(DOWNLOAD_PATH_YS) #解压当前文件
        resource=download_name.split(".")[0]+"."+datatemp.decodeFile
        DOWNLOAD_PATH_RESULT=os.path.join(DOWNLOAD_PATH,resource) #将路径进行拼接
        data.download_material_name=resource
        download_material_signal.send() # 下载成功信号
        return send_from_directory(path=DOWNLOAD_PATH_RESULT, directory=DOWNLOAD_PATH, filename=resource,as_attachment=True)
    else:
        DOWNLOAD_PATH_RESULT=os.path.join(DOWNLOAD_PATH,download_name)
        print(DOWNLOAD_PATH_RESULT)
        data.download_material_name=download_name
        download_material_signal.send() #下载成功发送信号
        return send_from_directory(path=DOWNLOAD_PATH_RESULT, directory=DOWNLOAD_PATH, filename=download_name,as_attachment=True)

'''
作业提交位置：
实现功能：压缩，查重
'''

@app.route('/direct_course/homework/', methods=['POST'])
def homework_submit(): #前端表单中多添加了一个元素，用于标志第几次作业
    data.initconflict()#初始化
    if request.method == "POST":
        UPLOAD_PATH = os.path.join(os.path.dirname(__file__), data.coursename + "_homework")  # 当前的文件路径
        if not os.path.exists(UPLOAD_PATH):  # 如果文件夹不存在则创建文件夹
            os.mkdir(UPLOAD_PATH)  # 创建文件夹
        #得到文件名
        homework_file = request.files.get("course-homework")
        # 保存文件
        filename = homework_file.filename
        file_name = secure_filename(filename)  # 文件名的安全转换
        index=int(request.form.get("homeworkoption"))#传递过来的提交第几次作业
        Directory_path=os.path.join(UPLOAD_PATH,f"第{index+1}次作业")
        if not os.path.exists(Directory_path):
            os.mkdir(Directory_path) #如果不存在第i次作业这个文件夹则创建
        #得到新的文件位置
        file_path = os.path.join(Directory_path, file_name)
        flag = -1  # 还是标志是否存在这个课程的名称 如果不存在则增加
        for i in range(0, len(homework)):
            if homework[i]["coursename"] == data.coursename:
                flag = i
                break
        if flag == -1:  # 如果不存在当前课程的作业，则增加当前的文件名
            temp = {"coursename": data.coursename}
            homework.append(temp)
        else:
            if file_name == homework[flag]["homework"][index]["filename"]:
                data.material_conflict=2 # 发生了冲突结果是这样的
                return redirect("/direct_course/" + data.coursename + "/")
            else: #如果当前不存在
                data.material_conflict=0 # 没有发生冲突
                homework_file.save(file_path)
                homework[flag]["homework"][index]["filename"]=file_name #如果当前没有发生冲突则增加
        if request.form.get('compress') == "yes":
            file_encode(file_path)
        upload_homework_signal.send() #上传成功作业
        with open('./static/data/homework.json', "w", encoding="utf-8") as fp:#最后重新写入
            json.dump(homework, fp, ensure_ascii=False, separators=('\n,', ':'))
        return redirect("/direct_course/" + data.coursename + "/")

@app.route('/direct_course/homework/addhomework/',methods=['POST'])
def addhomework():
    '''添加作业'''
    g.uname=session.get('now_user')
    add_homework.send() #向日志写入信息
    flag=-1 #用于判断是否存在当前课程的作业
    temp={}

    for i in range(0,len(homework)):
        print(data.coursename==homework[i]["coursename"])
        if data.coursename==homework[i]["coursename"]:
            flag=i
            break
    if flag==-1:#如果是-1的话就是证明没有找到 此时则向列表中添加
        temp={"coursename":data.coursename,"homework":[]}
        homework.append(temp)
    else:
        homework[flag]["homework"].append({"content":request.form.get("addhomework-content"),"filename":""})
    with open('./static/data/homework.json', "w", encoding="utf-8") as fp:  # 最后重新写入
        json.dump(homework, fp, ensure_ascii=False, separators=('\n,', ':'))
    return redirect("/direct_course/" + data.coursename + "/")

@app.route('/time_control', methods=['POST'])  # 用于控制时间 ，所有的时间系统都采用当前的操作
def time_control():
    time = request.form.get('time')
    data.time_list = json.loads(time)  # 得到了时间列表
    return "time_yes"

@app.route('/getData4JS', methods=['POST', 'GET'])
def get_data_4_js():
    return json.dumps(courses, ensure_ascii=False)


@app.route('/getData4JS2', methods=['POST', 'GET'])
def get_data_4_js_2():
    return json.dumps(out_courses, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True, port=2000)
    student_filePtr.close()
    admin_filePtr.close()
    course_filePtr.close()
    out_course_filePtr.close()
