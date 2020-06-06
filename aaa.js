
var map = L.map('map').setView([38.722278, 35.487246], 6);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '<a href="index.html">Harita Haber</a> Son Güncelleme Tarihi: 06/06/20 02:59:20'
}).addTo(map);        
                    