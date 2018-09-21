import os
import sys
import json

bdir ='/Users/tamilselvan/Documents/Personal/Journal/HackingNotes/Notes'
def test():
    data = []
    for (dirpath, dirnames, files) in os.walk(bdir):
        res = {}
        res.update({'name': dirpath.split('/')[-1]})
        res.update({'childern':[]})
        for file in files:
            with open(os.path.join(dirpath,file),'r') as f:
                first_line = f.readline()
                first_line = first_line.rstrip('\r\n')
                res['childern'].append({'name': first_line})
        data.append(res)
    print(data)


if __name__ == '__main__':
    test()
