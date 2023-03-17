import nltk
import json
#from resume_parser import resumeparse
from pyresparser import ResumeParser

#data = resumeparse.read_file('sameer.pdf')
data = ResumeParser('sameer.pdf').get_extracted_data()

print(json.dumps(data, indent = 3))

#print('Name: ', data['name'])
#print('Phone: ', data['phone'])
#print('Email: ', data['email'])
#print('Skills: ', data['skills'])
#print('Skills: ', data['experience'])
#print('Skills: ', data['languages'])
