#!/usr/bin/python3
import pymongo

client = pymongo.MongoClient("mongodb+srv://Bed-C:hassuchigisu@poll-c.nc9ejvj.mongodb.net/?retryWrites=true&w=majority")
db = client.test


result = client["Poll-C"]["Chairperson"].find()

if __name__ == "__main__":
    for i in result:
        print(i)
