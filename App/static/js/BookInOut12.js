$(document).ready(function () {
    $('#returnBook').submit(function (event) {
        let bookIdFlag = 0;
        // form表的提交事件
        // 中断默认的submit事件，先校验，在开启
        let bookId = $("#input_book_id4").val().trim();
        bookIdFlag = bookId.length ? 1 : 0;
        if (bookIdFlag === 0) {
            alert("温馨提示：请输入搜索条件");
            event.preventDefault();
        }
    });

    $('#changeBook').click(function (event) {
        let InputBookNameFlag = 0;
        let InputBookAuthorFlag = 0;
        let InputBookPubFlag = 0;
        let InputBookNumFlag = 0;
        let InputBookSortFlag = 0;
        // 中断默认的submit事件，先校验，在开启
        let Id = document.getElementById("BookId").innerHTML.trim();
        let Name = $("#inputBookName").val().trim();
        let Author = $("#inputBookAuthor").val().trim();
        let Pub = $("#inputBookPub").val().trim();
        let Num = $("#inputBookNum").val().trim();
        let Sort = $("#inputBookSort").val().trim();
        InputBookNameFlag = Name.length ? 1 : 0;
        InputBookAuthorFlag = Author.length ? 1 : 0;
        InputBookPubFlag = Pub.length ? 1 : 0;
        InputBookNumFlag = Num.length ? 1 : 0;
        InputBookSortFlag = Sort.length ? 1 : 0;
        if (InputBookNameFlag === 0) {
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
        } else {
            $.post('/2020/10/24/basums/manager/changeRedirect/basums2020vino/',
                {
                    "Id": Id,
                    "Name": Name,
                    "Author": Author,
                    "Pub": Pub,
                    "Num": Num,
                    "Sort": Sort
                }, function (data) {
                    alert(data.msg);
                });

        }
    })
    $('#deleteBook').click(function (event) {
        $.post('/2020/10/24/basums/manager/deleteRedirect/basums2020vino/',
            {
                "Id": document.getElementById("BookId").innerHTML.trim()
            }, function (data) {
                alert(data.msg);
            });
    })
});