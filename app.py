from flask import Flask,redirect,url_for,render_template,request,send_file
app = Flask(__name__, template_folder='../templates')
@app.route('/')
def tour():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True) 