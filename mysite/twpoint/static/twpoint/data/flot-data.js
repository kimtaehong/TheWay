//Flot Pie Chart
$(function() {
    var app_url = "/application";
    var way_url = "/waypoint";
    var app_data = [];
    var w_count = 0;

    /* application json */
    $.getJSON(app_url, function(a_json){
        a_json.forEach(function(item){
            app_data.push({'id': item.id, 'app_name': item.app_name});
        });
        /* way point json */
        $.getJSON(way_url, function(w_json){
            var way_count = 0;
            var data = [];
            app_data.forEach(function(item){
                var new_json = w_json.filter(function(w_item){
                    return w_item.app_name_id == item.id;
                });

                way_count = new_json.length;
                data.push({'label': item.app_name, "data": way_count});
            });
            w_count = w_json.length;
            CreateFlotChart($('#flot-pie-chart'), data);

            var pic_url = '/picture';
            var bs_url = '/basestation';
            var pic_count = 0, bs_count = 0;

            /* picture json */
            $.getJSON(pic_url,function(p_json){
                pic_count = p_json.length;
                /* base station json */
                $.getJSON(bs_url, function(b_json){
                    bs_count = b_json.length;

                    var donut_data = {
                        element: "data-donut-chart",
                        data: [],
                        resize: true,
                    };
                    var data = [];

                    data.push({label: "Application Location Data", value: w_count});
                    data.push({label: "Picture Location Data", value: pic_count});
                    if( bs_count != 0 ){
                        data.push({label: "Base Station Data", value: pic_count});
                    }

                    donut_data.data = data;
                    
                    Morris.Donut(donut_data);
                });
            });
        });
    })
});

function CreateFlotChart(div, data){
    var plotObj = $.plot(div, data, {
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
}




