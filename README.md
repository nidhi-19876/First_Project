# Student Attendance Tracker

A minimal Flask application for recording and viewing student attendance. Data is stored in a CSV file (`data/attendance.csv`).

## Features

- Mark attendance by entering name, year, semester, and section.
- Review all records in a report table.
- Search/filter records (both server-side and client-side).
- Download full CSV or clear all entries from the report page.
- Animated background and responsive design.
- Flash messages for user feedback.
- Automatically creates data directory and header row.

## Getting Started

1. **Install dependencies**

   ```bash
   python -m pip install -r requirements.txt
   ```

   _Tip_: you can trim unused packages from `requirements.txt` if you don't need `numpy`/`pandas`.

2. **Run locally**

   ```bash
   set FLASK_APP=app.py       # PowerShell on Windows
   flask run
   # or simply
   python app.py
   ```

   Visit `http://127.0.0.1:5000` in your browser.
4. **Run tests** (requires `pytest` in your environment):

   ```bash
   pytest
   ```

   The suite verifies the index page loads and that submissions are accepted.

3. **Configuration**

   - Environment variables accepted:
     - `HOST` and `PORT` for binding address.
     - `DEBUG` ("true"/"false").
     - `SECRET_KEY` to override the default.

4. **Deployment**

   The application is WSGI-compliant and can be deployed to any provider (Heroku, PythonAnywhere, etc.). Add a `Procfile` with:

   ```text
   web: gunicorn app:app
   ```

   Make sure `gunicorn` is added to `requirements.txt`.

## Improvements

- Consider switching to SQLite or another database for concurrency and querying.
- Add authentication if attendance should be restricted.
- Use JavaScript charting or API endpoints for visual summaries.
- Replace CSV storage with an ORM (e.g. SQLAlchemy) for scalability.

---

Feel free to customize the UI or extend the functionality!
