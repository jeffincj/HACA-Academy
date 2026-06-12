import pandas as pd
import numpy as np

from database import connect_db

def student_report():

    db = connect_db()

    df = pd.read_sql(
        "SELECT * FROM students",
        db
    )

    print("\n===== STUDENT REPORT =====")

    print(df)

    print("\nAverage CGPA")
    print(round(
        np.mean(df["cgpa"]),
        2
    ))

    print("\nHighest CGPA")
    print(
        np.max(df["cgpa"])
    )

    db.close()