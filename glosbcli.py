import requests
import sys
import urllib

def die(errormsg):
	print errormsg
	sys.exit(1)

word='ominousududu'
fromlang_iso='eng'
destlang_iso='deu'
fromparam='from'
destparam='dest'
phrase='phrase'
meanings='meanings'
tuc='tuc'
text='text'
language='language'
baseurl = 'https://glosbe.com/gapi/translate'
queryparams = urllib.urlencode({fromparam:fromlang_iso,destparam:destlang_iso,phrase:word,'format':'json'})
url=baseurl+'?'+queryparams

r = requests.get(url)
if r.status_code != 200: die('Statuscode != 200')
rjson = r.json()
if rjson['result'] != 'ok': die('Query was malformed')
fromlang=rjson[fromparam]
destlang=rjson[destparam]
translated=0
for trans in rjson[tuc]:
	translated=1
	if phrase in trans:
		transphrase=trans[phrase]
		if transphrase[language] != destlang: continue
		print transphrase[text]
	if meanings in trans:
		for x in trans[meanings]:
			if x[language] != destlang: continue
			print x[text]
if not translated: die('No translation available for ' + word)
