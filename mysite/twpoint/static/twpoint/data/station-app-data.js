var station_url = '/basestation';
var station_data = [];
var flag = false;
var circles;
var b_markers;

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
    $('#station_500').click(function(){
        if(station_data.length == 0){
            MyAlert("No Base Station Data!");
            return;
        }
        Action(station_data, 500);
    });

    $('#station_delete').click(function(){
        if(b_markers == null && circles == null){
            MyAlert("The base station is not selected");
            return;
        }
        b_markers.forEach(function(item){
            item.setMap(null);
        });
        circles.forEach(function(item){
            item.setMap(null);
        });
        flag = false;
    });
})

$.getJSON(station_url, function(json){
    station_data = json;
});

/* alert */
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

    var map = app_map;
    if(flag){
        circles.forEach(function(item){
            item.setRadius(radius);
        });
    } else{
        circles = locations.map(function(item, index){
            return new google.maps.Circle({
                fillColor: '#ff0000',
                fillOpacity: 0.08,
                strokeColor: '#ff0000',
                strokeOpacity: 1.0,
                radius: radius,
                center: item,
                map: map,
            });
        });
        b_markers = locations.map(function(item){
            return new google.maps.Marker({
                position: item,
                icon:{
                    url: '/static/twpoint/img/base_station_icon.png',
                    scaledSize: new google.maps.Size(50,50),
                },
                map: map,
            });
        });
        flag = true;
    }
}
