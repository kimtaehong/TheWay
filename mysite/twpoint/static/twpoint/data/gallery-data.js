
var gallery_map;
var pic_location;
var marker;
var markers = [];

$(function(){
    gallery_map = new google.maps.Map(document.getElementById('gallery_map'),{
        zoom: 18,
        center: {lat: 37.497518, lng: 127.029676 },
        scrollwheel: false,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true,
        scaleControl: true,
    });

    // checkbox check
    $(".g_check").click(function(){
        if($(this).is(":checked")){
            var id = Number(this.id);
            var pic = pic_data.filter(function(item, index, array){
                return item['id'] == id;
            });
            /* photo info change */
            var pic_info = $('#pic_info');
            var pic_img = pic_info.children()[0];
            var pic_caption = pic_info.children()[1];
            var src = "/image?file="+pic[0].path+"/"+pic[0].name;
            pic_img.src = src;
            var html = "<h5 class='page-header'>"+pic[0].name+"</h5>";
            html += "<h5> Device :" + pic[0].device + "</h5>\t";
            html += "<h5> Latitude :" + pic[0].lat + "</h5>\t";
            html += "<h5> Longitude :" + pic[0].lng + "</h5>\t";
            html += "<h5> Path: " + pic[0].path + "</h5>\t";
            html += "<h5> MD5: " + pic[0].md5 + "</h5>\t";
            html += "<h5> SHA1: " + pic[0].sha1 + "</h5>\t";
            pic_caption.innerHTML = html;

            /* marking */
            pic_location = { lat: Number(pic[0].lat), lng: Number(pic[0].lng)};
            marker = new google.maps.Marker({
                position: pic_location,
                map: gallery_map,
            });

            markers[pic[0].id] = marker;
            gallery_map.panTo(marker.getPosition());
        }
        else{
            markers[this.id].setMap(null);
        }
    });
})

// button click
function imageClick(id){

    var pic = pic_data.filter(function(item, index, array){
        return item['id'] == id;
    });

    /* photo info change */
    var pic_info = $('#pic_info');
    var pic_img = pic_info.children()[0];
    var pic_caption = pic_info.children()[1];
    var src = "/image?file="+pic[0].path+"/"+pic[0].name;
    pic_img.src = src;
    var html = "<h5 class='page-header'>"+pic[0].name+"</h5>";
    html += "<h5> Device :" + pic[0].device + "</h5>\t";
    html += "<h5> Latitude :" + pic[0].lat + "</h5>\t";
    html += "<h5> Longitude :" + pic[0].lng + "</h5>\t";
    html += "<h5> Path: " + pic[0].path + "</h5>\t";
    html += "<h5> MD5: " + pic[0].md5 + "</h5>\t";
    html += "<h5> SHA1: " + pic[0].sha1 + "</h5>\t";
    pic_caption.innerHTML = html;

    /* marking */
    pic_location = { lat: Number(pic[0].lat), lng: Number(pic[0].lng)};
    marker = new google.maps.Marker({
        position: pic_location,
        map: gallery_map,
    });

    markers[pic[0].id] = marker;
    gallery_map.panTo(marker.getPosition());
}

