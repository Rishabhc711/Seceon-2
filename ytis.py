# Reading the text file
filer = open('ytis.txt', 'r')
filew = open('ytis_hashes.txt', 'w')

lines = filer.readlines()
hashcount=0
hash_dict={}

from urllib.request import urlopen
dicts=["AndroRat_6Dec2013"]
url = "https://github.com/ytisf/theZoo/blob/master/malwares/Binaries/{}/{}.md5"
print(url)
page = urlopen(url)

html = page.read().decode("utf-8")
urlcount=0
with open('ytis.txt', 'w') as f:
    f.write(html)
    urlcount+=1
print(url)
print("Copied the text from the url to hashes.txt :{} urls",urlcount)

for line in lines:

    hash=line.strip()
    if len(hash)==32: #checks whether the line is an actual hash
        hashcount+=1
        filew.write(hash)
        hash_dict[hash]=filer.name

print("Counted  :{} hashes and pushed into dictionary",hashcount)
with open('hashes2dict389.txt', 'w') as filew2:
    print(hash_dict, file=filew2)
#file_content = file.read()
filer.close()
filew.close()
filew2.close()