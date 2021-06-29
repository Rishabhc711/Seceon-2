# import MySQLdb

# db = MySQLdb.connect(host="?",   
#                  user="root",        
#                  passwd="?",  
#                  db="test")
#cursor = db.cursor()

filer = open('/home/rishabh/Downloads/NSRL/NSRL-264-Android-Autopsy/NSRLFile-264-Android.txt-md5.idx', 'r')
# filew = open('hashes2.txt', 'w')

lines = filer.readlines()
count=0
#hash_dict={}

for line in lines:
    # hash=line.strip()
    # if len(hash)==32: #checks whether the line is an actual hash
        count+=1
        # filew.write(hash)
        # hash_dict[hash]=filer.name

# with open('hashes2dict.txt', 'w') as filew2:
#     print(hash_dict, file=filew2)
#file_content = file.read()
filer.close()
# filew.close()
# filew2.close()
print(str(count))

# query = "INSERT INTO EM VALUES (%s,%s,%s,%s,%s,%s)"

# values = [line.split() for line in file_content]
# cursor.executemany(query, values)

# db.commit()
# db.close()