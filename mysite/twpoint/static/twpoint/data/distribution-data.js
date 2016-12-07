var way_url = '/waypoint';
var way_data = [];
var d_map;

$(function(){

    $.getJSON(way_url,function(w_json){
        way_data = w_json;
        d_map = new google.maps.Map(document.getElementById('d_map'),{
            zoom: 8,
            center: {lat: 37.497518, lng: 127.029676 },
            scrollwheel: false,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            disableDefaultUI: true,
            scaleControl: true,
        });


        var data = {
            type: "FeatureCollection",
            metadata: {
                title: "Way Location",
                api:"1.0.13",
                "status":200,
            },
            features:[],
            bbox: [
                32.047978,
                132.160925,
                -3,
                38.538825,
                132.015932,
                609.13
            ]
        };
        var feature = createFeature();
        for ( var i=0; i<way_data.length; i++) {
            if(way_data[i].position != null && way_data[i].position_x != null && way_data[i].position_y != null){
                feature.geometry.coordinates.push(Number(way_data[i].position_x));
                feature.geometry.coordinates.push(Number(way_data[i].position_y));
                feature.geometry.coordinates.push(7);

                feature.id = way_data[i].id;
                data.features.push(feature);
                feature = createFeature();
            }
            else if(way_data[i].start != null && way_data[i].start_x != null && way_data[i].start_y != null){
                feature.geometry.coordinates.push(Number(way_data[i].start_x));
                feature.geometry.coordinates.push(Number(way_data[i].start_y));
                feature.geometry.coordinates.push(7);

                feature.id = way_data[i].id;
                data.features.push(feature);
                feature = createFeature();
            }
            else if(way_data[i].search != null && way_data[i].search_x != null && way_data[i].search_y != null){
                feature.geometry.coordinates.push(Number(way_data[i].search_x));
                feature.geometry.coordinates.push(Number(way_data[i].search_y));
                feature.geometry.coordinates.push(7);

                feature.id = way_data[i].id;
                data.features.push(feature);
                feature = createFeature();
            }
        }
        d_map.data.addGeoJson(data);

  });
})

function createFeature(){
    return {
        type: "Feature",
        geometry: {
            type: "Point",
            coordinates:[
            ]
        },
        id: "",
    };
}