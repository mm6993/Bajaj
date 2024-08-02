import json 
import os
from team_base import TeamBase 
class Team(TeamBase):
    def __init__(self):
        self.db_path='db/teams.json'
        if not os.path.exists('db'):
            os.makedirs('db')
        if not os.path.exists(self.db_path):
            with open(self.db_path,'w') as f:
                json.dump({},f)
    def create_team(self,team_id:str,team_name:str)->str:
        with open(self.db_path,'r+') as f:
            data=json.load(f) 
            if team_id in data: 
                raise ValueError("team id already exists")
            data[team_id]={"name":team_name,"users":[]} 
            f.seek(0)
            json.dump(data,f) 
        return json.dumps({"status":"success","team_id":team_id})
    def add_user_to_team(self,team_id:str,user_id:str)->str:
        with open(self.db_path,'r+')as f:
            data=json.load(f) 
            if team_id not in data: 
                raise ValueError("team id does not exist")
            if user_id in data[team_id]["users"]:
                raise ValueError("user id already exists in this team")
            data[team_id]["users"].append(user_id) 
            f.seek(0)
            json.dump(data,f) 
        return json.dumps({"status":"success","user_id":user_id}) 
    def remove_user_from_team(self,team_id:str,user_id:str)->str:
        with open(self.db_path,'r+')as f:
            data=json.load(f) 
            if team_id not in data: 
                raise ValueError("team id does not exist")
            if user_id not  in data[team_id]["users"]:
                raise ValueError("user id does not exists in this team")
            data[team_id]["users"].remove(user_id)
            f.seek(0)
            json.dump(data,f) 
        return json.dumps({"status":"success","user_id":user_id}) 
    def get_team(self,team_id:str)->str:
        with open(self.db_path,'r')as f:
            data=json.load(f) 
            if team_id not in data: 
                raise ValueError("team id does not exist")
        return json.dumps({"status":"success","team":data[team_id]})
    
     
            
    
                
                
            
            
                           