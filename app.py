import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
st.set_page_config(page_title="My webpage", page_icon=":tada:", layout= "wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

lottie_coding1 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_zxJdukqv9G.json")
lottie_coding2 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_zvcyhdqv.json")
lottie_coding3 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_Cse72PaM1R.json")
lottie_coding4 = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_cioqsmkr.json")
lottie_coding5 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_fyobuzf9.json")



img1 = Image.open("images/img1.jpg")

#header section
with st.container():
    st.subheader("Hi, I am Bushra :wave:")
    st.title("A Software Developer From New Mumbai, India")
    st.write("I am passionate about finding ways to use my technical skills for the improvement of the company or project.")
    st.write("[Learn More >](https://github.com/bushkhan)")
    
    
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I found my passion in coding almost 2 years ago.
            I dream of becoming the best and excel in my field.
            You'll know me as a collaborator, an explorer and a team player.
            My area of interests are:
            - hybrid mobile app development
            - backend development
            - creating restful APIs
            - mern stack development
            - currently exploring the field of AI/ML
            
            If this sounds exciting to you, consider visiting my LinkedIn Profile.
        """
        )
        st.write("[LinkedIn Profile >](https://www.linkedin.com/in/bushra-khan-3a883a214/)")
    with right_column:
        st_lottie(lottie_coding1, height= 440, key="coding")
        

with st.container():
    st.write("---")
    st.header("Product Services")
    st.write("##")
    left_column, right_column = st.columns((2,2))
    with left_column:
        
        st.subheader("App Designs")
        st.write(
            """
            - Converting ui/ux designs into interactive ui.
            - manage smooth operations between ui and user.
            - create and deploy frontend designs.
            """
        )
        st_lottie(lottie_coding2,height=250)
        
    with right_column:
        st.subheader("Rest API")
        st.write(
            """
            - Connecting and managing interactions with databases.
            - using backend frameworks and technologies.
            - managing overall software architectural style.
            """
        )
        st_lottie(lottie_coding3,height=250)
   
  
        

with st.container():
    st.write("---")
    st.header("Management Services")
    st.write("##")

    left_column, right_column = st.columns((2,2))
    with left_column:
        
        st.subheader("Database Management")
        st.write(
            """
            - Store, run and retrieve data securely.
            - Backup data regularly.
            - Maintaining data integrity.
            """
        )
        st_lottie(lottie_coding4,height=270)
        
    with right_column:
        st.subheader("Product Management")
        st.write(
            """
            - Understanding and representing user needs.
            - Defining vision of the product
            - Prioritizing features and capabilities.
            """
        )
        st_lottie(lottie_coding5,height=280)
        
   
   

        
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/bushrakhan2212002@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email"  required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    
    
    left_column, right_column  = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html= True)
    with right_column:
        st.empty()