function initWheel() {
    var mySwiper = new Swiper('#topSwiper', {
        loop: true,
        autoplay: 1000,
        pagination: '.swiper-pagination',
        autoplayDisableOnInteraction: false,
    })
}

function initMustBuy() {
    var mySwiper1 = new Swiper('#swiperMenu', {
        slidesPerView: 3,
    })
}


$(function () {
    initWheel();
    initMustBuy();
})


