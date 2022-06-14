import streamlit as st
import json

st.markdown("# New Personal Record! 🏋")
st.sidebar.markdown("# New Personal Record! 🏋")

LIFT_OPTIONS = ['Power Clean','Back Squat','Push Press','Deadlift','Front Squat', 'Bench Press']

with st.form("add_pr"):
    lift = st.selectbox('Lift', LIFT_OPTIONS)
    weight = st.number_input('Weight', min_value=0)
    reps = st.number_input('Reps', min_value=1)
    date = str(st.date_input('Date'))

    submitted = st.form_submit_button("Submit")
    if submitted:
            with open('personal_records.json', 'r+') as jf:
                pr_dict = {'lift':lift,'weight':weight, 'reps':reps, 'date':date}
                file_data = json.load(jf)
                file_data.append(pr_dict)
                jf.seek(0)
                json.dump(file_data, jf, indent=2)