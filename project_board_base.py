import abc
class ProjectBoardBase(abc.ABC):
  @abc.abstractmethod 
  def create_board(self,board_id:str,board_name:str)->str:
    pass
  @abc.abstractmethod 
  def add_task(self,board_id:str,task_id:str,task_description:str)->str:
    pass
  @abc.abstractmethod 
  def remove_task(self,board_id:str,task_id:str)->str:
    pass
  @abc.abstractmethod 
  def get_board(self,board_id:str)->str:
    pass
  