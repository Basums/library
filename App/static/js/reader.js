$(document).ready(function () {
    let bookIdFlag = 0;
    let bookNameFlag = 0;
    let bookAuthorFlag = 0;
    // form表的提交事件
    $('#searchBook').submit(function (event) {
        // 中断默认的submit事件，先校验，在开启
        let bookId = $("#input_book_id").val().trim();
        let bookName = $("#input_book_name").val().trim();
        let bookAuthor = $("#input_book_author").val().trim();
        bookIdFlag = bookId.length ? 1 : 0;
        bookNameFlag = bookName.length ? 1 : 0;
        bookAuthorFlag = bookAuthor.length ? 1 : 0;
        if ((bookIdFlag === 0) && (bookNameFlag === 0) && (bookAuthorFlag === 0)) {
            alert("温馨提示：请输入搜索条件");
            event.preventDefault();
        }
    });
});