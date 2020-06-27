$(function () {
    // 获取全部分类
    $('#all_type').click(function () {
        // ^的方向
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up');
        // ^方向下展示和收起
        $('#all_type_container').toggle();
    });
    // 获取综合排序
    $('#sort_rule').click(function () {
        // ^的方向
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up');
        // ^方向下展示和收起
        $('#sort_rule_container').toggle();
    })
    // 添加或则数量加一到购物车
    $('.addShopping').click(function () {
        // var $button = $(this);
        // attr可以获取自带的属性也可以获取自定义的属性
        // $button.attr('class')
        // $button.attr('goodsid')
        // prop只可以获取自带的属性
        // $button.prop('class')
        // $button.prop('goodsid')

        var $button = $(this)
        // 获取自定义的属性值
        var goodsid = $button.attr('goodsid')
        // ajax传递
        $.get('/axfcart/addToCart/',
            {'goodsid': goodsid},
            function (data) {
                if (data['status'] == 200) {
                    $button.prev().html(data['c_goods_num']);
                } else {
                    window.location.href = '/axfuser/login/'
                }
            })
    })
    // 删除或则数量减一到购物车
    $('.subShopping').click(function () {
        var $button = $(this)
        // 获取自定义的属性值
        var goodid = $button.attr('goodid');
        // ajax传递
        $.get('/axfcart/subToCart/',
            {'goodid': goodid},
            function (data) {
                if (data['status'] == 200) {
                    $button.next().html(data['c_goods_num']);
                } else {
                    window.location.href = '/axfuser/login/'
                }
            })
    })
})
