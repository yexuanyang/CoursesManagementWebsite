from flask import Flask, render_template, request, redirect, g, session
import setting
import json
import datetime
from signals import logging_in, login_space, in_course, route_in, out_activity, in_course_add, in_course_delete, \
    in_course_change, out_activity_set
from forms import OutCourseForms, InCourseForms

app = Flask(__name__)

app.config.from_object(setting)
app.config['SECRET_KEY'] = 'yyx'
app.config['JSON_AS_ASCII'] = False
admin_filePtr = open("./static/data/admin.json", "r", encoding='utf-8')
student_filePtr = open("./static/data/stu.json", "r", encoding='utf-8')
course_filePtr = open("./static/data/course.json", "r", encoding='utf-8')
out_course_filePtr = open("./static/data/out_course.json", "r", encoding='utf-8')

admins = json.load(admin_filePtr)
student = json.load(student_filePtr)
courses = json.load(course_filePtr)
out_courses = json.load(out_course_filePtr)
time_list = [10, 0, 0]
chToint = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "日": 7}


def sort_activity_time(e):
    return e['activity_time']


def strToWeekDay(str):
    str = str.split('-')
    time = datetime.datetime(int(str[0]), int(str[1]), int(str[2]))
    weekday = time.weekday() + 1
    return weekday


@app.route('/')
def index():
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
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
                return '密码错误'

        for us in admins:
            if us['usn'] == usn and us['pwd'] == pwd:
                session['now_user'] = usn
                g.uname = session['now_user']
                if g.uname:  # 如果这个名称存在的话
                    login_space.send()
                return redirect('/index/' + 'admin')
            elif us['usn'] == usn and us['pwd'] != pwd:
                return '密码错误'

        return '账号不存在'

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        usn = request.form.get('usn')
        pwd = request.form.get('pwd')
        pwd1 = request.form.get('pwd1')

        for stu in student:
            if stu['usn'] == usn:
                return '账号已存在'

        for us in admins:
            if us['usn'] == usn:
                return '账号已存在'

        if pwd1 == pwd:
            student.append({'usn': usn, 'pwd': pwd})
            fp = open("./static/data/stu.json", "w", encoding='utf-8')
            json.dump(student, fp, ensure_ascii=False, separators=(',', ':'))
            fp.close()

        else:
            return "密码输入不一致"

        print(type(usn))
        print(student)

    return render_template('register.html')


# 查看usn用户的密码，提供更新功能；若usn == 'admin' 那么显示所有的用户和密码并提供删除和更新功能
@app.route('/admin/<string:usn>', methods=['GET', 'POST'])
def admin(usn):
    if request.method == 'POST':
        print(request.form.get('usn'))
        print(request.form.get('pwd'))
    return render_template('admin.html', student=student, admins=admins, usn=usn)


# 删除
@app.route('/delete', methods=['GET', 'POST'])
def delete():
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
    print(request.method)
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
                            return '权限不足'
            return '用户不存在'
        else:
            return '密码输入不一致'

    return render_template('forget.html')


# 学生课程信息管理首页
@app.route('/index/admin')
def admin_index():
    global time_list
    return render_template('admin_new.html', cla1='active', time_que=time_list)


@app.route('/index/student')
def student_index():
    global time_list
    return render_template('student_index.html', cla1='active', time_que=time_list)


@app.route('/in_course/student', methods=['POST', 'GET'])
def in_course_fun_stu():
    global time_list
    g.uname = session.get('now_user')
    in_course.send()
    return render_template('student_course.html', cla2='active', posts=courses, time_que=time_list)


@app.route('/in_course/admin', methods=['POST', 'GET'])
def in_course_fun():
    global time_list
    g.uname = session.get('now_user')
    in_course.send()
    return render_template('student_course_admin.html', cla2='active', posts=courses, time_que=time_list)


@app.route('/in_course/admin/add', methods=['POST', 'GET'])
def in_course_add_func():
    form = InCourseForms()

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

        courses.append(newcourse)
        with open('./static/data/course.json', 'w', encoding='utf-8') as fp:
            json.dump(courses, fp, ensure_ascii=False, separators=('\n,', ':'))
        return redirect('/in_course/admin')

    return render_template('add_course.html', form=form)


