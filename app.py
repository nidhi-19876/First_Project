import os
import csv
from datetime import datetime

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    send_file,
)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev_secret")

# --- data file setup ---------------------------------------------------
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
DATA_FILE = os.path.join(DATA_DIR, "attendance.csv")

os.makedirs(DATA_DIR, exist_ok=True)
if not os.path.exists(DATA_FILE):
    # create file with header row
    with open(DATA_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "year", "semester", "section", "date", "time"])


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/attendance", methods=["GET", "POST"])
def attendance():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        year = request.form.get("year", "").strip()
        semester = request.form.get("semester", "").strip()
        section = request.form.get("section", "").strip()

        if name and year and semester and section:
            date = datetime.now().strftime("%Y-%m-%d")
            time = datetime.now().strftime("%H:%M:%S")
            with open(DATA_FILE, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([name, year, semester, section, date, time])
            flash(f"Attendance recorded for {name}.")
            return redirect(url_for("report"))
        else:
            flash("Please fill in all fields.", "error")
    return render_template("attendance.html")


@app.route("/report")
def report():
    search = request.args.get("search", "").strip()
    data = []

    try:
        with open(DATA_FILE, "r", newline="") as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            for row in reader:
                data.append(row)
    except Exception as e:
        app.logger.debug("could not read data file: %s", e)

    if search:
        data = [r for r in data if search.lower() in r[0].lower()]

    # sort by date then time (newest first)
    try:
        data.sort(key=lambda r: (r[4], r[5]), reverse=True)
    except Exception:
        pass

    return render_template(
        "report.html", data=data, today=datetime.now().strftime("%Y-%m-%d")
    )


@app.route("/download")
def download():
    try:
        return send_file(DATA_FILE, as_attachment=True)
    except Exception:
        flash("No data available to download", "error")
        return redirect(url_for("report"))


@app.route("/clear", methods=["POST"])
def clear():
    try:
        with open(DATA_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "year", "semester", "section", "date", "time"])
        flash("All records cleared.")
    except Exception as e:
        flash(f"Error clearing data: {e}", "error")
    return redirect(url_for("report"))


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(
        host=os.environ.get("HOST", "0.0.0.0"),
        port=int(os.environ.get("PORT", 5000)),
        debug=os.environ.get("DEBUG", "true").lower() == "true",
    )