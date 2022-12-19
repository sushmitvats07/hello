from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Project
import pymongo
from pymongo import MongoClient

# Replace the uri string with your MongoDB deployment's connection string.
uri = "mongodb+srv://Sushmit12:HhlXbuNdurVP1o1g@cluster0.5m6gsdn.mongodb.net/test"

client = MongoClient(uri)

# database and collection code goes here
db = client.Project
coll = db.collection2




current_year = datetime.now().year

context = {
        "current_year" : current_year
    }


# if __name__ == "__main__":
# client = pymongo.MongoClient("mongodb://localhost:27017/")

# db = client['Portdb']

# collection2 = db['Projects']

# Create your views here.
def index(request):
    return render(request, 'index.html', context)
    #return HttpResponse('This is home page')

def portfolio(request):
    all_projects = coll.find()
    
    context = {
        "current_year" : current_year,
        "all_projects": all_projects,
    }
    return render(request, 'portfolio.html', context)

def services(request):
    return HttpResponse('This is services page')

    # HhlXbuNdurVP1o1g