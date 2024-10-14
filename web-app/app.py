from flask import Flask, render_template

app = Flask(__name__)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    return render_template('form.html')


@app.route('/all')
def get_all_students():
    return render_template('students.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
