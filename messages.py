import pickle
import md5
import uuid

class Message:

    @staticmethod
    def generate(obj):
        if(type(obj) == dict):
            if("__hashCode" in obj.keys()):
                return obj['__hashCode']
            else:
                serialized = pickle.dumps(obj)
                hex = md5.new(serialized).hexdigest()
                uid = uuid.uuid1()

                obj['__hashCode'] = str(uid) + '::' + str(hex)
                return obj['__hashCode']
