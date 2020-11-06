$(document).ready(function () {
    let NameFlag = 0;
    let SexFlag = 0;
    let ProFlag = 0;
    let PasswordFlag = 0;
    // form表的提交事件
    $('#inputNameForm').submit(function (event) {
        // 中断默认的submit事件，先校验，在开启
        let Id = $("#inputName").val().trim();
        NameFlag = Id.length ? 1 : 0;
        if (NameFlag === 0) {
            alert("温馨提示：请输入要更新的用户名称");
            event.preventDefault();
        }
    });
    $('#inputProForm').submit(function (event) {
        // 中断默认的submit事件，先校验，在开启
        let Id = $("#inputPro").val().trim();
        ProFlag = Id.length ? 1 : 0;
        if (ProFlag === 0) {
            alert("温馨提示：请输入要更新的专业名称");
            event.preventDefault();
        }
    });
    $('#inputSexForm').submit(function (event) {
        // 中断默认的submit事件，先校验，在开启
        let Id = $("#inputSex").val().trim();
        SexFlag = Id.length ? 1 : 0;
        if (SexFlag === 0) {
            alert("温馨提示：请输入要更新的性别名称");
            event.preventDefault();
        }
    });
    $('#inputPasswordForm').submit(function (event) {
        // 中断默认的submit事件，先校验，在开启
        let Id = $("#inputPassword2").val().trim();
        PasswordFlag = Id.length ? 1 : 0;
        if (PasswordFlag === 0) {
            alert("温馨提示：请输入要更新的密码");
            event.preventDefault();
        }
    });
});