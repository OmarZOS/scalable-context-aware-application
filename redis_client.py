import os
import redis


REDIS_HOST=str(os.getenv("REDIS_HOST"))
REDIS_PORT=str(os.getenv("REDIS_PORT"))

myRedisClient = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT)

class redisClient(object):
    def getClient(self, *args):
        return myRedisClient

    def setValue(self,varName,value):
        myRedisClient.mset({str(varName): str(value)})

    def getValue(self,varName):
        try:
            return myRedisClient.get(str(varName))
        except :
            return []

