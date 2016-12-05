
var gallery_map;

$(function(){
    gallery_map = new google.maps.Map(document.getElementById('gallery_map'),{
        zoom: 18,
        center: {lat: 37.497518, lng: 127.029676 },
        scrollwheel: false,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true,
        scaleControl: true,
    });


})

// button click
function imageClick(id){
    var pic = pic_data.filter(function(item, index, array){
        return item['id'] == id;
    });

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
}

