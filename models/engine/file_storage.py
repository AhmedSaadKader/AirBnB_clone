import json
class FileStorage:
    __file_path = {"file.json"}
    __objects = {}
    def all(self):
        return self.__objects
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__object[key]=obj