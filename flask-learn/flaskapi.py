from flask import Flask, request, jsonify,session

app = Flask(__name__)
# 设置会话密钥
app.secret_key = "2200320211Aa!hgsfdijo2i33"

@app.route('/', methods=["GET", "POST"])
def index():
    return 'Hello, World!'


@app.route('/test/first', methods=["POST"])
def first_post():
    try:
        my_json = request.get_json()
        print(my_json)
        get_name = my_json.get("name")
        get_age = my_json.get("age")

        if not all([get_name, get_age]):
            return jsonify(msg="缺少输入的参数")

        return jsonify({"name": get_name, "age": get_age})
    except Exception as e:
        print(e)
        return jsonify(msg="出错了，重新输入")
@app.route('/test/login',methods=["POST"])
def login():
    get_data = request.get_json()
    username = get_data.get("username")
    password = get_data.get("password")
    if not all ([username, password]):
        return jsonify(msg="参数不完整")
    if username == "admin" and password == 123456:
        #保存登录状态到session中
        session["username"] = username
        return jsonify(msg="登陆成功")
    else:
        return jsonify(msg="用户名或密码错误")

@app.route('/session',methods=["GET"])
def check_session():
    username = session.get("username")
    if username is not None:
        return jsonify(username=username)
    else:
        return jsonify(msg="未登录")
@app.route('/logout',methods=["GET"])
def logout():
    session.clear()
    return jsonify(msg="退出成功")
if __name__ == '__main__':
    app.run(debug=True)
