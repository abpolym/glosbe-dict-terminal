import argparse
import re
import requests
import sys
from termcolor import colored
import urllib

def die(errormsg):
	print errormsg
	sys.exit(1)

parser = argparse.ArgumentParser()
parser.add_argument('lfrom', type=str, help="Language to translate from - in ISO_639 format")
parser.add_argument('ldest', type=str, help="Language to translate to - in ISO_639 format")
parser.add_argument('word', type=str, help="Word to translate")
parser.add_argument('-c', '--colored', action="store_true", default=False, help='Colorized output')
parser.add_argument('-e', '--examples', action="store_true", default=False, help='Show examples')
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
examples='examples'
baseurl = 'https://glosbe.com/gapi/translate'
queryparams = urllib.urlencode({fromparam:fromlang_iso,destparam:destlang_iso,phrase:word,'format':'json'})
url=baseurl+'?'+queryparams
if args.examples: url+='&tm=true'

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
		if not args.colored:
			print tword,
			continue
		if tword.islower(): print colored(tword,'blue'),
		else: print colored(tword, 'yellow'),
		#else: print colored(tword, 'yellow', attrs=['underline']),
	print

if not args.examples: sys.exit(0)

print '--------------------------------'
print '--------------------------------'

for ex in rjson[examples]:
	#print re.match('<strong class="keyword">.*?</strong>',ex['first'])
	#print ex['first']
	#for m in re.findall('<strong class="keyword">([\s\w\.\-]+)</strong>', ex['first']): print m
	p=re.compile('<strong class="keyword">[\u\s\w\.\-]+</strong>',re.UNICODE)
	p2=re.compile('<strong class="keyword">([\s\w\.\-]+)</strong>',re.UNICODE)
	#for m in re.findall('<strong class="keyword">[\s\w\.\-]+</strong>', ex['second']): print p.sub('DDD',ex['second'])
	for m in p.findall(ex['second']):
		for i in p2.findall(m):
			ex['second']=p.sub(colored(i,'yellow'),ex['second'])
	print ex['second']
	#print ex['second']
	#print re.search('strong', ex['first'])
	#print ex['second']
