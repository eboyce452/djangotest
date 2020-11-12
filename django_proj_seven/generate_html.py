import re
import os

html_files = input('Please list the html files you want to make (w/ or w/out .html, separated by commas: ')
html_files = html_files.split(',')
html_files = [a.replace('.html','') for a in html_files]
html_files = [a.replace(' ','') for a in html_files]
html_files = [(str(a) + '.html') for a in html_files]

app_name = input('app name: ')
pathing = os.path.join(os.getcwd(), 'templates', app_name)

for x in html_files:
    with open(os.path.join(pathing, '{}_extension.html'.format(app_name)), 'r') as f:
        extension_template = f.read()
        f.close()
    with open(os.path.join(pathing, x), 'w') as f:
        f.write(extension_template)
        f.close()