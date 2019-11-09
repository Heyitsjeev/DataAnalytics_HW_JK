// Read in data
d3.csv("../StarterCode/assets/data/data.csv").then(function (data) {
    visualize(data);
});

var graph_width = parseInt(d3.select('#scatter').style("width"));
var graph_height = graph_width * 2 / 3;
var padding = 45;
var text_Area = 110;
var graph_margin = 10;

var radius;
function radiusSizes() {
    if (graph_width <= 530) {
        radius = 7;
    }
    else {
        radius = 10;
    }
}
radiusSizes();

function visualize(info) {
    // define svg
    var svg = d3.select("#scatter")
        .append("svg")
        .attr("width", graph_width)
        .attr("height", graph_height)
        .attr("class", "chart");

    svg.append("g").attr("class", "xText");

    var xaxis_text = d3.select(".xText");

    // Transform to text
    var xtext = (graph_width - text_Area) / 2 + text_Area;
    var ytext = graph_height - graph_margin - padding;
    xaxis_text.attr("transform", `translate(${xtext}, ${ytext})`);

    var x = "poverty";
    var y = "healthcare";

    //scaling variables 
    var xScale = d3.scaleLinear().domain(
        [d3.min(info, function (d) { return parseFloat(d[x]) * 0.85; }),
        d3.max(info, function (d) { return parseFloat(d[x]) * 1.15; })]).range([graph_margin + text_Area, graph_width - graph_margin])

    var yScale = d3.scaleLinear().domain(
        [d3.min(info, function (d) { return parseFloat(d[y]) * 0.85; }),
        d3.max(info, function (d) { return parseFloat(d[y]) * 1.15; })]).range([graph_height - graph_margin - text_Area, graph_margin])


    var xAxis = d3.axisBottom(xScale);
    var yAxis = d3.axisLeft(yScale);

    // append axis to the svg 
    svg.append("g")
        .call(xAxis)
        .attr("class", "xAxis")
        .attr("transform", `translate(0, ${graph_height - graph_margin - text_Area})`);

    svg.append("g")
        .call(yAxis)
        .attr("class", "yAxis")
        .attr("transform", `translate(${graph_margin + text_Area}, 0 )`);

    // circles for data
    var dots = svg.selectAll("g allCircles").data(info).enter();

    dots.append("circle")
        .attr("cx", function (c) {return xScale(c[x]);})
        .attr("cy", function (c) {return yScale(c[y]);})
        .attr("r", radius)
        .attr("class", function (c) {return "stateCircle " + c.abbr;});

    // display state abbrivs to the circles 
    dots.append("text")
        .attr("font-size", radius)
        .attr("class", "stateText")
        .attr("dx", function (c) {return xScale(c[x]);})
        .attr("dy", function (c) {return yScale(c[y]) + radius / 3;})
        .text(function (c) {return c.abbr;});

    svg.append("g").attr("class", "yText");
    var yText = d3.select(".yText");

    // Transform to adjust for yText
    var leftTextX = graph_margin + padding;
    var leftTextY = (graph_height + text_Area) / 2 - text_Area;

    yText.attr("transform", `translate(${leftTextX}, ${leftTextY})rotate(-90)`);

    xaxis_text.append("text")
        .attr("y", -19)
        .attr("data-name", "poverty")
        .attr("data-axis", "x")
        .text("In Poverty (%)");

    yText.append("text")
        .attr("y", 22)
        .attr("data-name", "healthcare")
        .attr("data-axis", "y")
        .text("Lacks Healthcare (%)");
}



