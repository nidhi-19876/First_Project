import os
import tempfile
import pytest

import app as attendance_app


@pytest.fixture

def client(tmp_path):
    # use a temporary data file so tests are isolated
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    attendance_app.DATA_DIR = str(data_dir)
    attendance_app.DATA_FILE = str(data_dir / "attendance.csv")
    # ensure file created
    with open(attendance_app.DATA_FILE, "w", newline="") as f:
        f.write("name,year,semester,section,date,time\n")

    attendance_app.app.config["TESTING"] = True
    with attendance_app.app.test_client() as client:
        yield client


def test_index_route(client):
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"Welcome" in rv.data


def test_attendance_submission(client):
    rv = client.post(
        "/attendance",
        data={
            "name": "Test Student",
            "year": "1st Year",
            "semester": "Semester 1",
            "section": "A",
        },
        follow_redirects=True,
    )
    assert rv.status_code == 200
    assert b"Attendance recorded" in rv.data
