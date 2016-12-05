"use strict";
var app_id = location.href.split("result/")[1];     // 위치정보 app id
var way_url = '/waypoint/' + app_id;                // 위치 정보 url
var way_data = {};                                  // json 에서 얻어온 모든 위치 정보
var way_location;                                   // 특정 위치정보에 위도, 경도
var way_name = "None";
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
            var id = Number(this.id);
            way_point = way_data.filter(function(item, index, array){
                return item['id'] == id;
            });

            if(way_point[0] == null){
                MyAlert("Way Point is None");
                $(this)[0].checked = false;
                return;
            }

            if(way_point[0].position != null || way_point[0].position_x != null && way_point[0].position_y != null){
                console.log('position');
                way_name = way_point[0].position;
                way_location = {lat: Number(way_point[0].position_y), lng: Number(way_point[0].position_x) };
            }
            else if(way_point[0].start != null || way_point[0].start_x != null && way_point[0].start_y !=null){
                consoel.log('start');
                way_name = way_point[0].start;
                way_location = {lat: Number(way_point[0].start_y), lng: Number(way_point[0].start_x) };
            }
            else if(way_point[0].search != null && way_point[0].search_x != null && way_point[0].search_y != null){
                console.log('search');
                way_name = way_point[0].search;
                way_location = {lat: Number(way_point[0].search_y), lng: Number(way_point[0].search_x) };
            }

            if(way_location == null || way_location.lat == 0 && way_location.lng == 0){
                MyAlert("Location Data is None");
                $(this)[0].checked = false;
                return;
            }
            /* add custom control */
            if($('.location_info').length == 0){
                var ctrlDiv = document.createElement('div');
                ctrlDiv.className = "location_info";
                CreateControl(ctrlDiv, way_name, way_location.lat, way_location.lng);
                ctrlDiv.index = 1;
                app_map.controls[google.maps.ControlPosition.TOP_LEFT].push(ctrlDiv);
            }
            else{
                /* update custom control */
                UpdateControl($('.location_text')[0], way_name, way_location.lat, way_location.lng);
            }

            /* marking*/
            marker = new google.maps.Marker({
                position: way_location,
                map: app_map,
            });
            markers[this.id] = marker;
            app_map.panTo(marker.getPosition());

            way_location = null;
        }
        else{
            if($('.location_info').length != 0){
                DeleteControl($('.location_info')[0]);
            }
            markers[this.id].setMap(null);
        }
    })
})

$.getJSON(way_url,function(w_json){
    way_data = w_json;
});

function CreateControl( ctrlDiv, name, lat, lng){
    var ctrlUI = document.createElement('div');
    ctrlUI.className = "location_ui";
    ctrlUI.style.backgroundColor = '#fff';
    ctrlUI.style.border = '2px solid #fff';
    ctrlUI.style.borderRadius = '3px';
    ctrlUI.style.boxShadow = '0 2px 6px rgba(0,0,0,.5)';
    ctrlUI.style.marginTop = '3px';
    ctrlUI.style.marginLeft = '3px';

    ctrlDiv.appendChild(ctrlUI);

    var ctrlText = document.createElement('div');
    ctrlText.className = "location_text";
    ctrlText.style.paddingLeft = '5px';
    ctrlText.style.paddingRight = '5px';

    var html ="<h4>Name: "+ name +"</h4>";
    html += "<h5>Latitude: "+lat+"</h5>";
    html += "<h5>Longitude: "+lng+"</h5>";

    ctrlText.innerHTML = html;
    ctrlUI.appendChild(ctrlText);
}

function DeleteControl(ctrlDiv){
    app_map.controls[google.maps.ControlPosition.TOP_LEFT].pop(ctrlDiv);
}

function UpdateControl( ctrlText, name, lat, lng){
    ctrlText.innerHTML = '';

    var html ="<h4>Name: "+ name +"</h4>";
    html += "<h5>Latitude: "+lat+"</h5>";
    html += "<h5>Longitude: "+lng+"</h5>";

    ctrlText.innerHTML = html;
}

function MyAlert(msg){
    var alert_html = "";
    alert_html += "<div class='alert alert-danger alert-dismissable' role='alert'>\t\n";
    alert_html += "<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;</button>";
    alert_html += msg;
    alert_html += "</div>";

    $('.myAlert')[0].innerHTML = alert_html;
}

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