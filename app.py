import streamlit as st

from streamlit_extras.stylable_container import stylable_container
import pandas as pd

st.set_page_config(page_title="IPL Player Detail", page_icon="🏏")

with st.container():
    st.subheader("Hi, I am Krishnakant Verma :wave: ")
    st.write(
        "I am a Final Year CSE Student from Govt. College of Engineering, Amravati."
    )
    st.write(
        "I am passionate about navigating the confluence of code and data, specializing in the dynamic synergy of Data Science and Full Stack Development, focusing on React for front-end and Django/Django REST framework for back-end development."
    )

    st.markdown(
        """
        Connect with me on <b>LinkedIn</b> :link: &nbsp;&nbsp;&nbsp;[Click to view profile](https://www.linkedin.com/in/krishnakant-verma-a389a2245/)
        """,
        unsafe_allow_html=True,
    )

st.write("---")
st.subheader("Cricket Carnival Chronicles: Unveiling the Stars of IPL")
st.write("###")
player_name_list = (
    "Start your Player Selection",
    "Virat Kohli",
    "Shikhar Dhawan",
    "David Warner",
    "Rohit Sharma",
    "Suresh Raina",
    "AB de Villiers",
    "MS Dhoni",
    "Chris Gayle",
    "Robin Uthappa",
    "Dinesh Karthik",
    "Ajinkya Rahane",
    "Ambati Rayudu",
    "Gautam Gambhir",
    "KL Rahul",
    "Faf du Plessis",
    "Sanju Samson",
    "Shane Watson",
    "Manish Pandey",
    "Kieron Pollard",
    "Suryakumar Yadav",
    "Jos Buttler",
    "Yusuf Pathan",
    "Quinton de Kock",
    "Brendon McCullum",
    "Parthiv Patel",
    "Rishabh Pant",
    "Wriddhiman Saha",
    "Shubman Gill",
    "Shreyas Iyer",
    "Yuvraj Singh",
    "Virender Sehwag",
    "Glenn Maxwell",
    "David Miller",
    "Ravindra Jadeja",
    "Murali Vijay",
    "Mayank Agarwal",
    "Nitish Rana",
    "Steve Smith",
    "Shaun Marsh",
    "Jacques Kallis",
    "Dwayne Smith",
    "Sachin Tendulkar",
    "Ishan Kishan",
    "Hardik Pandya",
    "Andre Russell",
    "Rahul Dravid",
    "Kane Williamson",
    "Aaron Finch",
    "Rahul Tripathi",
    "Adam Gilchrist",
    "JP Duminy",
    "Michael Hussey",
    "Mahela Jayawardena",
    "Ruturaj Gaikwad",
    "Mandeep Singh",
    "Prithvi Shaw",
    "Kumar Sangakkara",
    "Manoj Tiwary",
    "Dwayne Bravo",
    "Naman Ojha",
    "Devdutt Padikkal",
    "Krunal Pandya",
    "Karun Nair",
    "Saurabh Tiwary",
    "Marcus Stoinis",
    "Subramaniam Badrinath",
    "Axar Patel",
    "Eoin Morgan",
    "Brad Hodge",
    "Sourav Ganguly",
    "Chris Lynn",
    "David Hussey",
    "Deepak Hooda",
    "Jonny Bairstow",
    "Nicholas Pooran",
    "Kedar Jadhav",
    "Yashasvi Jaiswal",
    "Irfan Pathan",
    "Shimron Hetmyer",
    "Matthew Hayden",
    "Shivam Dube",
    "Manan Vohra",
    "Lendl Simmons",
    "Sunil Narine",
    "Moeen Ali",
    "Vijay Shankar",
    "Ross Taylor",
    "Kevin Pietersen",
    "Moises Henriques",
    "Venugopal Rao",
    "Albie Morkel",
    "Andrew Symonds",
    "Venkatesh Iyer",
    "Cameron White",
    "Ben Stokes",
    "Devon Conway",
    "Abhishek Sharma",
    "Herschelle Gibbs",
    "Stuart Binny",
    "Harbhajan Singh",
    "Liam Livingstone",
    "Rahul Tewatia",
    "Manvinder Bisla",
    "Shakib Al Hasan",
    "Aiden Markram",
    "Sanath Jayasuriya",
    "Tilak Varma",
    "Graeme Smith",
    "Tillakaratne Dilshan",
    "Rinku Singh",
    "Angelo Mathews",
    "Ravichandran Ashwin",
    "Tirumalasetti Suman",
    "Abhishek Nayar",
    "George Bailey",
    "Evin Lewis",
    "Chris Morris",
    "Jason Roy",
    "Sam Curran",
    "Piyush Chawla",
    "Mitchell Marsh",
    "Jesse Ryder",
    "Riyan Parag",
    "Sarfaraz Khan",
    "Hashim Amla",
    "Jitesh Sharma",
    "Corey Anderson",
    "Ravi Bopara",
    "James Faulkner",
    "Heinrich Klaasen",
    "Gurkeerat Mann Singh",
    "Sai Sudharsan",
    "Owais Shah",
    "Paul Valthaty",
)
dataframe = pd.read_csv("All-Time-Best-Batsman.csv")

left_col, right_col = st.columns((2, 1))

with left_col:
    player_name = st.selectbox("Select Player", player_name_list)

player_data = ""
flag = False
with right_col:
    with stylable_container(
        key="sub_btn",
        css_styles="""
        button{
            margin-top : 28px;
        }
        """,
    ):
        if st.button("Submit"):
            player_data = dataframe[dataframe["Player"] == player_name]
            player_data = player_data.drop(["POS"], axis="columns")
            player_data.index.name = "Player Details"
            flag = True

if flag:
    st.write("---")
    st.write("Player Name :- ", player_name)
    st.write(player_data)
