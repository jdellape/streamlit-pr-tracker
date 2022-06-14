# Contents of ~/my_app/pages/page_3.py
import streamlit as st
import pandas as pd
import altair as alt
import datetime

#This code only for allowing tooltips to display when in full screen mode (https://discuss.streamlit.io/t/tool-tips-in-fullscreen-mode-for-charts/6800/8)
st.markdown('<style>#vg-tooltip-element{z-index: 1000051}</style>',
             unsafe_allow_html=True)

st.markdown("# Tracking 📈")
st.sidebar.markdown("# Tracking 📈")

df = pd.read_json('personal_records.json')

size_dict = {1:30,2:40,3:50,4:60}

dt: datetime.timedelta = datetime.datetime.now()  - df['date'].max()

days_since_last_pr = int(dt / datetime.timedelta(days=1)) % 7
weeks_since_last_pr = int(dt / datetime.timedelta(days=7))

st.header(f"Last PR Occurred: {df['date'].max().date()}")
st.subheader(f"{weeks_since_last_pr} weeks and {days_since_last_pr} days ago")

last_pr = df.tail(1)

st.metric(label=last_pr['lift'].iloc[0] + ' (' + str(last_pr['reps'].iloc[0]) + ')', value=str(last_pr['weight'].iloc[0]) + ' lbs')

#Reformat date and sort it so that it displays most recent prs at top
df['date'] = pd.to_datetime(df['date']).dt.date
df.sort('date', ascending=False)

chart = alt.Chart(df).mark_line(
    point=alt.OverlayMarkDef(color="red")
).encode(
    x='date',
    y='weight',
    tooltip=['lift','reps']
)

st.altair_chart(chart, use_container_width=True)

st.dataframe(df)