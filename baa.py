import streamlit as st

from BA_AI import analyse_business_idea


st.set_page_config(
    page_title="Business Idea Reality Check",
    page_icon="💡",
    layout="centered"
)

st.title("💡 Business Idea Reality Check")

st.write(
    "Explore your business idea, understand your potential "
    "customers and identify opportunities and challenges "
    "before investing."
)

st.subheader("Tell us about your business idea")

business_idea = st.text_area(
    "What business do you want to start?",
    placeholder="Example: An online bakery selling custom cakes"
)

location = st.text_input(
    "Where do you intend to operate?",
    placeholder="Example: Lagos, Nigeria"
)

target_customers = st.text_area(
    "Who are your intended customers?",
    placeholder="Example: Young professionals, families and event planners"
)


if st.button("Analyse My Business Idea", type="primary"):

    if not business_idea or not location or not target_customers:
        st.warning("Please complete all three fields.")

    else:
        with st.spinner("Analysing your business idea..."):

            try:
                result = analyse_business_idea(
                    business_idea,
                    location,
                    target_customers
                )

                st.success("Your business assessment is ready!")

                st.subheader("Your Business Idea Assessment")

                st.markdown(result)

            except Exception as e:
                st.error(f"Something went wrong: {e}")