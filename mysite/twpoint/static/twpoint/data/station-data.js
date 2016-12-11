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

var x=500;
$(function(){
        function CenterControl(controlDiv, bs_map) {
      // Set CSS for the control border.
      var controlUI = document.createElement('div');
      controlUI.style.backgroundColor = '#fff';
      controlUI.style.border = '2px solid #fff';
      controlUI.style.float = 'left';
      controlUI.style.borderRadius = '3px';
      controlUI.style.boxShadow = '0 2px 6px rgba(0,0,0,.3)';
      controlUI.style.cursor = 'pointer';
      controlUI.style.marginBottom = '22px';
      controlUI.style.textAlign = 'center';
      controlUI.title = 'Click to recenter the map';
      controlDiv.appendChild(controlUI);

      // Set CSS for the control interior.
      var controlText = document.createElement('div');
      controlText.style.color = 'rgb(25,25,25)';
      controlText.style.fontFamily = 'Roboto,Arial,sans-serif';
      controlText.style.fontSize = '16px';
      controlText.style.lineHeight = '38px';
      controlText.style.paddingLeft = '5px';
      controlText.style.paddingRight = '5px';
      controlText.innerHTML = '100m';
      controlUI.appendChild(controlText);

      var controlUI2 = document.createElement('div');
      controlUI2.style.backgroundColor = '#fff';
      controlUI2.style.border = '2px solid #fff';
      controlUI2.style.borderRadius = '3px';
      controlUI2.style.float = 'left';
      controlUI2.style.boxShadow = '0 2px 6px rgba(0,0,0,.3)';
      controlUI2.style.cursor = 'pointer';
      controlUI2.style.marginBottom = '22px';
      controlUI2.style.textAlign = 'center';
      controlUI2.title = 'Click to recenter the map';
      controlDiv.appendChild(controlUI2);

      // Set CSS for the control interior.
      var controlText2 = document.createElement('div');
      controlText2.style.color = 'rgb(25,25,25)';
      controlText2.style.fontFamily = 'Roboto,Arial,sans-serif';
      controlText2.style.fontSize = '16px';
      controlText2.style.lineHeight = '38px';
      controlText2.style.paddingLeft = '5px';
      controlText2.style.paddingRight = '5px';
      controlText2.innerHTML = '300m';
      controlUI2.appendChild(controlText2);

      var controlUI3 = document.createElement('div');
      controlUI3.style.backgroundColor = '#fff';
      controlUI3.style.border = '2px solid #fff';
      controlUI3.style.borderRadius = '3px';
      controlUI3.style.float = 'left';
      controlUI3.style.boxShadow = '0 2px 6px rgba(0,0,0,.3)';
      controlUI3.style.cursor = 'pointer';
      controlUI3.style.marginBottom = '22px';
      controlUI3.style.textAlign = 'center';
      controlUI3.title = 'Click to recenter the map';
      controlDiv.appendChild(controlUI3);

      // Set CSS for the control interior.
      var controlText3 = document.createElement('div');
      controlText3.style.color = 'rgb(25,25,25)';
      controlText3.style.fontFamily = 'Roboto,Arial,sans-serif';
      controlText3.style.fontSize = '16px';
      controlText3.style.lineHeight = '38px';
      controlText3.style.paddingLeft = '5px';
      controlText3.style.paddingRight = '5px';
      controlText3.innerHTML = '500m';
      controlUI3.appendChild(controlText3);

      // Setup the click event listeners: simply set the map to Chicago.
      controlUI.addEventListener('click', function() {
       x=100;
      });
      controlUI2.addEventListener('click', function() {
       x=300;
      });
      controlUI3.addEventListener('click', function() {
       x=500;
      });
    }


    // 맵 생성
    bs_map = new google.maps.Map(document.getElementById('bs_map'),{
        zoom: 18,
        center: {lat: 37.497518, lng: 127.029676 },
        scrollwheel: true,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true,
        scaleControl: true,
    });
    var centerControlDiv = document.createElement('div');
    var centerControl = new CenterControl(centerControlDiv, bs_map);

    centerControlDiv.index = 2;
    centerControlDiv.style['padding-top'] = '10px';
    bs_map.controls[google.maps.ControlPosition.TOP_CENTER].push(centerControlDiv);

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
               fillColor: '#ff8333',
               fillOpacity: 0.3,
               strokeColor: '#ff0000',
               strokeOpacity: 0,
               strokeWeight: 0,
               radius: x// 50 MILES in meters
            });
            circle.bindTo('center', marker , 'position');
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