// button click

function imageClick(){
    pic_id = $('.pic_marking');
    console.log(pic_id);
    var pic = pic_data.filter(function(item, index, array){
        return item['id'] == pic_id;
    });
    console.log(pic);
}