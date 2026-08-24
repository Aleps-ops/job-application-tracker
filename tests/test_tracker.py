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

def test_delete_application():
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
    tracker.delete(1)
    assert application not in tracker.applications

def test_delete_invalid_application():
    tracker = Tracker()

    with pytest.raises(ValueError):
        tracker.delete(99)

def test_delete_middle_application():
    tracker = Tracker()
    application1 = Application(
                1,
                "Google",
                "Software Engineer Intern",
                "Applied",
                "2026-08-21",
                "https://careers.google.com",
                ""
            )
    tracker.add(application1)
    application2 = Application(
                2,
                "Microsoft",
                "Software Engineer Intern",
                "Applied",
                "2026-08-21",
                "https://careers.microsoft.com",
                ""
            )
    tracker.add(application2)
    application3 = Application(
                3,
                "Amazon",
                "Software Engineer Intern",
                "Applied",
                "2026-08-21",
                "https://careers.microsoft.com",
                ""
                )
    tracker.add(application3)
    tracker.delete(2)

    assert application2 not in tracker.applications
    assert application1 in tracker.applications
    assert application3 in tracker.applications

def test_tracker_update_status():
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

    tracker.update_status(1, "Interview")

    assert application.status == "Interview"

def test_tracker_update_invalid_status():
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

    with pytest.raises(ValueError):
        tracker.update_status(1, "Banana")

def test_tracker_update_invalid_id():
    tracker = Tracker()

    with pytest.raises(ValueError):
        tracker.update_status(99, "Interview")

def test_search():
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
    result = tracker.search("google")
    assert "1. Google - Software Engineer Intern - Applied" in result

    application = Application(
            2,
            "Facebook",
            "Software Engineer Intern",
            "Applied",
            "2026-08-21",
            "https://careers.facebook.com",
            ""
        )
    tracker.add(application)
    result = tracker.search("facebook")
    assert "2. Facebook - Software Engineer Intern - Applied" in result

    result = tracker.search("Microsoft")
    assert result == "No applications found."

def test_search_by_position():
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
    result = tracker.search("engineer")
    assert result == "1. Google - Software Engineer Intern - Applied" in result
