#!/usr/bin/env python3

import argparse
import re
import time
from io import StringIO

def convert_file(infile, outfiles):
    out_texts = [StringIO(), StringIO()]
    for i in range(2):
        out_texts[i].write("id,text,comment,timestamp,translate\n")
    with open(infile, mode='r') as file:
        text = file.read()
    lines = re.findall('@[0-9]+[^@]*', text)
    find_number_re = re.compile('@([0-9]+)')
    find_replica_re = re.compile('~([^~]*)~')

    lines_n = len(lines)
    for num, line in enumerate(lines):
        numbers = find_number_re.findall(line)
        replicas = find_replica_re.findall(line)
        if len(numbers) != 1 or len(replicas) == 0 or len(replicas) > 2:
            print('Bad line: \n {}'.format(line))
            break

        if len(replicas) == 1:
            replicas.append(replicas[0])

        for i in range(2):
            replicas[i] = replicas[i].replace('"', "'")
            if replicas[i].find('"') != -1:
                print('Bad line: \n {}'.format(line))
                break
            out_texts[i].write('{},"{}","",{},1\n'.format(numbers[0], replicas[i], round(time.time())))

        if num % 100 == 0:
            print("processed {}/{}".format(num, lines_n))

    for i in range(2):
        with open(outfiles[i], mode='w') as outfile:
            outfile.write(out_texts[i].getvalue())


__desc__ = '''
The script to convert one \*.tra file (a localization file for infinity engine modding) 
into two \*.csv file (one for male and another one for female).

The format of csv file is

id,text,comment,timestamp,translate
"1","Зачем ты тревожишь меня? Тебя плохо воспитали? Убирайся!","","1431616436","1"
where:

id - line #
text - translated text
comment - always empty string
timestamp - linux epoch
translate - always "1"
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__desc__)
    parser.add_argument('infile', help='Input tra filename.')
    parser.add_argument('outfile_m', help='Output CSV filename for male.')
    parser.add_argument('outfile_f', help='Output CSV filename for female.')

    args = parser.parse_args()

    convert_file(args.infile, [args.outfile_m, args.outfile_f])
