import json 
import os
from user_base import UserBase 
class User(UserBase):
    def __init__(self):
        self.db_path='db/users.json'
        if not os.path.exists('db'):
            os.makedirs('db')
        if not os.path.exists(self.db_path):
            with open(self.db_path,'w') as f:
                json.dump({},f)
    def create_user(self,user_id:str,user_name:str)->str:
        with open(self.db_path,'r+') as f:
            data=json.load(f) 
            if user_id in data: 
                raise ValueError("user id already exists")
            data[user_id]={"name":user_name} 
            f.seek(0)
            json.dump(data,f) 
        return json.dumps({"status":"success","user_id":user_id})
    def get_user(self,user_id:str)->str:
        with open(self.db_path,'r')as f:
            data=json.load(f) 
            if user_id not in data: 
                raise ValueError("user id does not exist")
        return json.dumps({"status":"success","user":data[user_id]})
    