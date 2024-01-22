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

**Step 2:
Data extraction:**

Clone the Github using scripting to fetch the data from the Phonepe pulse Github repository and store it in a suitable format such as JSON. Use the below syntax to clone the phonepe github repository into your local drive.

    from git.repo.base import Repo
    Repo.clone_from("GitHub Clone URL","Path to get the cloded files")

**Step 3:
Data transformation:**

This step may include cleaning the data, handling missing values, and transforming the data into a format suitable for analysis and visualization.

path1 = "Path of the JSON files"
agg_trans_list = os.listdir(path1)

# Column names
columns1 = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [],'Transaction_amount': []}

Looping through each and every folder and opening the json files appending only the required key and values and creating the dataframe.

for state in agg_trans_list:
    cur_state = path1 + state + "/"
    agg_year_list = os.listdir(cur_state)

    for year in agg_year_list:
        cur_year = cur_state + year + "/"
        agg_file_list = os.listdir(cur_year)

        for file in agg_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            A = json.load(data)

            for i in A['data']['transactionData']:
                name = i['name']
                count = i['paymentInstruments'][0]['count']
                amount = i['paymentInstruments'][0]['amount']
                columns1['Transaction_type'].append(name)
                columns1['Transaction_count'].append(count)
                columns1['Transaction_amount'].append(amount)
                columns1['State'].append(state)
                columns1['Year'].append(year)
                columns1['Quarter'].append(int(file.strip('.json')))
df = pd.DataFrame(columns1)

**Converting the dataframe into csv file**
df.to_csv('filename.csv',index=False)

**Step 4:
Database insertion:**

Use the "psycopg2" library in Python to connect to a Postgre-SQL database and insert the transformed data using SQL commands.
