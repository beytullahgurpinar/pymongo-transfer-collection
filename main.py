import pymongo

mongo_client_main = pymongo.MongoClient("mongodb://main_server:port")
main_db = mongo_client_main['main-database']

mongo_client_another = pymongo.MongoClient("mongodb://another_server:port")
another_db = mongo_client_another['another-database']


def transfer(main_collectin, another_collection, page=1, bulk_size=2500):
    while True:
        offset = page * bulk_size - bulk_size
        items = main_db[main_collectin].find().sort("_id", -1).skip(offset).limit(bulk_size)

        if items != None:
            another_db[another_collection].insert_many(items)
            page += 1
        else:
            break


transfer("logs", "logs-another", 1, 5000)
