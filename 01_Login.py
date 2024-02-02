import pickle
from pathlib import Path

import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="streamlit Dashboard", page_icon=":bar_chart:", layout="wide")

hide_bar= """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        visibility:hidden;
        width: 0px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        visibility:hidden;
    }
    </style>
"""

# --- USER AUTHENTICATION ---
names = ["Peter Parker", "Rebecca Miller","bharath"]
usernames = ["pparker", "rmiller","bharath"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "SIPL_dashboard", "abcdef")

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")
    st.markdown(hide_bar, unsafe_allow_html=True)

if authentication_status == None:
    st.warning("Please enter your username and password")
    st.markdown(hide_bar, unsafe_allow_html=True)


if authentication_status:
    # # ---- SIDEBAR ----
    st.sidebar.title(f"Welcome {name}")
    # st.sidebar.header("select page here :")
    st.write("# Welcome to Streamlit!..")

    ###about ....
    st.subheader("Introduction :")
    st.text("1. \n2. \n3. \n4. \n5. \n")

    st.sidebar.success("Select a page above.")

    ###---- HIDE STREAMLIT STYLE ----
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)


    authenticator.logout("Logout", "sidebar")

# import streamlit as st
# import warnings
# import plotly.graph_objects as go
# from PIL import Image
# import pickle
# from pathlib import Path
# import streamlit_authenticator as stauth
# import pandas as pd
# import numpy as np
# import plotly.express as px
# from datetime import datetime
# import warnings
# from PIL import Image
# from ONDC import ONDC_dash

# import yaml
# from yaml.loader import SafeLoader

# warnings.filterwarnings('ignore')

# icon_ = Image.open("ICON/paytm_icon-icons.com_62778.ico")

# st.set_page_config(page_title="Paytm Reports", 
#                    page_icon=icon_,
#                    layout="wide")


# image = Image.open("ICON/Paytm_Logo.png")
# image = image.resize((300, 100))
# st.sidebar.image(image,caption=" ")


# names = ["Vijay Kumar","Suresh Fatehpuria"]
# usernames = ["vkumar","sfatehpuria"]

# # file_path = Path(__file__).parent / "hashed_pw.pkl"

# # with file_path.open("rb") as file:
# #     hashed_password = pickle.load(file)

# authenticator = stauth.Authenticate("Vijay Kumar", "vkumar", "$2b$12$0j/n3Zg73uysLYwiUtfq0.XUk.iObYCmx5X43VqxfQQjrMcE/BHwC",
#                                     "dashboard_password", "abcdef",cookie_expiry_days=10)

# # if 'authentication_status' not in st.session_state:
# #     st.session_state['authentication_status'] = None
# #     st.session_state['username'] = None
# # def page2():
# #     st.write("This is page 2")

# # def page3():
# #     st.write("This is page 3")


# # def create_pages_dict(page_numbers):
# #     all_pages = {
# #         1: ("ONDC", ONDC_dash),
# #         2: ("Test Page 2", page2),
# #         3: ("Test Page 3", page3),      
# #     }

# #     pages_dict = {}
# #     for num in page_numbers:
# #         if num in all_pages:
# #             page_name, page_function = all_pages[num]
# #             pages_dict[page_name] = page_function

# #     return pages_dict

# # pages = create_pages_dict([1, 2])

# # def main():

# #     if st.session_state.get('authentication_status') != True:
# #         name, authentication_status, username = authenticator.login("Login", "main")

# #         st.session_state['authentication_status'] = authentication_status
# #         st.session_state['username'] = username
        
# #         if authentication_status == False:
# #             st.error("Username/password is incorrect")
# #         elif authentication_status == None:
# #             st.warning("Please enter your username and password")
# #         return  

# #     st.sidebar.title(f"Welcome {st.session_state['username']}")
# #     page = st.sidebar.selectbox("Select Report", list(pages.keys()))
# #     pages[page]()

# #     authenticator.logout("Logout", "sidebar")

# # main()

