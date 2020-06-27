$(function () {
    $('#login').click(function () {
        // window.open('/axfuser/login/',target='_self');
        // 点击标签直接跳转到登录页面
        window.location.href='/axfuser/login/';
    })

    $('#regis').click(function () {
        // 点击标签直接调转到注册页面
        window.open('/axfuser/register/',target='_self');
    })
})