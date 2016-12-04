"use strict";
var bs_url = '/basestation';
var bs_data = {};
var bs_point = {};
var bs_location;                                // json 에서 얻어온 모든 기지국 정보
var bs_map;
var marker;
var circle;
var circles = [];
var markers = [];
// lat = 위도 (37...) , lng = 경도 (127...)

$(function(){
    // 맵 생성
    bs_map = new google.maps.Map(document.getElementById('bs_map'),{
        zoom: 18,
        center: {lat: 37.497518, lng: 127.029676 },
        scrollwheel: true,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true,
        scaleControl: true,
    });

    $(".bsmarking").click(function(){
        if($(this).is(":checked")){
            for(var i=0;i<bs_data.length;i++){
                if(bs_data[i].id == this.id){
                    bs_point = bs_data[i];
                    break;
                }
            }
            bs_location={lat: Number(bs_point.lat), lng: Number(bs_point.lng)}

            marker = new google.maps.Marker({
                position: bs_location,
                map: bs_map,
            });
            circle = new google.maps.Circle({
               map: bs_map,
               fillColor: '#ffffff',
               fillOpacity: 0.3,
               strokeColor: '#ff0000',
               strokeOpacity: 1.0,
               strokeWeight: 1.5,
               radius: 100// 50 MILES in meters
            });
            circle.bindTo('center', marker, 'position');
            markers[this.id] = marker;
            circles[this.id] = circle;
            circle.setMap(bs_map);
            bs_map.panTo(marker.getPosition());
        }
        else{
            markers[this.id].setMap(null);
            circles[this.id].setMap(null);
        }
    })
})

$.getJSON(bs_url,function(b_json){
    bs_data = b_json;
});
