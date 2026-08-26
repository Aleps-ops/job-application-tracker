from tracker import Tracker
from application import Application
from storage import load_applications, save_applications

def main():
    applications = load_applications("applications.json")
    tracker = Tracker(applications)

    print("Job Application Tracker")

    choice = ""

    while choice != "6":
        print()
        print("1. List applications")
        print("2. Add application")
        print("3. Search applications")
        print("4. Update status")
        print("5. Delete application")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            print()
            print(tracker.list_applications())
        elif choice == "2":
            add_application(tracker)
        elif choice == "3":
            query = input("\nSearch: ")
            print()
            print(tracker.search(query))
        elif choice == "4":
            update_application(tracker)
        elif choice == "5":
            delete_application(tracker)
        elif choice == "6":
            print("Goodbye!")
        else:
            print("Invalid option.")
    

def add_application(tracker):
    company = input("\nCompany: ")
    position = input("\nPosition: ")

    print_valid_statuses()

    date_applied = input("\nDate applied: ")
    job_url = input("\nJob URL: ")
    notes = input("\nNotes: ")
    id_app = tracker.next_id()

    while True:
        status = input("\nStatus: ")
        try:
            application = Application(
                id_app,
                company,
                position,
                status,
                date_applied,
                job_url,
                notes
            )
            break
        except ValueError:
            print("Invalid status. Please try again.")

    tracker.add(application)
    save_applications(tracker.applications, "applications.json")

def update_application(tracker):
    try:
        application_id = int(input("\nApplication ID: "))
    except ValueError:
        print("\nInvalid ID. Please enter a number.")
        return

    print_valid_statuses()

    status = input("\nNew status: ")

    try:
        tracker.update_status(application_id, status)
    except ValueError as error:
        print(f"\nError: {error}")
        return

    save_applications(tracker.applications, "applications.json")

def delete_application(tracker):
    try:
        application_id = int(input("\nApplication ID: "))
    except ValueError:
        print("\nInvalid ID. Please enter a number.")
        return

    try:
        tracker.delete(application_id)
    except ValueError as error:
        print(f"\nError: {error}")
        return

    print("\nApplication deleted successfully.")
    save_applications(tracker.applications, "applications.json")

def print_valid_statuses():
    print("\nValid statuses:")
    for status in Application.statuses:
        print(f"- {status}")

if __name__ == "__main__":
    main()

