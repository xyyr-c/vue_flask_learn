from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    t_int = 20
    t_str = 'xyyr'
    t_list = [1,2,3,4,5]
    t_dict = {'name':'xyyr', 'age':20}

    return render_template('index2.html', my_int=t_int, my_str=t_str, my_list=t_list, my_dict=t_dict)

if __name__ == '__main__':
    app.run(debug=True)