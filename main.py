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

    if choice == "8":
        print("Scheduler shutting down 🧾")
        break
