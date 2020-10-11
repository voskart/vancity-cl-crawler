from pymongo import MongoClient
import config
import urllib.parse

def init_connection():
    username = urllib.parse.quote_plus(config.mongouser)
    password = urllib.parse.quote_plus(config.mongopass)
    client = MongoClient("mongodb+srv://%s:%s@apartmentsvan.6re6i.mongodb.net/<dbname>?retryWrites=true&w=majority" % (username,password))
    return(client.VanCityApts.apts)