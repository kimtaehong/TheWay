$(function(){
    var dis_url = '/dataStatic';
    $.getJSON(dis_url, function(json){
        var data = [];
        var check = 0;
        var s_id;
        var sub_data = [];
        json.forEach(function(item){
            if(item.level == "1"){
                data.push({'label': item.name, "data": item.count });
                if(check < item.count){
                    check = item.count;
                    s_id = item.id;
                }
            }
        });
        json.forEach(function(item, index, array){
            if(item.pid == s_id){
                sub_data.push({'label':item.name, 'data': item.count});
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
        var plotObj_detail = $.plot($("#flot-pie-chart-detail"), sub_data, {
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