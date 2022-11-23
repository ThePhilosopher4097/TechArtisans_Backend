import nltk
from resume_parser import resumeparse

def res_parse(path_to_file):
    data = resumeparse.read_file(file_name)
    print('Name: ', data['name'])
    print('Phone: ', data['phone'])
    print('Email: ', data['email'])
    print('skills: ', data['skills'])
