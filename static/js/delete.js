var Delete = document.getElementById("delete");

Delete.onclick = function (){
    var checkbox = document.getElementsByName("checkbox");
    for (var checkboxKey in checkbox) {
        if(checkboxKey.checked){
            console.log(checkboxKey.value);
        }
    }
}
