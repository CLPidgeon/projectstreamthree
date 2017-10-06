queue()
    .defer(d3.json, "/progress/feature")
    .await(makeGraphs);

function makeGraphs(error, featureJson) {
    var FeatureData = featureJson;

    FeatureData.forEach(function(d) {
        d["updated"] = new Date(d["updated"]);
        d["status"] = d["status"];
    });

    // creating Crossfilter instance
    var ndx = crossfilter(FeatureData);

    // defining the data dimensions
    var dateDim = ndx.dimension(function(d){
        return d["updated"];
    });
    var statusDim = ndx.dimension(function(d){
        return d["status"];
    });

    // grouping data
    var numbyDate = dateDim.group();
    var numbyStatus = statusDim.group();

    console.log(numbyDate);

    // calculating dates
    var minDate = dateDim.bottom(1)[0]["updated"];
    var maxDate = dateDim.top(1)[0]["updated"];

    console.log(minDate);
    console.log(maxDate);

    // defining the charts
    var yearlyChart = dc.rowChart("#yearlyChart");
    var statusChart = dc.rowChart("#statusChart");

    // creating the charts
    yearlyChart
        .width(300)
        .height(200)
        .dimension(dateDim)
        .group(numbyDate)
        .xAxis().ticks(4);

    statusChart
        .width(300)
        .height(200)
        .dimension(statusDim)
        .group(numbyStatus)
        .xAxis().ticks(4);

    dc.renderAll();
}