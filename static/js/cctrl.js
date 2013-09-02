var cctrl = cctrl || {};
cctrl.happycloud = cctrl.happycloud  || {};
cctrl.happycloud.config = {
       apiUrl: "http://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=",
       serverErrorImage: "img/CloudWTF.jpeg"
};

cctrl.happycloud.init = function () {
    $.getJSON(cctrl.happycloud.config.apiUrl, {
        tags: "mount rainier",
        tagmode: "any",
        format: "json"
    }).done(function (data) {
            $.each(data.items, function (i, item) {
                $("#cloudMood").attr("src", item.media.m);
                return false;
            });
        }).fail(function (jqxhr, textStatus, error) {
            var err = textStatus + ', ' + error;
            $("#cloudMood").attr("src", cctrl.happycloud.config.serverErrorImage);
            console.log("Request Failed: " + err);
        });
}
cctrl.happycloud.init();