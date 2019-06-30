d3.json("/data2_without_IS_MH").then((energy_data) => {

  function drawRegionsMap() {
    let spendersData = [['Country', 'Energy Consumption per Capita over GDP per Capita']];
    
    for (let i=0; i<energy_data.population.length; i++) {
      spendersData.push([energy_data.name[i], energy_data.little_big_spenders[i]]);
    }
    console.log(spendersData)
    let data = google.visualization.arrayToDataTable(spendersData);

    let options = {
      colorAxis: {colors: ['white', 'green']},
      backgroundColor: '#81d4fa',
      defaultColor: '#f5f5f5',
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
  let population_trace = {
    x: energy_data.name.slice(0,15),
    y: energy_data.little_big_spenders.slice(0,15),
    type: "bar"
  };

  let population_layout = {
    title: "Top 15 Energy Consumers",
    xaxis: { title: "Countries" },
    yaxis: { title: "Energy Consumption per Capita" }
  };

  Plotly.newPlot("chart1", [population_trace], population_layout);


  console.log(energy_data)
  // Scatter Plot
  var population_little_big_spenders = {
    x: energy_data.gdppc,
    y: energy_data.little_big_spenders,
    mode: "markers",
    type: "scatter",
    name: "big spenders",
    marker: {
      color: "#2077b4",
      symbol: "hexagram"
    }
  };

  let PE_layout = {
    title: "Big Spenders vs GDP per Capita",
    xaxis: { title: "GDP per Capita" },
    yaxis: { title: "Big Spenders" }
  };

  Plotly.newPlot("chart2", [population_little_big_spenders], PE_layout);

});
