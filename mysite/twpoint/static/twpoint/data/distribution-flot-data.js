$(function(){
    var w_url = "/waypoint";
    $.getJSON(w_url, function(json){
        var data = [];
        var address;
        var geocoder = new google.maps.Geocoder();

        for(var i =0; i< json.length;i++){
            if(json[i].position_x != null && json[i].position_y != null){
                address = geocodeAddress(geocoder, json[i].position_y, json[i].position_x);
                console.log(address);
            }
            else if(json[i].start_x != null && json[i].start_y != null){
                address = geocodeAddress(geocoder, json[i].start_y, json[i].start_y);
                console.log(address);
            }
            else if(json[i].search_x !=null && json[i].search_y != null){
                address = geocodeAddress(geocoder, json[i].search_y, json[i].search_x);
                console.log(address);
            }
        }
    });
})

function geocodeAddress(geocoder, lat, lng) {
    geocoder.geocode({'address': lat.toString() + "," + lng.toString() }, function(results, status) {
        debugger;
        if (status === google.maps.GeocoderStatus.OK) {
            return results[0].geometry.location;
        } else {
            return 'Geocode was not successful for the following reason: ' + status;
        }
    });
}