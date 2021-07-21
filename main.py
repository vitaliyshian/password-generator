from pass_generator import PassGenerator
from flask import Flask
from flask import request, redirect, url_for, render_template, make_response

app = Flask(__name__, static_url_path='', static_folder='assets', template_folder='assets')

@app.route('/')
def index():
    return render_template('password.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
   length_pass = request.form.get('pass_length')
   pass_genery = PassGenerator()
   create_pass_genery = pass_genery.random_generator(length_pass)
   return '<h1>{0}</h1>'.format(create_pass_genery)

if __name__ == '__main__':
    app.run()

    #pass_genery = PassGenerator()
    # length_pass = input("Password length ?\n")
    # create_pass_genery = pass_genery.random_generator(length_pass)
    # print(create_pass_genery)

