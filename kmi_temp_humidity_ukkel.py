import urllib.request

def get_temp_humidity_ukkel():
    with urllib.request.urlopen('http://www.meteo.be/meteo/view/nl/123386-Waarnemingen.html') as response:
       kmi = str(response.read())
       
    ukkel_pos = kmi.find('<city code="6447">Ukkel</city>')
    kmi_data = kmi[ukkel_pos:ukkel_pos+99]
    kmi_data = kmi_data.split('</td>\\r\\n')
    kmi_temp = kmi_data[1].strip()[len('<td>'):]
    kmi_humidity = kmi_data[2].strip()[len('<td>'):]
    kmi_temp = float(kmi_temp.replace(',', '.'))
    kmi_humidity = float(kmi_humidity.replace(',', '.'))
    return kmi_temp, kmi_humidity


if __name__ == '__main__':
    print(get_temp_humidity_ukkel()[0])
    print(get_temp_humidity_ukkel()[1])


