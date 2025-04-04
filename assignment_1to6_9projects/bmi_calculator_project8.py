import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="😍", layout="centered")

st.title("BMI Calculator")
st.markdown("## Calculate your bmi ")

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (kg):", min_value=0.0, max_value=500.0, step=0.1, format="%.2f")

with col2:
    height = st.number_input("Height (m):", min_value=0.0, max_value=3.0, step=0.01, format="%.2f")

if height > 0 and weight > 0:
    bmi = weight / (height ** 2)
    st.success(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        st.error("You are underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight")
    else:
        st.error("You are obese")
else:
    st.error("Please enter a valid height and weight")



