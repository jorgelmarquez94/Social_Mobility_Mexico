//------- Individual Sample Metadata Info and Gauge Chart
function getUrl() {
  cadena = window.location.href;
  url = cadena.replace("http://127.0.0.1:5000","");
  loadSankey(url);
}

/*function getUrlAgain(variable) {
  cadena = window.location.href;
  url = cadena.replace("http://127.0.0.1:5000","");
  buildSankey(url,variable);
}


function buildSankey(url,variable){
    
  // //Gives the route for the sample selected
  var url_variable=url+"/${variable}";
  
  Plotly.d3.json(url_variable, function(fig){
    console.log("total: "+Object.keys(fig.perspectiva_se_14_anios).length);

    var sources = []
      for (var i = 0; i < Object.keys(fig.perspectiva_se_14_anios).length; i++) {
        sources.push(fig.perspectiva_se_14_anios[i]);
      }

      var targets = []
      for (var i = 0; i < Object.keys(fig.opinion_situacion_economica).length; i++) {
        targets.push(10+fig.opinion_situacion_economica[i]);
      }

      var values = []

      for (var i = 0; i < Object.keys(fig.factor_expansion).length; i++) {
        values.push(fig.factor_expansion[i]);
      }

      var colors = ["","rgb(125, 0, 0)","rgb(255, 0, 0)","rgb(255, 125, 0)","rgb(255, 255, 0)",
                           "rgb(255, 255, 0)","rgb(128, 128, 0)","rgb(0, 255, 0)","rgb(0, 128, 0)",
                           "rgb(0, 0, 255)","rgb(0, 0, 128)"]

      var color_path =[]
      for (var i = 0; i < Object.keys(fig.Link_color).length; i++) {
        color_path.push(fig.Link_color[i]);
      }

      var data = {
        type: "sankey",
        orientation: "h",
        domain:{
          x:[0,1],
          y:[0,1]
        },
        node: {
          pad: 15,
          thickness: 15,
          line: {
            color: "black",
            width: 0.5
          },
          //Ruta a documento "data" en formato JSON
          label: ["",1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10],
          color: colors,
          font: 10
        },
        link: {
        //Ruta a documento "data" en formato JSON
        source:sources,
        target:targets,
        value:values,
        //Color of the link/path 
        color: color_path
        }
      }

      var data = [data]

      var layout = {
        title: "Social Mobility",
        font: {
          size: 15
        }
      }

      Plotly.react('myDiv', data, layout, {showSendToCloud:true})
    }
  );
}*/


function loadSankey(url){
  var url_final=url+"/getMyJson";
  Plotly.d3.json(url_final, function(fig){
    console.log("total: "+Object.keys(fig.perspectiva_se_14_anios).length);

    var sources = []
      for (var i = 0; i < Object.keys(fig.perspectiva_se_14_anios).length; i++) {
        sources.push(fig.perspectiva_se_14_anios[i]);
      }

      var targets = []
      for (var i = 0; i < Object.keys(fig.opinion_situacion_economica).length; i++) {
        targets.push(10+fig.opinion_situacion_economica[i]);
      }

      var values = []

      for (var i = 0; i < Object.keys(fig.factor_expansion).length; i++) {
        values.push(fig.factor_expansion[i]);
      }

      var colors = ["","rgb(125, 0, 0)","rgb(255, 0, 0)","rgb(255, 125, 0)","rgb(255, 255, 0)",
                           "rgb(255, 255, 0)","rgb(128, 128, 0)","rgb(0, 255, 0)","rgb(0, 128, 0)",
                           "rgb(0, 0, 255)","rgb(0, 0, 128)"]

      var color_path =[]
      for (var i = 0; i < Object.keys(fig.Link_color).length; i++) {
        color_path.push(fig.Link_color[i]);
      }

      var data = {
        type: "sankey",
        orientation: "h",
        domain:{
          x:[0,1],
          y:[0,1]
        },
        node: {
          pad: 15,
          thickness: 15,
          line: {
            color: "black",
            width: 0.5
          },
          //Ruta a documento "data" en formato JSON
          label: ["",1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10],
          color: colors,
          font: 10
        },
        link: {
        //Ruta a documento "data" en formato JSON
        source:sources,
        target:targets,
        value:values,
        //Color of the link/path 
        color: color_path
        }
      }

      var data = [data]

      var layout = {
        title: "Social Mobility",
        font: {
          size: 15
        }
      }

      Plotly.react('myDiv', data, layout, {showSendToCloud:true})
    }
  );
}


function init() {
  // Grab a reference to the dropdown select element
  /*var selector = d3.select("#selDataset");
  cadena = window.location.href;
  url = cadena.replace("http://127.0.0.1:5000","");

  // Use the list of sample names to populate the select options
  d3.json(url+"/getMyVariables").then((sampleNames) => {
    sampleNames.forEach((variable) => {
      selector
        .append("option")
        .text(variable)
        .property("value", variable);
    });
  });*/
  getUrl();
}



/*function optionChanged(newVariable) {
  // Fetch new data each time a new sample is selected
  getUrlAgain(newVariable);
}*/

// Initialize the dashboard
init();