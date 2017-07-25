queue()
    .defer(d3.json, "/progress/feature", "/progress/bug")
    .await(makeGraphs);

function makeGraphs(error, featureJson, bugJson) {
    var FeatureData = featureJson;
    var BugData = bugJson;
    var dateFormat = d3.time.format("%Y-%m-%d");
    FeatureData.forEach(function(d) {
        d["updated"] = dateFormat.parse(String(d["updated"]));
        d["status"] = d["feature_status"];
    });

    BugData.forEach(function(d){
        d["updated"] = dateFormat.parse(String(d["updated"]));
        d["bug_status"] = d["status"];
    });

    // creating Crossfilter instance
    var ndx = crossfilter(FeatureData);

    // defining the data dimensions
    var dateDim = ndx.dimension(function(d){
        return d["updated"];
    });
    var feature_statusDim = ndx.dimension(function(d){
        return d["feature_status"];
    });

    var bug_statusDim = ndx.dimension(function(d){
        return d["bug_status"];
    });

    // grouping data

    var numbyDate = dateDim.group();
    var FeaturenumbyStatus = feature_statusDim.group();
    var BugnumbyStatus = bug_statusDim.group();

    // calculating dates
    var minDate = dateDim.bottom(1)[0]["updated"];
    var maxDate = dateDim.top(1)[0]["updated"];

    // defining the charts
    var FeatureyearlyChart = dc.barChart("#FeatureyearlyChart");
    var FeaturestatusChart = dc.rowChart("#FeaturestatusChart");
    var BugyearlyChart = dc.barChart("#BugyearlyChart");
    var BugstatusChart = dc.rowChart("#BugstatusChart");

    // creating the charts
    FeatureyearlyChart
        .width(300)
        .height(200)
        .dimension(dateDim)
        .group(numbyDate)
        .x(d3.time.scale().domain([minDate, maxDate]))
        .elasticY(true)
        .brushOn(false)
        .xAxisLabel("Year")
        .yAxis().ticks(4);

    FeaturestatusChart
        .width(300)
        .height(200)
        .dimension(feature_statusDim)
        .group(FeaturenumbyStatus)
        .xAxis().ticks(4);

    BugyearlyChart
        .width(300)
        .height(200)
        .dimension(dateDim)
        .group(numbyDate)
        .x(d3.time.scale().domain([minDate, maxDate]))
        .elasticY(true)
        .brushOn(false)
        .xAxisLabel("Year")
        .yAxis().ticks(4);

    BugstatusChart
        .width(300)
        .height(200)
        .dimension(bug_statusDim)
        .group(BugnumbyStatus)
        .xAxis().ticks(4);

    console.log(minDate);
    console.log(maxDate);

    dc.renderAll();
}