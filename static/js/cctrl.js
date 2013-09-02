var cctrl = cctrl || {};
cctrl.happycloud = cctrl.happycloud  || {};
cctrl.happycloud.config = {
       imageUrl: "img/",
//       apiUrl: "http://cloudcompanion.cloudcontrolled.com/",
       apiUrl: "js/fixture/server_response.json",
       serverErrorImage: "wtf"
};

cctrl.happycloud.init = function (config, appName) {
    var newImage = config.serverErrorImage;
    $.getJSON(config.apiUrl + appName )
        .done(function (data) {
        $.each(data, function (i, item) {
            newImage = item.state;
            return false;
        });

        }).fail(function (jqxhr, textStatus, error) {
            var err = textStatus + ', ' + error;
            console.log("Request Failed: " + err);
        });
    var newImageUrl = config.imageUrl + "Cloud_"+newImage+".jpeg";
    $("#cloudMood").attr("src", newImageUrl);
}
cctrl.happycloud.init(cctrl.happycloud.config, "");

