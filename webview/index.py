from flask import Flask, render_template
import json
import os
import sys
import fnmatch

app = Flask(__name__)

@app.route("/")
def index():
    fname = os.path.join(app.instance_path)
    sname = fname.split('StudyNotes')
    fname = sname[0]+'StudyNotes/Notes/'
    data = []
    for (dirpath, dirnames, files) in os.walk(fname):
        print(dirpath, " -> ", dirnames)
        res = {}
        if dirpath.split('/')[-1] == '':
            continue
        res.update({'name': dirpath.split('/')[-1]})
        res.update({'children': []})
        for file in files:
            with open(os.path.join(dirpath, file), 'r') as f:
                ques = f.readline()
                ques = ques.rstrip('\r\n')
                res['children'].append({'name': ques})
        data.append(res)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
