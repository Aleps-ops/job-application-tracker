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