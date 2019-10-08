//------- Individual Sample Metadata Info and Gauge Chart
function init(){
  var url_gender=`/gender`;
            Plotly.d3.json(url_gender, function(fig){
              console.log("total: "+Object.keys(fig.Perspectiva_SE_14_a\u00f1os).length);
              
              var sources = []
              for (var i = 0; i < Object.keys(fig.Perspectiva_SE_14_a\u00f1os).length; i++) {
                sources.push(fig.Perspectiva_SE_14_a\u00f1os[i]);
              }
            ​
              var targets = []
              for (var i = 0; i < Object.keys(fig.Opini\u00f3n_Situaci\u00f3n_Econ\u00f3mica).length; i++) {
                targets.push(10+fig.Opini\u00f3n_Situaci\u00f3n_Econ\u00f3mica[i]);
              }
            ​
              var values = []
              
              for (var i = 0; i < Object.keys(fig.Factor_Expansi\u00f3n).length; i++) {
                values.push(fig.Factor_Expansi\u00f3n[i]);
              }
            ​
              var colors = ["","rgb(125, 0, 0)","rgb(255, 0, 0)","rgb(255, 125, 0)","rgb(255, 255, 0)",
                           "rgb(255, 255, 0)","rgb(128, 128, 0)","rgb(0, 255, 0)","rgb(0, 128, 0)",
                           "rgb(0, 0, 255)","rgb(0, 0, 128)"]
            ​
              var color_path =[]
              for (var i = 0; i < Object.keys(fig.Link_color).length; i++) {
                color_path.push(fig.Link_color[i]);
              }
            ​
            ​
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
            ​
            var data = [data]
            ​
            var layout = {
              title: "Social Mobility",
              font: {
                size: 15
              }
            }
            ​
            Plotly.react('myDiv', data, layout, {showSendToCloud:true})
            });

}

// Initialize the dashboard
init();