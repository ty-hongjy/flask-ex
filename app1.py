# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 17:19:20 2017

@author: Administrator
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello1")
def hello1():
    return "Hello World1!"
    
if __name__=='_main_':
  app.run()