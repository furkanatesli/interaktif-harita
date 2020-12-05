#!/usr/bin/python
# coding=utf-8
import bs4 as bs
import urllib
import time, random
sehirler=['adana','adiyaman','afyon','agri','amasya','ankara','antalya','artvin','aydin','balikesir',
          'bilecik','bingol','bitlis','bolu','burdur','bursa','canakkale','cankiri','corum','denizli',
          'diyarbakir','edirne','elazig','erzincan','erzurum','eskisehir','gaziantep','giresun','gumushane','hakkari',
          'hatay','isparta','mersin','istanbul','izmir','kars','kastamonu','kayseri','kirklareli','kirsehir',
          'kocaeli','konya','kutahya','malatya','manisa','maras','mardin','mugla','mus','nevsehir',
          'nigde','ordu','rize','sakarya','samsun','siirt','sinop','sivas','tekirdag','tokat',
          'trabzon','tunceli','urfa','usak','van','yozgat','zonguldak','aksaray','bayburt','karaman',
          'kirikkale','batman','sirnak','bartin','ardahan','igdir','yalova','karabuk','kilis','osmaniye','duzce']
koordinatlar=[  '37.002,35.326','37.763,38.276','38.757,30.534','39.720,43.050','40.650,35.834','39.921,32.853','36.900,30.693','41.183,41.828','37.845,27.834','39.647,27.885',
                '40.143,29.975','38.885,40.496','38.400,42.108','40.733,31.613','37.724,30.288','40.182,29.066','40.150,26.414','40.600,33.616','40.548,34.960','37.771,29.086',
                '37.916,40.222','41.675,26.559','38.675,39.222','39.749,39.494','39.906,41.273','39.768,30.521','37.061,37.378','40.914,38.388','40.461,39.476','37.574,43.738',
                '36.217,36.165','37.770,30.555','36.812,34.634','41.009,28.965','38.414,27.144','40.605,43.097','41.375,33.776','38.724,35.485','41.736,27.224','39.145,34.161',
                '40.768,29.968','37.871,32.485','39.419,29.985','38.347,38.319','38.615,27.425','37.586,36.903','37.323,40.721','37.213,28.365','38.739,41.496','38.621,34.715',
                '37.970,34.679','40.980,37.884','41.022,40.519','40.765,30.407','41.289,36.332','37.930,41.940','42.026,35.150','39.749,37.016','40.978,27.515','40.326,36.554',
                '41.005,39.718','39.107,39.548','37.159,38.792','38.681,29.403','38.508,43.375','39.820,34.809','41.452,31.789','38.370,34.027','40.255,40.224','37.178,33.224',
                '39.847,33.528','37.884,41.128','37.518,42.461','41.632,32.338','41.109,42.704','39.921,44.046','40.655,29.272','41.197,32.623','36.717,37.116','37.073,36.255','40.842,31.157',]
def deprem_cek():
    oku=urllib.urlopen('http://udim.koeri.boun.edu.tr/zeqmap/xmlt/son24saat.xml').read()
    kaynak=bs.BeautifulSoup(oku,'xml')
    dosya = open("Depremler\\Depremler.js","w")
    for ic in kaynak.find_all('earhquake'):
        dosya.write(""" var deprem = L.marker(["""+ic.get('lat')+""","""+ic.get('lng')+"""],{icon: depremicon}).addTo(depremler);
                        marker.bindPopup("<b>Lokasyon :"""+ic.get('lokasyon')+"""</b><br><b>Buyukluk :"""+ic.get('mag')+"""</b><br><b>Derinlik :"""+ic.get('Depth')+"""</b><br><b>Olus Tarihi :"""+ic.get('name')+"""");
                    """)
        print(ic.get('name'))
    dosya.close()
def haber_cek():
    sayac=0
    for sehir in sehirler:
        print sehir
        oku=urllib.urlopen('https://rss.haberler.com/rsskonu.asp?konu='+sehir).read()
        kaynak=bs.BeautifulSoup(oku,'xml')
        kaynak=kaynak.find('item')
        dosya = open("Haberler\\"+sehir+".js","w")
        dosya.write("""
                        var haber = L.marker(["""+koordinatlar[sayac]+"""],{icon: habericon}).addTo(haberler);
                        marker.bindPopup("<b>"""+kaynak.title.text.encode('utf-8').strip()+"""</b><br>"""+kaynak.description.text.encode('utf-8').strip()+"""<br><b>Kaynak :</b> <a href="""+kaynak.link.text.encode('utf-8').strip()+""">"""+kaynak.link.text.encode('utf-8').strip()+"""</a><br><b>Paylasim Tarihi : <b>"""+kaynak.pubDate.text.encode('utf-8').strip()+"""");

                    """)
        dosya.close()
        sayac=sayac+1
        print "Basl�k = ",kaynak.title.text 
        time.sleep(random.randint(3,10))
while 1:
    try:
	    deprem_cek()
	    haber_cek()
	    time.sleep(600)
    except:
	    print "Bir Hata olu�tu."