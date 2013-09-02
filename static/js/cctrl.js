var cctrl = cctrl || {};
cctrl.happycloud = cctrl.happycloud  || {};
cctrl.happycloud.config = {
       imageUrl: "/static/img/",
       apiUrl: "/",
       serverErrorImage: "wtf"
};

cctrl.happycloud.updateImage= function (config, newImage) {
    var newImageUrl = config.imageUrl + "Cloud_" + newImage + ".jpeg";
    console.log("Request ok: new image url: " + newImageUrl);
    $("#cloudMood").attr("src", newImageUrl);
} ;

cctrl.happycloud.init = function (config, appName) {
    $.getJSON(config.apiUrl + appName )
        .done(function (data) {
            var newImage = data[0].state;
            console.log("Request ok: new image: " + newImage);
            cctrl.happycloud.updateImage(config, newImage);
        }).fail(function (jqxhr, textStatus, error) {
            var err = textStatus + ', ' + error;
            console.log("Request Failed: " + err);
            cctrl.happycloud.updateImage(config, config.serverErrorImage);
        });

};

cctrl.happycloud.init(cctrl.happycloud.config, "a");

