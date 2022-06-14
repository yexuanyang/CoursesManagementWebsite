## **数据结构说明和数据结构字典**

### 1.前端

#### 		(1)qustmap_shahe.js & qustmap_headquarter.js (导航页面使用的js)

​			var PathToEnd = new Array(20)  数组，对起始点到每一个点的最短距离所在的点的记录，例如PathtoEnd[1]=3，则说明到达其最短路径的点为索引为3的点

​			var ByBike=6 整数，骑自行车的速度，单位为m/s

​			var Onfootwalk=2  整数，步行的速度，单位为m/s

​			var pointName 数组，用于记录每一个点的名称，例如pointName[0]="商店",则代表索引为0的点的名称为商店

​			var pointCord 数组，用于记录每一个点的经纬度，用于百度地图API的调用

​			var INF = 99999 整数，用于标记两点之间无法到达，即长度为正无穷

​			var path 二维数组，用于标记每一个点到另外一个点的距离，当不存在该路径时为INF，例如第一行第二列的值为300，也就是说当前索引为0的点到索引为1的点距离为200m

​			var map 百度地图地图对象

​			var point 百度地图地图展开中心点坐标

​			var marker 地图上标记位置也就是我们支持导航的点的坐标

​			var button 界面上的按钮，利用DOM进行获取，点击获取最短时间路径导航

​			var button2 界面上的按钮，利用DOM进行获取，点击获取最短路径导航

#### 	(2)time.js（时间系统以及课程管理报时、课外活动管理报时使用的js）

​			var MonthTable 二维数组，用于记录每一个月的天数，用于日期更新的情况，例如第二行为[31,31]代表1月份平年和闰年均为31天

​			var t 定时器，用于记录时间的更新

​			var multiple 时间速度加倍，默认为1也就是1倍速度，若被调整为2也就是2倍速度

​			var timeset 设置的定时器间隔，默认为10，若增加倍速，则会进行调整

​			var accelerator 设置的加速按钮，点击之后时间会进行加速，同样是利用DOM进行获取

​			var music 获取前端音乐播放器标签，同样利用DOM进行获取

​			var year 获取前端的年份标签

​			var month 获取前端的月份标签

​			var day 获取前端的日标签

​			var week 获取前端的星期几标签

​			var minute 获取前端的分钟标签

​			var second1 获取前端的秒标签

​			var Y 前端年份的数值

​			var MONTH 前端月份的数值

​			var DAY 前端日的数值

​			var W 前端星期的数值

​			var H 前端小时的数值

​			var min 前端分钟的数值

​			var second 前端秒的数值

​			var btn2 获取前端的开始按钮

​			var pause 获取前端时间的暂停按钮

​			var data_list 数组，前端的整个日期年月日星期小时分秒的数组，用于打包之后传递给后端

​			var popupwindow 获取前端的弹出窗口对象

​			var popupwindow 获取前端弹出窗口对象的标题

​			var popupwindowmsg 获取前端弹出窗口对象的提示信息

​			var chtoInt 对象，用于将大写的数字“一”等转换为小写阿拉伯数字

​			var in_course_json 自调用函数，用于从后端获取课程的信息，格式为json

​			var out_course_json 自调用函数，用于从后端获取课外活动的信息，格式为json

​			var in_course_time_json json格式，用于记录课程的时间

​			var course_name_json json格式，用于记录课程的名称

​			var exam_time_json json格式，用于记录课程考试的时间

​			var out_course_begin_time_json json格式，用于记录课外活动的开始时间

​			var out_course_end_time json格式，用于记录课外活动的结束时间

​			var out_course_date_json json格式，用于记录课外活动的日期

​			var out_course_name_json json格式，用于记录课外活动的名称

​			var in_course_time 数组，获取前端的课内课程时间的标签

​			var course_name 数组，获取前端的课内课程名称的标签

​			var exam_time 数组，获取前端课内课程的考试时间的标签

​			var out_course_begin_time 数组，获取前端课外活动开始时间的标签

​			var out_course_end_time 数组，获取前端课外活动结束时间的标签

​			var out_course_date 数组，获取前端课外活动日期的标签

​			var out_course_name 数组，获取前端课外活动的名称的标签

​			var class_begin 布尔值，用于记录是否有课程开始

​			var class_end 布尔值，用于记录是否有课程结束

​			var out_course_begin 布尔值，用于记录课外活动是否开始

​			var out_course_end 布尔值，用于记录课外活动是否结束

​			var exam_start 布尔值，用于记录考试是否开始

​			var exam_end 布尔值，用于记录考试是否结束

​			var walk_time 整型，用于记录在采用公交的方式上走路使用的时间

​			var timetable_bus 获取前端公交时刻表标签

​			var timetable_schoolbus 获取前端校车时刻表标签

​			var btn_schoolbus 按钮，用于显示校车时刻表标签

​			var btn_bus 按钮，用于显示公交时刻表的标签

​			var show_btn_bus 按钮，用于显示公交的路线图

​			var imgforbus 图片，公交线路图

​			var list_schoolbus1 校车时刻表，从沙河到本部

​			var list_schoolbus  校车时刻表，从本部到沙河

​			var list_bus 公交时刻表

​			var confirm 按钮，确定按钮，点击后进行路线规划

### 2.后端

​		后端设计了35个路由，包含4个有效的.py文件包含管理员页面和学生页面路由，同时包含一些获取信息的路由，这里讲述他们具有的全局变量

#### 		(1)app.py (主文件)

​		admin_filePtr 指向json文件的指针，用于存储管理员的账号

​		student_filePtr 指向json文件的指针，用于存储学生的账号

​		course_filePtr 指向json文件的指针，用于存储课程

​		out_course_filePtr 指向json文件的指针，用于存储课外活动

​		course_material_filePtr 指向json文件的指针，用于存储课程资料与课程名称的对应关系

​		homework_filePtr 指向json文件的指针，用于存储课程作业与课程名称的对应关系

​		admins 列表，json格式数据，用于存储从文件中读出的json数据，管理员账号密码

​		student 列表，json格式数据，用于存储从文件中读出的json数据，学生账户密码

​		courses 列表，json格式数据，用于存储从文件中读出的json数据，课程

​		out_courses 列表，json格式数据，用于存储从文件中读出的json数据，课外活动

​		courses_material 列表，json格式数据，用于存储从文件中读出的json数据，课程资料

​		homework 列表，json格式数据，用于存储从文件中读出的json数据，课程作业 

​		chToint 字典，用于将大写的汉字数字转化为小写的阿拉伯数字

​		data1 DataStore类的实例对象，以下为DataStore的定义

```python
class DataStore:
    coursename = ""
    upload_path = ""
    time_list = [2022, 5, 16, 1, 10, 0, 0]
    homework_name=[]
    material_name=[]
    homework_conflict=-1 #0代表没有冲突 1代表发生了冲突
    material_conflict=-1 #代表材料的冲突 -1代表两种情况都没有发生
    # homework_note="" #提示信息 如果提交成功则赋值成为”提交成功“ 否则 赋值为"file_name+"与后台提交的文件名重复，提交失败"
    # material_note="" #提示信息 类似上面
    download_material_name=""; #下载的资料名称
    upload_material_name=""#上传的课程资料名称
    def initconflict(self): #初始化所有的变量 方便进行下一次操作
        self.homework_conflict= -1#没有发生冲突
        self.material_conflict=-1
```

#### 		(2)signals.py（用于存储定义信号，多用于日志系统）

​		space = Namespace()  命名空间

​		add_homework signal类的实例对象，用于添加作业时发送信号

​		direct_course_go signal类的实例对象，用于进入了某个具体的课程页面时发送到信号

​		login_space signal类的实例对象，用于用户登录之后发送的信号

​		in_course signal类的实例对象，用于用户进入具体课程页面之后发送的信号

​		in_course_delete signal类的实例对象，用于用户删除课程之后发送的信号

​		in_course_add signal类的实例对象，用于用户增加课程发送的信号

​		in_course_change signal类的实例对象，用于用户更改课程之后发送的信号

