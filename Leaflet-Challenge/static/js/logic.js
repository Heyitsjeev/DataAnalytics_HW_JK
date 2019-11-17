var url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

d3.json(url, function(data) {
    displayFeatures(data.features);
});

function displayFeatures(eqData) {

    function onClick(info, layer) {
        layer.bindPopup("<h3 align='center'>" + info.properties.place +"</h3><hr>" + 
         "<p>Time of Occurance: " + new Date(info.properties.time) + "</p>" +
            "<p>Earthquake Magnitude: " + info.properties.mag + "</p>");
    }

    var earthquakes = L.geoJSON(eqData, {
        onEachFeature: onClick,
        pointToLayer: function (feature, latLng) {
            var popUpBox = {
            radius: 4*feature.properties.mag,
            fillColor: getMagColor(feature.properties.mag),
            color: "black",
            weight: 0.9,
            opacity: 0.8,
            fillOpacity: 0.6
            };
            return L.circleMarker(latLng, popUpBox);
        }
    });
    
    displayMap(earthquakes);
}

function displayMap(earthquakes) {

    var lightMap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
        maxZoom: 15,
        id: "mapbox.light",
        accessToken: API_KEY
    });

    var overlays = {
        "Earthquakes": earthquakes
    };

    var baseMap = {
        "Light Map": lightMap 
    };

    var map = L.map("map", {
        center: [36.77, -119.41],
        zoom: 4.0,
        layers: [lightMap, earthquakes]
    });

    //defining legend
    var legend = L.control({position: "bottomright"});
  
    legend.onAdd = function (map) {    
        var div = L.DomUtil.create("div", "info legend"),
        mag = [0, 1, 2, 3, 4, 5],
        labels = [];
      
        for (var i = 0; i < mag.length; i++) {
            div.innerHTML += '<i style="background:' + getMagColor(mag[i] + 1) + '">&nbsp&nbsp</i> ' +
                mag[i] + (mag[i + 1] ? '&ndash;' + mag[i + 1] + '<br>' : '+');
        }
    
      return div;
    };
    
    //adding the layers and legend to map
    L.control.layers(baseMap, overlays, {collapsed: true}).addTo(map);

    legend.addTo(map);
}

function getMagColor(mag) {

    return mag < 1 ? 'palegreen' : 
           mag < 2 ? 'yellow' :
           mag < 3 ? 'salmon' :
           mag < 4 ? 'orangered' :
           mag < 5 ? 'coral' :
                   'indianred';
  }