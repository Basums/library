$(document).ready(function () {
    $("#ManagerLogout").click(function () {
        $.post('/2020/10/24/basums/manager/logout/basums2020vino/', function () {
            alert("退出登录");
            window.location.href = '/2020/10/24/basums/manager/login/basums2020vino/';
        });
    });
    $("#ManagerBorrow").click(function () {
        window.location.href = '/2020/10/24/basums/manager/borrow/basums2020vino/';
    });
    $("#ManagerReturn").click(function () {
        window.location.href = '/2020/10/24/basums/manager/return/basums2020vino/';
    });
    $("#ManagerSearch").click(function () {
        window.location.href = '/2020/10/24/basums/manager/reader/basums2020vino/';
    });

    $("#ManagerInOut").click(function () {
        window.location.href = '/2020/10/24/basums/manager/inout/basums2020vino/';
    });
});