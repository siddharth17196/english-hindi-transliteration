#    	 DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#	            Version 2, December 2004
#
#	Copyright (C) 2020 Siddharth Nair <www.github.com/siddharth17196>
#
#	Everyone is permitted to copy and distribute verbatim or modified
#	copies of this license document, and changing it is allowed as long
#	as the name is changed.
#
#	       DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#	TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#	0. You just DO WHAT THE FUCK YOU WANT TO.


lang = 'hi-t-i0-und'
import http.client
import json
import pickle

with open('encode.pkl', 'rb') as f:
    encode = pickle.load(f)

def request(q, lang):
    conn = http.client.HTTPSConnection('inputtools.google.com')
    conn.request('GET', '/request?text=' + q + '&itc=' + lang +
            '&num=1&cp=0&cs=1&ie=utf-8&oe=utf-8&app=test')
    res = conn.getresponse()
    return res

def get_hindi(q):
    output = ''
    res = request(q, lang)
    res = res.read()
    output = str(res)[14+4+len(q):-31]
    output=output.strip()
    return output[2:]

def convert(stops):
    hin = []
    j=0
    special_chars ='/.,><?][}{)(|;:-+='
    for i in range(len(stops)):
        j+=1
        h=''
        d = stops[i][:-1].split(' ')
        # print(d)
        for el in d:
            if type(el)==int:
                h += el
            elif el in special_chars:
                h += el
            else:
                x=get_hindi(el)
                l = (len(x)-1)//12
                d = 0
                op = ''
                for i in range(l):
                    while(x[d]!='\\'):
                        op += x[d]
                        d += 1
                    op+=encode[x[d:d+12]]
                    d+=12
                h += op
            h += ' '
        hin.append(h[:-1]+"\n")
    return hin

if __name__ == "__main__":
    inp = "n"
    stops = ["rohtak marg", "nirman vihar", "ghazipur depot", "tilak nagar"]
    hin = convert(stops)
    print(hin)
