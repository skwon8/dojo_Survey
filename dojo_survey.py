from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'iCanDoThis'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/result_present', methods=['POST'])
def result_present():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')


@app.route('/clear_session')
def clear():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
