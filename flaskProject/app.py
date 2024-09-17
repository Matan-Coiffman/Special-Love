from flask import Flask

import check_handle
import loginAndSignup

app = Flask(__name__)


@app.route('/signup')
def handle_user_creation():  #פונקציה שמטפלת באופן כללי ביצירת המשתמש
    user_info = loginAndSignup.create_user()
    for i in range(2):
        if not check_handle.check_string_name(user_info[i]):
            print('Error at \'app.py\' line 14 - check names  function')
    if not check_handle.check_password(user_info[2]):
        print('Error at \'app.py\' line 16 - check password function')
    if not check_handle.check_phone_number(3):
        print('Error at \'app.py\' line 18 - check phone number function')
    return 'Hello World!'


if __name__ == '__main__':
    print(check_handle.check_phone_number('0535208597'))
    app.run()
