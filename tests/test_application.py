import pytest
from application import Application


def test_application_creation():
    application = Application(
        1,
        "Google",
        "Software Engineer Intern",
        "Applied",
        "2026-08-21",
        "https://careers.google.com",
        ""
    )

    assert application.company == "Google"
    assert application.position == "Software Engineer Intern"
    assert application.status == "Applied"


def test_invalid_status():
    with pytest.raises(ValueError):
        Application(
            2,
            "Microsoft",
            "Software Engineer Intern",
            "Banana",
            "2026-08-21",
            "https://careers.microsoft.com",
            ""
        )

def test_update_status():
    application = Application(
        1,
        "Google",
        "Software Engineer Intern",
        "Applied",
        "2026-08-21",
        "https://careers.google.com",
        ""
    )

    application.update_status("Interview")

    assert application.status == "Interview"

def test_application_to_dict():
    application = Application(
        1,
        "Google",
        "Software Engineer Intern",
        "Applied",
        "2026-08-21",
        "https://careers.google.com",
        "My first application"
    )

    result = application.to_dict()

    assert result["id"] == 1
    assert result["company"] == "Google"
    assert result["position"] == "Software Engineer Intern"
    assert result["status"] == "Applied"
    assert result["date_applied"] == "2026-08-21"
    assert result["job_url"] == "https://careers.google.com"
    assert result["notes"] == "My first application"