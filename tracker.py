from application import Application

class Tracker:
    def __init__(self, applications = None):
        if applications is None:
            applications = []

        self.applications = applications

    def add(self, application: Application):
        self.applications.append(application)

    def list_applications(self):
        if not self.applications:
            return "No applications found."

        return "\n".join(
            f"{application.id}. {application}"
            for application in self.applications
        )

    def delete(self, application_id: int):
        for application in self.applications:
            if application.id == application_id:
                self.applications.remove(application)
                return

        raise ValueError("Application not found")

    def update_status(self, application_id: int, status: str):
        for application in self.applications:
            if application.id == application_id:
                application.update_status(status)
                return
        raise ValueError("Application not found")

    def search(self, query: str):
        query = query.lower()
        results = []

        for application in self.applications:
            if query in application.company.lower() or query in application.position.lower():
                results.append(application)

        if not results:
            return "No applications found."

        return "\n".join(
            f"{result.id}. {result}" 
            for result in results
        )

    def next_id(self):
        if not self.applications:
            return 1

        return max(application.id for application in self.applications) + 1