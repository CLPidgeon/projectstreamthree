queue()
    .defer(d3.json, "/progress/feature")
    .await(makeGraphs);

function makeGraphs(error, featureJson, bugJson) {
    var FeatureData = featureJson;
    var dateFormat = d3.time.format("%Y-%m-%d");
    FeatureData.forEach(function(d) {
        d["updated"] = dateFormat.parse(String(d["updated"]));
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

    // calculating dates
    var minDate = dateDim.bottom(1)[0]["updated"];
    var maxDate = dateDim.top(1)[0]["updated"];

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

    console.log(minDate);
    console.log(maxDate);

    dc.renderAll();
}