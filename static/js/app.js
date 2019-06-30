d3.json("/data").then((energy_data) => {

  function drawRegionsMap() {
    let populationData = [['Country', 'Population']];
    
    for (let i=0; i<energy_data.population.length; i++) {
      populationData.push([energy_data.name[i], energy_data.population[i]]);
    }
    console.log(populationData)
    let data = google.visualization.arrayToDataTable(populationData);

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
    'mapsApiKey': "Add API key here"
  });

  google.charts.setOnLoadCallback(drawRegionsMap);

  // Bar Graph
  let population_trace = {
    x: energy_data.name.slice(0,10),
    y: energy_data.big_spenders.slice(0,10),
    type: "bar"
  };

  let population_layout = {
    title: "Top 10 Population",
    xaxis: { title: "Countries" },
    yaxis: { title: "Big Spenders" }
  };

  Plotly.newPlot("chart1", [population_trace], population_layout);


  console.log(energy_data)
  // Scatter Plot
  var population_econsumption = {
    x: energy_data.gdppc,
    y: energy_data.econsumption/energy_data.population,
    mode: "markers",
    type: "scatter",
    name: "energy consumption",
    marker: {
      color: "#2077b4",
      symbol: "hexagram"
    }
  };

  let PE_layout = {
    title: "Energy Consumption vs Population",
    xaxis: { title: "Population" },
    yaxis: { title: "Energy Consumption" }
  };

  Plotly.newPlot("chart2", [population_econsumption], PE_layout);









});


