import docx2txt
import re
import os
base_folder = './docs';

documents = os.listdir(base_folder)
filtered_docs=[]
text=''
ending_with_docs= ['docx','doc']

print "Started parsing documents........"
for doc in documents:
    if doc.split(".")[1] == ending_with_docs[0].lower() or doc.split(".")[1]==ending_with_docs[1].lower():
        filtered_docs.append(doc)
        text=text+docx2txt.process('./docs/'+doc)
    else:
        print "Invalid file(Not doc/docx)"+doc
print "Finished parsing documents"
regex_email=re.findall(r"[\w\S]+[@]\w+[.]\w{3,}",text)
print 'Emails are:'
print regex_email


