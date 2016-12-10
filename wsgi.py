from uTrip import app

app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
if __name__ == "__main__":
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()
