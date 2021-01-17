todo_list=[]
def creat_list():
    """creat list
    parametrs:
        none
        there is a global variable
    return: 
        none    """
    global todo_list


def add_task():
    """task add in list
    parametrs:
        none
        there is global variable
    return:
        list->global variable"""
    
    task={}
    
    task['text']="write"
    task['state']=False
    todo_list.append(task)

    task={}
    task['text']="read"
    task['state']=False
    todo_list.append(task)

    task={}
    task['text']="listen"
    task['state']=False
    todo_list.append(task)

    

    return todo_list


def remove_task():
    """todo removes the first task of the list
        parameters:
        none
        there is global variable
        return:
        list->global variable"""
    
    todo_list.pop(0)

    return  todo_list

def update_task():
    """updated task of todo list
    parameters:
    none 
    code has global variable
    return:
    list->global variable   """
    
    todo_list[1]['text']='speak'
    todo_list[0]['state']=True

    return todo_list

def checking_task():
    """   checks todo list {do} or {donot}
    parameters:
    none 
    code has global variable
    return:
    dict->information about {do} or {donot}"""
    do=0
    do_not=0
    task_chek={}
    for task in todo_list:
        if task['state']==True:
            do+=1
        else:
            do_not+=1
    task_chek['do']=do
    task_chek['do_not']=do_not
    return  task_chek

def clear_task() :
    """clears todo list
    parameters:
    none 
    code has global variable   
    return:
    empty list->global variable"""

    todo_list.clear()
    return todo_list

