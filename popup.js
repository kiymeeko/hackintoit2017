
$(document).ready(function($){
  $('#future').hide();
  $('#spendingHabits').on('click', some_function);
  function some_function() {
    $('#chartdiv').fadeToggle();
  }
  $('#goal').on('click', other_function);
  function other_function() {
    $('#chartdiv').hide();
    $('#future').fadeIn();
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

  $('head style[type="text/css"]').attr('type', 'text/less');
  less.refreshStyles();
  window.randomize = function() {
  	$('.radial-progress').attr('data-progress', Math.floor(35));
  }
  setTimeout(window.randomize, 200);
  $('.radial-progress').click(window.randomize);

});
