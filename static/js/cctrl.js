var cctrl = cctrl || {};
cctrl.happycloud = cctrl.happycloud  || {};

cctrl.happycloud.init = function () {
    var flickerAPI = "http://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=?";
    $.getJSON(flickerAPI, {
        tags: "mount rainier",
        tagmode: "any",
        format: "json"
    }).done(function (data) {
            $.each(data.items, function (i, item) {
                $("<img/>").attr("src", item.media.m).appendTo("#image");
                return false;
            });
        }).fail(function (jqxhr, textStatus, error) {
            var err = textStatus + ', ' + error;
            $("<img/>").attr("src", "http://blog.extreme-advice.com/wp-content/uploads/2013/01/error.png").appendTo("#image");
            console.log("Request Failed: " + err);
        });
}

cctrl.happycloud.init();