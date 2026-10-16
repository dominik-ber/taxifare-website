import streamlit as st
import datetime
import requests

'''
# TaxiFare - predict your taxi fare!
'''

st.markdown('''
We only need a few simple inputs from you...
''')

pu_datetime = st.datetime_input("What is the date and time of pick up?")
pu_longitude = st.number_input("What is the pickup longitude?",key=1,min_value=-74.3,max_value=-73.7)
pu_latitude = st.number_input("What is the pickup latitude?",key=2,min_value=40.5,max_value=40.9)
do_longitude = st.number_input("What is the dropoff longitude?",key=3,min_value=-74.3,max_value=-73.7)
do_latitude = st.number_input("What is the dropoff latitude?",key=4,min_value=40.5,max_value=40.9)
passenger_count = st.number_input("What is the passenger count?",min_value=1,max_value=7,step=1,key=5)


url = 'https://taxifare.lewagon.ai/predict'

# 2. Let's build a dictionary containing the parameters for our API...
params = {
    "pickup_datetime": pu_datetime,
    "pickup_longitude": pu_longitude,
    "pickup_latitude": pu_latitude,
    "dropoff_longitude": do_longitude,
    "dropoff_latitude": do_latitude,
    "passenger_count": int(passenger_count),
}

# Green, rectangular button
st.markdown('''
<style>
button[kind="primary"] {
    background-color: #2e9e44;
    border-color: #2e9e44;
    border-radius: 0;
    color: white;
}
button[kind="primary"]:hover {
    background-color: #25833a;
    border-color: #25833a;
    color: white;
}
</style>
''', unsafe_allow_html=True)

# 3. Let's call our API using the `requests` package (only when the button is clicked)...
if st.button("Calculate Fare", type="primary"):
    response = requests.get(url, params=params)

    # 4. Let's retrieve the prediction from the **JSON** returned by the API...
    ## Finally, we can display the prediction to the user
    if response.status_code == 200:
        prediction = response.json()["fare"]
        st.success(f"Estimated fare: ${prediction:.2f}")
    else:
        st.error(f"API error {response.status_code}: {response.text}")
