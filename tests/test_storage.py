import json

from application import Application
from storage import save_applications, load_applications


def test_save_applications(tmp_path):
    application = Application(
        1,
        "Google",
        "Software Engineer Intern",
        "Applied",
        "2026-08-21",
        "https://careers.google.com",
        ""
    )

    filename = tmp_path / "applications.json"

    save_applications([application], filename)

    with open(filename, "r") as file:
        data = json.load(file)

    assert data[0]["id"] == 1
    assert data[0]["company"] == "Google"
    assert data[0]["position"] == "Software Engineer Intern"
    assert data[0]["status"] == "Applied"

def test_load_applications(tmp_path):
    application = Application(
        1,
        "Google",
        "Software Engineer Intern",
        "Applied",
        "2026-08-21",
        "https://careers.google.com",
        ""
    )

    filename = tmp_path / "applications.json"

    save_applications([application], filename)

    applications = load_applications(filename)

    assert len(applications) == 1
    assert isinstance(applications[0], Application)
    assert applications[0].id == 1
    assert applications[0].company == "Google"
    assert applications[0].position == "Software Engineer Intern"
    assert applications[0].status == "Applied"