#!/usr/bin/python
import subprocess

f = open('requirements.txt')
p = f.readlines()
for i in [j.split('\n')[0] for j in p]:
    subprocess.call(['pip', 'install', i])
