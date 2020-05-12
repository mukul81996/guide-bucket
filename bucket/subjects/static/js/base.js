$(document).ready(function () {
    AOS.init({
        disable: "mobile"
    }), $("[data-bs-hover-animate]").mouseenter(function () {
        var a = $(this);
        a.addClass("animated " + a.attr("data-bs-hover-animate"))
    }).mouseleave(function () {
        var a = $(this);
        a.removeClass("animated " + a.attr("data-bs-hover-animate"))
    })
});