from flask import Flask, render_template, jsonify, request
from database import load_courses_from_db,load_course_from_db, add_enrollment_to_db



app = Flask(__name__)


@app.route("/")
def hello_educa():
  courses = load_courses_from_db()
  return render_template('home.html',courses=courses)

@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/api/courses")
def list_course():
  courses = load_courses_from_db()
  return jsonify(courses)




@app.route("/course/<id>")
def show_course(id):
  course = load_course_from_db(id)
  if not course:
    return "Not Found", 404
  return render_template('coursepage.html', course=course)


@app.route("/api/course/<id>")
def show_course_json(id):
  course=load_course_from_db(id)
  return jsonify(course)


@app.route("/course/<id>/enroll", methods=['post'])
def apply_to_course(id):
  data = request.form
  course = load_course_from_db(id)
  add_enrollment_to_db(id, data)
  # store this in the DB
  return render_template('enrollment_submitted.html',enrollment=data, course=course)



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)