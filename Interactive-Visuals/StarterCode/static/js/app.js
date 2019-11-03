function buildMetadata(sample) {
  // getting the metadata for a certain sample 
    d3.json(`/metadata/${sample}`).then((data) => {
        var slot = d3.select("#sample-metadata");
        slot.html("");
        // using entries to add key value pairs to the display slot
        Object.entries(data).forEach(([key, value]) => {
          slot.append("p").text(`${key}:${value}`);
        })
    })
}

function buildCharts(sample) {

  //Use d3 to fetch the sample data for the plots
    var url = "/samples/" + sample;
    d3.json(url).then(function(responseInfo) {

      var sampleValues = [];
      var sampleOtuIds   = [];
      var sampleOtuLabels = [];
      var size = responseInfo.sample_values.length;
      var index = new Array(size);

      for (var i = 0; i < size; i++) {
        index[i] = i;
        index.sort(function (key, value) { 
          return responseInfo.sample_values[key] < responseInfo.sample_values[value] ? 1 : responseInfo.sample_values[key] > responseInfo.sample_values[value] ? -1 : 0; });
      } 

      //getting the top 10 of each
      for (var j =0; j<10; j++){
        var k = index[j];
        sampleValues.push(responseInfo.sample_values[k]);
        sampleOtuIds.push(responseInfo.otu_ids[k]);
        sampleOtuLabels.push(responseInfo.otu_labels[k]);
      }
    
      //plot pie chart
      var pieChart = [{
        type: "pie",
        values: sampleValues,
        labels: sampleOtuIds.map(String),
        text: sampleOtuLabels,
        textinfo: "percent"
      }];
      var pieLayout = {
        height: 500,
        width: 500
      };
      Plotly.newPlot("pie", pieChart, pieLayout);

      //plot bubble chart
      var bubbleChart = [{
        x: responseInfo.otu_ids,
        y: responseInfo.sample_values,
        text: responseInfo.otu_labels,
        mode: "markers",
        marker: {
          color:responseInfo.otu_ids,
          size: responseInfo.sample_values
        }
      }];
      var bubbleLayout = {
        showlegend: true,
        height: 600,
        width: 1400
      };
      Plotly.newPlot("bubble", bubbleChart, bubbleLayout);
    });
 
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
