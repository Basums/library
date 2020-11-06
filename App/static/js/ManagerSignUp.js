$(document).ready(function () {
    $("#checkManager").submit(function (event) {
        let mobileFlag = 0;
        let KeyFlag = 0;
        let nameFlag = 0;
        let passwordFlag = 0;
        // 中断默认的submit事件，先校验，在开启
        let mobile = $("#inputManagerPhone").val().trim();
        let Key = $("#inputManagerCheck").val().trim();
        let name = $("#inputManagerName").val().trim();
        let pass = $("#inputManagerPas").val().trim();
        passwordFlag = pass.length ? 1 : 0;
        nameFlag = name.length ? 1 : 0;
        mobileFlag = mobile.length ? 1 : 0;
        KeyFlag = Key.length ? 1 : 0;
        event.preventDefault();
        if (mobileFlag === 0) {
            alert("温馨提示：请输入手机号");
            return;
        } else if (mobile.length !== 11) {
            alert("温馨提示：请输入正确的手机号码");
            return;
        }
        if (nameFlag === 0) {
            alert("温馨提示：用户名为空");
            return;
        }
        if (KeyFlag === 0) {
            alert("温馨提示：Key为空");
            return;
        }
        if (passwordFlag === 0) {
            alert("温馨提示：请输入密码");
            return;
        } else if (pass.length <= 6) {
            alert("温馨提示：密码最好6位以上");
            return;
        }
        $.post('/2020/10/24/basums/manager/signUp/basums2020vino/', {
            'mobile': mobile,
            'name': name,
            'pass': pass,
            'key': Key
        }, function (data) {
            if (data.msg === "Key错误") {
                alert("温馨提示：Key错误");
            } else if (data.msg === "管理员注册成功") {
                alert("温馨提示：管理员注册成功");
                // window.location.href = '/s/login/';
            } else if (data.msg === "账号重复") {
                alert("温馨提示：账号重复");
            }
        });

    });

});





