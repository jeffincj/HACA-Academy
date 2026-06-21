from database import connect_db

class Student:

    def add_student(
        self,
        sid,
        name,
        dept,
        cgpa,
        email
    ):

        db = connect_db()
        cur = db.cursor()

        query = """
        INSERT INTO students
        VALUES(%s,%s,%s,%s,%s)
        """

        values = (
            sid,
            name,
            dept,
            cgpa,
            email
        )

        cur.execute(
            query,
            values
        )

        db.commit()

        cur.close()
        db.close()

    def view_students(self):

        db = connect_db()
        cur = db.cursor()

        cur.execute(
            "SELECT * FROM students"
        )

        data = cur.fetchall()

        cur.close()
        db.close()

        return data