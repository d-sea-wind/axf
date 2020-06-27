$(function () {
    // 用户名字的前台验证  blur()焦点集中
    $('#exampleInputName').blur(function () {
        // html()获取标签里的所有
        // text()获取标签里的文本

        // 获取文本框输入的信息
        var name = $(this).val();

        // 校验文本框的内容是否满足下面的正则表达式(js中用/正则表达式/)
        var reg = /^[a-z]{3,6}$/;
        var b = reg.test(name);

        // $('#nameinfo').html('✔用户名字可以使用').css({'color':'green','font-size':10});
        if (b) {
            //    $.getJson   $.get   $.POST  $.AJAX
            // $.getJSON(url,参数，function(data))
            $.getJSON('/axfuser/checkName/',
                {'name': name},
                function (data) {
                    if (data['status'] == 200) {
                        $('#nameinfo').html(data['msg']).css({'color': 'green', 'font-size': 10});
                    } else {
                        $('#nameinfo').html(data['msg']).css({'color': 'red', 'font-size': 10});
                    }
                }
            )
        } else {
            $('#nameinfo').html('❌用户名格式不正确').css({'color': 'red', 'font-size': 10});
        }
    })
    // 确认密码验证
    $('#passwordconfirm').blur(function () {
        // 获取用户的密码内容
        var password = $('#password').val()
        // 获取用户的确认密码内容
        var confirmatepassword = $(this).val()
        if (!confirmatepassword) {
            $('#passwordinfo').html('❌请输入密码').css({'color': 'red', 'font-size': 10});
        } else if (password != confirmatepassword) {
            $('#passwordinfo').html('❌两次输入的密码不一致').css({'color': 'red', 'font-size': 10});
        } else {
            $('#passwordinfo').html('✔两次输入的密码一致').css({'color': 'green', 'font-size': 10});
        }
    })
})

function parse1() {
    var password = document.getElementById('password').value;
    password = md5(password)
    document.getElementById('password').value = password
    return true
}