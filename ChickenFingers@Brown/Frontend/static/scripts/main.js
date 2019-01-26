$(document).ready(function(){
    const URL='http://127.0.0.1:5000/'
    var cf = ""
    var statement = ""

    $.getJSON(URL,function(result){
        header1 = document.getElementById("ratty-chicken-finger")
        header2 = document.getElementById("statment")
        obj = result
        var text1 = obj.conf.replace(/\"/g, "")
        var text2 = obj.stat.replace(/\"/g, "")


        header1.innerText = text1
        header2.innerText = text2


    })
})