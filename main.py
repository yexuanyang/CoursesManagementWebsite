from flask import Flask, render_template, g, request
from signals import logging_in, login_space, in_course, route_in, out_activity

app = Flask(__name__)



@app.route('/')
def hello():
    g.uname = "小b登"
    if g.uname:  # 如果这个名称存在的话
        login_space.send()
        return "hello world"
    else:
        return "您未登录"


# 首页
@app.route('/index/<usn>')
def admin_index(usn):
    g.uname = usn
    return render_template('admin_new.html')


# 课内
@app.route('/in_course/', methods=['POST', 'GET'])
def in_course_fun():
    g.uname = "小b登"
    in_course.send()
    return render_template('admin_new.html')


# 课外
@app.route('/out_course/', methods=['POST', 'GET'])
def out_course_fun():
    g.uname = "小b登"
    out_activity.send()
    return render_template('admin_new.html')


# 导航
@app.route('/route/', methods=['POST', 'GET'])
def route():
    g.uname = "小b登"
    route_in.send()
    return render_template('admin_new.html')


# 日志


@app.route('/logging/', methods=['POST', 'GET'])
def logging_fun():
    g.uname = "小b登"
    if (request.method == 'POST'):
        with open('logging.log', 'r+', encoding='utf-8') as f:
            f.seek(0)
            f.truncate()
        return render_template('admin_new.html')
    else:
        logging_in.send()
        with open('logging.log', 'r', encoding='utf-8') as f:
            contents = f.read()
            a = contents.split('\n')
        return render_template('admin_new.html', posts=a)


if __name__ == '__main__':
    app.run(debug=True)
