import streamlit as st

if "grams" not in st.session_state:
    st.session_state.grams = None

st.markdown("""
    <style>
    .stButton > button {
        width: 100%;
        margin-top: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)


def calculate_pours(grams):
    total_water = grams * 15
    first_pour = grams * 2
    addition_water = round((total_water - first_pour) / 3)

    second_pour = round(first_pour + addition_water)
    third_pour = round(second_pour + addition_water)
    fourth_pour = round(third_pour + addition_water)

    return {
        "total_water": total_water,
        "first_pour": first_pour,
        "second_pour": second_pour,
        "third_pour": third_pour,
        "fourth_pour": fourth_pour,
    }


st.title("Coffee Pour Calculator")

with st.container():
    st.subheader("Quick Select")
    col1, col2 = st.columns(2, gap="small")

    with col1:
        if st.button("One Cup"):
            st.session_state.grams = 16
    with col2:
        if st.button("Two Cups"):
            st.session_state.grams = 30

st.markdown("<div style='margin-top: 32px;'></div>", unsafe_allow_html=True)

grams = st.number_input(
    "Enter coffee grams:",
    min_value=0,
    step=1,
    key="grams"
)

if st.button("Calculate"):
    result = calculate_pours(grams)
    st.success(f"Total Water: {result['total_water']} ml")
    st.markdown("---")
    st.info(f"First pour: {result['first_pour']} ml")
    st.info(f"Second pour: {result['second_pour']} ml")
    st.info(f"Third pour: {result['third_pour']} ml")
    st.info(f"Fourth pour: {result['fourth_pour']} ml")
