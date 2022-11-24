# import nltk
# from resume_parser import resumeparse
import PyPDF2
import re

file_name = input()

pdfFileObj = open(file_name, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
pdfText = pageObj.extractText()

# NAME
name = pdfText.split('\n')[0]
name = name.split('+')[0].strip()
print('Name: ', name)

# EMAIL
email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')
email = re.search(email_regex, pdfText).group()
print('Email: ', email)

# PHONE
phone_regex = re.compile(r'((\+*)((0[ -]*)*|((91 )*))((\d{12})+|(\d{10})+))|\d{5}([- ]*)\d{6}')
phone = re.search(phone_regex, pdfText).group()
print('Phone: ', phone)

# DOB
dob_regex = re.compile(r'DOB.*')
dob = re.search(dob_regex, pdfText).group()
dob = dob.replace("DOB:", "")
print('Data of Birth: ', end='')
print(dob.lstrip().split())

# Programming
prog_regex = re.compile(r'[Pp]rogramming.*')
programming = re.search(prog_regex, pdfText).group()
programming = programming.replace("Programming :", "")
programming.strip()
print('Programming: ', end='')
print(programming.split('|'))

# Languages
lang_regex = re.compile(r'[Ll]anguage.*')
languages = re.search(lang_regex, pdfText).group()
languages = languages.replace("Languages:", "")
languages.strip()
print('Languages: ', end='')
print(languages.split('|'))

# Interests
inte_regex = re.compile(r'Interest.*')
interests = re.search(inte_regex, pdfText).group()
interests = interests.replace("Interests:", "")
print('Interests: ', end='')
print(interests.split(','))

# Certifications
certs = []
print("Certifications: ", end='')
cert = False
for line in pdfText.split('\n'):
    if line.__contains__("Project"):
        break
    for word in line.split():
        if word == 'Certifications':
            cert = True
    if cert == True:
        line = line.replace("", "")
        certs.append(line)
print(certs[0:-1])


# print(pdfText)
# data = resumeparse.read_file(file_name)
# print('Name: ', data['name'])
# print('Phone: ', data['phone'])
# print('Email: ', data['email'])
