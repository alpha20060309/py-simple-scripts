import json
import os
import argparse
from datetime import datetime
from traceback import print_tb


TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE,'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks,f,indent=4)

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def add_task(title, description=None, due=None,status="not started"):
    tasks = load_tasks()
    task_id = get_next_id(tasks)
    task = {
        "id" : task_id,
        "title" : title,
        "description" : description or "",
        "status" : status,
        "created_at" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "due_date": due
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task {task_id} added successfully")

def list_tasks(filter_status=None, sort_by=None):
    tasks = load_tasks()
    if filter_status:
        tasks =  [t for t in tasks if t["status"]== filter_status]
    if sort_by == "date":
        tasks.sort(key= lambda x: x["due_date"] or "")
    elif sort_by == "created":
        tasks.sort(key=lambda x: x["created_at"])
    if not tasks:
        print("No tasks found")
        return 
    print(f"{'ID':<4} {'Title':<30} {'Status':<10} {'Due Date':<12} {'Created At'}")
    print("-"*70)
    for t in tasks:
        print(f"{t['id']:<4} {t['title']:<30} {t['status']:<10} {t['due_date'] or '':<12} {t['created_at']}")


def mark_done(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            if t["status"] == "completed":
                print(f"Task {task_id} is already completed")
                return
            t["status"] = "completed"
            save_tasks(tasks)
            print(f"Task {task_id} is marked as completed.")
            return
    print(f"Task {task_id} is not found")

def edit_task(task_id, title=None, description=None,due=None):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            if title: t["title"] = title
            if description is not None: t["description"] = description
            if due is not None: t["due_date"] = due
            save_tasks(tasks)
            print(f"Task {task_id} updated sucessfully.")
            return
    print(f"Task {task_id} is not found.")

def delete_task(task_id,force=False):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            if not force:
                confirm = input(f"Are you sure you want to delete task {task_id
                }? (y/n)")
                if confirm.lower() != "y":
                    print("Deletion cancelled.")
                    return
            tasks.remove(t)
            save_tasks(tasks)
            print(f"Task {task_id} deleted.")
            return
    print(f"Task {task_id} is not found")

def search_tasks(keyword):
    tasks = load_tasks()
    results = [t for t in tasks if keyword.lower() in t["title"].lower() or keyword.lower() in t["description"].lower()]
    if not results:
        print(f"Not matching tasks not found with this keyword: {keyword}")
        return
    print(f"{'ID':<4}{'Title':<30}{'Status':<10}{'Due Date':<12}{'Created At'}")
    print("-"*70)
    for t in results:
        print(f"{t['id']:<4} {t['title']:<30} {t['status']:<10} {t['due_date'] or '':<12} {t['created_at']}")

def clear_tasks(force=False):
    if not force:
        confirm = input("Are you sure you want to delete ALL tasks? (y/n): ")
        if confirm.lower() != "y":
            print("Operation cancelled.")
            return
        save_tasks([])
        print("All tasks cleared.")

def main():
    parser = argparse.ArgumentParser(description="CLI To-Do List Application")
    subparsers = parser.add_subparsers(dest="command")

    #Add
    parser_add = subparsers.add_parser("add")
    parser_add.add_argument("title")
    parser_add.add_argument("--description")
    parser_add.add_argument("--due")


    #List
    parser_list = subparsers.add_parser("list")
    parser_list.add_argument("--completed", action="store_true")
    parser_list.add_argument("--pending", action="store_true")
    parser_list.add_argument("--sort", choices=["date","created"])

    #Done
    parser_done = subparsers.add_parser("done")
    parser_done.add_argument("task_id", type=int)

    #Edit
    parser_edit = subparsers.add_parser("edit")
    parser_edit.add_argument("task_id", type=int)
    parser_edit.add_argument("--title")
    parser_edit.add_argument("--description")
    parser_edit.add_argument("--due")


    #Delete
    parser_delete = subparsers.add_parser("delete")
    parser_delete.add_argument("task_id", type=int)
    parser_delete.add_argument("--force",action="store_true")

    #Search
    parser_search = subparsers.add_parser("search")
    parser_search.add_argument("keyword")

    #Clear
    parser_clear = subparsers.add_parser("clear")
    parser_clear.add_argument("--force",action="store_true")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title, args.description, args.due)
    elif args.command == "list":
        status = "completed" if args.completed else "pending" if args.pending else None
        list_tasks(status, args.sort)
    elif args.command == "done":
        mark_done(args.task_id)
    elif args.command == "edit":
        edit_task(args.task_id,args.title, args.description,args.due)
    elif args.command == "delete":
        delete_task(args.task_id, args.force)
    elif args.command == "search":
        search_tasks(args.keyword)
    elif args.command == "clear":
        clear_tasks(args.force)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()