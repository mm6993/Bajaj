from project_board import ProjectBoard 
from team import Team 
from user import User 
project_board=ProjectBoard() 
team=Team()
user=User()
def main():
    while True:
        print("Select an option :")
        print("1.Create User")
        print("2.Remove User")
        print("3.Create Team")
        print("4.Add User To Team")
        print("5.Remove user from Team")
        print("6.Create Board")
        print("7.Add Task to Board")
        print("8.Remove Task from Board")
        print("9.Get User")
        print("10.Get Team")
        print("11.Get Board")
        print("12.Exit")
        choice=input("Enter the number of your choice: ")
        if choice=="1":
            user_id=input("Enter User Id: ")
            user_name=input("Enter user name: ")
            print(user.create_user(user_id,user_name))
        elif choice=="2":
            user_id=input("Enter User Id: ")
            print(user.remove_user(user_id))
        elif choice=="3":
            team_id=input("Enter team Id: ")
            team_name=input("Enter team name: ")
            print(team.create_team(team_id,team_name))
        elif choice=="4":
            team_id=input("Enter team Id: ")
            user_id=input("Enter user id: ")
            print(team.add_user_to_team(team_id,user_id))
        elif choice=="5":
            team_id=input("Enter team Id: ")
            user_id=input("Enter user id: ")
            print(team.remove_user_from_team(team_id,user_id))  
        elif choice=="6":
            board_id=input("Enter board Id: ")
            board_name=input("Enter board name: ")
            print(project_board.create_board(board_id,board_name))
        elif choice=="7":
            board_id=input("Enter board Id: ")
            task_id=input("Enter task id: ")
            task_description=input("enter task description: ")
            print(project_board.add_task(board_id,task_id,task_description))
        elif choice=="8":
            board_id=input("Enter board Id: ")
            task_id=input("Enter task id: ") 
            print(project_board.remove_task(board_id,task_id))
        elif choice=="9":
            user_id=input("Enter user id: ")
            print(user.get_user(user_id)) 
        elif choice=="10":
            team_id=input("enter team id: ")
            print(team.get_team(team_id))
        elif choice=="11":
            board_id=input("enter board id: ")
            print(project_board.get_board(board_id))
        elif choice=="12":
            print("exiting from the application.......") 
            break
        else:
            print("Invalid choice.please try again with appropriate choice.......") 
if __name__=="__main__":
    main()                      
               
            
            
                  
                 
            
                
                
                
    