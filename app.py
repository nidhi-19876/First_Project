from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/attendance', methods=['GET','POST'])
def attendance():
    if request.method == 'POST':
        name = request.form.get('name')
        year = request.form.get('year')
        semester = request.form.get('semester')
        section = request.form.get('section')

        if name:
            date = datetime.now().strftime("%Y-%m-%d")
            time = datetime.now().strftime("%H:%M:%S")
            with open('data/attendance.csv','a',newline='') as f:
                writer = csv.writer(f)
                writer.writerow([name, year, semester, section, date, time])
        return redirect('/report')
    return render_template('attendance.html')

@app.route('/report')
def report():
    search = request.args.get('search')
    data = []

    try:
        with open('data/attendance.csv','r') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
    except:
        pass

    if search:
        data = sorted(data, key=lambda x: search.lower() not in x[0].lower())

    return render_template('report.html', data=data, today=datetime.now().strftime("%Y-%m-%d"))

if __name__ == "__main__":
    app.run(debug=True)