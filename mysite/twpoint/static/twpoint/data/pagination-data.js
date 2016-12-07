var pic_url = '/picture'
var pic_count = 0;
var pic_data;

$(function(){
    $.getJSON(pic_url,function(p_json){
        pic_count = p_json.length;
        pic_data = p_json;
        var result = [];
        for(var i = 0; i < pic_count; i++){
            result.push(i);
        }
        var container = $('#pagination');
        var option = {
            dataSource: result,
            pageSize: 8,
            callback: function( source , pagination) {
                var html = "";
                $.each(source, function(index, item){
                    html += "<div class='col-sm-6 col-md-3' style='margin-top: 10px;'>\n\t";
                    html += "<div class='thumbnail pic_marking_" + pic_data[source[index]].id + "' >\n\t";
                    html += "<img src=/image?file="+pic_data[source[index]].path+"/"+pic_data[source[index]].name+" >\n";
                    html += "<div class='caption'>\n\t";
                    html += "<h5 class='page-header'>" + pic_data[source[index]].name + "</h5>\n\t";
                    html += "<p>";
                    html += "<a class='btn btn-info btn-lg btn-block' role='button' onclick='imageClick(";
                    html += pic_data[source[index]].id +")'>Select</a></p>\n</div>";
                    html += "\n</div>\n</div>";
                });
                container.prev().html(html);
            }
        };

        container.pagination(option);
    });
})


