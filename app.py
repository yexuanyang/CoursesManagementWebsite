from flask import Flask, render_template, request, redirect, g, session
import setting
import json
from signals import logging_in, login_space, in_course, route_in, out_activity

app = Flask(__name__)

app.config.from_object(setting)
app.config['SECRET_KEY'] = 'yyx'
admin_filePtr = open("./static/data/admin.json", "r", encoding='utf-8')
student_filePtr = open("./static/data/stu.json", "r", encoding='utf-8')
course_filePtr = open("./static/data/course.json", "r", encoding='utf-8')
# admins = [{"usn": "master", "pwd": "123"}]
# student = [{"usn": "student", "pwd": "123"}]

admins = json.load(admin_filePtr)
student = json.load(student_filePtr)
courses = json.load(course_filePtr)
print(admins)
print(student)
print("hello world")

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
            json.dump(student, fp)

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
            json.dump(student, fp)
            return redirect('/admin/admin')

    for ad in admins:
        print(ad['usn'])
        print(ad)
        if usn == ad['usn']:
            admins.remove(ad)
            print(ad)
            fp = open("./static/data/admin.json", "w", encoding='utf-8')
            json.dump(admins, fp)
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
                    json.dump(student, fp)
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
                    json.dump(student, fp)
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
    return render_template('admin_new.html', cla1='active')


@app.route('/index/student')
def student_index():
    return render_template('student_index.html', cla1='active')


@app.route('/in_course/student', methods=['POST', 'GET'])
def in_course_fun_stu():
    g.uname = session.get('now_user')
    in_course.send()
    return render_template('student_course.html', cla2='active', posts=courses)


@app.route('/in_course/admin', methods=['POST', 'GET'])
def in_course_fun():
    g.uname = session.get('now_user')
    in_course.send()
    return render_template('student_course_admin.html', cla2='active', posts=courses)


@app.route('/out_course/admin', methods=['POST', 'GET'])
def out_course_fun():
    g.uname = session.get('now_user')
    out_activity.send()
    return render_template('admin_new.html', cla3='activate')


@app.route('/out_course/student', methods=['POST', 'GET'])
def out_course_fun_stu():
    g.uname = session.get('now_user')
    out_activity.send()
    return render_template('student_course.html', cla4='activate')


@app.route('/route/admin', methods=['POST', 'GET'])
def route():
    g.uname = session.get('now_user')
    str_all = ["/static/js/qustmap_shahe.js", "/static/js/qustmap_headquarter.js"]
    str_choose = "/static/js/qustmap_shahe.js"
    route_in.send()
    if request.method == 'POST':  # 此时如果是提交
        way = request.form.get('way')
        print(way)
        if way == '010':  # 此时是沙河
            str_choose = str_all[0]
            print(str_choose)
            # render_template('qustmap_student.html',ways=str_choose)
        elif way == '001':  # 此时为本部
            str_choose = str_all[1]
            # render_template('qustmap_student.html',ways="/static/js/qustmap_headquarter.js")
    return render_template('qustmap_admin.html', ways=str_choose, cla4="active", usn="admin")


@app.route('/route/student', methods=['POST', 'GET'])
def route_stu():
    g.uname = session.get('now_user')
    str_all = ["/static/js/qustmap_shahe.js", "/static/js/qustmap_headquarter.js"]
    str_choose = "/static/js/qustmap_shahe.js"
    route_in.send()
    if request.method == 'POST':  # 此时如果是提交
        way = request.form.get('way')
        if way == '010':  # 此时是沙河
            str_choose = str_all[0]
            # render_template('qustmap_student.html',ways=str_choose)
        elif way == '001':  # 此时为本部
            str_choose = str_all[1]
            # render_template('qustmap_student.html',ways="/static/js/qustmap_headquarter.js")
    return render_template('qustmap_student.html', ways=str_choose, cla4="active", usn="student")


@app.route('/logging/admin', methods=['POST', 'GET'])
def logging_fun():
    g.uname = session.get('now_user')
    if request.method == 'POST':
        with open('logging.log', 'r+', encoding='utf-8') as f:
            f.seek(0)
            f.truncate()
            contents = f.read()
            a = contents.split('\n')
        return render_template('admin_new.html', posts=a)
    else:
        logging_in.send()
        with open('logging.log', 'r', encoding='utf-8') as f:
            contents = f.read()
            a = contents.split('\n')
        return render_template('admin_new.html', posts=a)


@app.route('/course_inf', methods=['POST', 'GET'])
def show():
    return


if __name__ == '__main__':
    app.run()
    student_filePtr.close()
    admin_filePtr.close()
    course_filePtr.close()
