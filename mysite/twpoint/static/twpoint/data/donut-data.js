$(function(){
    var pic_url = '/picture';
    var bs_url = '/basestation';
    var pic_count = 0, bs_count = 0;
    $.getJSON(pic_url,function(p_json){
        pic_count = p_json.length;

        $.getJSON(bs_url, function(b_json){
            bs_count = b_json.length;

            var donut_data = {
                element: "data-donut-chart",
                data: [],
                resize: true,
            };
            var data = [];

            data.push({label: "Application Location Data", value: way_count});
            data.push({label: "Picture Location Data", value: pic_count});
            if( bs_count != 0 ){
                data.push({label: "Base Station Location Data", value: pic_count});
            }

            donut_data.data = data;

            Morris.Donut(donut_data);
        });
    });
})