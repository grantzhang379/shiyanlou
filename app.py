#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, abort,request
import json
import os

app = Flask(__name__)

def getContent(filename):
    with open(filename) as f:
        content = json.load(f)
        return content

@app.route('/')
def index():
    filePath = '/home/shiyanlou/files/'
    fileList = os.listdir(filePath)
    titleList = []
    for file in fileList:
        filename = filePath+file
        with open(filename) as f:
            temp = json.load(f)
            title = temp['title']
            titleList.append(title)
    return render_template('index.html',titleList=titleList)

@app.route('/files/<filename>')
def file(filename):
    filename = filename + '.json'
    print(filename)
    if filename not in os.listdir('/home/shiyanlou/files'):
        return render_template('404.html'),404
    else:
        filePath = '/home/shiyanlou/files/'
        filename = filePath + filename
        content = getContent(filename)
        return render_template('file.html',content=content)

@app.errorhandler(404)
def not_found(error):
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
            
