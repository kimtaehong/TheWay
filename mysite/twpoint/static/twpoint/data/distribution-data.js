var way_url = '/waypoint';
var way_data = [];
var d_map;

$(function(){

    $.getJSON(way_url,function(w_json){
        way_data = w_json;
        d_map = new google.maps.Map(document.getElementById('d_map'),{
            zoom: 9,
            center: {lat: 37.497518, lng: 127.029676 },
            scrollwheel: false,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            disableDefaultUI: true,
            scaleControl: true,
            zoomControl: true,
        });


        var data = {
            type: "FeatureCollection",
            metadata: {
                title: "Way Location",
                api: "1.0.13",
                status: 200,
                count: 0,
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
        data.metadata.count = data.features.length;
        d_map.data.setStyle(function(feature) {
          var magnitude = 5;
          return {
            icon: getCircle(magnitude)
          };
        });
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

function getCircle(magnitude) {
        return {
          path: google.maps.SymbolPath.CIRCLE,
          fillColor: 'red',
          fillOpacity: 0.18,
          scale: Math.pow(2, magnitude) / 2,
          strokeColor: 'white',
          strokeWeight: .5
        };
      }