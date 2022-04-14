// 用于模拟系统时间
var t = null; //这里是执行时间的函数
var H = 10;
var min = 0;
var second = 0;
var statue = 0; //0代表正常运行状态 1代表设置状态
t = setInterval(faketime, 2.78);
var statue1 = 0; //是否点击了按钮
var btn1 = document.getElementById('pause');
var btn2 = document.getElementById('act');
btn2.onclick = act;
var inputH = document.getElementById('setH');
var inputM = document.getElementById('setM');
var inputS = document.getElementById('setS');

function faketime() {
    if (inputH.value != '' || inputM.value != '' || inputS.value != '') {
        statue = 1;
        H = inputH.value;
        min = inputM.value;
        second = inputS.value;
        if (H >= 24) {
            H %= 24;
        }
        if (min >= 60) {
            min %= 60;
        }
        if (second >= 60) {
            second %= 60;
        }
    } else {
        statue = 0;
    }
    if (statue == 1) {

    } else {
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
    }
    draw();
    if (statue1 == 1) {
        statue = 0;
        statue1 = 0;
    }
}

function draw() {
    var hour = document.getElementById('hour');
    var minute = document.getElementById('min');
    var second1 = document.getElementById('second');
    hour.innerHTML = H;
    minute.innerHTML = min;
    second1.innerHTML = second;
}

function pause() { //用于停止时间
    statue = 1; //此时为暂停的状态
}

function act() {
    statue = 0;
    statue1 = 1;
    inputH.value = '';
    inputM.value = '';
    inputS.value = '';
}