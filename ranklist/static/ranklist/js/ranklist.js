$('#listBtn').click(function(){
    var margin = {top: 5, right: 15, bottom: 20, left: 115},
    //width = 960 - margin.left - margin.right,
        width = $('#contents').empty().width() - margin.left - margin.right,
        height = 50 - margin.top - margin.bottom;

    var chart = d3.bullet()
        .width(width)
        .height(height);

    d3.json("../project_static/ranklist/js/bullets/bullets.json", function(error, data) {
        var svg = d3.select("#contents").selectAll("svg")
            .data(data)
            .enter().append("svg")
            .attr("class", "bullet")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
            .call(chart);

        var title = svg.append("g")
            .style("text-anchor", "end")
            .attr("transform", "translate(-6," + height / 2 + ")");

        title.append("text")
            .attr("class", "title")
            .text(function(d) { return d.title; });

        title.append("text")
            .attr("class", "subtitle")
            .attr("dy", "1em")
            .text(function(d) { return d.subtitle; });
    });
});

function change_list() {
    $('#listContents').empty();
    var pickerTime = $('#datepicker').datepicker("getDate");
    var pickerYear = pickerTime.getFullYear();
    var pickerMonth = pickerTime.getMonth(); //getMonth (from 0-11)
    var pickerDate = pickerTime.getDate();
    var daylist = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];

    if(page === "months"){
        if(pickerYear < year){
            for(var i = 12; i > 0; i--) {
                $('#listContents').append("<button type='button' class='btn btn-info-width'>" + i + "</button><br>");
            }
        }else if(pickerYear === year){
            for(var i = month; i > 0; i--) {
                $('#listContents').append("<button type='button' class='btn btn-info-width'>" + i + "</button><br>");
            }
        }else{

        }
    }else if(page === "days"){
        if((pickerYear < year) || (pickerYear === year && pickerMonth < (month-1))){
            var monthFinalTime = new Date(pickerYear, pickerMonth+1, pickerDate-1);
            var monthFinalDate = monthFinalTime.getDate();
            var monthFinalDay = monthFinalTime.getDay(); //getDay (from 0-6), (from SUN-SAT)

            for(var i = monthFinalDate; i > 0; i--) {
                $('#listContents').append("<button type='button' class='btn btn-info-width'>" + i + " " + daylist[monthFinalDay] + "</button>");
                monthFinalDay -= 1;
                if(monthFinalDay === -1){
                    monthFinalDay = 6;
                }
            }
        }else if(pickerYear === year && pickerMonth === (month-1)){
            var todayDay = new Date(pickerYear, pickerMonth, date).getDay();

            for(var i = date; i > 0; i--) {
                $('#listContents').append("<button type='button' class='btn btn-info-width'>" + i + " " + daylist[todayDay] + "</button>");
                todayDay -= 1;
                if(todayDay === -1){
                    todayDay = 6;
                }
            }
        }else{

        }
    }else if(page === "hours"){
        if((pickerYear < year) || (pickerYear === year && pickerMonth < (month-1)) || (pickerYear === year && pickerMonth === (month-1) && pickerDate < date)){
            for(var i = 23; i >= 0; i--) {
                $('#listContents').append("<button type='button' class='btn btn-info-width'>" + i + " : 00</button>");
            }
        }else if(pickerYear === year && pickerMonth === (month-1) || pickerDate === date){
            for(var i = hour; i >= 0; i--) {
                $('#listContents').append("<button type='button' class='btn btn-info-width'>" + i + " : 00</button>");
            }
        }else{

        }
    }
};
