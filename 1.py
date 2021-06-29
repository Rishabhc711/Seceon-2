from urllib.request import urlopen

url = "https://raw.githubusercontent.com/CYB3RMX/MalwareHashDB/main/HashDB.json"
print(url)
page = urlopen(url)

html = page.read().decode("utf-8")
urlcount=0
with open('jsonfile.txt', 'w') as f:
    f.write(html)
    urlcount+=1
print(url)
print("Copied the text from the url  :{} urls",urlcount)

# # Reading the text file
# filer = open('hashes1.txt', 'r')
# filew = open('hashes2.txt', 'w')

# lines = filer.readlines()
# hashcount=0
# hash_dict={}

# for line in lines:

#     hash=line.strip()
#     if len(hash)==32: #checks whether the line is an actual hash
#         hashcount+=1
#         filew.write(hash)
#         hash_dict[hash]=filer.name

# print("Counted  :{} hashes and pushed into dictionary".hashcount)
# with open('hashes2dict.txt', 'w') as filew2:
#     print(hash_dict, file=filew2)
# #file_content = file.read()
# filer.close()
# filew.close()
# filew2.close()