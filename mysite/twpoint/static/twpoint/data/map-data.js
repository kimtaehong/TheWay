"use strict";
var app_id = location.href.split("result/")[1];     // 위치정보 app id
var way_url = '/waypoint/' + app_id;                // 위치 정보 url
var way_data = {};                                  // json 에서 얻어온 모든 위치 정보
var way_location = {};                              // 특정 위치정보에 위도, 경도
var way_point = {};                                 // 특정 위치정보
var app_map;
// lat = 위도 (37...) , lng = 경도 (127...)

$(function(){

    // map을 처음 그릴 때 center 값 설정

    // 위치 정보에서 첫 번째 데이터를 중심으로 선택
    way_point = way_data[0];

    // position, start & end, search 값 중 존재하는 값으로 저장
    if(way_point.position != null){
        way_location = {lat: way_point.position_y, lng: way_point.position_x };
    }
    else if(way_point.start != null){
        way_location = {lat: way_point.start_y, lng: way_point.start_x };
    }
    else if(way_point.search != null){
        way_location = {lat: way_point.search_y, lng: way_point.search_x };
    }

    // 위치 정보가 없으면 BOB 센터로 중심을 잡는다.
    if(way_location.lat == null){
        way_location.lat = 37.497518;
        way_location.lng = 127.029676;
    }

    // 맵 생성
    function initMap() {
        app_map = new google.maps.Map(document.getElementById('app_map'),{
            zoom: 18,
            center: way_location,
            scrollwheel: false,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            disableDefaultUI: true,
            scaleControl: true,
        });
    };



    /*
    ////////////////////////////////////////////
    // 시작시 첫 데이터 마킹
    // var waypoint = waypoints[Object.keys(waypoints)[0]];
    // var location = {lat: waypoint.latitude, lng: waypoint.longitude};
    // var locations = [];
    var markers = [];
    var marker, poly;

    // map
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 18,
        center: location,
        scrollwheel: false,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true,
        scaleControl: true,
    });

    // click, checked
    $(".marking").click(function(){
        if($(this).is(":checked")){
            waypoint = waypoints[this.id];
            location = {lat: waypoint.latitude, lng: waypoint.longitude };
            locations.push(location);

            marker = new google.maps.Marker({
                position: location,
                map: map,
            });
            markers[this.id] = marker;

            map.panTo(marker.getPosition());
        }
        else{
            waypoint = waypoints[this.id];
            location = {lat: waypoint.latitude, lng: waypoint.longitude };
            markers[this.id].setMap(null);
            locations.splice(location,1);
        }
    })
    */

    // Data Table
    $('#waypointTable').DataTable();

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