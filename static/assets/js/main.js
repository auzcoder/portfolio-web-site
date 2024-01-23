var $window = $(window),
    $root = $("html, body");

function validateEmail(o) {
    return /\S+@\S+\.\S+/.test(o)
}

function sendEmail() {
    var o = $("#name").val(),
        e = $("#family").val(),
        t = $("#email").val(),
        s = $("#comments").val();
    o ? e ? t ? validateEmail(t) ? s || ($("#message").toast("show").addClass("bg-danger").removeClass("bg-success"), $(".toast-body").html("Xabaringizni kiriting")) : ($("#message").toast("show").addClass("bg-danger").removeClass("bg-success"), $(".toast-body").html("Iltimos, to'g'ri e-pochta manzilini kiriting")) : ($("#message").toast("show").addClass("bg-danger").removeClass("bg-success"), $(".toast-body").html("Email addressingizni kiriting.")) : ($("#message").toast("show").addClass("bg-danger").removeClass("bg-success"), $(".toast-body").html("Familiyangizni kiriting.")) : ($("#message").toast("show").addClass("bg-danger").removeClass("bg-success"), $(".toast-body").html("Ismingizni kiriting"))
}
$(document).ready(function() {
    var o = $(".mouse-cursor");
    if (o.length && $("body")) {
        const r = document.querySelector(".cursor"),
            l = document.querySelector(".cursor-effect");
        let e, t = 0;
        window.onmousemove = function(o) {
            l.style.transform = "translate(" + o.clientX + "px, " + o.clientY + "px)", r.style.transform = "translate(" + o.clientX + "px, " + o.clientY + "px)", e = o.clientY, t = o.clientX
        }, $("body").on("mouseenter", "a, .cursor-pointer", function() {
            r.classList.add("cursor-hover"), l.classList.add("cursor-hover")
        }), $("body").on("mouseleave", "a, .cursor-pointer", function() {
            $(this).is("a") && $(this).closest(".cursor-pointer").length || (r.classList.remove("cursor-hover"), l.classList.remove("cursor-hover"))
        }), r.style.visibility = "visible", l.style.visibility = "visible"
    }
    $(".header .navbar-nav a, .to-contact, .scroll-down a").on("click", function(o) {
        var e = $(this);
        $root.stop().animate({
            scrollTop: $(e.attr("href")).offset().top - 60
        }, 1500, "easeInOutQuart"), o.preventDefault(), $(".navbar-collapse").collapse("hide")
    }), $(".sidebar .navbar-nav a, .sidebar .list-group a").on("click", function(o) {
        var e = $(this);
        $root.stop().animate({
            scrollTop: +$(e.attr("href")).offset().top
        }, 1500, "easeInOutQuart"), o.preventDefault()
    });
    var e = $(".sidebar-toggler"),
        t = $(".sidebar"),
        s = $(".page-content");
    e.on("click", function() {
        $(this).toggleClass("move lni-chevron-left lni-menu"), t.toggleClass("hide")
    }), $window.width() < 1199 && (e.addClass("move lni-menu"), e.removeClass("lni-chevron-left"), t.addClass("hide"), s.addClass("full-width"), $(".sidebar .navbar-nav a, .sidebar .list-group a").on("click", function() {
        setTimeout(function() {
            e.toggleClass("move lni-chevron-left lni-menu"), t.toggleClass("hide"), s.toggleClass("full-width")
        })
    })), $(".color-scheme li .dark-scheme").on("click", function() {
        $("body").addClass("westin-dark"), $(".color-scheme li a").removeClass("active"), $(this).addClass("active"), $("#logo").attr("src", "assets/img/westin-logo-dark.png")
    }), $(".color-scheme li .light-scheme").on("click", function() {
        $("body").removeClass("westin-dark"), $(".color-scheme li a").removeClass("active"), $(this).addClass("active"), $("#logo").attr("src", "assets/img/westin-logo.png")
    }), $(".theme-skin li .border-skin").on("click", function() {
        $("body").addClass("border-style-demo"), $(".theme-skin li a").removeClass("active"), $(this).addClass("active")
    }), $(".theme-skin li .flat-skin").on("click", function() {
        $("body").removeClass("border-style-demo"), $(".theme-skin li a").removeClass("active"), $(this).addClass("active")
    }), $("ul.pattern .color1").on("click", function() {
        return $("#option-color").attr("href", "assets/css/color/azure.css"), !1
    }), $("ul.pattern .color2").on("click", function() {
        return $("#option-color").attr("href", "assets/css/color/blue.css"), !1
    }), $("ul.pattern .color3").on("click", function() {
        return $("#option-color").attr("href", "assets/css/color/purple.css"), !1
    }), $("ul.pattern .color4").on("click", function() {
        return $("#option-color").attr("href", "assets/css/color/dark-purple.css"), !1
    }), $("ul.pattern .color5").on("click", function() {
        return $("#option-color").attr("href", "assets/css/color/golden.css"), !1
    }), $("ul.pattern .color6").on("click", function() {
        return $("#option-color").attr("href", "assets/css/color/green.css"), !1
    }), $("ul.pattern .color7").on("click", function() {
        return $("#option-color").attr("href", "assets/css/color/citrus.css"), !1
    }), $("ul.pattern .color8").on("click", function() {
        return $("#option-color").attr("href", "assets/css/color/light-orange.css"), !1
    }), $("ul.pattern .color9").on("click", function() {
        return $("#option-color").attr("href", "assets/css/color/orange.css"), !1
    }), $("ul.pattern .color10").on("click", function() {
        return $("#option-color").attr("href", "assets/css/color/red.css"), !1
    }), $("ul.pattern .color11").on("click", function() {
        return $("#option-color").attr("href", "assets/css/color/pink.css"), !1
    }), $("ul.pattern .color12").on("click", function() {
        return $("#option-color").attr("href", "assets/css/color/mono.css"), !1
    }), $("#color-switcher .pallet-button").on("click", function() {
        return $("#color-switcher .color-pallet").toggleClass("show"), !1
    }), $("ul.pattern .color13").on("click", function() {
        return $("#option-color-two").attr("href", "assets/css/color/pink.css"), !1
    }), $("ul.pattern .color14").on("click", function() {
        return $("#option-color-two").attr("href", "assets/css/color/sky-blue.css"), !1
    }), $("ul.pattern .color15").on("click", function() {
        return $("#option-color-two").attr("href", "assets/css/color/golden.css"), !1
    });
    o = $(".element");
    o.length && (o = {
        strings: o.attr("data-elements").split(","),
        typeSpeed: 100,
        backDelay: 3e3,
        backSpeed: 50,
        loop: !0
    }, new Typed(".element", o)), 0 < ".portfolio-items".length && $(".portfolio-items").each(function() {
        $(this).magnificPopup({
            delegate: ".js-zoom-gallery",
            type: "image",
            gallery: {
                enabled: !0
            }
        })
    }), $("#testimonial .owl-carousel").owlCarousel({
        items: 1,
        nav: !1,
        autoplay: !1,
        loop: !0,
        dots: !0,
        mouseDrag: !0,
        touchDrag: !0,
        smartSpeed: 1e3,
        autoplayHoverPause: !0
    })
}), $window.on("load", function() {
    $("#angela-preloader").addClass("loaded"), $("#angela-preloader").hasClass("loaded") && $("#angela-preloader").delay(900).queue(function() {
        $(this).remove()
    });
    var o, e, t, s = $("#showMore-initials").data("initial"),
        r = $("#showMore-initials").data("next"),
        l = $("#portfolio-filter"),
        a = $(".portfolio-items"),
        i = $("#showMore");
    a.isotope({
        itemSelector: ".portfolio-item",
        layoutMode: "masonry"
    }), l.find("a").on("click", function() {
        var o = $(this).attr("data-filter");
        return l.find("a").removeClass("active"), $(this).addClass("active"), a.isotope({
                filter: o
            }),
            function() {
                var o = a.isotope("getFilteredItemElements");
                $(o).length > s ? (i.show(), i.parent(".button-border").addClass("mr-2 mr-sm-4").removeClass("p-0")) : (i.hide(), i.parent(".button-border").removeClass("mr-2 mr-sm-4").addClass("p-0")), $(".portfolio-item").hasClass("visible_item") && $(".portfolio-item").removeClass("visible_item");
                var e = 0;
                $(o).each(function() {
                    s <= e && $(this).addClass("visible_item"), e++
                }), a.isotope("layout")
            }(), !1
    }), i.on("click", function(o) {
        var e, t;
        o.preventDefault(), e = r, o = $(".visible_item").length, t = 0, $(".visible_item").each(function() {
            t < e && ($(this).removeClass("visible_item"), t++)
        }), o <= t && (i.hide(), i.parent(".button-border").removeClass("mr-2 mr-sm-4").addClass("p-0")), a.isotope("layout")
    }), o = s, e = $(".portfolio-item").length, t = 0, $(".portfolio-item").each(function() {
        o <= t && $(this).addClass("visible_item"), t++
    }), (t < e || e <= s) && (i.hide(), i.parent(".button-border").removeClass("mr-2 mr-sm-4").addClass("p-0")), a.isotope("layout")
}), $window.on("scroll", function() {
    var o = $(".return-to-top");
    150 < $window.scrollTop() ? o.addClass("show") : o.removeClass("show"), o.on("click", function() {
        $root.stop().animate({
            scrollTop: 0
        }, 1500)
    });
    var e = $window.scrollTop(),
        o = $("#count-up");
    o.length && (t = $window.height(), o.offset().top < e + t && ($(".timer").countTo(), $(".count-number").removeClass("timer")));
    var t, e = $window.scrollTop(),
        o = $("#skills");
    0 < o.length && (t = $window.height(), o.offset().top < e + t && $(".skillbar").each(function() {
        $(this).find(".skillbar-bar").animate({
            width: $(this).attr("data-percent")
        }, 6e3)
    }))
});