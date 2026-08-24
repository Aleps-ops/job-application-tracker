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