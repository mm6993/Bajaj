def get_team(self,team_id:str)->str:
        with open(self.db_path,'r')as f:
            data=json.load(f) 
            if team_id not in data: 
                raise ValueError("team id does not exist")
        return json.dumps({"status":"success","team":data[team_id]})