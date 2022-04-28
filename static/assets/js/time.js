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
            console.log("")
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
    clearInterval(t);//先清除掉定时器
    t = setInterval(faketime, timeset);
}

var walk_time=40;//步行时间
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
//上面修复了时间加速的问题
list_schoolbus1=[
    "9:30",
    "11:30",
    "12:30",
    "14:30",
    "16:30",
    "18:00"
];//用于校车发车的时间
list_schoolbus=[
    "10:00",
    "12:00",
    "13:00",
    "15:00",
    "17:00"
];//用于校车发车的时间
list_bus=[
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
var confirmbtn=document.getElementById("confirm");//得到了确定按钮
var cityform=document.getElementById("location");
console.log(cityform.value)
confirmbtn.onclick=route_organization;
function route_organization(){
    var nowtime=H+":"+min;//当前的时间
    var nowlist=nowtime.split(":");//当前时间的分割
    if (cityform.value==0)//如果在沙河
    {
        var sbindex=0;
        var sblist=null;//对第一个时间的分割
        var sub1=parseInt(nowlist[0]),sub2=parseInt(nowlist[1]),sub3=0,sub4=0;
        var sbwt=800;
        for(var i=0;i<list_schoolbus.length;i++){
            sblist=list_schoolbus[i].split(":");
            sub3=parseInt(sblist[0]);
            sub4=parseInt(sblist[1]);
            var temp=(sub3*60+sub4)-(sub1*60+sub2);//求出新的结果
            if(temp>0 && temp<sbwt){
                sbindex=i;
                sbwt=temp;
            }
        }
        //同理检索普通公交
        var blist=null;//用于存储公交的变量
        var bindex=0
        var sub5=0,sub6=0;
        var bwt=800;//最小的变量
        for(var i=0;i<list_bus.length;i++){
            blist=list_bus[i].split(":");//得到变量
            sub5=parseInt(blist[0]);
            sub6=parseInt(blist[1])
            var temp1=(sub5*60+sub6)-(sub1*60+sub2);
            if(temp1<bwt && temp1>0){
                bindex=i;
                bwt=temp1;
            }
        }
        var bus_need=document.getElementById("bus_need");
        var bus_needtime=document.getElementById("bus_needtime");
        bus_need.innerHTML=list_bus[bindex];//这里让其中为最近的车的时间
        bus_needtime.innerHTML=bwt+40+walk_time;//走路时间+等待时间+车辆行驶时间
        var schoolbus_need=document.getElementById("schoolbus_need");
        var schoolbustime=document.getElementById("schoolbus_needtime");
        schoolbus_need.innerHTML=list_schoolbus[sbindex];
        schoolbustime.innerHTML=sbwt+40;//等待时间+车辆行驶时间
    }else{//如果在本部或者不进行选择
        var sbindex=0;
        var sblist=null;//对第一个时间的分割
        var sub1=parseInt(nowlist[0]),sub2=parseInt(nowlist[1]),sub3=0,sub4=0;
        var sbwt=800;
        for(var i=0;i<list_schoolbus1.length;i++){
            sblist=list_schoolbus1[i].split(":");
            sub3=parseInt(sblist[0]);
            sub4=parseInt(sblist[1]);
            var temp=(sub3*60+sub4)-(sub1*60+sub2);//求出新的结果
            if(temp>0 && temp<sbwt){
                sbindex=i;
                sbwt=temp;
            }
        }
        //同理检索普通公交
        var blist=null;//用于存储公交的变量
        var bindex=0
        var sub5=0,sub6=0;
        var bwt=800;//最小的变量
        for(var i=0;i<list_bus.length;i++){
            blist=list_bus[i].split(":");//得到变量
            sub5=parseInt(blist[0]);
            sub6=parseInt(blist[1])
            var temp1=(sub5*60+sub6)-(sub1*60+sub2);
            if(temp1<bwt && temp1>0){
                bindex=i;
                bwt=temp1;
            }
        }
        var bus_need=document.getElementById("bus_need");
        var bus_needtime=document.getElementById("bus_needtime");
        bus_need.innerHTML=list_bus[bindex];//这里让其中为最近的车的时间
        bus_needtime.innerHTML=bwt+40+walk_time;//走路时间+等待时间+车辆行驶时间
        var schoolbus_need=document.getElementById("schoolbus_need");
        var schoolbustime=document.getElementById("schoolbus_needtime");
        schoolbus_need.innerHTML=list_schoolbus1[sbindex];
        schoolbustime.innerHTML=sbwt+40;//等待时间+车辆行驶时间
    }
}