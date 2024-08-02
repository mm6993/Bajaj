import abc  
class UserBase(abc.ABC):
  @abc.abstractmethod 
  def create_user(self,user_id:str,user_name:str)->str:
    pass
  @abc.abstractmethod 
  def get_user(self,user_id:str)->str:
    pass