"use strict";
var way_data = {};                                  // json 에서 얻어온 모든 위치 정보
var way_location = {lat: 37.497518, lng: 127.029676 }; // 특정 위치정보에 위도, 경도
var way_point = {};                                 // 특정 위치정보
var bs_map;
// lat = 위도 (37...) , lng = 경도 (127...)

$(function(){
    // 맵 생성
    bs_map = new google.maps.Map(document.getElementById('bs_map'),{
        zoom: 18,
        center: way_location,
        scrollwheel: false,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true,
        scaleControl: true,
    });

})
