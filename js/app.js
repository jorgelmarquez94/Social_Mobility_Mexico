//------- Individual Sample Metadata Info and Gauge Chart
function buildMetadata(sample){
    
  // //Gives the route for the sample selected
  var url_metadata=`/metadata/${sample}`;
  
  //------- Metadata Info
  d3.json(url_metadata).then(function(data){
      console.log(data.WFREQ);
      //console.log("Metadata ", url_metadata);

      // Select the panel with id of `#sample-metadata` to include info
      var sample_metadata=d3.select("#sample-metadata");
      
      // `.html("") to clear any existing metadata
      sample_metadata.html("")

      // `Object.entries` to add each key and value pair to the panel
      Object.entries(data).forEach(function([k,v]){
          var row = sample_metadata.append("p");
          row.text(`${k}:${v}`);
      });
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

// Initialize the dashboard
init();