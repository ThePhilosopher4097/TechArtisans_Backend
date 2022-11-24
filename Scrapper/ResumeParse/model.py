import nltk
from resume_parser import resumeparse

data = resumeparse.read_file('sameer.pdf')
print('Name: ', data['name'])
print('Phone: ', data['phone'])
print('Email: ', data['email'])
print('Skills: ', data['skills'])
