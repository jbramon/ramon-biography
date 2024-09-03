import streamlit as st
import time
import pandas as pd
 
# Title and Subtitle
st.title("My Autobiography & Portfolio")
st.subheader("Welcome to my personal page!")

# Display the image above the title
st.image("biography.jpg")
 
# Autobiography Section
st.header("Autobiography")
st.write("""
Hi, I'm John Bryan P. Ramon, an enthusiastic IT student and web developer in - progress. 
Born and raised in Urgello, Cebu City, I discovered my fondness for technology - related subjects at a fairly young age. I am currently a BSIT 4th year student
in Cebu Institute of Technology University where I am honing and refining my skills in programming. I aim to master different programming languages to be able to create and code useful and meaningful web app and mobile applications that are also user - friendly to users.
""")
 
# Adding a Divider
st.markdown("---")
 
# Portfolio Section
st.header("Portfolio")
 
# Project 1
st.subheader("Project: Peer to Peer Development Website")
st.write("""
Developed a full-stack Peer to Peer Development Platform, where students can share and post their projects/works to be assessed by other students, using Spring Boot and React. Students can assess each other's work with the goal of giving constructive criticism to help their peers improve in their projects. The website also has a filter system to block certain offending/inappropriate and unproductive words so as to maintain the website's student - friendly and toxic free environment. 
""")
 

# Adding a Contact Form with your information
st.header("Contact Me")
st.write("Feel free to reach out to me through the form below or directly via email:")
 
# Displaying contact information
st.write("**Name:** John Bryan P. Ramon")
st.write("**Email:** ramonbryan2001@gmail.com")
st.write("**Contact no.:** 09912106498")
 
# Adding Social Media Links
st.header("Find me on Social Media")
st.write("""
- [FaceBook](https://www.facebook.com/bryan.ramon2001/)
- [GitHub](https://github.com/jbramon)

""")
 
# Adding an Expander Section for Skills
st.header("Skills")
with st.expander("Programming Languages"):
    st.write("""
    - c++
    - Python
    - Java
    - JavaScript
    - TypeScript
    """)
with st.expander("Frameworks & Libraries"):
    st.write("""
    - Spring Boot
    - React
    - Streamlit
    """)
with st.expander("Tools & Platforms"):
    st.write("""
    - EclipseIDE
    - MySQL
    - Git
    - Visual Studio Code
    """)
 
# Adding a Progress Bar for Fun
st.header("A Fun Progress Bar")
progress_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.05)
    progress_bar.progress(percent_complete + 1)
 
# Footer
st.write("Thank you for visiting my page!")