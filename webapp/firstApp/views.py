from django.shortcuts import render
import joblib
import os
import json
import pandas as pd
#from .models import medicin123
import psycopg2

# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    model=joblib.load('../prediction_service/model/model.joblib')
    list=[]
    list.append(float(request.GET['age']))
    list.append(float(request.GET['sex']))
    list.append(float(request.GET['bmi']))
    list.append(float(request.GET['children']))
    list.append(float(request.GET['smoker']))
    list.append(float(request.GET['region']))

    answer=model.predict([list]).tolist()[0]

    # b=medicin123(age=request.GET['age'],sex=request.GET['sex'],bmi=request.GET['bmi'],children=request.GET['children'],smoker=request.GET['smoker'],region=request.GET['region'],charges=answer)
    # b.save()

    return render(request, "index.html", {'answer':answer})
