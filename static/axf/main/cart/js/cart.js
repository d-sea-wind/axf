$(function () {
    // 商品添加到购物车或商品数据加一
    $('.addShopping').click(function () {
        // var $button = $(this);
        // attr可以获取自带的属性也可以获取自定义的属性
        // $button.attr('class')
        // $button.attr('goodsid')
        // prop只可以获取自带的属性
        // $button.prop('class')
        // $button.prop('goodsid')

        var $button = $(this)
        // 获取button标签的爷爷标签div
        var $div = $button.parent().parent();
        // 获取div中的属性值
        var cartid = $div.attr('cartid');
        // ajax传递
        $.post('/axfcart/addCart/',
            {'cartid': cartid},
            function (data) {
                if (data['status'] == 200) {
                    $button.prev().html(data['c_goods_num']);
                    $('#total_price').html(data['total_price']);
                } else {
                    $div.remove();
                    $('#total_price').html(data['total_price']);
                }
            })
    })
    // 商品从购物车中删除或商品数量减一
    $('.subShopping').click(function () {
        var $button = $(this)
        // 获取button标签的爷爷标签div
        var $div = $button.parent().parent();
        // 获取div中的属性值
        var cartid = $div.attr('cartid');
        // ajax传递
        $.post('/axfcart/subCart/',
            {'cartid': cartid},
            function (data) {
                if (data['status'] == 200) {
                    $button.next().html(data['c_goods_num']);
                    $('#total_price').html(data['total_price']);
                } else {
                    $div.remove();
                    $('#total_price').html(data['total_price']);
                }
            })
    })
    // 单选按钮 显示和取消✔
    $('.confirm').click(function () {
        var $confirm = $(this);
        var $div = $confirm.parent();
        var cartid = $div.attr('cartid');

        $.ajax({
            url: '/axfcart/changeStatus/',
            data: {'cartid': cartid},
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                if(data['status'] ==200){
                    if(data['c_is_select']){
                        // 修改✔
                        $confirm.find('span').find('span').html('✔');
                        // 刷新总价
                        $('#total_price').html(data['total_price']);
                    }else{
                        // 修改✔
                        $confirm.find('span').find('span').html('');
                        // 刷新总价
                        $('#total_price').html(data['total_price']);
                    }
                    if (data['is_all_select']){
                        $('#all_select').find('span').find('span').html('✔');
                    }else{
                        $('#all_select').find('span').find('span').html('');
                    }
                }
            }
        })
    })
    // 点击全选
    $('#all_select').click(function () {
        // 全选的div
        var $all_select = $('#all_select');
        // 选中的商品
        var select_list = [];
        // 未选中
        var unselect_list = [];
        // 单选的div
        var $confirm = $('.confirm');
        // 遍历
        $confirm.each(function () {
            // menuList的div
            var cartid = $(this).parent().attr('cartid');
            if($(this).find('span').find('span').html()){
                // 把数据添加到数组中
                select_list.push(cartid);
            }else{
                unselect_list.push(cartid);
            }
        })
        if(unselect_list.length > 0){
            $.getJSON('/axfcart/allSelect/',
                    {'cartidlist':unselect_list.join('#')},
                    function (data) {
                        if(data['status'] == 200){
                            $confirm.find('span').find('span').html('✔');
                            $('#all_select').find('span').find('span').html('✔');
                            $('#total_price').html(data['total_price']);
                        }
                    })
        }else{
            $.getJSON('/axfcart/allSelect/',
                    {'cartidlist':select_list.join('#')},
                    function (data) {
                        if(data['status'] == 200){
                            $confirm.find('span').find('span').html('');
                            $('#all_select').find('span').find('span').html('');
                            $('#total_price').html(data['total_price']);
                        }
                    })
        }
    })
    // 下单
    $('#make_order').click(function () {
        // 获取属性为confirm的div
        var $confirm = $('.confirm');
        // 选中的商品
        var select_list = [];
        // 未选中的商品
        var unselect_list = [];
        // 遍历
        $confirm.each(function () {
            var cartid = $(this).parent().attr('cartid');
            // 被选中的商品
            if($(this).find('span').find('span').html()){
                select_list.push(cartid);
            }else{
                // 没有被选中的商品
                unselect_list.push(cartid);
            }
        })
        // 没有一个商品被选中
        if(select_list.length == 0){
            return;
        }else{
            // 有商品被选中
            $.ajax(
                {
                    url:'/axforder/make_order/',
                    type:'GET',
                    dataType:'json',
                    success:function (data) {
                        if(data['status'] == 200){
                            window.location.href = '/axforder/order_detail/?order_id='+data['order_id']
                        }
                    }
                }
            )
        }
    })
})