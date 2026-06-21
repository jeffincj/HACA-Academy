import pandas as pd
from database import connect_db

def get_student_report():

    db = connect_db()

    df = pd.read_sql(
        "SELECT * FROM students",
        db
    )

    db.close()

    return df