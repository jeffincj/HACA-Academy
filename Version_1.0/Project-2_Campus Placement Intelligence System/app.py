import streamlit as st
import pandas as pd

from student import Student
from company import Company
from placement_ai import PlacementAI
from analytics import get_student_report

# ======================
# PAGE CONFIG
# ======================

st.set_page_config(
    page_title="PlacementPilot AI",
    page_icon="🚀",
    layout="wide"
)

# ======================
# OBJECTS
# ======================

student = Student()
company = Company()
ai = PlacementAI()

# ======================
# TITLE
# ======================

st.title("🚀 PlacementPilot AI")

# ======================
# SIDEBAR MENU
# ======================

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Dashboard",
        "Add Student",
        "View Students",
        "Add Company",
        "View Companies",
        "Placement Score"
    ]
)

# ======================
# DASHBOARD
# ======================

if menu == "Dashboard":

    st.header("📊 Dashboard")

    df = get_student_report()

    if df.empty:

        st.warning(
            "No Student Records Found"
        )

    else:

        st.dataframe(
            df,
            use_container_width=True
        )

        st.subheader("Statistics")

        st.write(
            "Total Students:",
            len(df)
        )

        if "cgpa" in df.columns:

            st.write(
                "Average CGPA:",
                round(
                    df["cgpa"].mean(),
                    2
                )
            )

            st.write(
                "Highest CGPA:",
                df["cgpa"].max()
            )

            st.subheader(
                "CGPA Chart"
            )

            chart_data = df.set_index(
              "name"
            )["cgpa"]

            st.bar_chart(
              chart_data
            )
# ======================
# ADD STUDENT
# ======================

elif menu == "Add Student":

    st.header(
        "👨‍🎓 Student Registration"
    )

    sid = st.number_input(
        "Student ID",
        step=1
    )

    name = st.text_input(
        "Name"
    )

    dept = st.text_input(
        "Department"
    )

    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        step=0.1
    )

    email = st.text_input(
        "Email"
    )

    if st.button(
        "Add Student"
    ):

        try:

            student.add_student(
                sid,
                name,
                dept,
                cgpa,
                email
            )

            st.success(
                "Student Added Successfully"
            )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )

# ======================
# VIEW STUDENTS
# ======================

elif menu == "View Students":

    st.header(
        "📋 Students"
    )

    data = student.view_students()

    df = pd.DataFrame(
        data,
        columns=[
            "Student ID",
            "Name",
            "Department",
            "CGPA",
            "Email"
        ]
    )

    df = df.sort_values(
        by="Student ID"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

# ======================
# ADD COMPANY
# ======================

elif menu == "Add Company":

    st.header(
        "🏢 Add Company"
    )

    cid = st.number_input(
        "Company ID",
        step=1
    )

    cname = st.text_input(
        "Company Name"
    )

    min_cgpa = st.number_input(
        "Minimum CGPA",
        min_value=0.0,
        max_value=10.0,
        step=0.1
    )

    skill = st.text_area(
        "Required Skill"
    )

    if st.button(
        "Add Company"
    ):

        try:

            company.add_company(
                cid,
                cname,
                min_cgpa,
                skill
            )

            st.success(
                "Company Added Successfully"
            )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )

# ======================
# VIEW COMPANIES
# ======================

elif menu == "View Companies":

    st.header(
        "🏢 Companies"
    )

    data = company.view_companies()

    df = pd.DataFrame(
        data,
        columns=[
            "Company ID",
            "Company Name",
            "Minimum CGPA",
            "Required Skill"
        ]
    )

    df = df.sort_values(
        by="Company ID"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

# ======================
# PLACEMENT SCORE
# ======================

elif menu == "Placement Score":

    st.header(
        "🤖 Placement Readiness Report"
    )

    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        step=0.1
    )

    skills = st.number_input(
        "Number of Skills",
        min_value=0,
        step=1
    )

    if st.button(
        "Calculate"
    ):

        score, status = ai.readiness_score(
            cgpa,
            skills
        )

        st.metric(
            "Placement Score",
            score
        )

        st.success(
            status
        )

        st.subheader(
            "Recommended Roles"
        )

        if score >= 90:

            st.write(
                "✅ Software Engineer"
            )

            st.write(
                "✅ Data Analyst"
            )

            st.write(
                "✅ Python Developer"
            )

        elif score >= 70:

            st.write(
                "✅ Junior Developer"
            )

            st.write(
                "✅ QA Engineer"
            )

        else:

            st.write(
                "⚠ Improve Skills"
            )

            st.write(
                "⚠ Practice Projects"
            )

# ======================
# FOOTER
# ======================

st.markdown("---")

st.caption(
    "PlacementPilot AI | Built using Python, MySQL, Pandas and Streamlit"
)