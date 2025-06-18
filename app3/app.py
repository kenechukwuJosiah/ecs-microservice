from datetime import datetime
import random
import string

from . import create_app

flask_app = create_app()


@flask_app.route('/')
def hello() -> str:
    ''' Return a friendly HTTP greeting '''
    return f'Hello, World from flask app 3! Time is {datetime.now()}'


@flask_app.route('/return_message')
def get_message() -> str:
    ''' endpoint to test AWS ECS Service Connect functionality '''
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    return f'Random string from flask_app_3: {random_str}'

# if __name__ == '__main__':
#     flask_app.run(host='0.0.0.0')
