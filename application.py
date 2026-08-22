class Application:
    statuses = [
        "Applied",
        "OA",
        "Interview",
        "Rejected",
        "Offer",
        "Withdrawn"
    ]

    def __init__(self, id: int, company: str, position: str,
                 status: str, date_applied: str,
                 job_url: str, notes: str):

        if status not in self.statuses:
            raise ValueError("Invalid status")

        self.id = id
        self.company = company
        self.position = position
        self.status = status
        self.date_applied = date_applied
        self.job_url = job_url
        self.notes = notes

    def __str__(self):
        return f"{self.company} - {self.position} - {self.status}"