from flask import Flask, request #
from random import randint#
from dataclasses import dataclass#

app = Flask(__name__)#

@dataclass#
class User:#
    name: str = "Ihor"#
    language: str = "Python"#
    course: str = "Pro"#
    grade: int = 60#

    def __init__(self, name='', language=''):#
        self.name = name#
        self.language = language#
    def choose_course(self, course: str):#
        self.course = course#

    def get_grade(self) -> int:#
        return randint(0, 100)#

user = User()#

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        language = request.form.get("language")
        user = User(name=name, language=language)
        return """
            <h3>Choose a course:</h3>
            <form method="post" action="/course">
              <div>
                <input type="radio" id="python" name="course" value="Python Programming">
                <label for="python">Python Programming</label>
              </div>
              <div>
                <input type="radio" id="java" name="course" value="Java Programming">
                <label for="java">Java Programming</label>
              </div>
              <div>
                <input type="radio" id="web" name="course" value="Web Development">
                <label for="web">Web Development</label>
              </div>
              <button type="submit">Submit</button>
            </form>
        """
    else:
        return """
            <h3>Enter your name and language:</h3>
            <form method="post">
              <div>
                <label for="name">Name:</label>
                <input type="text" id="name" name="name">
              </div>
              <div>
                <label for="language">Language:</label>
                <input type="text" id="language" name="language">
              </div>
              <button type="submit">Submit</button>
            </form>
        """#

@app.route("/course", methods=["POST"])
def course():
    course = request.form.get("course")
    user.choose_course(course)
    return """
        <h3>Your course is selected!</h3>
        <form method="post" action="/grade">
          <button type="submit">Get a grade</button>
        </form>
    """#

@app.route("/grade", methods=["POST"])#
def grade():#
    grade = user.get_grade()#
    return f"""
        <h3>Thank you for using our service, {user.name}!</h3>
        <p>Your information:</p>
        <ul>
          <li>Language: {user.language}</li>
          <li>Course: {user.course}</li>
          <li>Grade: {grade}</li>
        </ul>
    """

if __name__ == "__main__":#
    app.run(host='0.0.0.0', port=8000, debug=True)
