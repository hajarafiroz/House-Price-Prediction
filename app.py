import streamlit as st
import pandas as pd
import joblib


# ---------------- LOAD MODEL ----------------

model = joblib.load("models/house_price_model.pkl")
le = joblib.load("models/label_encoder.pkl")


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="House Price AI",
    page_icon="🏠",
    layout="wide"
)


# ---------------- CUSTOM CSS ----------------

st.markdown(
"""
<style>

.stApp {

    background:
    linear-gradient(
    135deg,
    #0f2027,
    #203a43,
    #2c5364);

}


/* Title */

.title {

    font-size:48px;
    font-weight:900;
    text-align:center;
    color:white;

}


.subtitle {

    text-align:center;
    color:#dddddd;
    font-size:20px;

}


/* Cards */

.card {

    background:rgba(255,255,255,0.12);

    padding:25px;

    border-radius:20px;

    backdrop-filter:blur(12px);

    color:white;

}


/* Button */

.stButton button {


    width:100%;

    height:55px;

    border-radius:15px;

    background:#00ff99;

    color:black;

    font-size:20px;

    font-weight:bold;

}


.stButton button:hover {

    background:#00cc77;

}


/* Result */

.result {

    background:rgba(0,255,150,0.18);

    padding:30px;

    border-radius:25px;

    text-align:center;

    color:white;

}


h1,h2,h3,p,label {

    color:white !important;

}


</style>
""",
unsafe_allow_html=True
)



# ---------------- HEADER ----------------


st.markdown(
"""
<div class="title">
🏠 House Price Prediction
</div>

<div class="subtitle">
AI Powered Real Estate Price Estimation System
</div>

<br>

""",
unsafe_allow_html=True
)



# ---------------- SIDEBAR ----------------


st.sidebar.markdown(
"## 🏡 House Details"
)



area = st.sidebar.number_input(
    "📐 Area (sq ft)",
    500,
    20000,
    5000
)


bedrooms = st.sidebar.slider(
    "🛏 Bedrooms",
    1,
    10,
    3
)


bathrooms = st.sidebar.slider(
    "🚿 Bathrooms",
    1,
    5,
    2
)


stories = st.sidebar.slider(
    "🏢 Stories",
    1,
    5,
    2
)


parking = st.sidebar.slider(
    "🚗 Parking",
    0,
    5,
    1
)




# ---------------- MAIN INPUTS ----------------


col1,col2 = st.columns(2)



with col1:

    st.markdown(
    "<div class='card'>",
    unsafe_allow_html=True
    )


    st.subheader("🏠 Facilities")


    mainroad = st.selectbox(
        "Main Road",
        ["yes","no"]
    )


    guestroom = st.selectbox(
        "Guest Room",
        ["yes","no"]
    )


    basement = st.selectbox(
        "Basement",
        ["yes","no"]
    )


    airconditioning = st.selectbox(
        "Air Conditioning",
        ["yes","no"]
    )


    st.markdown(
    "</div>",
    unsafe_allow_html=True
    )





with col2:


    st.markdown(
    "<div class='card'>",
    unsafe_allow_html=True
    )


    st.subheader("✨ Extra Features")


    hotwaterheating = st.selectbox(
        "Hot Water Heating",
        ["yes","no"]
    )


    prefarea = st.selectbox(
        "Preferred Area",
        ["yes","no"]
    )


    furnishingstatus = st.selectbox(
        "Furnishing Status",
        [
            "furnished",
            "semi-furnished",
            "unfurnished"
        ]
    )


    st.markdown(
    "</div>",
    unsafe_allow_html=True
    )




st.write("")



# ---------------- PREDICT ----------------


if st.button("🔮 Predict House Price"):


    mainroad = 1 if mainroad=="yes" else 0

    guestroom = 1 if guestroom=="yes" else 0

    basement = 1 if basement=="yes" else 0

    hotwaterheating = 1 if hotwaterheating=="yes" else 0

    airconditioning = 1 if airconditioning=="yes" else 0

    prefarea = 1 if prefarea=="yes" else 0



    furnishingstatus = le.transform(
        [furnishingstatus]
    )[0]



    input_data = pd.DataFrame([{

        "area":area,

        "bedrooms":bedrooms,

        "bathrooms":bathrooms,

        "stories":stories,

        "mainroad":mainroad,

        "guestroom":guestroom,

        "basement":basement,

        "hotwaterheating":hotwaterheating,

        "airconditioning":airconditioning,

        "parking":parking,

        "prefarea":prefarea,

        "furnishingstatus":furnishingstatus

    }])



    prediction = model.predict(input_data)[0]



    st.markdown(

    f"""

    <div class="result">

    <h2>🏠 Estimated House Price</h2>

    <h1>
    ₹ {prediction:,.2f}
    </h1>

    <p>
    Prediction generated using Machine Learning Model
    </p>


    </div>

    """,

    unsafe_allow_html=True

    )



# ---------------- FOOTER ----------------


st.markdown(
"""
<br>

<center style="color:white">

Built with Python + Machine Learning + Streamlit 🚀

</center>

""",
unsafe_allow_html=True
)