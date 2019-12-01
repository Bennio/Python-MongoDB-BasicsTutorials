from pymongo import MongoClient                
democlient = MongoClient()
myclient = MongoClient('localhost',27017)
mydb = myclient["demo"]
mycoll=mydb["dbtable"]

myquery={"name":"John"}  #normal query
#myquery={"name":{"$regex":"^S"}}  # query search using regex

mydoc=mycoll.find(myquery)
print(mydoc)
for x in mydoc:
    print(x)