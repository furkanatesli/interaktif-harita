
var depremler = L.layerGroup();
var haberler = L.layerGroup();

var mbAttr = '',
    mbUrl = 'https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw';

var grayscale   = L.tileLayer(mbUrl, {id: 'mapbox/light-v9', tileSize: 512, zoomOffset: -1, attribution: mbAttr}),
    streets  = L.tileLayer(mbUrl, {id: 'mapbox/streets-v11', tileSize: 512, zoomOffset: -1, attribution: mbAttr});

var map = L.map('map', {
    center: [38.722278, 35.487246],
    zoom: 6,    
    layers: [grayscale, depremler,haberler]
});

var baseLayers = {
};

var overlays = {
    "Depremler": depremler,
    "Haberler": haberler
};

L.control.layers(baseLayers, overlays).addTo(map);


L.tileLayer('', {
    attribution: '<a href="https://www.mapbox.com/">Mapbox</a> |' + '<a href="index.html">Harita Haber</a> Son Güncelleme Tarihi: 12/05/20 21:01:26'
}).addTo(map);
                    