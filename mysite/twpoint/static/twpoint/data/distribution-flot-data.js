$(function(){
    var dis_url = '/dataStatic';
    $.getJSON(dis_url, function(json){
        var data = [];
        var check = 0;
        var s_id;
        var sub_data = [];
        var location_drop = document.getElementById('location-drop');
        json.forEach(function(item){
            if(item.level == "1"){
                data.push({'label': item.name, "data": item.count });
                if(check < item.count){
                    check = item.count;
                    s_id = item.id;
                }
                CreateDropData(location_drop, item.name, item.id);
            }
        });
        json.forEach(function(item){
            if(item.pid == s_id){
                sub_data.push({'label':item.name, 'data': item.count});
            }
        });

        /* left */
        CreateFlotChart($("#flot-pie-chart"), data);
        CreateFlotChart($("#flot-pie-chart-detail"), sub_data);

        /* drop box click */
        $('.location_drop').click(function(){
            var l_id = this.id;
            sub_data = [];
            json.forEach(function(item){
                if(item.pid == l_id){
                    sub_data.push({'label':item.name, 'data': item.count});
                }
            });
            CreateFlotChart($("#flot-pie-chart-detail"), sub_data);
        });

    });
})

function CreateDropData(div, name, id){
    var li = document.createElement('li');
    var a = document.createElement('a');
    a.id = id;
    a.className = "location_drop";
    a.innerHTML = name;
    li.appendChild(a);
    div.appendChild(li);
}

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
};
/*

                            <ul class="dropdown-menu pull-right" role="menu">
                                <li>
                                    <a id="station_100">100m</a>
                                </li>
                                <li>
                                    <a id="station_300">300m</a>
                                </li>
                                <li>
                                    <a id="station_500">500m</a>
                                </li>
                                <li>
                                    <a id="station_delete">Delete</a>
                                </li>
                            </ul>

*/