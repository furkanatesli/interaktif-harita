
var depremler = L.layerGroup();
var haberler = L.layerGroup();

var mbAttr = '',
    mbUrl = 'https://tile.openstreetmap.org/{z}/{x}/{y}.png';

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
    attribution: '<a href="https://www.x.com/">X</a> |' + '<a href="index.html">Harita Haber</a> Son Güncelleme Tarihi: 10/17/24 19:13:42'
}).addTo(map);
                    