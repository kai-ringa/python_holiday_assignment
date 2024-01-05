# Build a command-line todo list application.
# Implement functions to add tasks, mark tasks as completed, display the list, and delete tasks.
# Use a text file to persist the tasks between program runs.

import os

def add_task(task):
    with open('tasks.txt', 'a') as f:
        f.write(task + '\n')

def complete_task(task):
    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()
    with open('tasks.txt', 'w') as f:
        for t in tasks:
            if t.strip() == task:
                f.write(f'[x] {t}')
            else:
                f.write(t)

def delete_task(task):
    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()
    with open('tasks.txt', 'w') as f:
        for t in tasks:
            if t.strip() != task:
                f.write(t)

def display_tasks():
    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()
    if not tasks:
        print('No tasks.')
    else:
        for i, t in enumerate(tasks):
            print(f'{i+1}. {t}', end='')

while True:
    print('1. Add Task')
    print('2. Complete Task')
    print('3. Delete Task')
    print('4. Display Task')
    print('5. Quit')
    choice = input('Enter your choice: ')
    if choice == '1':
        task = input('Enter your task: ')
        add_task(task)
    elif choice == '2':
        task = input('Enter task: ')
        complete_task(task)
    elif choice == '3':
        task = input('Enter task: ')
        delete_task(task)
    elif choice == '4':
        display_tasks()
    elif choice == '5':
        break
    else:
        print('Invalid choice')