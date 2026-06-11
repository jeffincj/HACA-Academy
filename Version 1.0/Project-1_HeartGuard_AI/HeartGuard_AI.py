import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# HEARTGUARD AI
# Heart Disease Risk Analysis System
# ==========================================

st.set_page_config(
    page_title="HeartGuard AI",
    page_icon="❤️",
    layout="wide"
)

st.title("❤️ HeartGuard AI")
st.subheader("Heart Disease Risk Analysis Dashboard")

# ==========================================
# SESSION STORAGE
# ==========================================

if "patients" not in st.session_state:
    st.session_state.patients = []

# ==========================================
# SIDEBAR MENU
# ==========================================

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Add Patient",
        "View Patients",
        "Risk Analytics"
    ]
)

# ==========================================
# ADD PATIENT
# ==========================================

if menu == "Add Patient":

    st.header("➕ Add Patient")

    name = st.text_input("Patient Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        step=1
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    bp = st.number_input(
        "Blood Pressure",
        min_value=0
    )

    sugar = st.number_input(
        "Sugar Level",
        min_value=0
    )

    chol = st.number_input(
        "Cholesterol Level",
        min_value=0
    )

    if st.button("Analyze Risk"):

        risk = 0

        # BP
        if bp > 140:
            risk += 30
        elif bp > 120:
            risk += 15

        # Sugar
        if sugar > 180:
            risk += 30
        elif sugar > 120:
            risk += 15

        # Cholesterol
        if chol > 240:
            risk += 30
        elif chol > 200:
            risk += 15

        # Age
        if age > 60:
            risk += 10
        elif age > 40:
            risk += 5

        if risk <= 30:
            category = "Low Risk"

        elif risk <= 60:
            category = "Moderate Risk"

        else:
            category = "High Risk"

        st.session_state.patients.append(
            {
                "Name": name,
                "Age": age,
                "Gender": gender,
                "BP": bp,
                "Sugar": sugar,
                "Cholesterol": chol,
                "Risk": risk,
                "Category": category
            }
        )

        st.metric(
            "Risk Score",
            f"{risk}%"
        )

        if category == "Low Risk":
            st.success(category)

        elif category == "Moderate Risk":
            st.warning(category)

        else:
            st.error(category)

# ==========================================
# VIEW PATIENTS
# ==========================================

elif menu == "View Patients":

    st.header("📋 Patient Records")

    if len(st.session_state.patients) == 0:

        st.warning("No Patient Records Found")

    else:

        df = pd.DataFrame(
            st.session_state.patients
        )

        st.dataframe(
            df,
            use_container_width=True
        )

# ==========================================
# ANALYTICS
# ==========================================

elif menu == "Risk Analytics":

    st.header("📊 Heart Disease Analytics")

    if len(st.session_state.patients) == 0:

        st.warning(
            "Please Add Patients First"
        )

    else:

        df = pd.DataFrame(
            st.session_state.patients
        )

        highest_risk = df["Risk"].max()

        lowest_risk = df["Risk"].min()

        avg_risk = round(
            df["Risk"].mean(),
            2
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Highest Risk",
            f"{highest_risk}%"
        )

        c2.metric(
            "Lowest Risk",
            f"{lowest_risk}%"
        )

        c3.metric(
            "Average Risk",
            f"{avg_risk}%"
        )

        # ==========================
        # BAR CHART
        # ==========================

        st.subheader(
            "Risk Percentage by Patient"
        )

        fig1, ax1 = plt.subplots(
            figsize=(8,5)
        )

        colors = []

        for risk in df["Risk"]:

            if risk <= 30:
                colors.append("green")

            elif risk <= 60:
                colors.append("orange")

            else:
                colors.append("red")

        ax1.bar(
            df["Name"],
            df["Risk"],
            color=colors
        )

        ax1.axhline(
            y=60,
            color="red",
            linestyle="--"
        )

        ax1.set_title(
            "Heart Disease Risk"
        )

        ax1.set_ylabel(
            "Risk Percentage"
        )

        st.pyplot(fig1)

        # ==========================
        # AGE GROUP ANALYSIS
        # ==========================

        risk_0_20 = 0
        risk_21_40 = 0
        risk_41_60 = 0
        risk_60_plus = 0

        for i in range(len(df)):

            age = df.iloc[i]["Age"]
            risk = df.iloc[i]["Risk"]

            if age <= 20:
                risk_0_20 += risk

            elif age <= 40:
                risk_21_40 += risk

            elif age <= 60:
                risk_41_60 += risk

            else:
                risk_60_plus += risk

        st.subheader(
            "Risk Distribution by Age Group"
        )

        fig2, ax2 = plt.subplots(
            figsize=(6,6)
        )

        age_groups = [
            "0-20",
            "21-40",
            "41-60",
            "60+"
        ]

        values = [
            risk_0_20,
            risk_21_40,
            risk_41_60,
            risk_60_plus
        ]

        ax2.pie(
            values,
            labels=age_groups,
            autopct="%1.1f%%"
        )

        ax2.set_title(
            "Risk Distribution"
        )

        st.pyplot(fig2)

        # ==========================
        # PATIENT SUMMARY
        # ==========================

        st.subheader(
            "Patient Summary"
        )

        st.dataframe(df)

