var way_url = '/waypoint';
var way_data = [];
var d_map;

$(function(){
    $.getJSON(way_url,function(w_json){
        way_data = w_json;
        /* create map */
        d_map = new google.maps.Map(document.getElementById('d_map'),{
            zoom: 10,
            center: {lat: 37.497518, lng: 127.029676 },
            scrollwheel: false,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            disableDefaultUI: true,
            scaleControl: true,
            zoomControl: true,
        });

        var locations = [];

        /* sort location */
        way_data.forEach(function(item, index, array){
            var location;
            if(item.position != null && item.position_x != null && item.position_y != null){
                location = {lat: Number(item.position_y), lng: Number(item.position_x)};
                locations.push(location);
            } else if (item.start != null && item.start_x != null && item.start_y != null){
                location = {lat: Number(item.start_y), lng: Number(item.start_x)};
                locations.push(location);
            } else if (item.search != null && item.search_x != null && item.search_y != null){
                location = {lat: Number(item.search_y), lng: Number(item.search_x)};
                locations.push(location);
            }
        });

        /* create marker */
        var markers = locations.map(function(location) {
            return new google.maps.Marker({
                position: location,
            });
        });

        /* marker cluster */
        var markerCluster = new MarkerClusterer(d_map, markers,
                {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'}
            );
  });
})
