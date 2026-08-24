import pytest
from application import Application
from tracker import Tracker

def test_tracker_add():
    tracker = Tracker()
    application = Application(
        1,
        "Google",
        "Software Engineer Intern",
        "Applied",
        "2026-08-21",
        "https://careers.google.com",
        ""
    )
    tracker.add(application)
    assert application in tracker.applications

def test_list_applications():
    tracker = Tracker()
    application = Application(
            1,
            "Google",
            "Software Engineer Intern",
            "Applied",
            "2026-08-21",
            "https://careers.google.com",
            ""
        )
    tracker.add(application)
    result = tracker.list_applications()
    assert "1. Google - Software Engineer Intern - Applied" in result