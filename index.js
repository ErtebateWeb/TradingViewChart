//Pseudo code
//Step 1: Define chart properties.
//Step 2: Create the chart with defined properties and bind it to the DOM element.
//Step 3: Add the CandleStick Series.
//Step 4: Set the data and render.


//Code
const log = console.log;

const chartProperties = {
  width:1300,
  height:600,
  timeScale:{
    timeVisible:true,
    secondsVisible:true,
  }
}

const domElement = document.getElementById('tvchart');
const chart = LightweightCharts.createChart(domElement,chartProperties);
const candleSeries = chart.addCandlestickSeries();
const interval='1h'

fetch('https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval='+interval+'&limit=1000')

  .then(res => res.json())
  .then(data => {
    const cdata = data.map(d => {
      return {time:d[0]/1000,open:parseFloat(d[1]),high:parseFloat(d[2]),low:parseFloat(d[3]),close:parseFloat(d[4])}
    });
    candleSeries.setData(cdata);




 fetch('http://127.0.0.1:8000/Events/')
      .then(response => response.json())
      .then(data1 => 
        {
        const mark = data1;
var datesForMarkers = ['1601554194000','1600553294000'];

var markers = [];

console.log(mark.length);

for (i = 0; i < mark.length; i++) {
  console.log(mark[i].timestamp);
  markers.push({ time: mark[i].timestamp/1000-3599, position: mark[i].position, color: mark[i].color, shape: mark[i].shape, text: mark[i].text });

}
candleSeries.setMarkers(markers);
  })
})
  .catch(err => log(err))

