import pymongo
import pprint
from video import Video

CLIENT = pymongo.MongoClient("mongodb://py-user:pyuser1@cluster0-shard-00-00-gm9y9.mongodb.net:27017,cluster0-shard-00-01-gm9y9.mongodb.net:27017,cluster0-shard-00-02-gm9y9.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
DB = CLIENT['ReSeed']
# COL = DB['posts']
COL = DB['testPosts']

pp = pprint.PrettyPrinter(indent=4)

rootVid = COL.find_one()
pp.pprint(rootVid)

rootVidObj = Video('null', rootVid, 1)
print(rootVidObj.toString())

report = COL.find_one(
  sort=[( '_id', pymongo.ASCENDING )]
)

count = 0
# vid = rootVid

# recs = vid.recs

recs = rootVidObj.recs

for post in COL.find():
    pp.pprint(post)
