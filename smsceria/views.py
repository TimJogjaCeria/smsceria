from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest

def home(request):
    import urllib2
    import csv
    import json

    url = 'http://data.go.id/dataset/fec232bd-9e08-49f8-8165-51971d961581/resource/a7ba5107-7614-4a1e-adf1-9181f5599597/download/perkembanganhargaratarataberasgrosirdipasarindukcipinangpicmenurutjenisberas2011.csv'
    response = urllib2.urlopen(url)
    cr = csv.reader(response)
    result = []
    last_beras = ''
    # import ipdb; ipdb.set_trace();
    for row in cr:
        if row[2] == 'jenis_beras':
            pass
        elif last_beras != row[2]:
            last_beras = row[2]
            beras = {'jenis_beras':row[2], 'harga':row[3]}
            result.append(beras)

    return HttpResponse(json.dumps(result, indent=4, sort_keys=True))
