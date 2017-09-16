$(document).ready(function($){
  $('#spendingHabits').on('click', some_function);
  console.log($('#spendingHabits').id);
  function some_function() {
    $('#chartdiv').fadeToggle();
  }

  var chart = AmCharts.makeChart( "chartdiv", {
    "type": "serial",
    "theme": "light",
    "dataProvider": [ {
      "country": "Food",
      "visits": 25
    }, {
      "country": "Clothing",
      "visits": 32
    }, {
      "country": "Electronics",
      "visits": 13
    }, {
      "country": "Kitchen",
      "visits": 13
    }, {
      "country": "Other",
      "visits": 17
    }],
    "valueAxes": [ {
      "gridColor": "#FFFFFF",
      "gridAlpha": 0.2,
      "dashLength": 0
    } ],
    "gridAboveGraphs": true,
    "startDuration": 1,
    "graphs": [ {
      "balloonText": "[[category]]: <b>[[value]]</b>",
      "fillAlphas": 0.8,
      "lineAlpha": 0.2,
      "type": "column",
      "valueField": "visits"
    } ],
    "chartCursor": {
      "categoryBalloonEnabled": false,
      "cursorAlpha": 0,
      "zoomable": false
    },
    "categoryField": "country",
    "categoryAxis": {
      "gridPosition": "start",
      "gridAlpha": 0,
      "tickPosition": "start",
      "tickLength": 20
    },
    "export": {
      "enabled": true
    }

  } );
});
