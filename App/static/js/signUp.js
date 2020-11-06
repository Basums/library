$(document).ready(function () {
    let mobileFlag = 0;
    // form表的提交事件
    document.getElementById("inputCheck").disabled = true;
    $('#checkMe').submit(function (event) {
        // 中断默认的submit事件，先校验，在开启
        let mobile = $("#inputPhone").val().trim();
        mobileFlag = mobile.length ? 1 : 0;
        event.preventDefault();
        if (mobileFlag === 0) {
            alert("温馨提示：请输入手机号");
        } else if (mobile.length !== 11) {
            alert("温馨提示：请输入正确的手机号码");
        } else {
            document.getElementById('CheckBtn').disabled = true;
            $.post('/s/send_message/', {'mobile': mobile}, function (data) {
                if (data.msg === "该手机已经注册过了") {
                    document.getElementById('CheckBtn').disabled = false;
                    alert("温馨提示：手机号码已注册");
                } else if (data.msg === "验证码已经发送") {
                    document.getElementById("inputCheck").disabled = false;
                    RemainTime();
                }
            });
        }
    });

    //按钮倒计时
    let iTime = 60;

    function RemainTime() {
        let sTime;
        if (iTime === 0) {
            document.getElementById('CheckBtn').disabled = false;
            sTime = "获取验证码";
            iTime = 60;
            document.getElementById('CheckBtn').innerHTML = sTime;
            return;
        } else {
            document.getElementById('CheckBtn').disabled = true;
            sTime = "重新发送(" + iTime + ")";
            iTime--;
        }
        setTimeout(function () {
            RemainTime()
        }, 1000)
        document.getElementById('CheckBtn').innerHTML = sTime;
    }

    // let mobileFlag = 0;
    let checkFlag = 0;
    let nameFlag = 0;
    let proFlag = 0;
    let sexFlag = 0;
    let passwordFlag = 0;
    $("#checkUs").submit(function (event) {
        // 中断默认的submit事件，先校验，在开启
        let mobile = $("#inputPhone").val().trim();
        let check = $("#inputCheck").val().trim();
        let name = $("#inputStuName").val().trim();
        let pro = $("#inputStuPro").val().trim();
        let sex = $("#inputStuSex").val().trim();
        let pass = $("#inputStuPas").val().trim();
        mobileFlag = mobile.length ? 1 : 0;
        checkFlag = check.length ? 1 : 0;
        nameFlag = name.length ? 1 : 0;
        proFlag = pro.length ? 1 : 0;
        sexFlag = sex.length ? 1 : 0;
        passwordFlag = pass.length ? 1 : 0;
        event.preventDefault();
        if (mobileFlag === 0) {
            alert("温馨提示：请输入手机号");
            return;
        } else if (mobile.length !== 11) {
            alert("温馨提示：请输入正确的手机号码");
            return;
        }
        if (checkFlag === 0) {
            alert("温馨提示：请输入验证码");
            return;
        } else if (check.length !== 6) {
            alert("温馨提示：请输入正确的验证码");
            return;
        }
        if (nameFlag === 0) {
            alert("温馨提示：用户名为空");
            return;
        }
        if (proFlag === 0) {
            alert("温馨提示：专业为空");
            return;
        }
        if (sexFlag === 0) {
            alert("温馨提示：性别为空");
            return;
        } else if ((sex !== "男") && (sex !== "女")) {
            alert("温馨提示：请输入正常性别(男/女)");
            return;
        }
        if (passwordFlag === 0) {
            alert("温馨提示：请输入密码");
            return;
        } else if (pass.length <= 6) {
            alert("温馨提示：密码最好6位以上");
            return;
        }
        $.post('/s/signUp/', {
            'mobile': mobile,
            'name': name,
            'pro': pro,
            'sex': sex,
            'pass': pass,
            'check': check
        }, function (data) {
            if (data.msg === "验证码错误") {
                alert("温馨提示：验证码输入错误");
            } else if (data.msg === "用户注册成功") {
                alert("温馨提示：用户注册成功");
                window.location.href = '/s/login/';
            }
        });

    });

});





