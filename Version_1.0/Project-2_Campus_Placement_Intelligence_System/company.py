from database import connect_db

class Company:

    def add_company(
        self,
        cid,
        cname,
        min_cgpa,
        skill
    ):

        db = connect_db()
        cur = db.cursor()

        query = """
        INSERT INTO companies
        VALUES(%s,%s,%s,%s)
        """

        cur.execute(
            query,
            (cid, cname, min_cgpa, skill)
        )

        db.commit()

        cur.close()
        db.close()

    def view_companies(self):

        db = connect_db()
        cur = db.cursor()

        cur.execute(
            "SELECT * FROM companies"
        )

        data = cur.fetchall()

        cur.close()
        db.close()

        return data