d3.json("/data1_without_IS_MH").then((energy_data) => {

  function drawRegionsMap() {
    let econsumptionData = [['Country', 'Energy Consumption per Capita']];

    for (let i=0; i<energy_data.econsumption.length; i++) {
      econsumptionData.push([energy_data.name[i], energy_data.econsumptionpc[i]]);
    }
    console.log(econsumptionData)
    let data = google.visualization.arrayToDataTable(econsumptionData);

    let options = {
      colorAxis: {colors: ['white', 'green']},
      backgroundColor: '#81d4fa',
      defaultColor: '#f5f5f5'
    };

    let chart = new google.visualization.GeoChart(document.getElementById('map'));

    chart.draw(data, options);
  }

  google.charts.load('current', {
    'packages':['geochart'],
    // Note: you will need to get a mapsApiKey for your project.
    // See: https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings
    'mapsApiKey': "AIzaSyANBI6Hih0SheCC1ICsciRp66qrNPveX9A"
  });

  google.charts.setOnLoadCallback(drawRegionsMap);

  // Bar Graph
  let econsumption_trace = {
    x: energy_data.name.slice(0,15),
    y: energy_data.econsumptionpc.slice(0,15),
    type: "bar"
  };

  let econsumption_layout = {
    title: "Top 15 Energy Consumers",
    xaxis: { title: "Countries" },
    yaxis: { title: "Energy Consumption per Capita" },
    height: 750
  };

  Plotly.newPlot("chart1", [econsumption_trace], econsumption_layout);


  // Scatter Plot
  var gdppc_econsumption = {
    x: energy_data.gdppc,
    y: energy_data.econsumptionpc,
    mode: "markers",
    type: "scatter",
    name: "energy consumers",
    marker: {
      color: "#2077b4",
      symbol: "hexagram"
    }
  };

  let PE_layout = {
    title: "Energy Consumption vs GDP per Capita",
    xaxis: { title: "GDP per Capita" },
    yaxis: { title: "Energy Consumption" },
    height: 750
  };

  Plotly.newPlot("chart2", [gdppc_econsumption], PE_layout);

});