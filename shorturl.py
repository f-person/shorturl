#!/usr/bin/python3.6

from requests import post
from sys import exit, argv

if len(argv) == 3:
    long_url = argv[1]
    custom_path = argv[2]
elif len(argv) == 2:
    long_url = argv[1]
    custom_path = ''
else:
    if len(argv) == 1:
        exit('please enter the url.')
    exit('too many arguments.')
if 'http://' not in long_url and 'https://' not in long_url:
    long_url = 'http://' + long_url
check = post('http://gg.gg/check', data={'custom_path': custom_path, 'use_norefs': '0', 'long_url': long_url, 'app': 'site', 'version': '0.1'})

if check.text != 'ok':
    exit(check.text)
print(post('http://gg.gg/create', data={'custom_path': custom_path, 'use_norefs': '0', 'long_url': long_url, 'app': 'site', 'version': '0.1'}).text)
