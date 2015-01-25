# glosbe-dict-terminal
Commandline Dictionary lookup using the [glosbe API](https://glosbe.com/a-api)

# Usage
```
$ python globscli.py -h
usage: glosbcli.py [-h] lfrom ldest word

positional arguments:
	lfrom       Language to translate from - in ISO_639 format
	ldest       Language to translate to - in ISO_639 format
	word        Word to translate
```

# Example
```
$ python glosbcli.py deu eng unheilvoll
appearing to be true
baleful
balefully
baneful
calamitous
calamitously
dire
disasterous
disasterously
disastrous
evil or malignant
fatal
likely to grow worse
malign
ominous
ominuosly
portentous
portentously
siderally
sinister
unpropitious
```

# Languages
Please see the [ISO\_639](http://en.wikipedia.org/wiki/ISO_639:d) format for available languages.

A list of common languages, sorted by the size of the globsbe dictionaries, is here:

| ISO\_639 ID   | Language |
|----------|:---------:|
| eng | English |
| deu | German |
| jpn | Japanese |
| fra | French |
| spa | Spanish |
| pol | Polish |
| rus | Russian |
| ita | Italian |
| ces | Czech |
| cmn | Mandarin Chinese |
| nld | Dutch |
| por | Portoguese |
| swe | Swedish |
| hrv | Croatian |
| fin | Finnish |
| hin | Hindi |
| hun | Hungarian |
| arb | Arabic |
| vie | Vietnamese |
| tur | Turkish |
