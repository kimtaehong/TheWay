//Flot Pie Chart

var app_url = "/application";
var way_url = "/waypoint";

var app_data = [] , way_count = 0;
var data = [];

$(function() {
    $.getJSON(way_url,function(w_json){
        for(i=0;i<app_data.length;i++){
            var new_json = w_json.filter(function(item,index,array){
                return item['app_name_id'] == app_data[i]['id'];
            });
            way_count = new_json.length;
            data.push({'label': app_data[i]["app_name"], "data": way_count});
        }
        var plotObj = $.plot($("#flot-pie-chart"), data, {
            series: {
                pie: {
                    show: true
                }
            },
            grid: {
                hoverable: true
            },
            tooltip: true,
            tooltipOpts: {
                content: "%p.0%, %s", // show percentages, rounding to 2 decimal places
                shifts: {
                    x: 20,
                    y: 0
                },
                defaultTheme: false
            }
        });
    });
});

$.getJSON(app_url,function(a_json){
    for(i=0; i<a_json.length; i++){
        app_data.push({'id': a_json[i].id, 'app_name': a_json[i].app_name});
    }
});