​		out_activity signal类的实例对象，用于用户进入了课外管理页面发送的信号

​		out_activity_set signal类的实例对象，用于用户增加课外活动发送的信号

​		out_activity_delete signal类的实例对象，用于用户删除课外活动之后的发送的信号

​		out_activity_in signal类的实例对象，用于用户更改了课外活动发送的信号

​		route_in signal类的实例对象，用于用户进入导航系统时发送的信号

​		route_search signal类的实例对象，用于用户进行路线规划时发送的信号

​		upload_material_signal signal类的实例对象，用于用户上传课程资料时发送的信号

​		logging_in signal类的实例对象，用于用户进入日志系统时发送的信号

​		download_material_signal signal类的实例对象，用于用户下载课程资料发送的信号

​		upload_homework_signal signal类的实例对象，用于用户提交课程作业发送的信号

​		search_course_activity signal类的实例对象，用于用户搜索课程时发送的信号

#### 		(3)compress.py（用于存储压缩算法的文件）

​		datatemp  datatmp的实例对象，datatmp的定义如下:

```python
class datatmp:
    decodeFile="" #解压之后的文件名
```

#### 	  (4)forms.py（用于存储WTF表单的文件）

​		无全局变量

## 各模块设计说明

​	本次课程设计中我们将项目分成了以下几个模块：

​	1.日志模块

​	2.课程管理模块

​	3.课外活动管理模块

​	4.登录模块

​	5.导航模块

​	6.时间模块

​	7.文件管理模块

以下是具体介绍：

### 	1.日志模块

#### （1）算法思想

利用Python namespace中的signal进行信号的发送以及日志文件的写入，将signal绑定函数，打开logging.log文件进行写入，最后在使用的时候再读出内部的所有数据，返回到前端，实现日志的前端展现。

#### （2）算法

这里以添加作业的信号为例

```python
space = Namespace()  # 创建命名空间
add_homework=space.signal("添加了作业") #添加作业信号的创建
def addhomework_act(sender): #添加作业的函数
    '''添加了作业'''
    info=f"{g.uname}在{data.coursename}添加了新的作业"
    with open('logging.log', 'a', encoding='utf-8') as f:  # 打开日志文件然后写入
        f.write(
            f'{data.time_list[0]}-{data.time_list[1]}-{data.time_list[2]} 星期{intoch[int(data.time_list[3])]} {data.time_list[4]}:{data.time_list[5]}:{data.time_list[6]}\t' + info + "\n")  # 写入日志信息
in_course_add.connect(in_course_add_into)  # 信号与函数的绑定
```

这里实现了作业添加信号的实现

在添加作业的路由中，使用send()方法可以实现发送

```python
add_homework.send() #向日志写入信息
```

显示日志的路由如下：

```python
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
```

#### （3）特点

这样设计简单明确，同时可以实现各个模块调用日志模块时区分度高，降低了程序的耦合性

#### （4）与其他模块的关系

