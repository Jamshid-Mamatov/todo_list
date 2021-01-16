todo_list=[]

def creat_list(lst):
    """this function takes a single value and this function is the main function and 
    it combines functions such as task creation task removal modification tasks input tasks"""

    print('Enter a list name = ',end="")
    name=input()
    task=add_task(lst)
    
    print(f"list name = {name}\ntasks\n{task}")

    print("Do you remove the task -> yes or no = ")
    remove=input()
    if remove=="yes":
        
        task_remove=remove_task(task)
        task=task_remove
        print(task_remove)

    print("Do you update the task -> yes or no = ")
    update=input()
    if update=="yes":
        
        task_update=update_task(task)
        task=task_update
        print(task_update)   

    print("Do you checking the task -> yes or no = ")
    checking=input()
    if checking=="yes":
        
        task_checking=checking_task(task)
        
        print(task_checking) 

    print("Do you clear the task -> yes or no = ")
    clear=input()
    if clear=="yes":

        task_clear=clear_task(task)
        task=task_clear
        print(task)         



def add_task(add_lst):
    """this function takes a single list and 
    adds tasks to that list returns the state and text state and the task list"""

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


def remove_task(tasks):
    """this function takes a single list and 
    removes the task you specified in that list and returns the list"""
    task_remove=[]
    for task in tasks:
        print(f"{task}  remove this task ->yes or no = ",end="")
        remove=input()
        if remove!='yes':
            task_remove.append(task)

    return  task_remove

def update_task(tasks):
    """this function accepts the list and 
    updates and returns the list to the task you want"""
    
    for task in tasks:
        print(f"{task}  update this task ->yes or no = ",end="")
        update=input()
        if update=="yes":
            print(f"{task['text']} enter new text if you change = ",end="")
            new_text=input()
            if new_text!="":
                task['text']=new_text

            print(f"{task['state']} enter new text if you change False or True = ",end="")

            new_state=input()
            if new_state!="":
                task['state']=bool(new_state)
    return tasks

def checking_task(tasks):
    """   this function accepts the list and 
    checks the tasks do or donot"""
    do=0
    do_not=0
    task_chek={}
    for task in tasks:
        if task['state']==True:
            do+=1
        else:
            do_not+=1
    task_chek['do']=do
    task_chek['do_not']=do_not
    return  task_chek

def clear_task(tasks) :
    """   this function accepts the list and 
    clears the list then returns an empty list"""

    tasks.clear()
    return tasks

creat_list(todo_list)       