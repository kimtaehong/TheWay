"use strict";
var app_id = location.href.split("result/")[1];     // 위치정보 app id
var way_url = '/waypoint/' + app_id;                // 위치 정보 url
var way_data = {};                                  // json 에서 얻어온 모든 위치 정보
var way_location; // 특정 위치정보에 위도, 경도
var way_point = {};                                 // 특정 위치정보
var app_map;
var marker;
var markers = [];
// lat = 위도 (37...) , lng = 경도 (127...)

$(function(){
    // 맵 생성

    app_map = new google.maps.Map(document.getElementById('app_map'),{
        zoom: 18,
        center: {lat: 37.497518, lng: 127.029676 },
        scrollwheel: false,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true,
        scaleControl: true,
    });

    $(".marking").click(function(){
        if($(this).is(":checked")){
            for(var i=0;i<way_data.length;i++){
                if(way_data[i].id == this.id){
                    way_point = way_data[i];
                    break;
                }
            }
            if(way_point == null){
                console.log("Way Point is NULL!!(checked)");
                $(this).checked = false;
                return;
            }
            if(way_point.position != null || way_point.position_x != null && way_point.position_y != null){
                console.log('position');
                way_location = {lat: Number(way_point.position_y), lng: Number(way_point.position_x) };
            }
            else if(way_point.start != null || way_point.start_x != null && way_point.start_y !=null){
                console.log('start');
                way_location = {lat: Number(way_point.start_y), lng: Number(way_point.start_x) };
            }
            else if(way_point.search != null && way_point.search_x != null && way_point.search_y != null){
                console.log('search');
                way_location = {lat: Number(way_point.search_y), lng: Number(way_point.search_x) };
            }

            if(way_location == null){
                console.log("Way Location is NULL!!(checked)");
                $(this).checked = false;
                return;
            }

            marker = new google.maps.Marker({
                position: way_location,
                map: app_map,
            });
            markers[this.id] = marker;
            app_map.panTo(marker.getPosition());
        }
        else{
            markers[this.id].setMap(null);
        }
    })
})

$.getJSON(way_url,function(w_json){
    way_data = w_json;
});



/*
    Google Maps Api 사용

    /// map ///
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom:           // 지도의 줌
        center:         // 지도의 중심 위치
        scrollwheel:    // 스크롤윌 사용 여부
        mapTypeId:      // 지도의 종류 선택  ex) ROADMAP, ...
        disableDefaultUI: // true: 모든 control 없이 기본으로
        scaleControl:   // true: 오른쪽 아래에 거리?를 표시
        mapTypeControl  // 지도, 위성 선택
        ...
    });
    map.setZoom(18);            // 지도의 zoom 설정
    map.setCenter(location);    // 지도의 center 설정
    map.panTo(location);        // 지도 이동

    /// map event ///
    map.addListener('event_name', function(){
        // action
    });

    event_name : center_changed, click, ...

    /// map custom style ///
    url: https://developers.google.com/maps/documentation/javascript/examples/maptype-styled-simple?hl=ko

    /// marker ///
    var marker = new google.maps.Marker({
       position:        // marker의 위치
       map:             // marker의 map
       title:           // marker의 title
       label:           // marker의 label
    });
    marker.getPosition();       // marker의 position 가져오기
    marker.setMap(map);         // map에 marker를 추가, null일 경우 없어진다.
*/