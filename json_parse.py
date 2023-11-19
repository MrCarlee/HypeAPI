def monthToNum(string):

    m = {
         'jan': 1,
         'feb': 2,
         'mar': 3,
         'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month!')

def categoryToNum(string):

    m = {
            'lavoro e ' : 1,
            'rendite'   : 2,
            'casa'      : 3,
            'veicoli e' : 4,
            'alimentar' : 5,
            'atm'       : 6,
            'salute'    : 7,
            'cura del ' : 8,
            'bollette ' : 9,
            'famiglia'  : 10,
            'animali'   : 11,
            'assicuraz' : 12,
            'finanziam' : 13,
            'investime' : 14,
            'rimborsi'  : 15,
            'tasse e c' : 16,
            'vendite'   : 17,
            'ricarica'  : 18,
            'ricariche' : 19,
            'viaggi e ' : 20,
            'ristorant' : 21,
            'sport e h' : 22,
            'regali e ' : 23,
            'varie'     : 24,
            'elettroni' : 25,
            'abbigliam' : 26,
            'intratten' : 27,
            'istruzion' : 28,
            'criptoval' : 29,
            'shopping'  : 30,
        }
    s = string.strip()[:9].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a category!')

def parseHypeJson(hypeJson, wantedYear):

    json_formatted_str = json.dumps(hypeJson, indent=2)
    loaded_json = json.loads(json_formatted_str)

    cont = numpy.zeros((12+1, 2, 30+1))

    print("------------------------\nPrinting %s movements:\n------------------------\n" % wantedYear)
    #For each month
    for month in tqdm(loaded_json['month']):
        ##Loop only inside the wanted year
        if month['yearDescription'] == wantedYear:
            print (month['monthDescription'])
            ##For each movement of the wanted year
            for movements in month['movements']:
                print("\t %s%.2f\t\t%s" %( "+" if movements['income'] else "-", movements['amount'], movements['additionalInfo']['category']['name']))
                ##Sum into the income or outcome totals
                if movements['income']:
                    cont[monthToNum(month['monthDescription']), 0, categoryToNum(movements['additionalInfo']['category']['name'])]+=movements['amount']
                else:
                    cont[monthToNum(month['monthDescription']), 1, categoryToNum(movements['additionalInfo']['category']['name'])]-=movements['amount']
        sleep(0.1)
    print("------------------------\nEnd of %s movements:\n------------------------\n" % wantedYear)
    return cont