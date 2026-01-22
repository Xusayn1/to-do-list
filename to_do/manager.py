from core.db_settings import *
import logging

logger = logging.getLogger(__name__)


def add_task():
    """
    Add a task to the tasks table
    :return: nothing
    """
    task = input("Add task: ")
    time = input("Add time: ")
    query = "INSERT INTO todo (item, time) VALUES (%s, %s)"
    parameters =  (task, time,)
    tasks = execute_query(query=query, params=parameters)
    print('Task added successfully')
    logging.info(f'Task added successfully: {tasks}')

def remove_task():
    """
    Remove a task from the tasks table
    :return: nothing
    """
    task = input("Remove task: ")
    query = "DELETE FROM todo WHERE item=%s"
    parameters = (task,)
    tasks = execute_query(query=query, params=parameters)
    print('Task removed successfully')
    logging.info(f'Task removed successfully: {tasks}')


def do_list_tasks():
    """
    shows what to do.
    :return: do table's info
    """
    query = "SELECT * FROM todo"
    tasks = execute_query(query=query, fetch='all')

    if not tasks:
        print("No tasks found")
        logging.info("No tasks found in do list")
    else:
        for task in tasks:
            print(f' ID: {task[0]} Task: {task[1]} time: {task[2]}')
            logging.info('tasks list is shown ')



def done_list_tasks():
    """
    shows what have done.
    :return: done list
    """
    query = "SELECT * FROM done"
    tasks = execute_query(query=query, fetch='all')

    if not tasks:
        print("No tasks found")
        logging.info("No tasks found in done list")
    else:
        for task in tasks:
            print(f' ID: {task[0]} Task: {task[1]} time: {task[2]}')
            logging.info('tasks list is shown ')


def do_tasks():
    """
    this is to do a smth from do list and
    to add to done list items from do list
    :return: nothing
    """
    task = input("which item do you want to do: ")
    time = input("which time: ")

    query = f"SELECT * FROM todo WHERE item=%s"
    parameters = (task,)
    tasks = execute_query(query=query, params=parameters)
    if tasks:
        query = " insert into done (item, time) values (%s, %s)"
        parameters = (task, time)
        tasks = execute_query(query=query, params=parameters)
        print(' task is done successfully')
        logger.info(f'Task done successfully: {tasks}')
    else:
        print("No tasks found")
        logging.warning("No tasks found in do list")

