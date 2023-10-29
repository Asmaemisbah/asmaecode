import dataclasses
from unicodedata import name
from flask import jsonify  # Import jsonify
from flask import Flask, render_template , url_for,session,redirect,request,Response
from pymongo import MongoClient
from datetime import datetime



def prof():
    if request.method == 'POST':
        dataList = []
        for doc in dataclasses:
            for key in doc:
                dataList.append(doc[key]) 
                print("dataList:", dataList)  # Add this line to check the contents
        return render_template("employe.html",Name_employe=dataList[0],email=dataList[2],service=dataList[1],len=len)
