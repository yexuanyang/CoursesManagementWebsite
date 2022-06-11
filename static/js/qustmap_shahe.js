//Dijkstra单源最短路径
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
function dijkstraLeastlucheng(path, index) {
    var m = path && path.length;
    var n = m && path[0].length;
    if (m && n && m === n && index < n) {
        //初始化distance
        var dis = [];
        var randomNumber=Math.random();
        var visited = []; //用于标识index号至其他顶点的距离是否确定
        for (var i = 0; i < n; ++i) {
            dis.push(path[index][i]);
            visited.push(false)
            PathToEnd[i] = -1;
        }
        visited[index] = true;


        for (i = 0; i < n; i++) {
            var minIndex, min = Infinity;
            //找出剩余的不确定的点到index最短的距离对应的索引
            for (var j = 0; j < n; ++j) {
                if (!visited[j] && dis[j] < min) {
                    minIndex = j;
                    min = dis[j];
                }
            }
            visited[minIndex] = true; //标识index到此顶点的距离已经确认
            for (var k = 0; k < n; ++k) {
                //判断minIndex到k之间有无道路
                if (!visited[k] && path[minIndex][k] < Infinity) {
                    //更新distance
                    if (dis[k] > dis[minIndex] + path[minIndex][k]) {
                        dis[k] = dis[minIndex] + path[minIndex][k];
                        PathToEnd[k] = minIndex;
                    }
                }
            }
        }
        return dis;
    }
}

//结点信息
var pointName = [
    "商店1",
    "西门",
    "停车场",
    "运动场",
    "办公楼1",
    "办公楼2",
    "办公楼3",
    "学生公寓D",
    "学生公寓E",
    "学生公寓S3",
    "学生公寓S4",
    "学生公寓S5",
    "学生公寓S6",
    "教工食堂",
    "学生食堂",
    "商店2",
    "学生活动中心",
    "教学楼1",
    "南门",
    "图书馆",
    "教学楼2",
    "人工湖",
    "学院楼",
    "实验楼S1",
    "实验楼S2",
    "实验楼S3",
    "体育馆1",
    "体育馆2",
    "体育馆3"
];
//结点经纬度
var pointCord = [
        [116.289484, 40.165067],
        [116.290544, 40.162572],
        [116.292161, 40.159787],
        [116.291208, 40.165397],
        [116.291963, 40.164267],
        [116.29243, 40.163137],
        [116.292969, 40.162089],
        [116.293077, 40.166059],
        [116.293652, 40.165067],
        [116.294298, 40.163798],
        [116.294837, 40.162778],
        [116.295233, 40.161841],
        [116.295628, 40.160793],
        [116.295017, 40.166114],
        [116.295305, 40.16537],
        [116.296706, 40.1665],
        [116.297101, 40.165783],
        [116.296167, 40.163412],
        [116.297209, 40.161179],
        [116.298646, 40.166059],
        [116.299545, 40.16424],
        [116.29976, 40.163164],
        [116.300623, 40.1673],
        [116.301162, 40.166417],
        [116.301736, 40.165425],
        [116.302096, 40.164736],
        [116.302743, 40.163854],
        [116.303246, 40.162999],
        [116.300443, 40.162144]
    ]
    //邻接矩阵
