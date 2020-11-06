$(document).ready(function () {
    $("#logout").click(function () {
        $.post('/s/logout/', function () {
            alert("退出登录");
            window.location.href = '/s/login/';
        });
    });
    $("#changeInfo").click(function () {
        window.location.href = '/s/changeInfo/';
    });
});