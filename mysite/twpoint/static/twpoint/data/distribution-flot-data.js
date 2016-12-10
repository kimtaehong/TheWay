$(function(){
    var dis_url = '/dataStatic';
    $.getJSON(dis_url, function(json){
        var data = [];
        json.forEach(function(item, index, array){
            if(item.level == "1"){
                data.push({'label': item.name, "data": item.count });
            }
        });
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
})