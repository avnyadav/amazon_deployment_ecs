from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return "Hello avnish!! You did it. Let's do the development"


if __name__=="__main__":
    app.run(port=5005)
