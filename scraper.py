import os
import subprocess


print(os.getcwd())
print(os.listdir('.'))
print(subprocess.call('scrapy', shell=True))
