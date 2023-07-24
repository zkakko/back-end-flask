from flask import Flask
from flask import request
from datetime import datetime, timedelta
import jwt,logging

app = Flask(__name__)
app.config['DEBUG'] = True

my_secret = "my_secret_key"

def create_token(user):
    expire_time_datetime = datetime.now() + timedelta(hours=1)
    payload ={
        "user": user,
        "expire-timestamp": expire_time_datetime.strftime("%m%d%Y,%H:%M:%S")
    }
    token = jwt.encode(payload=payload, key=my_secret)
    return token

def authentication():
    auth = request.headers.get('Authentication:Bearer')
    if auth:
        token = auth[7:]
        payload = jwt.decode(token, my_secret,algorithms=['HS256'])
        user = payload.get('user')
        return user

@app.route('/')
def hi():
    return "hellos"

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
#        user = request.form.get['user']
#        password = request.form.get['password']
        app.logger.debug(request.json.get('user'))
        user = request.json.get('user')
        password = request.json.get('password')

        
        if user == "Mike" and password == "123":
            token = create_token(user)
            return {"result":"OK","token":token}
        else:
            return {"result":"fail", "reason":"password is wrong"}
        
@app.route('/status',methods=['GET'])
def status():
    authentication()

   
        
if __name__ == '__main__':
    app.run(debug=True)