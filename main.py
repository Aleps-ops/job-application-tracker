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

        if choice == "2":
            add_application(tracker)
    

def add_application(tracker):
    company = input("\nCompany: ")
    position = input("\nPosition: ")
    status = input("\nStatus: ")
    date_applied = input("\nDate applied: ")
    job_url = input("\nJob URL: ")
    notes = input("\nNotes: ")
    id_app = tracker.next_id()

    application = Application(
        id_app,
        company,
        position,
        status,
        date_applied,
        job_url,
        notes    
    )

    tracker.add(application)
    save_applications(tracker.applications, "applications.json")

if __name__ == "__main__":
    main()

