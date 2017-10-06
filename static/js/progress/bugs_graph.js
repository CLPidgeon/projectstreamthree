queue()
    .defer(d3.json, "/progress/bug")
    .await(makeGraphs);

function makeGraphs(error, bugJson) {
    var BugData = bugJson;

    BugData.forEach(function(d){
        d["updated"] = new Date(d["updated"]);
        d["status"] = d["status"];
    });

    // creating Crossfilter instance
    var ndx = crossfilter(BugData);

    // defining the data dimensions
    var dateDim = ndx.dimension(function(d){
        return d["updated"];
    });
    var statusDim = ndx.dimension(function(d){
        return d["status"];
    });

    var statustypeDim = ndx.dimension(function(d){
        var type = d["status"];
        if (type === "done") {
            return "Done";
        } if (type === "doing") {
            return "Doing";
        } if (type === "todo") {
            return "ToDo";
        }
    });

    // grouping data

    var numbyDate = dateDim.group();
    var numbyStatus = statusDim.group();
    var statustypeGroup = statustypeDim.group().reduceCount();

    // calculating dates
    var minDate = dateDim.bottom(1)[0]["updated"];
    var maxDate = dateDim.top(1)[0]["updated"];

    console.log(minDate);
    console.log(maxDate);

    // defining the charts
    var yearlyChart = dc.barChart("#yearlyChart");
    var statusChart = dc.rowChart("#statusChart");

    // creating the charts
    yearlyChart
        .width(300)
        .height(200)
        .dimension(dateDim)
        .group(numbyDate)
        .x(d3.time.scale().domain([minDate, maxDate]))
        .elasticY(true)
        .brushOn(false)
        .xAxisLabel("Year")
        .yAxis().ticks(4);

    statusChart
        .width(300)
        .height(200)
        .dimension(statusDim)
        .group(numbyStatus)
        .xAxis().ticks(4);

    dc.renderAll();
}