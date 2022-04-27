// 用于模拟系统时间
var t = null; //这里是执行时间的函数
var multiple = 3; //这里是加速的倍数
var timeset = 10 / multiple; //开始为每10毫秒运行一次  这里除以倍数
console.log(timeset);
var accelerator = document.getElementById('quicker');
accelerator.onclick = bequicker;
t = setInterval(faketime, timeset);
var hour = document.getElementById('hour');
var minute = document.getElementById('min');
var second1 = document.getElementById('second');
var H = hour.innerHTML;
var min = minute.innerHTML;
var second = second1.innerHTML;
var btn2 = document.getElementById('act');
btn2.onclick = act;
var pause = document.getElementById('pause');
pause.onclick = pause_fun;
var data_list=[H,min,second];//用于记录数组的格式
console.log(data_list);
function faketime() {
    if (H >= 24) {
        H %= 24;
    }
    if (min >= 60) {
        min %= 60;
    }
    if (second >= 60) {
        second %= 60;
    }
    if (second == 59) {
        second = 0;
        if (min == 59) {
            if (H == 23) {
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
    data_list=[H,min,second];
    var time_json={
        time:JSON.stringify(data_list)
    };
    $.ajax({
        type:'post',
        async:false,
        url:"/time_control",
        data:time_json,
        success:function (result){
            console.log("好耶")
        }
    });
    draw();
}

function draw() {

    hour.innerHTML = H;
    minute.innerHTML = min;
    second1.innerHTML = second;
}

function pause_fun() { //用于停止时间
    console.log(t);
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
    console.log(t);
    t = setInterval(faketime, timeset);
}

var walk_time=40;//步行时间
var wait_time=0;//等车时间
var timetable_bus=document.getElementById("timetable_bus");
var timetable_schoolbus=document.getElementById("timetable_schoolbus");
var btn_schoolbus=document.getElementById("show_schoolbus");
var btn_bus=document.getElementById("show_bus");
var show_btn_bus=document.getElementById("show_busroute");
btn_schoolbus.onclick=function (){
    timetable_bus.style.display="none";
    timetable_schoolbus.style.display="none";
    timetable_schoolbus.style.display="block";
}
btn_bus.onclick=function (){
    timetable_bus.style.display="none";
    timetable_schoolbus.style.display="none";
    timetable_bus.style.display="block";
}
list_schoolbus=[]//用于校车发车的时间
