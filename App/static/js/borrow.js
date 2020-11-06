$(document).ready(function () {
    $('#borrowBook').submit(function (event) {
        let bookIdFlag = 0;
        // form表的提交事件
        // 中断默认的submit事件，先校验，在开启
        let bookId = $("#input_book_id2").val().trim();
        bookIdFlag = bookId.length ? 1 : 0;
        if (bookIdFlag === 0) {
            alert("温馨提示：请输入搜索条件");
            event.preventDefault();
        }
    });

    $('#ManagerBorrow').click(function () {
        window.location.href =
            '/2020/10/24/basums/manager/borrowRedirect/basums2020vino/?book_id='
            +
            document.getElementById('ManagerBorrow').value;
    });
});