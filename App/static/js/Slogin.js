$(document).ready(function () {
    let IdFlag = 0;
    let PasswordFlag = 0;
    // form表的提交事件
    $('#StudentForm').submit(function (event) {
        // 中断默认的submit事件，先校验，在开启
        let Id = $("#InputId").val().trim();
        let Password = $("#InputPassword").val().trim();
        IdFlag = Id.length ? 1 : 0;
        PasswordFlag = Password.length ? 1 : 0;
        if (IdFlag === 0) {
            alert("温馨提示：请输入ID");
            event.preventDefault();
        } else if (PasswordFlag === 0) {
            alert("温馨提示：请输入密码");
            event.preventDefault();
        }
    });
});