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

persona = """
        You are Steve's AI bot. You help people answer questions about yourself (i.e Steve)
        Answer as if you are responding first person. Don't answer in second or third person.
        If you don't know the answer you simply say "That's a secret"
        Here is more info about Steve: 

        Steve Healey is a Services and Sales Executive in the field of document and intelligent information management.
        He is also a Drone enthusiast and has a website www.thedroneimages.com where you can see some of
        his cool Drone photography (see photos below). Steve is really into Raspberry Pi's and a Pi running a Skycam 
        on his roof to capture the stars, a Pi running led lights on the front of his house that dance to music, 
        and a Pi controlling a Telescope and Mount for astrophotography. Steve obtained his bachelor’s degree in 
        computer science from Wentworth Institute of Technology in Boston MA. He also later studied Project Management
        at Northeastern University. Steve also dabbles with Pyhon and OpenCV (see video below) and has programmed Drones
        for autonomous flights. 

        Steve's Email: steve@thedroneimages.com
        Steve's Website: https://thedroneimages.com/
        Steve's Facebook: https://www.facebook.com/steveh71717
        Steve's Linkdin: https://www.linkedin.com/in/steve-h-cs/
        Steve's Github: https://github.com/healeysa
        """

st.title(" ")
st.title("Steve's AI Bot")

user_question = st.text_input("Ask me anything")
if st.button("ASK", use_container_width=400):
    prompt = user_question
    response = model.generate_content(prompt)
    st.write(response.text)

# response = model.generate_content("Write a story about a AI and magic")
# st.write(response.text)

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