todo_list=[]

def creat_list(lst):
    print('Enter a list name = ',end="")
    name=input()
    task=add_task(lst)
    
    print(f"list name = {name}\ntasks\n{task}")



def add_task(add_lst):
    add=True
    
    
    while add:
        task={}
        print("write the task = ",end="")
        task_text=input()
        task['text']=task_text
        task['state']=False
        add_lst.append(task)
        
        print('Do you add a new task ->yes or no = ',end="")
        add=input()
        if add=='no':
            add=False

    return add_lst



creat_list(todo_list)       