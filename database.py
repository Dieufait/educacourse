from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION']

engine = create_engine(db_connection_string, 
                      connect_args={
                        "ssl":{
                          "ssl_ca": "/etc/ssl/cert.pem"
                        }
})


def load_courses_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from courses"))
    courses = []
    for row in result.all():
      courses.append(row._asdict())
    return courses


def load_course_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM courses WHERE id = {id}")
    )
    
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()


def add_enrollment_to_db(course_id, data):
  with engine.connect() as conn:
    query= text('INSERT INTO enrollments(course_id, full_name, email, linkedin_url, grade) VALUES(:course_id, :full_name, :email, :linkedin_url, :grade)')
    conn.execute(query,{'course_id':course_id, 'full_name':data['full_name'],'email':data['email'],'linkedin_url':data['linkedin_url'],'grade':data['grade']})
