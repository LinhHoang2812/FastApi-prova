import streamlit as st
import requests
import json


def app():
    st.title("Predict profit")
    rd = st.number_input("R&D spend", value=165349.2)
    administration = st.number_input("Administration spend", value=136897.8)
    marketing = st.number_input("Marketing spend", value=471784.1)
    if st.button("Predict with GET"):
        params = {"rd": rd, "administration": administration, "marketing": marketing}
        response = requests.get("http://127.0.0.1:8000/predict", params=params)
        result = response.json()
        st.success(f"The result is: {result}")

    if st.button("Predict with POST"):
        params = {"rd": rd, "administration": administration, "marketing": marketing}
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            headers={"Content-Type": "application/json"},
            data=json.dumps(
                {"rd": rd, "administration": administration, "marketing": marketing}
            ),
        )
        result = response.json()
        st.success(f"The result is: {result}")


if __name__ == "__main__":
    app()
