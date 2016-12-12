var g_table;
var a_table;
$(function(){
    /* data table */

    /* application page */
    a_table = $('#waypointTable').DataTable();

    /* base station page */
    $('#station_table').DataTable();

    /* gallery page */
    g_table = $('#gallery_table').DataTable();

    /* result page */
    $('#static_table').DataTable();
})
