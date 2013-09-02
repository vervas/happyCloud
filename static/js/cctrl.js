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
    var api_url = config.apiUrl + appName;
    console.log("Api call to: " + api_url);
    $.getJSON(api_url )
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

cctrl.happycloud.getParameterByName = function(name) {
    name = name.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results == null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

cctrl.happycloud.init(cctrl.happycloud.config, cctrl.happycloud.getParameterByName("name"));

