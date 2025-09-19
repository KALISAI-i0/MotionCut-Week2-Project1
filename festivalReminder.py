import datetime
import json
import os

# Load festivals from file or start with defaults
FILENAME = "festivals.json"
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        festivals = json.load(f)
else:
    festivals = {
        "Diwali": "2025-10-20",
        "Christmas": "2025-12-25"
    }

def save_data():
    with open(FILENAME, "w") as f:
        json.dump(festivals, f, indent=4)

def view_festivals():
    print("\n--- All Festivals ---")
    for name, date in sorted(festivals.items(), key=lambda x: x[1]):
        print(f"{name}: {date}")

def add_festival():
    name = input("Enter festival name: ")
    date_str = input("Enter date (YYYY-MM-DD): ")
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        festivals[name] = date_str
        save_data()
        print(f"Festival '{name}' added successfully.")
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD.")

def delete_festival():
    name = input("Enter festival name to delete: ")
    if name in festivals:
        del festivals[name]
        save_data()
        print(f"Festival '{name}' deleted.")
    else:
        print("Festival not found.")

def check_reminders():
    today = datetime.date.today()
    print("\n--- Reminders ---")
    for name, date_str in festivals.items():
        fest_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        days_left = (fest_date - today).days
        if days_left == 0:
            print(f"🎉 Today is {name}!")
        elif 0 < days_left <= 7:
            print(f"⏳ {name} is in {days_left} day(s).")
    print("No upcoming festivals within 7 days." if all(
        (datetime.datetime.strptime(date_str, "%Y-%m-%d").date() - today).days > 7 
        for date_str in festivals.values()
    ) else "")

def main():
    while True:
        print("\n--- Festival Reminder Bot ---")
        print("1. View all festivals")
        print("2. Add a new festival")
        print("3. Delete a festival")
        print("4. Check reminders")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            view_festivals()
        elif choice == "2":
            add_festival()
        elif choice == "3":
            delete_festival()
        elif choice == "4":
            check_reminders()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
