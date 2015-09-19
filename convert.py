import csv
from sys import argv, exit
from jinja2 import Template
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')


def make_id(name):
    return re.sub(r'\W+', '', name)

with open('template.html') as template_file:
    template = Template(template_file.read())

if len(argv) != 2 or not argv[1].endswith('.csv'):
    print "Please provide a CSV filename"
    exit(1)

with open(argv[1], 'rb') as csvfile:
    with open('index.html', 'w') as out:
        reader = csv.DictReader(csvfile)
        out.write(template.render(
            people=sorted(list(reader),
                          key=lambda x: x['Full Name:'].split()[-1]),
            make_id=make_id)
        )
