# Name: main.py
# Author: Sergey Mikhaylov
# Date: 2019-07
# Description:
#   an database implementated by python dictionary


#################### Database CRUD Implementation ######################
class Model():
    database = {}
    
    def __init__(self, database={}):
        self.database = database


    ############################ create item ###########################
    def create(self, key, value):
        # key = "1"
        # value = {"firstName": "Sergey", "lastName": "Mikhaylov"}
        # return = True
        #          False
        if key in self.database:
            return False
        # invalid value
        try:
            if (len(value["firstName"]) == 0
                    and len(value["lastName"]) == 0):
                return False
        except KeyError:
            return False
        # succeed
        self.database[key] = value
        return True


    ############################ read item ###########################
    def read(self, key):
        # key = "1"
        # reutrn value = {"firstName": "Sergey", "lastName": "Mikhaylov"}
        #                None
        if key in self.database:
            return self.database[key]
        else:
            return None


    ############################ update item ###########################
    def update(self, key, value):
        # key = "1"
        # value = {"firstName": "Sergey", "lastName": "Mikhaylov"}
        # return = True
        #          False
        # invalid value
        try:
            if (len(value["firstName"]) == 0
                    and len(value["lastName"]) == 0):
                return False
            # not found
            if (key not in self.database):
                return False
        # invalid value
        except KeyError:
            print("key error")
            return False
        # succeed
        self.database[key] = value
        return True


    ############################ delete item ###########################
    def delete(self, key):
        # key = "1"
        # return = True 
        #          False
        if key not in self.database:
            return False
        # succeed
        del self.database[key]
        return True


    ############################ debug method ###########################
    def debug(self):
        # return = database if implemented
        #          None if not implemented
        return self.database


############################ Test Function #############################
if __name__ == "__main__":
    model = Model({
            "1": {"firstName": "Sergey", "lastName": "Mikhaylov"},
            "5": {"firstName": "Strong", "lastName": "Dinosaur"},
            "12": {"firstName": "Black", "lastName": "Cat"}
            })
    print(model.create("7",{"firstName": "Sergey", "lastName": "Mikhaylov"}))
    print(model.database)
    print(model.create("7",{"firstName": "Sergey", "lastName": "Mikhaylov"}))
    print(model.database)