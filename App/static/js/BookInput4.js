$(document).ready(function () {

    // form表的提交事件
    $('#BookInput').submit(function (event) {
        let InputBookIdFlag = 0;
        let InputBookNameFlag = 0;
        let InputBookAuthorFlag = 0;
        let InputBookPubFlag = 0;
        let InputBookNumFlag = 0;
        let InputBookSortFlag = 0;
        // 中断默认的submit事件，先校验，在开启
        let Id = $("#InputBookId").val().trim();
        let Name = $("#InputBookName").val().trim();
        let Author = $("#InputBookAuthor").val().trim();
        let Pub = $("#InputBookPub").val().trim();
        let Num = $("#InputBookNum").val().trim();
        let Sort = $("#InputBookSort").val().trim();
        InputBookIdFlag = Id.length ? 1 : 0;
        InputBookNameFlag = Name.length ? 1 : 0;
        InputBookAuthorFlag = Author.length ? 1 : 0;
        InputBookPubFlag = Pub.length ? 1 : 0;
        InputBookNumFlag = Num.length ? 1 : 0;
        InputBookSortFlag = Sort.length ? 1 : 0;
        if (InputBookIdFlag === 0) {
            alert("温馨提示：请输入ID");
            event.preventDefault();
        } else if (InputBookNameFlag === 0) {
            alert("温馨提示：请输入书名");
            event.preventDefault();
        } else if (InputBookAuthorFlag === 0) {
            alert("温馨提示：请输入作者");
            event.preventDefault();
        } else if (InputBookPubFlag === 0) {
            alert("温馨提示：请输入出版社");
            event.preventDefault();
        } else if (InputBookNumFlag === 0) {
            alert("温馨提示：请输入数量");
            event.preventDefault();
        } else if (InputBookSortFlag === 0) {
            alert("温馨提示：请输入种类");
            event.preventDefault();
        }
    });
});