@app.route('/in_course/admin/delete', methods=['POST', 'GET'])
def in_course_delete_fun():
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
    global time_list
    form = InCourseForms()
    id1 = request.args.get('id1')
    cause_name = request.args.get('cause_name')
    teacher = request.args.get('teacher')
    time = request.args.get('time')
    location = request.args.get('location')
    qq = request.args.get('qq')
    exam_time = request.args.get('exam_time')

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

        courses.insert(int(id1) - 1, newcourse)

        with open('./static/data/course.json', 'w', encoding='utf-8') as fp:
            json.dump(courses, fp, ensure_ascii=False, separators=('\n,', ':'))

        return redirect('/in_course/admin')
    return render_template('change_course.html', form=form, time=time, location=location, exam_time=exam_time,
                           cause_name=cause_name, qq=qq, teacher=teacher)


@app.route('/out_course/admin', methods=['POST', 'GET'])
def out_course_fun():
    global time_list
    g.uname = session.get('now_user')
    out_activity.send()
    return render_template('student_out_course_admin.html', cla3='active', posts=out_courses, time_que=time_list)


@app.route('/out_course/admin/add', methods=['POST', 'GET'])
def out_course_add_fun():
    conflict = False
    conflict_activity = {}
    conflict_in_course = False
    conflict_which_course = {}
    form = OutCourseForms()
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
            return redirect('/out_course/admin')

    return render_template('add_out_course.html', cla3='active', posts=out_courses, time_que=time_list, form=form,
                           conflict=conflict, conflict_activity=conflict_activity,
                           conflict_in_course=conflict_in_course, conflict_which_course=conflict_which_course)


@app.route('/out_course/admin/delete', methods=['POST', 'GET'])
def out_course_del_fun():
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
    global time_list
    g.uname = session.get('now_user')
    out_activity.send()
    return render_template('student_out_course.html', cla3='active', posts=out_courses, time_que=time_list)


@app.route('/out_course/student/add', methods=['POST', 'GET'])
def out_course_add_fun_stu():
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
    g.uname = session.get('now_user')
    out_activity_set.send()
    delete_list = request.form.getlist('checklist')
    print(delete_list)
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
        return render_template(template_chose, ways=str_choose, cla4="active", usn="admin", time_que=time_list)
    else:
        return render_template(template_chose, cla4="active", usn="admin", time_que=time_list)


@app.route('/route/student', methods=['POST', 'GET'])
def route_stu():
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
        return render_template(template_chose, ways=str_choose, cla4="active", usn="student", time_que=time_list)
    else:
        return render_template(template_chose, cla4="active", usn="student", time_que=time_list)


@app.route('/logging/admin', methods=['POST', 'GET'])
def logging_fun():
    global time_list
    g.uname = session.get('now_user')
    if request.method == 'POST':
        with open('logging.log', 'r+', encoding='utf-8') as f:
            f.seek(0)
            f.truncate()
            contents = f.read()
            a = contents.split('\n')
            a.reverse()
        return render_template('admin_new.html', posts=a,time_que=time_list)
    else:
        logging_in.send()
        with open('logging.log', 'r', encoding='utf-8') as f:
            contents = f.read()
            contents.split('\n')
            a = contents.split('\n')
            a.reverse()
        return render_template('admin_new.html', posts=a, time_que=time_list)

@app.route('/direct_course/<course>/')
def direct_course(course):
    flag = 0
    post = None
    print(courses)
    for a in courses:
        if a.get("cause_name") == course:
            flag = 1
            post = a
    if flag == 0:
        return render_template("NotFound.html")
    else:
        return render_template("causes_page.html", post=post)


@app.route('/time_control', methods=['POST'])  # 用于控制时间 ，所有的时间系统都采用当前的操作
def time_control():
    time = request.form.get('time')
    global time_list
    if (time_list == []):
        time_list = [10, 0, 0]
    time_list = json.loads(time)  # 得到了时间列表
    return "time_yes"


if __name__ == '__main__':
    app.run(debug=True, port=2000)
    student_filePtr.close()
    admin_filePtr.close()
    course_filePtr.close()
    out_course_filePtr.close()
