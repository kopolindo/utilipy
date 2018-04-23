import cStringIO
import os
import sys
import re


recover_file = "out.txt"
f = open("log.txt", "rb")


def clean_file(file_path):
    fm = cStringIO.StringIO()
    if not os.path.isfile(file_path):
        return fm
    with open(file_path) as input_file:
        for line in input_file:
            # if line is contains printable chars
            if line.strip() != '':
                out = line.replace(u'\u001a', ' ')
                fm.write(out)
    return fm


def make_recover_if_not_exists(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'a+'):
            pass


def seek_and_append_no_set(recover_file_path, buff):
    i = None
    lines = []
    with open(recover_file_path, "r+") as recoverf:
        for i, line in enumerate(buff):
            print "Query su mem: %s" % line
            lines.append(line)
            if "ERR" in line:
                # not fan of re-seeking the entire file
                for recoverl in recoverf:
                    if recoverl == line:
                        break
                    # ?
                    elif not recoverl.strip() or recoverl.strip() == '':
                        recoverf.seek(0, 2)
                        recoverf.write(line + '\n')
    return i, lines


def seek_and_append_with_set(recover_file_path, buff):
    i = None
    lines = []
    # open the file and load the lines in a set
    with open(recover_file_path, 'r') as f:
        recover_file_lines = set([l for l in f])

    with open(recover_file_path, 'a+') as f:
        for i, line in enumerate(buff):
            if line.strip() == '':
                continue
            print "Query su mem: %s" % line
            lines.append(line)
            if 'ERR' in line:
                if line not in recover_file_lines:
                    recover_file_lines.add(line)
                    f.write(line + '\n')
    return i, lines


if __name__ == '__main__':

    fm = clean_file("log.txt")
    make_recover_if_not_exists(recover_file)

    try:
        buff = fm.getvalue()
    except Exception as e:
        print e
        sys.exit(-1)

    buff = re.sub(r'\n([^"])', r'\1', buff).split("\n")

    ctr, goodlines = seek_and_append_with_set(recover_file, buff)

    sys.exit(0)