![未命名文件(4)](https://github.com/yexuanyang/CoursesManagementWebsite/blob/933ce7e889e7d7ae32de038f4818d51563518cbc/Images/%E6%9C%AA%E5%91%BD%E5%90%8D%E6%96%87%E4%BB%B64.png)

### 	2.课程管理模块

#### （1）算法思想

①对课程的增加和更改（管理员独占）

增加和更改本质上是相同的东西，前端发送表单给后端数据路由，改变后端中存储的课程信息，并将信息重新写回到json文件当中。

②通过某个关键字对课程进行查询

利用字符串匹配算法，利用js中的DOM流，获取课程表格中的数据，然后对输入需要查询的内容，根据选择按钮的不同，采用课程名称，或者任课教师的关键字进行注意匹配，其中利用的遍历的思想，然后不符合条件的隐藏，符合条件的保留，完成了搜索算法。

③对课程的删除（管理员独占）

在前端利用checkbox进行选择，然后点击删除按钮将信息传递到后端，删除被选中项的信息，并将新的信息写入到json文件中，实现了数据的更新。

④增加课程时进行的冲突检测

利用了判断两条线段重合的思想，可以将两个课程的时间看成两条线段，若时间有重合，也就是线段有重合，此时证明课程时间发生了冲突，后端会让前端有一个提示框进行提示。

#### （2）算法

①对课程的增加和更改（管理员独占）

展示后端中路由的处理：

增加：

```python
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
```

修改：

```python
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
```

②通过某个关键字对课程进行查询

```js
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    list="";
    // 循环表格每一行，查找匹配项
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[2];
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                list=list+"<tr>"+"\n"+tr[i].innerHTML+"\n"+"</tr>"+"\n"
            }
        }
    }
    var mydata=document.getElementById("myData");
    mydata.innerHTML=list;
    te.init('demo', { //重新加载
            height: 500 //设置高度
            ,limit: 10 //注意：请务必确保 limit 参数（默认：10）是与你服务端限定的数据条数一致
            ,page:true //开启分页
});
```

③对课程的删除（管理员独占）

后端中路由的处理：

```python
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
```

④增加课程时或更改课程时进行的冲突检测

```Python
        in_course_temp = list(courses)
        weekday = strToWeekDay(activity_time)
        for one_in_course in in_course_temp:
            int_day = chToint[one_in_course["time"][2]]
            if weekday == int_day:
                course_begin_time = one_in_course['time'][3:8]
                course_end_time = one_in_course['time'][9:]
                if (course_begin_time <= begin_time <= course_end_time) or (
                        course_begin_time <= end_time <= course_end_time):
                    conflict_in_course = True
                    conflict_which_course = one_in_course
                    break

        if not (conflict or conflict_in_course):
            out_courses.insert(int(id2) - 1, new_out_course)
```

#### （3）特点

①对课程的增加和更改（管理员独占）

在前端表单中，对时间进行了约束，只能选择特定的上课下课时间，同时也对QQ群这样的信息进行了约束，这样可以避免用户错误输入导致后端数据出现的问题。

②通过某个关键字对课程进行查询

利用朴素遍历，同时也利用了js中自带的字符串匹配，可以实现模糊搜索，可以针对某个关键字进行搜索，但是若是正式开发中，数据量增大可能导致效率降低明显。

③对课程的删除（管理员独占）

 可以进行多项选择，同时删除多个课程，极大的遍历了批量处理的需求。

④增加课程时或更改课程时进行的冲突检测

将一个具象的时间相交问题抽象化成两个线段相交的模型，极大的简化了算法设计的难度，实现了需求。

#### （4）与其他模块的关系

![2(2)](https://github.com/yexuanyang/CoursesManagementWebsite/blob/933ce7e889e7d7ae32de038f4818d51563518cbc/Images/2(2).png)

### 	3.课外活动管理模块

#### （1）算法思想

总体的思想与课外活动管理模块类似，分为以下几个算法：

①对课外活动的增加和更改

②通过某个关键字对课外活动进行查询

③对课外活动的删除

④增加课外活动或更改课外活动时进行的冲突检测

#### （2）算法

①对课外活动的增加和更改

增加：

```Python
@app.route('/out_course/admin/add', methods=['POST', 'GET'])
def out_course_add_fun():
    data.initconflict()  # 初始化
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
                if (out_courses_activity['begin_time'] <= begin_time <= out_courses_activity['end_time']) \
                        or (
                        out_courses_activity['begin_time'] <= end_time <= out_courses_activity['end_time']):
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
                if (course_begin_time <= begin_time <= course_end_time) or (
                        course_begin_time <= end_time <= course_end_time):
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
```

更改：

```Python
@app.route('/out_course/admin/change', methods=['POST', 'GET'])
def out_course_change_fun():
    data.initconflict()  # 初始化
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
                if (out_courses_activity['begin_time'] <= begin_time <= out_courses_activity['end_time']) \
                        or (
                        out_courses_activity['begin_time'] <= end_time <= out_courses_activity['end_time']):
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
                if (course_begin_time <= begin_time <= course_end_time) or (
                        course_begin_time <= end_time <= course_end_time):
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
```

②通过某个关键字对课外活动进行查询

```js
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    list="";
    // 循环表格每一行，查找匹配项
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[2];
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                list=list+"<tr>"+"\n"+tr[i].innerHTML+"\n"+"</tr>"+"\n"
            }
        }
    }
    var mydata=document.getElementById("myData");
    mydata.innerHTML=list;
    te.init('demo', { //重新加载
            height: 500 //设置高度
            ,limit: 10 //注意：请务必确保 limit 参数（默认：10）是与你服务端限定的数据条数一致
            ,page:true //开启分页
});
```

③对课外活动的删除

```Python
@app.route('/out_course/admin/delete', methods=['POST', 'GET'])
def out_course_del_fun():
    data.initconflict()  # 初始化
    global time_list
    g.uname = session.get('now_user')
    out_activity.send()
    delete_list = request.form.getlist('checklist')
    print(delete_list)
    for i in delete_list:
        if int(i) - 1 == len(out_courses):
            out_courses.pop(-1)
        else:
            out_courses.pop(int(i) - 1)
    with open('./static/data/out_course.json', "w", encoding='utf-8') as fp:
        json.dump(out_courses, fp, ensure_ascii=False, separators=('\n,', ':'))
    return redirect('/out_course/admin')
```

④增加课外活动或更改课外活动时进行的冲突检测

```Python
    # 课程时间冲突检测
    in_course_temp = list(courses)
    weekday = strToWeekDay(activity_time)
    for one_in_course in in_course_temp:
        int_day = chToint[one_in_course["time"][2]]
        if weekday == int_day:
            course_begin_time = one_in_course['time'][3:8]
            course_end_time = one_in_course['time'][9:]
            if (course_begin_time <= begin_time <= course_end_time) or (
                    course_begin_time <= end_time <= course_end_time):
                conflict_in_course = True
                conflict_which_course = one_in_course
                break

    if not (conflict or conflict_in_course):
        out_courses.insert(int(id2) - 1, new_out_course)

        with open('./static/data/out_course.json', "w", encoding='utf-8') as fp:
            json.dump(out_courses, fp, ensure_ascii=False, separators=('\n,', ':'))
        return redirect('/out_course/admin')
```

#### （3）特点

特点基本与课内管理系统相同

#### （4）与其他模块的关系

![3](https://github.com/yexuanyang/CoursesManagementWebsite/blob/933ce7e889e7d7ae32de038f4818d51563518cbc/Images/3.png)

### 	4.登录模块：

#### （1）算法思想：

①实现用户类型的判断

后端中有两个存储文件，分别存储管理员账户和普通学生账户，在程序运行之后，将两个文件分别读入到两个不同的列表中，此时若用户存在于管理员列表，则设定为管理员，同时密码正确，进入到管理员系统，若存在于学生列表中，则设定为学生，同时密码正确，进入到学生系统。在算法上，使用了遍历的思想，遍历两个列表，看用户存在于哪一个列表中。

②实现用户注册

前端的form表单传递数据到后端，只能注册学生用户，会将数据存储到普通学生列表中，此时将列表重写写回文件，实现数据文件的更新，实现了用户的注册。

③实现对用户信息的管理

总体思想为将信息通过表单传递到后端然后更新后端的数据。

#### （2）算法：

①实现用户类型的判断

```Python
admin_filePtr = open("./static/data/admin.json", "r", encoding='utf-8')
student_filePtr = open("./static/data/stu.json", "r", encoding='utf-8')
admins = json.load(admin_filePtr)
student = json.load(student_filePtr)
@app.route('/login', methods=['GET', 'POST'])
def login():
    data.initconflict()  # 初始化
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
```

②实现用户注册

```python
@app.route('/register', methods=['GET', 'POST'])
def register():
    data.initconflict()  # 初始化
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
```

③实现对用户信息的管理以及忘记密码进行修改密码

```python
# 查看usn用户的密码，提供更新功能；若usn == 'admin' 那么显示所有的用户和密码并提供删除和更新功能
@app.route('/admin/<string:usn>', methods=['GET', 'POST'])
def admin(usn):
    data.initconflict()  # 初始化
    if request.method == 'POST':
        print(request.form.get('usn'))
        print(request.form.get('pwd'))
    return render_template('admin.html', student=student, admins=admins, usn=usn)
```

```Python
# 删除
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    data.initconflict()  # 初始化
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
```

```Python
# 更新
@app.route('/change', methods=['GET', 'POST'])
def change():
    data.initconflict()  # 初始化
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
```

```Python
# 忘记密码
@app.route('/forget', methods=['GET', 'POST'])
def forget():
    data.initconflict()  # 初始化
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
```

#### （3）特点：

①实现用户类型的判断

仍然是利用了遍历的思想进行判断，环境在用户较少的情况，若用户数量增多，可能由于遍历导致算法拖慢程序运行。

②实现用户注册

简单的实现了用户注册的功能，利用了前后端数据的传递。

③实现对用户信息的管理以及忘记密码进行修改密码

简单的实现了对用户信息的管理，在管理员权限下对用户权限进行了简单管理

#### （4）与其他模块的关系

无

### 	5.导航模块（针对于单校区内部导航）

#### （1）算法思想

实现最短路径和最短时间的导航，同时生成随机的拥挤度，主要算法为迪杰斯特拉算法，利用无向图的最短路径算法，计算从开始点到其他所有点的最短距离，值得注意的是，在计算最短路径的时候，将两点之间的距离作为边，在计算最短时间时，将路程所用的时间作为边；同时为了模拟实时的拥挤度，我们采用了一个随机数的形式，若是最短路径，则采用将路径×拥挤度的形式作为新的边，若是最短时间，则是时间×拥挤度的形式进行模拟。

#### （2）算法

迪杰斯特拉算法（最短时间）

```js
var PathToEnd = new Array(20);
var ByBike=6; //通过自行车 10m/s
var Onfootwalk=2;//通过走路 2m/s
function dijkstra(path, index) {
    var m = path && path.length; //用于判断是不是为空
    var n = m && path[0].length;//用于判断第一行是不是为空
    if (m && n && m === n && index < n) { //如果表不为空 同时第一行不为空 然后
        //初始化distance
        var dis = [];
        pathLength=[];
        var visited = []; //用于标识index号至其他顶点的距离是否确定
        var randomNum;
        //这里进行一定更改，把时间作为边的权值压入栈
        for (var i = 0; i < n; ++i) { //循环遍历 把到index节点的所有距离压入栈区
            randomNum=Math.random();//生成一个随机数为拥挤度
            if(path[index][i]==99999){
                dis.push(path[index][i]);
            }else{
                dis.push(path[index][i]/((randomNum+1)*Onfootwalk)); //随机生成拥挤度
            }
            console.log(dis);
            pathLength.push(path[index][i]); //用于记录路径
            visited.push(false) //把访问的地方进行初始化
            PathToEnd[i] = -1; //到达最后的路径初始化为-1
        }
        visited[index] = true; //把开始节点的访问设置为已经访问

        for (i = 0; i < n; i++) {
            var minIndex, min = Infinity; //将最小值设置为正无穷 方便进行比较
            //找出剩余的不确定的点到index最短的距离对应的索引
            for (var j = 0; j < n; ++j) { //循环查找最小的点
                if (!visited[j] && dis[j] < min) { //如果当前的节点没有访问 也就是没有加入到当前的点中 并且值小于当前的最小值可以将
                    minIndex = j;
                    min = dis[j];
                }
            }
            visited[minIndex] = true; //标识index到此顶点的距离已经确认
            for (var k = 0; k < n; ++k) {
                //判断minIndex到k之间有无道路
                if (!visited[k] && path[minIndex][k] < Infinity) {
                    //更新distance
                    var randomTest=Math.random();
                    if (dis[k] > dis[minIndex] + path[minIndex][k]/((1+randomTest)*Onfootwalk)) {
                        dis[k] = dis[minIndex] + path[minIndex][k]/((1+randomTest)*Onfootwalk);
                        pathLength[k]=pathLength[minIndex]+path[minIndex][k];
                        PathToEnd[k] = minIndex;
                    }
                }
            }
        }
        return dis;
    }
}
```

迪杰斯特拉算法（最短路径）

```js
function dijkstra(path, index) {
    var m = path && path.length; //用于判断是不是为空
    var n = m && path[0].length;//用于判断第一行是不是为空
    if (m && n && m === n && index < n) { //如果表不为空 同时第一行不为空 然后
        //初始化distance
        var dis = [];
        pathLength=[];
        var visited = []; //用于标识index号至其他顶点的距离是否确定
        var randomNum;
        //这里进行一定更改，把时间作为边的权值压入栈
        for (var i = 0; i < n; ++i) { //循环遍历 把到index节点的所有距离压入栈区
            randomNum=Math.random();//生成一个随机数为拥挤度
            if(path[index][i]==99999){
                dis.push(path[index][i]);
            }else{
                dis.push(path[index][i]/((randomNum+1)*Onfootwalk)); //随机生成拥挤度
            }
            console.log(dis);
            pathLength.push(path[index][i]); //用于记录路径
            visited.push(false) //把访问的地方进行初始化
            PathToEnd[i] = -1; //到达最后的路径初始化为-1
        }
        visited[index] = true; //把开始节点的访问设置为已经访问

        for (i = 0; i < n; i++) {
            var minIndex, min = Infinity; //将最小值设置为正无穷 方便进行比较
            //找出剩余的不确定的点到index最短的距离对应的索引
            for (var j = 0; j < n; ++j) { //循环查找最小的点
                if (!visited[j] && dis[j] < min) { //如果当前的节点没有访问 也就是没有加入到当前的点中 并且值小于当前的最小值可以将
                    minIndex = j;
                    min = dis[j];
                }
            }
            visited[minIndex] = true; //标识index到此顶点的距离已经确认
            for (var k = 0; k < n; ++k) {
                //判断minIndex到k之间有无道路
                if (!visited[k] && path[minIndex][k] < Infinity) {
                    //更新distance
                    var randomTest=Math.random();
                    if (dis[k] > dis[minIndex] + path[minIndex][k]/((1+randomTest)*Onfootwalk)) {
                        dis[k] = dis[minIndex] + path[minIndex][k]/((1+randomTest)*Onfootwalk);
                        pathLength[k]=pathLength[minIndex]+path[minIndex][k];
                        PathToEnd[k] = minIndex;
                    }
                }
            }
        }
        return dis;
    }
}
```

前端输出（最短时间）

```js
var btn=document.getElementById("button1");
btn.addEventListener("click", function() {
    if (button.click == false) {
        return;
    }

    var StartIndex = startnode.selectedIndex; //起点的索引值
    var StartValue = startnode.options[StartIndex].value; //起点的信息
    var EndIndex = endnode.selectedIndex; //终点的索引值
    var EndValue = endnode.options[EndIndex].value; //终点的信息

    PathArray = dijkstraLeastlucheng(path, StartIndex);
    DisplayPath(StartIndex, EndIndex);
    var timebybike=parseInt((PathArray[EndIndex]/ByBike)/60);//得到的结果是骑自行车用时
    var timeonfoot=parseInt((PathArray[EndIndex]/Onfootwalk)/60);//步行所用的时间
    document.getElementById("showdis").style.bottom = "5%";
    document.getElementById("showdis").innerHTML = "采用最短路径策略："+"<br>"+"当前路径的距离为：" + PathArray[EndIndex].toString() + "米"+"<br>"+"步行所用的时间为："+timeonfoot+"分钟"+"<br>"+"自行车所用的时间为："+timebybike+"分钟";
    var message=[
        "进行了最短路径导航从"+pointName[StartIndex]+"导航到"+pointName[EndIndex],
        PathArray[EndIndex].toString(),
        timeonfoot,
        timebybike
    ]

    var message_json={
        MSG:JSON.stringify(message)
    }
    $.ajax({
        url:"/GetRouteLog",
        type:"post",
        async:false,
        data:message_json,
        success:function (data){
            console.log("yes");
        }
    });
});
```

前端输出（最短路径）

```js
var button = document.getElementById("button");
button.addEventListener("click", function() {
    if (button.click == false) {
        return;
    }

    var StartIndex = startnode.selectedIndex; //起点的索引值
    var StartValue = startnode.options[StartIndex].value; //起点的信息
    var EndIndex = endnode.selectedIndex; //终点的索引值
    var EndValue = endnode.options[EndIndex].value; //终点的信息
    if (StartIndex == EndIndex) {
        alert("起点和终点不能为同一点！");
        return;
    }

    PathArray = dijkstra(path, StartIndex);
    //alert("该点到其余各点的最短距离为：" + PathArray);
    //将最短路径在地图上展示出来
    DisplayPath(StartIndex, EndIndex);
    //将最短路径的距离在页面上展示出来
    var timebybike=parseInt((PathArray[EndIndex]/3));//得到的结果是骑自行车用时
    document.getElementById("showdis").style.bottom = "5%";
    document.getElementById("showdis").innerHTML = "采用最短时间策略："+"<br>"+"当前路径的距离为：" + pathLength[EndIndex].toString() + "米"+"<br>"+"步行所用的时间为："+parseInt(PathArray[EndIndex]/60)+"分钟"+"<br>"+"自行车所用的时间为："+parseInt(PathArray[EndIndex]/180)+"分钟";
    var message=[
        "进行了最短时间导航从"+pointName[StartIndex]+"导航到"+pointName[EndIndex],
        pathLength[EndIndex].toString() ,
        parseInt(PathArray[EndIndex]/60),
        parseInt(PathArray[EndIndex]/180)
    ];
    var message_json={
        MSG:JSON.stringify(message)
    }
    $.ajax({
        url:"/GetRouteLog",
        type:"post",
        dataType:"json",
        async:false,
        data:message_json,
        success:function (data){
            console.log("yes");
        }
    });
});
```

#### （3）特点

利用迪杰斯特拉算法计算路径上到每个节点的最短路径值，同时采用随机数的方式进行拥挤度的模拟。

#### （4）与其他模块的关系

![文件](https://github.com/yexuanyang/CoursesManagementWebsite/blob/933ce7e889e7d7ae32de038f4818d51563518cbc/Images/%E6%96%87%E4%BB%B6.png)

### 	6.时间模块

#### （1）算法思想

①时间的模拟，日期更新

先是日期的更新 ，设置一个二维数组，二维数组的第一维代表是哪个月份，index为1时，则代表1月份，第二维代表平年闰年，当即将新的一天时，先判断是否是本月的最后一天，若是最后一天，则进入下个月，日转为1，月份+1，若没有到达最后一天，则是日+1，到达新的一年时，会判断本年份时平年还是闰年，来决定二月份选取哪一个项。

然后讲解时钟的模拟，利用js的定时器，实现现实的1s为系统中的1min，实现时间的同步，也就是定时器每1/60s进行一次更新，更新作为全局变量的时间。

②上课提醒、下课提醒、考试开始提醒、考试结束提醒、课外开始提醒、课外结束提醒

先从后端获取到课程的时间信息，然后循环遍历时间的数组，同时获取课程的名称信息，两个数组的索引要相对应，之后在系统每次进行时间更新时，循环遍历存储的数组，进行逐一判断，当到达时间时，则进行提醒，弹出我们设置的弹窗播放我们的音乐，同时我们也需要解决一个问题，我们的时钟是精确到秒的，而考试时间是精确到分的，此时我们设置了一个变量，当进行报时时，则将其赋值为true，防止重复进行判断报时。

③随机播放音乐

我们设置了一个随机数，生成后利用switch语句进行判断，当为1，2，3，4，5时选择存储的不同音乐，实现在提醒时随机播放音乐。

④跨校区方式导航

这里我们仍然是采用了循环遍历的方式，我们在底层存储了校车时刻表和公交车时刻表，前端有当前所在地“沙河”或者“本部”进行选择，当选择某个地方时，会选择当地的校车时刻表，然后利用时间系统，循环遍历当前的时刻表，对于校车来说，会将固定时间×随机生成的拥挤度作为行车时间，同时计算等车时间，即当前时间到时刻表中的某个时间的最小值，同时要注意的是，最小值只能选取当前时间之后的时间，然后根据这个时间计算出当前时间到到达目的地的最短时间，同时打印出拥挤度；而对于公交车而言，仍然是循环遍历公交车的时刻表，然后找到最近的公交车，然后计算等待时间+步行时间+行车时间×拥挤度，最终实现了算法。

#### （2）算法

①时间的模拟，日期更新

日期更新：

```js
var MonthTable=[
    [0,0],
    [31,31],
    [28,29],
    [31,31],
    [30,30],
    [31,31],
    [30,30],
    [31,31],
    [31,31],
    [30,30],
    [31,31],
    [30,30],
    [31,31]
];
console("MONTH:"+MONTH);
function dateplie(){ //用于日期的自增
    //判断是平年还是闰年
    var f=0;//默认是平年
    //逻辑
    /*
    访问逻辑：
        当到达当月最多的天数的时候
        当f=1访问数组中的元素是MonthTable[MONTH][f]则可以判断
     */
    if(isLeap(Y)){//如果是闰年
        f=1;
    }
    else{
        f=0;
    }
    if(parseInt(DAY)===MonthTable[parseInt(MONTH)][f]){ //如果达到当月的最后一天
        DAY=1;
        if(MONTH==12){ //如果到达12月份
            Y++;//到达下一个年份
            MONTH=1;
        }else{
            MONTH++;
        }
    }else{
        DAY++;
    }
}
/*
判断闰年
判断逻辑：
    整除4但不能除以100
    或者 可以整除400
 */
function isLeap(year){
    return (year %4==0 && year%100!=0) || (year %400==0);
}
```

时间更新：

```js
function faketime() {
    if (parseInt(W) >= 7) {
        W %= 7;
    }
    if (parseInt(H) >= 24) {
        H %= 24;
    }
    if (parseInt(min) >= 60) {
        min %= 60;
    }
    if (parseInt(second) >= 60) {
        second %= 60;
    }
    if (parseInt(second) === 59) {
        second = 0;
        if (parseInt(min) === 59) {
            if (parseInt(H) === 23) {
                dateplie();
                if (parseInt(W) === 7) {
                    W = 1;
                } else {
                    W++;
                }
                H = 0;
                min = 0;
                second = 0;
            } else {
                H++;
                min = 0;
                second = 0;
            }
        } else {
            min++;
            second = 0;
        }
    } else {
        second++;
    }
    }
```

②上课提醒、下课提醒、考试开始提醒、考试结束提醒、课外开始提醒、课外结束提醒

```js
for (let i = 0; i < in_course_json.length; i++) {
    //const inCourseTimeKey = in_course_time[i].innerHTML;
    const inCourseTimeKey = in_course_time_json[i];
    const weekday = chtoInt[inCourseTimeKey[2]];
    //const examTimeKey = exam_time[i].innerHTML;
    const examTimeKey = exam_time_json[i];
    let startYear = parseInt(examTimeKey.substring(0, 4));
    let startMonth = parseInt(examTimeKey.substring(5, 7));
    let startDay = parseInt(examTimeKey.substring(8, 10));
    let startHour = parseInt(examTimeKey.substring(11, 13));
    let startMin = parseInt(examTimeKey.substring(14, 16));
    let endYear = parseInt(examTimeKey.substring(18, 22));
    let endMonth = parseInt(examTimeKey.substring(23, 25));
    let endDay = parseInt(examTimeKey.substring(26, 28));
    let endHour = parseInt(examTimeKey.substring(29, 31));
    let endMin = parseInt(examTimeKey.substring(32));
    let endDate = examTimeKey.substring(18);
    if (!exam_start && startYear === parseInt(Y) && startMonth === parseInt(MONTH) && startDay === parseInt(DAY) && startHour === parseInt(H) && startMin === parseInt(min)) {
        exam_start = true;
        exam_end = false;
        class_begin = true;
        class_end = true;
        out_course_begin = true;
        out_course_end = true;
        generateRandom();
        music.play();//播放音乐
        popupwindowtitle.innerHTML="考试开始了";
        popupwindowmsg.innerHTML=course_name_json[i] + "考试" + "开始了\n结束时间：" + endDate;
        popupwindow.style.display="block";
        break;
    }
    if (!exam_end && endYear === parseInt(Y) && endMonth === parseInt(MONTH) && endDay === parseInt(DAY) && endHour === parseInt(H) && endMin === parseInt(min)) {
        exam_start = false;
        exam_end = true;
        class_begin = false;
        class_end = false;
        out_course_begin = false;
        out_course_end = false;
        generateRandom();
        music.play();//播放音乐
        popupwindowtitle.innerHTML="考试";
        popupwindowmsg.innerHTML=course_name_json[i] + "考试结束了";
        popupwindow.style.display="block";
        break;
    }

    if (weekday === parseInt(W)) {
        if (!class_begin && parseInt(H) === parseInt(inCourseTimeKey.substring(3, 5)) && parseInt(min) === parseInt(inCourseTimeKey.substring(6, 8))) {
            // window.alert(course_name_json[i] + "开始上课了");
            randomNum=parseInt(Math.random()*5);
            switch (randomNum){
                case 0:
                    music.src="/static/music/qb.mp3";
                    break;
                case 1:
                    music.src="/static/music/stay.mp3";
                    break;
                case 2:
                    music.src="/static/music/wmzb.mp3";
                    break;
                case 3:
                    music.src="/static/music/xc.mp3";
                    break;
                case 4:
                    music.src="/static/music/yw.mp3";
                    break;
                default:break;
            }
            generateRandom();
            music.play();//播放音乐
            popupwindowtitle.innerHTML="上课";
            popupwindowmsg.innerHTML=course_name_json[i] + "上课了";
            popupwindow.style.display="block";
            class_begin = true;
            class_end = false;
            //上课不能进行课外活动，把课外活动设置为已经开始
            out_course_begin = true;
            out_course_end = true;
            break;
        }
        if (!class_end && parseInt(H) === parseInt(inCourseTimeKey.substring(9, 11)) && parseInt(min) === parseInt(inCourseTimeKey.substring(12))) {
            // window.alert(course_name_json[i] + "下课了");
            randomNum=parseInt(Math.random()*5);
            switch (randomNum){
                case 0:
                    music.src="/static/music/qb.mp3";
                    break;
                case 1:
                    music.src="/static/music/stay.mp3";
                    break;
                case 2:
                    music.src="/static/music/wmzb.mp3";
                    break;
                case 3:
                    music.src="/static/music/xc.mp3";
                    break;
                case 4:
                    music.src="/static/music/yw.mp3";
                    break;
                default:break;
            }
            generateRandom();
            music.play();//播放音乐
            popupwindowtitle.innerHTML="下课了";
            popupwindowmsg.innerHTML=course_name_json[i] + "下课了";
            popupwindow.style.display="block";
            class_end = true;
            class_begin = false;
            //下课了可以进行课外活动，把课外活动设置为未开始
            out_course_begin = false;
            out_course_end = false;
            break;
        }
    }


}

for (let i = 0; i < out_course_json.length; i++) {
    const out_course_date_key = out_course_date_json[i];
    const out_course_begin_time_key = out_course_begin_time_json[i];
    const out_course_end_time_key = out_course_end_time_json[i];
    let year = parseInt(out_course_date_key.substring(0, 4));
    let month = parseInt(out_course_date_key.substring(5, 7));
    let day = parseInt(out_course_date_key.substring(8));
    let BeginTimeHour = parseInt(out_course_begin_time_key.substring(0, 2));
    let BeginTimeMin = parseInt(out_course_begin_time_key.substring(3));
    let EndTimeHour = parseInt(out_course_end_time_key.substring(0, 2));
    let EndTimeMin = parseInt(out_course_end_time_key.substring(3));
    if (!out_course_begin && year === parseInt(Y) && month === parseInt(MONTH) && day === parseInt((DAY)) && BeginTimeHour === parseInt(H) && BeginTimeMin === parseInt(min)) {
        out_course_begin = true;
        out_course_end = false;
        generateRandom()
        music.play();//播放音乐
        popupwindowtitle.innerHTML="课外活动";
        popupwindowmsg.innerHTML="课外活动 " + out_course_name_json[i] + " 开始了\n结束时间：" + out_course_end_time_key;
        popupwindow.style.display="block";
        break;
    }
    if (!out_course_end && year === parseInt(Y) && month === parseInt(MONTH) && day === parseInt((DAY)) && EndTimeHour === parseInt(H) && EndTimeMin === parseInt(min)) {
        out_course_begin = false;
        out_course_end = true;
        generateRandom()
        music.play();//播放音乐
        popupwindowtitle.innerHTML="课外活动";
        popupwindowmsg.innerHTML="课外活动 " + out_course_name_json[i] + " 结束了";
        popupwindow.style.display="block";
        break;
    }

}
```

③随机播放音乐

```js
function generateRandom(){
                randomNum=parseInt(Math.random()*5);
                switch (randomNum){
                    case 0:
                        music.src="/static/music/qb.mp3";
                        break;
                    case 1:
                        music.src="/static/music/stay.mp3";
                        break;
                    case 2:
                        music.src="/static/music/wmzb.mp3";
                        break;
                    case 3:
                        music.src="/static/music/xc.mp3";
                        break;
                    case 4:
                        music.src="/static/music/yw.mp3";
                        break;
                    default:break;
                }
    console.log(randomNum);
}
```

④跨校区方式导航

```js
list_schoolbus1 = [
    "9:30",
    "11:30",
    "12:30",
    "14:30",
    "16:30",
    "18:00"
];//用于校车发车的时间
list_schoolbus = [
    "10:00",
    "12:00",
    "13:00",
    "15:00",
    "17:00"
];//用于校车发车的时间
list_bus = [
    "5:30",
    "6:30",
    "7:00",
    "7:30",
    "8:00",
    "8:30",
    "9:00",
    "9:30",
    "10:00",
    "11:00",
    "12:00",
    "13:00",
    "14:00",
    "15:00",
    "16:00",
    "17:00",
    "17:30",
    "18:00",
    "18:30",
    "19:00",
    "19:30",
    "20:00",
    "20:30",
    "21:30",
    "22:30"
];//用于标志公交车的发车时间
//下面编写算法解决判断问题
var confirmbtn = document.getElementById("confirm");//得到了确定按钮
var cityform = document.getElementById("location");
console.log(cityform.value)
confirmbtn.onclick = route_organization;

function route_organization() {
    var nowtime = H + ":" + min;//当前的时间
    var nowlist = nowtime.split(":");//当前时间的分割
    if (cityform.value == 0)//如果在沙河
    {
        var sbindex = 0;
        var sblist = null;//对第一个时间的分割
        var sub1 = parseInt(nowlist[0]), sub2 = parseInt(nowlist[1]), sub3 = 0, sub4 = 0;
        var sbwt = 800;
        for (var i = 0; i < list_schoolbus.length; i++) {
            sblist = list_schoolbus[i].split(":");
            sub3 = parseInt(sblist[0]);
            sub4 = parseInt(sblist[1]);
            var temp = (sub3 * 60 + sub4) - (sub1 * 60 + sub2);//求出新的结果
            if (temp > 0 && temp < sbwt) {
                sbindex = i;
                sbwt = temp;
            }
        }
        //同理检索普通公交
        var blist = null;//用于存储公交的变量
        var bindex = 0
        var sub5 = 0, sub6 = 0;
        var bwt = 800;//最小的变量
        for (var i = 0; i < list_bus.length; i++) {
            blist = list_bus[i].split(":");//得到变量
            sub5 = parseInt(blist[0]);
            sub6 = parseInt(blist[1])
            var temp1 = (sub5 * 60 + sub6) - (sub1 * 60 + sub2);
            if (temp1 < bwt && temp1 > 0) {
                bindex = i;
                bwt = temp1;
            }
        }
        var bus_need = document.getElementById("bus_need");
        var bus_needtime = document.getElementById("bus_needtime");
        bus_need.innerHTML = list_bus[bindex];//这里让其中为最近的车的时间
        var rndom2=Math.random();//生成一个随机数
        bus_needtime.innerHTML = parseInt(bwt + 40*(1+rndom2) + walk_time)+"分钟，拥挤度为："+(1+rndom2).toFixed(2);//走路时间+等待时间+车辆行驶时间
        var schoolbus_need = document.getElementById("schoolbus_need");
        var schoolbustime = document.getElementById("schoolbus_needtime");
        schoolbus_need.innerHTML = list_schoolbus[sbindex];
        var rndom=Math.random();//生成一个随机数
        schoolbustime.innerHTML = parseInt(sbwt + 40*(1+rndom))+"分钟，拥挤度为："+(1+rndom).toFixed(2);//等待时间+车辆行驶时间
    } else {//如果在本部或者不进行选择
        var sbindex = 0;
        var sblist = null;//对第一个时间的分割
        var sub1 = parseInt(nowlist[0]), sub2 = parseInt(nowlist[1]), sub3 = 0, sub4 = 0;
        var sbwt = 800;
        for (var i = 0; i < list_schoolbus1.length; i++) {
            sblist = list_schoolbus1[i].split(":");
            sub3 = parseInt(sblist[0]);
            sub4 = parseInt(sblist[1]);
            var temp = (sub3 * 60 + sub4) - (sub1 * 60 + sub2);//求出新的结果
            if (temp > 0 && temp < sbwt) {
                sbindex = i;
                sbwt = temp;
            }
        }
        //同理检索普通公交
        var blist = null;//用于存储公交的变量
        var bindex = 0
        var sub5 = 0, sub6 = 0;
        var bwt = 800;//最小的变量
        for (var i = 0; i < list_bus.length; i++) {
            blist = list_bus[i].split(":");//得到变量
            sub5 = parseInt(blist[0]);
            sub6 = parseInt(blist[1])
            var temp1 = (sub5 * 60 + sub6) - (sub1 * 60 + sub2);
            if (temp1 < bwt && temp1 > 0) {
                bindex = i;
                bwt = temp1;
            }
        }
        var bus_need = document.getElementById("bus_need");
        var bus_needtime = document.getElementById("bus_needtime");
        var rndom1=Math.random();//随机拥挤度
        bus_need.innerHTML = list_bus[bindex];//这里让其中为最近的车的时间
        bus_needtime.innerHTML = parseInt(bwt + 40*(1+rndom1) + walk_time)+"分钟，拥挤度为："+(1+rndom1).toFixed(2);//走路时间+等待时间+车辆行驶时间
        var schoolbus_need = document.getElementById("schoolbus_need");
        var schoolbustime = document.getElementById("schoolbus_needtime");
        schoolbus_need.innerHTML = list_schoolbus1[sbindex];
        var rndom=Math.random();//生成一个随机数
        schoolbustime.innerHTML = parseInt(sbwt + 40*(1+rndom))+"分钟，拥挤度为："+(1+rndom).toFixed(2);//等待时间+车辆行驶时间*拥挤度
    }
}
```

#### （3）特点

①时间的模拟，日期更新

利用了定时器的思想，让时间实现了自动更新，同时利用了二维数组作为日期的存储，完整的实现了时间和日期的更新。

②上课提醒、下课提醒、考试开始提醒、考试结束提醒、课外开始提醒、课外结束提醒

巧妙利用了更新的同时进行判断的思路，可以实现到达时间进行弹窗。

③随机播放音乐

利用生成的随机数，播放随机的音乐，提升用户的体验

④跨校区方式导航

判断了最近的时间，方便用户进行选择。

#### （4）与其他模块的关系

![图片](https://github.com/yexuanyang/CoursesManagementWebsite/blob/933ce7e889e7d7ae32de038f4818d51563518cbc/Images/%E5%9B%BE%E7%89%87.png)

### 	7.文件管理模块

#### （1）算法思想

①资料、作业的上传

这里的主要思想是将作业和资料上传到后端对应的文件夹当中，然而当后端不存在该课程的文件夹时，会生成一个文件夹，然后更新存储资料与课程名称对应关系的json文件，同时作业上传的流程是将此时的作业与上传的作业内容，上传到的课程两者都进行对应，如果不存在课程的作用文件夹则创建作业文件夹，如果不存在当前作业文件夹（例如，第1次作业文件夹不存在），则会创建新的文件夹

②资料的下载

资料下载与文件的解压缩进行了绑定，由于我们后台的文件压缩之后格式为.ys，没有软件可以进行解析的格式，此时我们呢下载时，会先在后端解压缩然后传递回原本文件下载；解压缩使用的是逆哈夫曼编码，也就将其解码。当然如果开始用户存储时，没有进行压缩存储到后台，那么返回时也没有必要进行解压缩

③提交资料、作业时文件重复检测

重复检测思想，是遍历当前作业或者当前课程资料的列表（列表中采用json格式存储，在python中体现为字典），然后查找，如果此时的名称和列表中的名称有冲突，则会在前端有冲突提示。

④实现文件的压缩上传

文件的压缩上传利用的是哈夫曼编码，我们先统计了所有字符出现的个数作为字符的权值，再利用哈夫曼树的思想，进行文件中二进制数的重新排序，从而在使文件大小压缩的同时，也没有损失文件的质量。

#### （2）算法

①资料、作业的上传

主要展示后端的路由：

作业的上传：

```Python
@app.route('/direct_course/homework/', methods=['POST'])
def homework_submit():  # 前端表单中多添加了一个元素，用于标志第几次作业
    g.uname = session.get('now_user')
    data.initconflict()  # 初始化
    if request.method == "POST":
        UPLOAD_PATH = os.path.join(os.path.dirname(__file__), data.coursename + "_homework")  # 当前的文件路径
        if not os.path.exists(UPLOAD_PATH):  # 如果文件夹不存在则创建文件夹
            os.mkdir(UPLOAD_PATH)  # 创建文件夹
        # 得到文件名
        homework_file = request.files.get("course-homework")
        # 保存文件
        filename = homework_file.filename
        file_name = secure_filename(filename)  # 文件名的安全转换
        index = int(request.form.get("homeworkoption"))  # 传递过来的提交第几次作业
        Directory_path = os.path.join(UPLOAD_PATH, f"第{index + 1}次作业")
        if not os.path.exists(Directory_path):
            os.mkdir(Directory_path)  # 如果不存在第i次作业这个文件夹则创建
        # 得到新的文件位置
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
                data.material_conflict = 2  # 发生了冲突结果是这样的
                return redirect("/direct_course/" + data.coursename + "/")
            else:  # 如果当前不存在
                data.material_conflict = 0  # 没有发生冲突
                homework_file.save(file_path)
                homework[flag]["homework"][index]["filename"] = file_name  # 如果当前没有发生冲突则增加
        if request.form.get('compress') == "yes":
            file_encode(file_path)
        upload_homework_signal.send()  # 上传成功作业
        with open('./static/data/homework.json', "w", encoding="utf-8") as fp:  # 最后重新写入
            json.dump(homework, fp, ensure_ascii=False, separators=('\n,', ':'))
        return redirect("/direct_course/" + data.coursename + "/")
```

资料的上传：

```Python
@app.route('/direct_course/materials/<coursename_temp>', methods=['POST'])
def materials_submit(coursename_temp):
    g.uname = session.get('now_user')
    data.initconflict()  # 初始化
    if request.method == "POST":
        UPLOAD_PATH = os.path.join(os.path.dirname(__file__), data.coursename)  # 当前的文件路径
        if not os.path.exists(UPLOAD_PATH):  # 如果文件夹不存在则创建文件夹
            os.mkdir(UPLOAD_PATH)  # 创建文件夹
        material_file = request.files.get("course-file")
        # 保存文件
        filename = material_file.filename
        file_name = secure_filename(filename)  # 文件名的安全转换
        file_path = os.path.join(UPLOAD_PATH, file_name)
        material_file.save(file_path)  # 保存文件
        flag = -1  # 还是标志是否存在这个课程的名称 如果不存在则增加
        for i in range(0, len(courses_material)):
            if courses_material[i]["coursename"] == data.coursename:
                flag = i
                break
        if request.form.get('compress') == "yes":
            file_encode(file_path)
            os.remove(file_path)  # 删除源文件 然后生成一个新的名字
            file_name = file_name.split(".")[0] + ".ys"  # 生成一个新的名字
        for i in range(0, len(courses_material[flag]["material_name"])):
            if courses_material[flag]["material_name"][i].split(".")[0] == file_name.split(".")[0]:
                data.material_conflict = 1  # 发生了冲突
                return redirect("/direct_course/" + coursename_temp)  # 如果发生了冲突则直接返回
            else:
                data.material_conflict = 0
        if flag == -1:  # 如果不存在
            length = len(courses_material)
            temp = {"coursename": data.coursename, "material_name": [file_name]}
            courses_material.append(temp)
            with open('./static/data/courses_material.json', "w", encoding="utf-8") as fp:
                json.dump(courses_material, fp, ensure_ascii=False, separators=('\n,', ':'))
        else:
            courses_material[flag]["material_name"].append(file_name)  # 如果存在则增加名字
        data.upload_material_name = file_name
        upload_material_signal.send()  # 发送信号
        with open('./static/data/courses_material.json', "w", encoding="utf-8") as fp:  # 最后重新写入
            json.dump(courses_material, fp, ensure_ascii=False, separators=('\n,', ':'))
        return redirect("/direct_course/" + coursename_temp)
```

②资料的下载

资料下载的路由：

```Python
@app.route('/course/download/', methods=['POST'])  # 实现下载的路由
def download_material():
    data.initconflict()  # 初始化
    g.uname = session.get('now_user')
    DOWNLOAD_PATH = os.path.join(os.path.dirname(__file__), data.coursename)  # 当前的文件路径
    # 得到文件名
    download_name = request.form.get("downloadmaterial")
    # 将文件名拆分

    if download_name.split(".")[1] == "ys":  # 如果是一个压缩文件
        DOWNLOAD_PATH_YS = os.path.join(DOWNLOAD_PATH, download_name)  # 将字符串进行连接
        file_decode(DOWNLOAD_PATH_YS)  # 解压当前文件
        resource = download_name.split(".")[0] + "." + datatemp.decodeFile
        DOWNLOAD_PATH_RESULT = os.path.join(DOWNLOAD_PATH, resource)  # 将路径进行拼接
        data.download_material_name = resource
        download_material_signal.send()  # 下载成功信号
        return send_from_directory(path=DOWNLOAD_PATH_RESULT, directory=DOWNLOAD_PATH, filename=resource,
                                   as_attachment=True)
    else:
        DOWNLOAD_PATH_RESULT = os.path.join(DOWNLOAD_PATH, download_name)
        print(DOWNLOAD_PATH_RESULT)
        data.download_material_name = download_name
        download_material_signal.send()  # 下载成功发送信号
        return send_from_directory(path=DOWNLOAD_PATH_RESULT, directory=DOWNLOAD_PATH, filename=download_name,
                                   as_attachment=True)
```

解压缩算法

```Python
#文件的解压缩
#解压缩前，重温下压缩文件.cc的内容：第一行为原文件名
#第二行的开始两个字节纪录结点数量n，然后一个字节纪录频率的位宽width，后面纪录每个字节与其频率
#之后全部是数据内容
def file_decode(input_file):
    print('开始解压缩文件')
    with open(input_file,'rb') as f_in:

        f_in.seek(0,2)
        length=f_in.tell() #读出文件的总长度
        f_in.seek(0)

        path_list = input_file.split('.')
        name = f_in.readline().decode(encoding="UTF-8").split('/')[-1].replace('\n','')
        name = name.split('.')[-1]                   #读出文件名
        datatemp.decodeFile=name #得到文件名
        with open(path_list[0]+'.'+name,'wb') as f_out:
            n=int.from_bytes(f_in.read(2), byteorder = 'big')     #读出结点数量
            width=int.from_bytes(f_in.read(1), byteorder = 'big') #读出位宽
            count_dict={}
            i=0
            while i<n:
                dict_key=f_in.read(1)
                dict_value=int.from_bytes(f_in.read(width),byteorder='big')
                count_dict[dict_key]=dict_value
                i+=1


            print('生成反向字典中...')
            #以下过程与编码时的构建过程相同
            node_dict = {}  # 使用一个字典将count_list中的值node化,其中key为对应的字符，值为字符对应的结点
            for x in count_dict.keys():
                node_dict[x] = node(count_dict[x])  # 结点的权重即count_dict[x]


            nodes = []  # 使用一个列表来保存结点并由此构建哈夫曼树
            for x in node_dict.keys():
                nodes.append(node_dict[x])

            root = creat_tree(nodes)  # 构建哈夫曼树

            # 对叶子结点编码，输出字节与哈夫曼码的字典
            bytes_dict = {}
            for x in node_dict.keys():
                bytes_dict[x] = node_encode(node_dict[x])

            # print(bytes_dict)
            # 生成反向字典,key为编码，value为对应的字节
            diff_dict={}
            for x in bytes_dict.keys():
                diff_dict[bytes_dict[x]]=x


            print('解码中...')
            # 解码时不停读取单个数字，遍历二叉树，直到找到叶子结点
            out=b''
            i=f_in.tell()
            node_now = root
            result = b''
            while i < length-2:
                i+=1
                temp=int.from_bytes(f_in.read(1),byteorder='big')
                for mm in range(8):        #将数据转换成b'01'形式
                    if temp&1 == 1:
                        out=b'1'+out
                    else:
                        out=b'0'+out
                    temp=temp>>1

                while out:       #遍历哈夫曼树
                    if out[0]==49:
                        node_now=node_now.right
                        result = result+b'1'
                    if out[0]==48:
                        node_now=node_now.left
                        result = result+b'0'
                    out=out[1:]
                    if node_now.left==None and node_now.right==None:
                        f_out.write(diff_dict[result])
                        result=b''
                        node_now=root

            # 处理最后可能不满8位的数据
            last_length = int.from_bytes(f_in.read(1), byteorder='big')
            print(last_length)
            temp= int.from_bytes(f_in.read(1), byteorder='big')
            print(temp)
            for mm in range(last_length):  # 将数据转换成b'01'形式
                if temp & 1 == 1:
                    out = b'1' + out
                else:
                    out = b'0' + out
                temp = temp >> 1
            print(out)
            while out:  # 遍历哈夫曼树
                if out[0] == 49:
                    node_now = node_now.right
                    result = result + b'1'
                if out[0] == 48:
                    node_now = node_now.left
                    result = result + b'0'
                out = out[1:]
                if node_now.left == None and node_now.right == None:
                    f_out.write(diff_dict[result])
                    print(result)
                    result = b''
                    node_now = root
    print('解压成功！')
```

③提交资料、作业时文件重复检测

资料：

```Python
for i in range(0, len(courses_material[flag]["material_name"])):
    if courses_material[flag]["material_name"][i].split(".")[0] == file_name.split(".")[0]:
        data.material_conflict = 1  # 发生了冲突
        return redirect("/direct_course/" + coursename_temp)  # 如果发生了冲突则直接返回
    else:
        data.material_conflict = 0
```

作业：

```Python
if file_name == homework[flag]["homework"][index]["filename"]:
    data.material_conflict = 2  # 发生了冲突结果是这样的
    return redirect("/direct_course/" + data.coursename + "/")
else:  # 如果当前不存在
    data.material_conflict = 0  # 没有发生冲突
    homework_file.save(file_path)
    homework[flag]["homework"][index]["filename"] = file_name  # 如果当前没有发生冲突则增加
```

④实现文件的压缩上传

压缩算法：

```Python
def creat_tree(nodes_list):
    nodes_list.sort(key=lambda x: x.value)      #将结点列表进行升序排序
    if len(nodes_list)==1:
        return nodes_list[0]        #只有一个结点时，返回根结点
    father_node=node(nodes_list[0].value+nodes_list[1].value,nodes_list[0],nodes_list[1]) #创建最小的两个权重结点的父节点
    nodes_list[0].father=nodes_list[1].father=father_node
    nodes_list.pop(0)
    nodes_list.pop(0)
    nodes_list.insert(0,father_node)   #删除最小的两个结点并加入父结点
    return creat_tree(nodes_list)

def node_encode(node1):            #对叶子结点进行编码
    if node1.father==None:
        return b''
    if node1.father.left==node1:
        return node_encode(node1.father)+b'0'
    else:
        return node_encode(node1.father)+b'1'

def file_encode(input_file):
    print('打开文件并读取中...\n')
    with open(input_file,'rb') as f:
        f.seek(0, 2)        #读取文件的总长度，seek(0,2)移到文件末尾，tell()指出当前位置，并且用seek(0)重新回到起点
        size=f.tell()
        f.seek(0)
        bytes_list=[0]*size  #创建一个长度为size的列表，存放读入的字节

        i=0
        while i<size:
            bytes_list[i]=f.read(1)  #每次读取一个符号
            i+=1

    print('统计各字节出现频率中...\n')
    count_dict = {}  # 使用一个字典统计一下出现次数
    for x in bytes_list:
        if x not in count_dict.keys():
            count_dict[x] = 0
        count_dict[x] += 1

    node_dict={}   #使用一个字典将count_list中的值node化,其中key为对应的字符，值为字符对应的结点
    for x in count_dict.keys():
        node_dict[x]=node(count_dict[x])  #结点的权重即count_dict[x]

    print('生成哈夫曼编码中...\n')
    nodes=[]      #使用一个列表来保存结点并由此构建哈夫曼树
    for x in node_dict.keys():
        nodes.append(node_dict[x])

    root=creat_tree(nodes)   #构建哈夫曼树

    #对叶子结点编码，输出字节与哈夫曼码的字典
    bytes_dict={}
    for x in node_dict.keys():
        bytes_dict[x]=node_encode(node_dict[x])

    # print(bytes_dict)
    #开始压缩文件
    print('开始压缩文件...\n')
    path_list=input_file.split('.')
    name=input_file.split('/')[-1]
    print (path_list)
    with open(path_list[0]+'.ys','wb') as object:
        #首先将文件的原名写入
        object.write((name+'\n').encode(encoding='UTF-8'))
        #写入结点数量，占位2个字节
        n=len(count_dict.keys())
        object.write(int.to_bytes(n ,2 ,byteorder = 'big'))

        #先计算最大频率所占的字节数
        times=0
        for x in count_dict.keys():
            if times<count_dict[x]:
                times=count_dict[x]
        width=1
        if times>255:
            width=2
            if times>65535:
                width=3
                if times>16777215:
                    width=4
        # 写入width
        object.write(int.to_bytes(width,1,byteorder='big'))
```

#### （3）特点

①资料、作业的上传

上传时，以名字作为字典中存储的元素，而不是以文件，节约了空间，同时对文件夹进行整理和判断，让文件也十分的整齐，同时在后端返回到前端展示作业内容时，将作业标序号为“第1次作业”、“第2次作业”等，也提高了用户的体验感。

②资料的下载

资料的压缩功能为了让空间变小，便于用户下载，而我们下载时解压缩也提高了用户的体验，不需要在本地再利用一些软件进行解压，降低了空间消耗的同时也提高了用户的体验

③提交资料、作业时文件重复检测

重复检测，会有上方弹窗，友好提示，防止用户提交时出现错误。

④实现文件的压缩上传

文件压缩采用哈夫曼编码，可以极大的减少bmp、docx等文件的大小，方便存储和管理。

#### （4）与其他模块的关系

![图片4](https://github.com/yexuanyang/CoursesManagementWebsite/blob/933ce7e889e7d7ae32de038f4818d51563518cbc/Images/%E5%9B%BE%E7%89%874.png)

### 	8.总体各个模块的相互调用关系

![未命名文件5](https://github.com/yexuanyang/CoursesManagementWebsite/blob/933ce7e889e7d7ae32de038f4818d51563518cbc/Images/%E6%9C%AA%E5%91%BD%E5%90%8D%E6%96%87%E4%BB%B65.png)
