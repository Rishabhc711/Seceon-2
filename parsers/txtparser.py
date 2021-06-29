# Reading the text file
filer = open('hashesr.txt', 'r')


lines = filer.readlines()
hashcount=0
hash_dict={}

for line in lines:

    hash=line.strip()
    if len(hash)==32: #checks whether the line is an actual hash
        hashcount+=1
        hash_dict[hash]=filer.name

print("Counted  :{} hashes and pushed into dictionary",hashcount)
with open('hashes2dict.txt', 'w') as filew2:
    print(hash_dict, file=filew2)
#file_content = file.read()
filer.close()
filew2.close()