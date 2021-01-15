todo_list=[]

def creat_list(lst):
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


def remove_task(tasks):
    task_remove=[]
    for task in tasks:
        print(f"{task}  remove this task ->yes or no = ",end="")
        remove=input()
        if remove!='yes':
            task_remove.append(task)

    return  task_remove

def update_task(tasks):

    
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


creat_list(todo_list)       