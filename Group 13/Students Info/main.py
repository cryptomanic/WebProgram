from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home_page.html')
@app.route('/<username>')
def user_page(username):
    if username == 'deepak':
        return render_template('deepak.html')
    elif username == 'amrinder':
        return render_template('amrinder.html')
    elif username == 'chandrakant':
        return render_template('chandrakant.html')
    
    

if __name__ == '__main__':
    app.run()
