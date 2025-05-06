import os
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return (

        "Fullname: Inah Laine M. Pacatang<br>"
        "Section: BSIT 3A 1st 25<br>"
        "Subject: System Integration<br>"
        "Semi_Final Exam"
    )
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


