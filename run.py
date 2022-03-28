##(was)start of flask framework webapp##its now a run.py file only##
from flaskweb import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
