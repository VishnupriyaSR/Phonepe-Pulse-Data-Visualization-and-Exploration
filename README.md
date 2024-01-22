# Phonepe-Pulse-Data-Visualization-and-Exploration
**Introduction**

PhonePe has become a leader among digital payment platforms, serving millions of users for their daily transactions. Known for its easy-to-use design, fast and secure payment processing, and creative features, PhonePe has gained praise and recognition in the industry. The PhonePe Pulse Data Visualization and Exploration project aims to gather valuable information from PhonePe's GitHub repository, process the data, and present it using an interactive dashboard that's visually appealing. This is accomplished using Python, Streamlit, and Plotly.

**PhonePe Pulse:**
The PhonePe Pulse website showcases more than 2000+ Crore transactions by consumers on an interactive map of India. With over 45% market share, PhonePe's data is representative of the country's digital payment habits. The insights on the website and in the report have been drawn from two key sources - the entirety of PhonePe's transaction data combined with merchant and customer interviews. The report is available as a free download on the PhonePe Pulse website and GitHub.

**Required Libraries**
Plotly - (To plot and visualize the data)
Pandas - (To Create a DataFrame with the scraped data)
Psycopg2 - (To store and retrieve the data)
Streamlit - (To Create Graphical user Interface)
json - (To load the json files)
git.repo.base - (To clone the GitHub repository)

**Steps:
Step 1:
Importing the Libraries:**
    !pip install ["Name of the library"]
    
If the libraries are already installed then we have to import those into our script by mentioning the below codes.

    import pandas as pd
    import psycopg2 as pg
    import streamlit as st
    import plotly.express as px
    import os
    import json
    from streamlit_option_menu import option_menu
    from PIL import Image
    from git.repo.base import Repo
