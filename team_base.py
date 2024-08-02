import abc 
class TeamBase(abc.ABC):
  @abc.abstractmethod 
  def create_team(self,team_id:str,team_name:str)->str:
    pass
  @abc.abstractmethod 
  def add_user_to_team(self,team_id:str,user_id:str)->str:
    pass
  @abc.abstractmethod 
  def remove_user_from_team(self,team_id:str,user_id:str)->str:
    pass
  @abc.abstractmethod 
  def get_team(self,team_id:str)->str:
    pass