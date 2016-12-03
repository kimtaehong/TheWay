"use strict";
var bs_url = '/basestation';
var bs_data = {};                                  // json 에서 얻어온 모든 기지국 정보
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

$.getJSON(bs_url,function(b_json){
    bs_data = b_json;
});