var INF = 99999;
var path = [
    [0, 300, INF, 200, INF, INF, INF, 400, 400, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [300, 0, 400, 450, 250, 200, 250, INF, INF, INF, INF, INF, 600, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, 400, 0, INF, INF, 450, 350, INF, INF, INF, INF, 450, 400, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [200, 450, INF, 0, 200, INF, INF, 250, 250, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, 250, INF, 200, 0, 100, INF, INF, 250, 250, INF, 400, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, 200, 450, INF, 100, 0, 100, INF, INF, 250, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, 250, 350, INF, INF, 100, 0, INF, INF, INF, 250, 250, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [400, INF, INF, 250, INF, INF, INF, 0, 250, INF, INF, INF, INF, 250, INF, INF, INF, 500, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [400, INF, INF, 250, 250, INF, INF, 250, 0, 200, INF, INF, INF, 300, 250, INF, INF, 400, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, 250, 250, INF, INF, 200, 0, 100, INF, INF, INF, INF, INF, INF, 300, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, 250, INF, INF, 100, 0, 200, INF, INF, INF, INF, INF, 300, 400, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, 450, INF, 400, INF, 250, INF, INF, INF, 200, 0, 100, INF, INF, INF, INF, 400, 350, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, 600, 400, INF, INF, INF, INF, INF, INF, INF, INF, 100, 0, INF, INF, INF, INF, 500, 300, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, 250, 300, INF, INF, INF, INF, 0, 250, 250, 300, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, 250, INF, INF, INF, INF, 250, 0, 300, 250, 200, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 250, 300, 0, 250, INF, INF, 200, INF, INF, 450, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 300, 250, 250, 0, 200, INF, 200, 300, 500, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, 500, 400, 300, 300, 400, 500, INF, 200, INF, 200, 0, 400, INF, 400, 300, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 400, 350, 300, INF, INF, INF, INF, 400, 0, INF, INF, 300, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 200, 200, INF, INF, 0, 300, 500, 300, 350, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 300, 400, INF, 300, 0, 100, 400, 300, 250, INF, 300, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 650, INF, INF, INF, INF, 500, 300, 300, 500, 100, 0, INF, INF, INF, 400, 400, 450, 200],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 450, INF, INF, INF, 300, 400, INF, 0, 200, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 350, 300, INF, 200, 0, 100, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 250, INF, INF, 100, 0, 50, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 400, INF, INF, 50, 0, 50, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 300, 400, INF, INF, INF, 50, 0, 200, 450],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 450, INF, INF, INF, INF, 200, 0, 450],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 250, INF, INF, 200, INF, INF, INF, INF, 450, 450, 0],
];

//给select添加选项text
function addSelect(id, text) {
    var select_node = document.getElementById(id);
    var option = document.createElement("option");
    option.text = text;
    try {
        select_node.add(option, select_node.options[null]);
    } catch (e) {
        select_node.add(option, null);
    }
}

for (var i = 0; i < pointName.length; ++i) {
    addSelect("startnode", pointName[i]);
    addSelect("endnode", pointName[i]);
}

//百度地图-MapV-API
var map = new BMapGL.Map("container", {
    enableMapClick: false
});
var point = new BMapGL.Point(116.296167, 40.163412);
map.centerAndZoom(point, 17);
map.enableScrollWheelZoom(true); // 开启鼠标滚轮缩放

//Marker标记
var marker = new Array();
for (var i = 0; i < pointName.length; ++i) {
    var point = new BMapGL.Point(pointCord[i][0], pointCord[i][1]); //默认  可以通过Icon类来指定自定义图标
    marker[i] = new BMapGL.Marker(point);
    var label = new BMapGL.Label(pointName[i], { offset: new BMapGL.Size(20, -10) }); //标注标签
    marker[i].setLabel(label) //设置标注说明
    map.addOverlay(marker[i]);
}
var mapvLayer;

function DisplayPath(StartIndex, EndIndex) {
    var data = [];
    var animationtmp=[];
    var animation=[]; //这是真是的animation 上面那个是倒着进行的操作
    var StartPoint = pointCord[StartIndex];
    var EndPoint = pointCord[EndIndex];
    console.log("StartPoint: " + StartPoint);
    console.log("EndPoint: " + EndPoint);
    //获取最短路径
    var p = EndIndex;
    EndPoint = pointCord[p];
    animationtmp.push(
        {
            'lng':EndPoint[0],
            'lat':EndPoint[1]
        }
        )
    while (PathToEnd[p] != -1) {
        StartPoint = pointCord[PathToEnd[p]];
        animationtmp.push(
            {
                'lng':StartPoint[0],
                'lat':StartPoint[1]
            }
        );
        p = PathToEnd[p];
    }
    console.log(StartIndex);
    StartPoint = pointCord[StartIndex];
    animation.push(
            {
                'lng':StartPoint[0],
                'lat':StartPoint[1]
            }
        );
    for(var i=animationtmp.length-1;i>=0;i--){
        animation.push(animationtmp[i]);
    }
    var animationpoint=[];
    for(var i=0;i<animation.length;i++){
        animationpoint.push(new BMapGL.Point(animation[i].lng,animation[i].lat));
    }
    console.log(animationpoint);
    var pl=new BMapGL.Polyline(animationpoint);
    var trackAni=null;
    if(trackAni==null){ //如果不存在则创建新的
        trackAni=new BMapGLLib.TrackAnimation(map, pl, {
        overallView: true, // 动画完成后自动调整视野到总览
        tilt: 30,          // 轨迹播放的角度，默认为55
        duration: 4000,   // 动画持续时长，默认为10000，单位ms
        delay: 0        // 动画开始的延迟，默认0，单位ms
    });
    }else{
        trackAni=null;//如果存在则隐藏 然后创建新的
        trackAni=new BMapGLLib.TrackAnimation(map, pl, {
        overallView: true, // 动画完成后自动调整视野到总览
        tilt: 30,          // 轨迹播放的角度，默认为55
        duration: 4000,   // 动画持续时长，默认为10000，单位ms
        delay: 0        // 动画开始的延迟，默认0，单位ms
    });
    }
    trackAni.start();
}

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
    document.getElementById("showdis").innerHTML = "当前路径的距离为：" + pathLength[EndIndex].toString() + "米"+"<br>"+"步行所用的时间为："+parseInt(PathArray[EndIndex]/60)+"分钟"+"<br>"+"自行车所用的时间为："+timebybike+"分钟";
});

var button2 = document.getElementById("warninginfo");
button2.addEventListener("click", function() {
    if (button2.click == false) {
        return;
    }
    document.getElementById("showdis").style.bottom = "1%";
    document.getElementById("showdis").innerHTML = "👿如不能正常使用：<br/>🕸检查网络<br/>💻更换浏览器";

});
var btn=document.getElementById("button1");
btn.addEventListener("click", function() {
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

    PathArray = dijkstraLeastlucheng(path, StartIndex);
    DisplayPath(StartIndex, EndIndex);
    var timebybike=parseInt((PathArray[EndIndex]/ByBike)/60);//得到的结果是骑自行车用时
    var timeonfoot=parseInt((PathArray[EndIndex]/Onfootwalk)/60);//步行所用的时间
    document.getElementById("showdis").style.bottom = "5%";
    document.getElementById("showdis").innerHTML = "采用最短路径策略："+"<br>"+"当前路径的距离为：" + PathArray[EndIndex].toString() + "米"+"<br>"+"步行所用的时间为："+timeonfoot+"分钟"+"<br>"+"自行车所用的时间为："+timebybike+"分钟";
});
