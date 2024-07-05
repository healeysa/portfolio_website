import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hello :wave:")
    st.title("I'm Steve Healey")

with col2:
    st.image("images/steve.png")

#
# persona = """ You are Murtaza AI bot. You help people answer questions about your self (i.e Murtaza)
#  Answer as if you are responding . dont answer in second or third person.
# If you don't know they answer you simply say "That's a secret"
#
#
# st.title(" ")
# st.title("Steve's AI Bot")
#
# user_question = st.text_input("Ask me anything")
# if st.button("ASK", use_container_width=400):
#     prompt = user_question
#     response = model.generate_content(prompt)
#     st.write(response.text)
#
# # response = model.generate_content("Write a story about a AI and magic")
# # st.write(response.text)

st.title(" ")

col1, col2 = st.columns(2)

with col1:
    st.subheader("YouTube Channel")
    st.write("- OpenCV Sample Video")

with col2:
    st.video("https://www.youtube.com/watch?v=DF7mNSgyKH8")

st.write(" ")
st.title("My Setup")
st.image("images/setup1.jpg")

st.write(" ")
st.title("My Skills")
st.slider("Programming", 0, 100, 82)
st.slider("Python", 0, 100, 75)
st.slider("AI", 0, 100, 60)

st.write(" ")
st.title("Drone Photo Gallery")

col1, col2, col3 = st.columns(3)

# Try to run as a Nested Loop

with col1:
    st.image("images/s1.jpg")
    st.image("images/s2.jpg")
    st.image("images/s3.jpg")

with col2:
    st.image("images/s4.jpg")
    st.image("images/s5.jpg")
    st.image("images/s6.jpg")

with col3:
    st.image("images/s7.jpg")
    st.image("images/s8.jpg")
    st.image("images/s9.jpg")

st.subheader(" ")
st.write("CONTACT INFO")

st.write(" ")
st.title("For inquiries, email me at")

st.subheader("steve@thedroneimages.com")