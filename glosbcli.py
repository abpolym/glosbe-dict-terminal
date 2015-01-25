import argparse
import requests
import sys
from termcolor import colored
import urllib

def die(errormsg):
	print errormsg
	sys.exit(1)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('lfrom', type=str, help="Language to translate from - in ISO_639 format")
parser.add_argument('ldest', type=str, help="Language to translate to - in ISO_639 format")
parser.add_argument('word', type=str, help="Word to translate")
#parser.add_argument('--colored', type=bool, nargs=0, help='Print in beautiful colors', default=False)
args = parser.parse_args()
word=args.word
fromlang_iso=args.lfrom
destlang_iso=args.ldest
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
translations=[]
translated=0
for trans in rjson[tuc]:
	translated+=1
	if phrase in trans:
		transphrase=trans[phrase]
		if transphrase[language] != destlang: continue
		translations.append(transphrase[text].encode('utf-8'))
	if meanings in trans:
		for x in trans[meanings]:
			if x[language] != destlang: continue
			translations.append(x[text].encode('utf-8'))
if not translated: die('No translation available for ' + word)
translations=list(set(translations))
#translations=(sorted(translations, key=str.swapcase))
translations.sort(key=lambda x:(not x.islower(), x))
for tsent in translations:
	for tword in tsent.split():
		print tword,
	#	if not args.colored:
	#		print tword,
	#		continue
	#	if tword.islower(): print colored(tword,'blue'),
	#	else: print colored(tword, 'green'),
	print
