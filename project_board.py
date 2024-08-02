import json 
import os
from project_board_base import ProjectBoardBase 
class ProjectBoard(ProjectBoardBase):
    def __init__(self):
        self.db_path='db/project_boards.json'
        if not os.path.exists('db'):
            os.makedirs("db")
        if not os.path.exists(self.db_path):
            with open(self.db_path,'w') as f:
                json.dump({},f)
    def create_board(self,board_id:str,board_name:str)->str:
        with open(self.db_path,'r+') as f:
            data=json.load(f) 
            if board_id in data: 
                raise ValueError("Board id already exists")
            data[board_id]={"name":board_name,"tasks":{}} 
            f.seek(0)
            json.dump(data,f) 
        return json.dumps({"status":"success","board_id":board_id})
    def add_task(self,board_id:str,task_id:str,task_description:str)->str:
        with open(self.db_path,'r+')as f:
            data=json.load(f) 
            if board_id not in data: 
                raise ValueError("Board id does not exist")
            if task_id in data[board_id]["tasks"]:
                raise ValueError("Task id already exists in this board")
            data[board_id]["tasks"][task_id]=task_description 
            f.seek(0)
            json.dump(data,f) 
        return json.dumps({"status":"success","task_id":task_id}) 
    def remove_task(self,board_id:str,task_id:str)->str:
        with open(self.db_path,'r+')as f:
            data=json.load(f) 
            if board_id not in data: 
                raise ValueError("Board id does not exist")
            if task_id not  in data[board_id]["tasks"]:
                raise ValueError("Task id does not exists in this board")
            del data[board_id]["tasks"][task_id]
            f.seek(0)
            json.dump(data,f) 
        return json.dumps({"status":"success","task_id":task_id}) 
    def get_board(self,board_id:str)->str:
        with open(self.db_path,'r')as f:
            data=json.load(f) 
            if board_id not in data: 
                raise ValueError("Board id does not exist")
        return json.dumps({"status":"success","board":data[board_id]}) 
            
    
                
                
            
            
                           