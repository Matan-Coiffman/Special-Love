from flask import Flask

import check_handle

app = Flask(__name__)


@app.route('/signup')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    print(check_handle.check_phone_number('0535208597'))
    app.run()


class SignupPage:
    pass
