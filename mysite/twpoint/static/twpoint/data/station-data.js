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
        zoom: 15,
        center: {lat: 37.497518, lng: 127.029676 },
        scrollwheel: false,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true,
        scaleControl: true,
        zoomControl: true,
    });

    $(".s_check").click(function(){
        if($(this).is(":checked")){
            var id = Number(this.id);
            bs_point = bs_data.filter(function(item, index, array){
                return item['id'] == id;
            });

            bs_location = {lat: bs_point[0].lat, lng: bs_point[0].lng };

            marker = new google.maps.Marker({
                position: bs_location,
                map: bs_map,
                icon:{
                    url: '/static/twpoint/img/base_station_icon.png',
                    scaledSize: new google.maps.Size(50,50),
                }
            });

            circle = new google.maps.Circle({
               map: bs_map,
               fillColor: '#ff0000',
               fillOpacity: 0.3,
               strokeColor: '#ff0000',
               strokeOpacity: 1.0,
               strokeWeight: 1.5,
               radius: 500,
               center: bs_location,
            });

            markers[this.id] = marker;
            circles[this.id] = circle;
            bs_map.panTo(marker.getPosition());
        }
        else{
            markers[this.id].setMap(null);
            circles[this.id].setMap(null);
        }
    });
})

$.getJSON(bs_url,function(b_json){
    bs_data = b_json;
});
