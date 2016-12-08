var station_url = '/basestation';
var station_data = [];
var flag = false;
var circles;

$(function(){
    /* base station 100m option */
    $('#station_100').click(function(){
        if(station_data.length == 0){
            MyAlert("No Base Station Data!");
            return;
        }
        Action(station_data, 100);
    });

    /* base station 300m option */

    $('#station_300').click(function(){
        if(station_data.length == 0){
            MyAlert("No Base Station Data!");
            return;
        }
        Action(station_data, 300);
    });

    /* base statoin 500m option */
    $('#station_100').click(function(){
        if(station_data.length == 0){
            MyAlert("No Base Station Data!");
            return;
        }
        Action(station_data, 500);
    });
})

$.getJSON(station_url, function(json){
    station_data = json;
});


function MyAlert(msg){
    var alert_html = "";
    alert_html += "<div class='alert alert-danger alert-dismissable' role='alert'>\t\n";
    alert_html += "<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;</button>";
    alert_html += msg;
    alert_html += "</div>";

    $('.myAlert')[0].innerHTML = alert_html;
}

function Action(station_data, radius){
    var locations = [];

    station_data.forEach(function(item, index, array){
        locations.push({lat: item.lat, lng: item.lng});
    });

    var map = google.maps.Map(document.getElementById('app_map'));

    if(flag){
        circles.setRadius(radius);
    } else{
        circles = locations.map(function(item, index){
            return google.maps.Circle({
                fillcolor: 'red',
                fillOpacity: 0.3,
                strokeColor: 'white',
                radius: radius,
                position: item,
                map: map,
            });
        });

        flag = true;
    }



}
