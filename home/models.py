from django.db import models


# # Create your models here.
# class Project(models.Model):
#     title = models.TextField(max_length=250)
#     description = models.TextField(max_length=600)
#     img_url = models.TextField(max_length=600)
#     link = models.TextField(max_length=600)
    
import pymongo

class Project(models.Model):

    def collection2():

        if __name__ == "__main__":
            client = pymongo.MongoClient("mongodb://localhost:27017/")

            db = client['Portdb']

            collection2 = db['Projects']
            return collection2.find()