$(document).ready(function () {
    $('#ManagerBorrowRedirectForm').submit(function (event) {
        let IdFlag = 0;
        let Id = $("#InputStudentID").val().trim();
        IdFlag = Id.length ? 1 : 0;
        event.preventDefault();
        if (IdFlag === 0) {
            alert("温馨提示：请输入ID");
        } else {
            $.post('/2020/10/24/basums/manager/borrowRedirect/basums2020vino/',
                {
                    "book_id": document.getElementById("InputBookId").innerHTML,
                    "student_id": document.getElementById("InputStudentID").value
                }, function (data) {
                    if (data.msg === "用户未注册") {
                        alert("温馨提示: 用户未注册");
                    } else if (data.msg === "206") {
                        alert("温馨提示: 借阅成功");
                    } else if (data.msg === "407") {
                        alert("温馨提示: 该用户已经借过了这本书");
                    }
                })
        }
    });
});