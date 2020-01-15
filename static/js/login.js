window.onload = function () {
    function setCookie(name, value, day) {
        var date = new Date();
        date.setDate(date.getDate() + day);
        document.cookie = name + '=' + value + ';expires=' + date;
    };

    //获取cookie
    function getCookie(name) {
        var reg = RegExp(name + '=([^;]+)');
        var arr = document.cookie.match(reg);
        if (arr) {
            return arr[1];
        } else {
            return '';
        }
    };

    //删除cookie
    function delCookie(name) {
        setCookie(name, '', -1);
    }

    $("#username").val(getCookie('username'));
    $("#password").val(getCookie('password'));
    if (getCookie('username') != '') {
        var checkbox = $('#remember_pwd');
        checkbox.attr('checked', 'checked')
    }


    $('#submit').on("click", function () {
        var checkbox = $('#remember_pwd');
        if (checkbox[0].checked) {
            var name = $("#username").val();
            var pswd = $("#password").val();
            setCookie('username', name, 7)
            setCookie('password', pswd, 7)
        } else {
            delCookie('username')
            delCookie('password')
        }
    })


}
