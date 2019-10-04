from  functions import userRegform
from functions.userRegform import createUser, tom

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
    