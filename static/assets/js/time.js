// 用于模拟系统时间
var t = null; //这里是执行时间的函数
var multiple = 3; //这里是加速的倍数
var timeset = 10 / multiple; //开始为每10毫秒运行一次  这里除以倍数
// console.log(timeset);
var accelerator = document.getElementById('quicker');
accelerator.onclick = bequicker;
t = setInterval(faketime, timeset);
//获取日期
var year=document.getElementById('year');
var month=document.getElementById('month');
var day=document.getElementById('day');
var week = document.getElementById('week');
var hour = document.getElementById('hour');
var minute = document.getElementById('min');
var second1 = document.getElementById('second');
var Y=year.innerHTML;
var MONTH=month.innerHTML;
var DAY=day.innerHTML;
var W = week.innerHTML;
var H = hour.innerHTML;
var min = minute.innerHTML;
var second = second1.innerHTML;
var btn2 = document.getElementById('act');
btn2.onclick = act;
var pause = document.getElementById('pause');
pause.onclick = pause_fun;
//用于记录数组的格式
var data_list = [Y,MONTH,DAY,W,H, min, second];
var date=new Date(2022,5,19);

console.log("yes"+date);
var chtoInt = {
    "一": 1,
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7
};

var in_course_time = document.getElementsByClassName("courseTime");
// console.log(in_course_time);
console.log(parseInt(in_course_time[1].innerHTML.substring(3, 5)));
console.log(parseInt(in_course_time[1].innerHTML.substring(6, 8)));
console.log(parseInt(in_course_time[1].innerHTML.substring(9, 11)));
console.log(parseInt(in_course_time[1].innerHTML.substring(12)));

var course_name = document.getElementsByClassName("courseName");

var exam_time = document.getElementsByClassName("examTime");

var out_course_begin_time = document.getElementsByClassName("outCourseBeginTime");
var out_course_end_time = document.getElementsByClassName("outCourseEndTime");
var out_course_date = document.getElementsByClassName("outCourseDate");
var class_begin = false;
var class_end = false;

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
    data_list = [Y,MONTH,DAY,W, H, min, second];
    for (let i = 0; i < in_course_time.length; i++) {
        const inCourseTimeKey = in_course_time[i].innerHTML;
        const day = chtoInt[inCourseTimeKey[2]];
        if (day === parseInt(W)) {
            if (!class_begin && parseInt(H) === parseInt(inCourseTimeKey.substring(3, 5)) && parseInt(min) === parseInt(inCourseTimeKey.substring(6, 8))) {
                window.alert(course_name[i].innerHTML + "开始上课了");
                class_begin = true;
                class_end = false;
                break;
            }
            if (!class_end && parseInt(H) === parseInt(inCourseTimeKey.substring(9, 11) ) && parseInt(min) === parseInt(inCourseTimeKey.substring(12))) {
                window.alert(course_name[i].innerHTML + "下课了");
                class_end = true;
                class_begin = false;
                break;
            }
        }
    }
    var time_json = {
        time: JSON.stringify(data_list)
    };
    $.ajax({
        type: 'post',
        async: false,
        url: "/time_control",
        data: time_json,
        success: function (result) {
            console.log("")
        }
    });
    draw();
}
/*
绘制时间
*/
function draw() {
    year.innerHTML=Y;
    month.innerHTML=MONTH;
    day.innerHTML=DAY;
    week.innerHTML = W;
    hour.innerHTML = H;
    minute.innerHTML = min;
    second1.innerHTML = second;
}

function pause_fun() { //用于停止时间
    clearInterval(t);
}

function act() {
    if (t > 0) {
        t = setInterval(faketime, timeset)
    }
}

function bequicker() {
    if (multiple < 2) { //最高支持两倍速
        multiple++;
    } else {
        multiple = 1;
    }
    timeset = 100 / multiple
    clearInterval(t);//先清除掉定时器
    t = setInterval(faketime, timeset);
}

var walk_time = 40;//步行时间
var timetable_bus = document.getElementById("timetable_bus");
var timetable_schoolbus = document.getElementById("timetable_schoolbus");
var btn_schoolbus = document.getElementById("show_schoolbus");
var btn_bus = document.getElementById("show_bus");
var show_btn_bus = document.getElementById("show_busroute");
btn_schoolbus.onclick = function () {
    timetable_bus.style.display = "none";
    timetable_schoolbus.style.display = "none";
    timetable_schoolbus.style.display = "block";
}
btn_bus.onclick = function () {
    timetable_bus.style.display = "none";
    timetable_schoolbus.style.display = "none";
    timetable_bus.style.display = "block";
}
//上面修复了时间加速的问题
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
        bus_needtime.innerHTML = bwt + 40 + walk_time;//走路时间+等待时间+车辆行驶时间
        var schoolbus_need = document.getElementById("schoolbus_need");
        var schoolbustime = document.getElementById("schoolbus_needtime");
        schoolbus_need.innerHTML = list_schoolbus[sbindex];
        schoolbustime.innerHTML = sbwt + 40;//等待时间+车辆行驶时间
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
        bus_need.innerHTML = list_bus[bindex];//这里让其中为最近的车的时间
        bus_needtime.innerHTML = bwt + 40 + walk_time;//走路时间+等待时间+车辆行驶时间
        var schoolbus_need = document.getElementById("schoolbus_need");
        var schoolbustime = document.getElementById("schoolbus_needtime");
        schoolbus_need.innerHTML = list_schoolbus1[sbindex];
        schoolbustime.innerHTML = sbwt + 40;//等待时间+车辆行驶时间
    }
}
//记录平年和闰年每个月的日期
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
//var data_list = [Y,MONTH,DAY,W,H, min, second]; 定义
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
    if(parseInt(DAY)===MonthTable[MONTH][f]){ //如果达到当月的最后一天
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