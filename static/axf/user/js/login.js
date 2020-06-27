function changeImage() {
    var i = document.getElementById('changeImg');

    i.src = '/axfuser/get_code/?'+Math.random();
}

function parse() {
    // 获取页面中的密码
    var password = document.getElementById('password').value;
    // 前端md5加密
    password = md5(password);
    // 重新赋值,把原没加密的密码覆盖
    document.getElementById('password').value = password;
    return true
}