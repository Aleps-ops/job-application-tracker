from application import Application

class Tracker:
    def __init__(self):
        self.applications = []

    def add(self, application: Application):
        self.applications.append(application)

    def list_applications(self):
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