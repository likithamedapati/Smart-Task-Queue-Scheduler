from datetime import datetime

print("Welcome to Smart Task Queue Scheduler 🧾")
print("-" * 40)

task_queue = []
completed_tasks = []
completed_time = {}

print("System ready. No tasks yet.")
while True:
    print("\n------ MENU ------")
    print("1. Add task")
    print("2. Process next task")
    print("3. View next task")
    print("4. Show waiting tasks")
    print("5. Completed history")
    print("6. Cancel task")
    print("7. Clear queue")
    print("8. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
     task = input("Enter task name: ")

     if task.strip() == "":
        print("Task cannot be empty.")
     else:
        task_queue.append(task)
        print(f"Task added: {task}")
    elif choice == "2":
     if not task_queue:
        print("No tasks to process.")
     else:
        task = task_queue.pop(0)
        time_done = datetime.now().strftime("%H:%M:%S")

        completed_tasks.append(task)
        completed_time[task] = time_done

        print(f"Processing: {task}")
        print(f"Completed at {time_done}")
        print("Great job! Ready for the next task ")
    elif choice == "3":
     if not task_queue:
        print("No tasks in queue.")
     else:
        print(f"Next task: {task_queue[0]}")
    elif choice == "4":
     print("\n--- Waiting Tasks ---")

     if not task_queue:
        print("Queue is empty.")
     else:
        for i, task in enumerate(task_queue, start=1):
            print(f"{i}. {task}")
    elif choice == "5":
     print("\n--- Completed Tasks ---")

     if not completed_tasks:
        print("No tasks completed yet.")
     else:
        for task in completed_tasks:
            time_done = completed_time.get(task, "Unknown")
            print(f"{task} → completed at {time_done}")
    elif choice == "6":
     if not task_queue:
        print("Queue is empty.")
     else:
        task = input("Enter task name to cancel: ")

        if task in task_queue:
            task_queue.remove(task)
            print(f"Task cancelled: {task}")
        else:
            print("Task not found.")
    elif choice == "7":
     confirm = input("Clear all tasks? (yes/no): ").lower()

     if confirm == "yes":
        task_queue.clear()
        print("Queue cleared.")
     else:
        print("Cancelled.")

    elif choice == "8":
        print("Scheduler shutting down ")
        break
    else:
       print("Invalid choice,try again!")
