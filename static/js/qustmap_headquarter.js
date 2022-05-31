//Dijkstra单源最短路径
var PathToEnd = new Array(13);
var ByBike=10; //通过自行车 10m/s
var Onfootwalk=2;//通过走路 2m/s
function dijkstra(path, index) {
    var m = path && path.length;
    var n = m && path[0].length;
    if (m && n && m === n && index < n) {
        //初始化distance
        var dis = [];
        var randomNumber=Math.random();
        console.log(randomNumber);
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
    "学生公寓1",
    "学生公寓2",
    "西门",
    "学生公寓3",
    "学生活动中心",
    "邮局",
    "北门",
    "教学楼3",
    "图书馆",
    "运动场",
    "办公楼",
    "教学楼4",
    "食堂",
    "南门",
    "医务室",
    "马克思主义楼",
    "东门",
    "体育馆"
];
//结点经纬度
var pointCord = [
        [116.361725, 39.970637],
        [116.361725, 39.969586],
        [116.361725, 39.968619],
        [116.361725, 39.967374],
        [116.361725, 39.965633],
        [116.361725, 39.963987],
        [116.363594, 39.970637],
        [116.363594, 39.968951],
        [116.363594, 39.967426],
        [116.363594, 39.965633],
        [116.36539, 39.970789],
        [116.366145, 39.968798],
        [116.365965, 39.96714],
        [116.365534, 39.963987],
        [116.367798, 39.964015],
        [116.367798, 39.968798],
        [116.367798, 39.965633],
        [116.367798, 39.964018]
    ]
    //邻接矩阵
var INF = 99999;
var path = [
    [0, 200, INF, INF, INF, INF, 250, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [200, 0, 200, INF, INF, INF, 300, 250, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, 200, 0, 200, INF, INF, 400, 200, 250, 450, INF, 600, INF, INF, INF, INF, INF, INF],
    [INF, INF, 200, 0, 250, INF, INF, INF, INF, 350, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, 250, 0, 300, INF, INF, 350, 200, INF, INF, 600, 600, INF, INF, INF, INF],
    [INF, INF, INF, INF, 300, 0, INF, INF, INF, 350, INF, INF, INF, 500, INF, INF, INF, INF],
    [250, 300, 400, INF, INF, INF, 0, 300, INF, INF, 300, 500, INF, INF, INF, INF, INF, INF],
    [INF, 250, 200, INF, INF, INF, 300, 0, 300, INF, 450, 450, 500, INF, 600, INF, INF, INF],
    [INF, INF, 250, INF, 350, INF, INF, 300, 0, 300, INF, 450, 400, 650, INF, INF, INF, INF],
    [INF, INF, 450, 350, 200, 350, INF, INF, 300, 0, INF, 600, 400, INF, INF, INF, 600, INF],
    [INF, INF, INF, INF, INF, INF, 300, 450, INF, INF, 0, 500, INF, INF, 350, 600, INF, INF],
    [INF, INF, 600, INF, INF, INF, 500, 450, 450, 600, 500, 0, 200, INF, 300, 200, 500, INF],
    [INF, INF, INF, INF, 600, INF, INF, 500, 400, 400, INF, 200, 0, 550, INF, 300, INF, 600],
    [INF, INF, INF, INF, 600, 500, INF, INF, 650, INF, INF, INF, 550, 0, INF, INF, 400, 300],
    [INF, INF, INF, INF, INF, INF, INF, 600, INF, INF, 350, 300, INF, INF, 0, 300, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 600, 200, 300, INF, 300, 0, 500, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, 600, INF, 500, INF, 400, INF, 500, 0, 300],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 600, 300, INF, INF, 300, 0]
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
var point = new BMapGL.Point(116.363594, 39.968951);
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
    var animation=[]; //这是真的animation 上面那个是倒着进行的操作
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
    console.log("起点：" + StartIndex + "  " + StartValue);
    console.log("终点：" + EndIndex + "  " + EndValue);

    if (StartIndex == EndIndex) {
        alert("起点和终点不能为同一点！");
        return;
    }

    PathArray = dijkstra(path, StartIndex);
    console.log(PathArray);
    //alert("该点到其余各点的最短距离为：" + PathArray);
    //将最短路径在地图上展示出来
    DisplayPath(StartIndex, EndIndex);
    console.log(PathToEnd);
    //将最短路径的距离在页面上展示出来
    var timebybike=parseInt((PathArray[EndIndex]/ByBike)/60);//得到的结果是骑自行车用时
    var timeonfoot=parseInt((PathArray[EndIndex]/Onfootwalk)/60);//步行所用的时间
    document.getElementById("showdis").style.bottom = "5%";
    document.getElementById("showdis").innerHTML = "当前路径的距离为：" + PathArray[EndIndex].toString() + "米"+"<br>"+"步行所用的时间为："+timeonfoot+"分钟"+"<br>"+"自行车所用的时间为："+timebybike+"分钟";
});

var button2 = document.getElementById("warninginfo");
button2.addEventListener("click", function() {
    if (button2.click == false) {
        return;
    }
    document.getElementById("showdis").style.bottom = "1%";
    document.getElementById("showdis").innerHTML = "👿如不能正常使用：<br/>🕸检查网络<br/>💻更换浏览器";

});