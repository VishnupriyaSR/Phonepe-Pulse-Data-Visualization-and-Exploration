#Pandas library
import pandas as pd

#SQL Library
import psycopg2 

#Dashboard Libraries
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import plotly.express as px


#Connect to PostGre-SQL
mydb=psycopg2.connect(host="localhost",user="postgres",password="vishnu",database="Phonepe",port=5432)
cursor=mydb.cursor()


# Configuring Streamlit GUI

st.set_page_config(layout="wide")
col8,col9=st.columns([2,10])
with col8:
    st.image("PhonePe_logo.jpg")
with col9:
    st.write("")

selected = option_menu(None,
                           options = ["Home","Explore Data","Data Visualization","Data APIs"],
                           icons = ["house","toggles","clipboard-data","database"],
                           default_index=0,
                           orientation="horizontal",
                           styles={"container": {"width": "100%"},
                                   "icon": {"color": "white", "font-size": "24px"},
                                   "nav-link": {"font-size": "24px", "text-align": "center", "margin": "-2px"},
                                   "nav-link-selected": {"background-color": "#6F36AD"}})
# # # MENU 1 - Home
if selected == "Home":
    col1,col2 = st.columns(2)
    with col1:
        
        st.write("PhonePe is an Indian digital payments and financial services company headquartered in Bengaluru, Karnataka, India.PhonePe was founded in December 2015,by Sameer Nigam, Rahul Chari and Burzin Engineer.The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016")
        st.write("The PhonePe app is available in 11 Indian languages.Using PhonePe, users can send and receive money, recharge mobile, DTH, data cards, make utility payments, pay at shops, invest in tax saving funds, buy insurance, mutual funds, and digital gold.")
        st.write("PhonePe is accepted as a payment option by over 3.6 crore offline and online merchant outlets, constituting 99% of pin codes in the country.The app served more than 10 crore users as of June 2018,processed 500 crore transactions by December 2019,and crossed 10 crore transactions a day in April 2022.It currently has over 50 crore registered users with over 20 crore monthly active users.")
    with col2:
        st.image("home.png")
        
        
#Menu-4- DATA APIs        
if selected=="Data APIs":
    col1,col2=st.columns(2)
    with col1:
        st.write("The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and state-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government")
        st.write("Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. PhonePe Pulse is our way of giving back to the digital payments ecosystem.")
        st.write("PhonePe Pulse is your window to the world of how India transacts with interesting trends, deep insights and in-depth analysis based on our data put together by the PhonePe team.")
        st.write("This year, as crossed 2000 Cr. transactions and 30 Crore registered users, thought as India's largest digital payments platform with 46% UPI market share, have a ring-side view of how India sends, spends, manages and grows its money. So it was time to demystify and share the what, why and how of digital payments in India.")
                 
                 
    with col2:
        st.video("C:\\Users\\User\\Desktop\\videoplayback.mp4")

    st.header("GUIDE")
    st.write("This data has been structured to provide details on data cuts of Transactions and Users on the Explore tab")
    col3,col4=st.columns([9,15])
    with col3:
        st.header("Categories")
    # execute a SELECT statement
        cursor.execute("select transaction_type,sum(transaction_count) from agg_trans group by transaction_type")
        df = pd.DataFrame(cursor.fetchall(),columns=["Transaction Type",  "Aggregated values"])
        st.dataframe(df,hide_index=True)
    with col4:
        st.header("1.Aggregated")
        st.write("Aggregated values of various payment categories as shown under Categories section")
    col5,col6=st.columns([9,15])
    with col5:
        col5.image(Image.open("map.jpg"))
    with col6:
        st.header("2.Map")
        st.write("Total values at the State and District levels")
    col7,col8=st.columns([9,15])
    with col7:
        col7.image(Image.open("top.jpg"))
    with col8:
        st.header("3.Top")
        st.write("Totals of top States / Districts / Postal Codes")



        
#Menu=Explore-Data
if selected == "Explore Data":
    select = option_menu(None,
                             options=["INDIA", "STATES", "TOP CATEGORIES" ],
                             default_index=0,
                             orientation="horizontal",
                             styles={"container": {"width": "100%"},
                                       "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px"},
                                       "nav-link-selected": {"background-color": "#6F36AD"}})
    if select == "INDIA":
        tab1, tab2 = st.tabs(["TRANSACTION","USER"])

# TRANSACTION TAB
        with tab1:
            col1, col2, col3 = st.columns(3)
            with col1:
                Year = st.selectbox('**Select Year**', ('2018', '2019', '2020', '2021', '2022','2023'), key='Year')
            with col2:
                Quarter = st.selectbox('**Select Quarter**', ('1', '2', '3', '4'), key='Quarter')
            with col3:
                Type = st.selectbox('**Select Transaction type**',('Recharge & bill payments', 'Peer-to-peer payments','Merchant payments', 'Financial Services', 'Others'), key='Type')

#State and Transaction Count Query
            col3,col4=st.columns([15,9])
            with col3:
                if Year == 2023 and Quarter == 4:
                    st.write("#### Sorry No Data to Display for 2023 Quarter 4")
                else:
                    cursor.execute(f"select state, transaction_count as Transaction_count, transaction_amount as All_Transactions from agg_trans where year = {Year} and quarter = {Quarter} and transaction_type='{Type}' ")

                    df1 = pd.DataFrame(cursor.fetchall(),columns= ['State', 'Transaction_count','All_Transactions'])
                    df2 = pd.read_csv('Statenames.csv')
                    df1.State = df2

    #india map
                    fig = px.choropleth(df1,          geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations='State',
                color='All_Transactions',
                color_continuous_scale='bluyl',title="All India Transactions")

                    fig.update_geos(fitbounds="locations", visible=True)
                    fig.update_layout(title_font=dict(size=33), title_font_color='Green', height=500)
                    fig.update_layout(margin=dict(l=20, r=20, t=100, b=20),paper_bgcolor="LightSteelBlue",)
                    st.plotly_chart(fig,use_container_width=True)

        with col4:
            st.markdown("## :violet[Transactions]")
            st.header(":violet[All PhonePe Transactions]")
            cursor.execute("select sum(transaction_amount) from agg_trans")
            df=pd.DataFrame(cursor.fetchone(),columns=["Overall Transactions"])
            st.dataframe(df,hide_index=True)

            st.header(":violet[Categories]")
# Transaction-Type analysis
            cursor.execute("select transaction_type,sum(transaction_count) from agg_trans group by transaction_type")
            df = pd.DataFrame(cursor.fetchall(),columns=["Transaction Type",  "Aggregated values"])
            st.dataframe(df,hide_index=True)

        
#User Tab
        with tab2:
            col1, col2= st.columns(2)
            with col1:
                Year = st.selectbox('**Select Year**', ('2018', '2019', '2020', '2021', '2022','2023'))
            with col2:
                Quarter = st.selectbox('**Select Quarter**', ('1', '2', '3', '4'))

            cursor.execute(f"select state,registeredusers as Registered_Users from map_users where year = {Year} and quarter = {Quarter}")

            df1 = pd.DataFrame(cursor.fetchall(),columns= ['State', 'Registered_Users'])
            df2 = pd.read_csv('Statenames.csv')
            df1.State = df2

            col3,col4=st.columns([15,9])
            with col3:
                fig = px.choropleth(df1,          geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations='State',
                color='Registered_Users',
                color_continuous_scale='ylgn',title="All India Users")
                fig.update_geos(fitbounds="locations", visible=True)
                fig.update_layout(title_font=dict(size=33), title_font_color='green', height=500)
                fig.update_layout(margin=dict(l=20, r=20, t=100, b=20),paper_bgcolor="LightSteelBlue",)
                st.plotly_chart(fig,use_container_width=True)
#Total Users Query
            with col4:
                st.markdown("## :violet[Users]")
                st.header(":violet[Registered PhonePe Users Till Q3 2023]")
                cursor.execute("select sum(registeredusers) from map_users")
                df=pd.DataFrame(cursor.fetchone(),columns=["PhonePe Users"])
                st.dataframe(df,hide_index=True)
#States Data
    if select=="STATES":
        tab3 ,tab4 = st.tabs(["TRANSACTION","USER"])

        #TRANSACTION TAB FOR STATE
        with tab3:
            col1, col2, col3 = st.columns(3)
            with col1:
                select_state = st.selectbox('**Select State**', (
                    'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar',
                    'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                    'haryana', 'himachal-pradesh',
                    'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                    'maharashtra', 'manipur',
                    'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                    'tamil-nadu', 'telangana',
                    'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal'))
            with col2:
                year = st.selectbox('**Select Year**', ('2018', '2019', '2020', '2021', '2022','2023'))
            with col3:
                quarter = st.selectbox('**Select Quarter**', ('1', '2', '3', '4'))
#display Transaction Analysis-Bar chart            
            col4,col5=st.columns([15,9])
            with col4:
                cursor.execute(f"select transaction_type as Transaction_Type,transaction_amount as Transaction_Amount from agg_trans where state='{select_state}' and year={year} and quarter={quarter}")
                df1 = pd.DataFrame(cursor.fetchall(),columns= ['Transaction_Type', 'Transaction_Amount'])
                df2 = df1.set_index(pd.Index(range(1, len(df1) + 1)))

                df2['Transaction_type'] = df2['Transaction_Type'].astype(str)
                df2['Transaction_amount'] = df2['Transaction_Amount'].astype(float)
                df_fig = px.bar(df2, x='Transaction_Type',y='Transaction_Amount', color='Transaction_Amount',color_continuous_scale='temps',
                                                        title='Transaction Analysis Chart', height=500, )
                df_fig.update_layout(title_font=dict(size=33), title_font_color='#AD71EF')
                st.plotly_chart(df_fig, use_container_width=True)
             
            with col5:
                st.markdown("## :violet[ALL TRANSACTIONS]")
                cursor.execute(f"select transaction_type as TRANSACTION_TYPE,sum(transaction_amount) as TRANSACTION_AMOUNT,sum(transaction_count) as TRANASCTION_COUNT from agg_trans where state='{select_state}'and year={year} and quarter={quarter} group by state,transaction_type")
                df=pd.DataFrame(cursor.fetchall(),columns=["TRANSACTION_TYPE","TRANSACTION_AMOUNT","TRANASCTION_COUNT"])
                st.dataframe(df,hide_index=True)
                
                
                st.markdown("## :violet[TOTAL PAYMENT VALUE]")
                cursor.execute(f"select sum(transaction_amount) as TRANSACTION_AMOUNT from agg_trans where state='{select_state}'and year={year} and quarter={quarter}")
                df=pd.DataFrame(cursor.fetchall(),columns=["TRANSACTION_AMOUNT"])
                st.dataframe(df,hide_index=True)
                
                st.markdown("## :violet[AVG.PAYMENT VALUE]")
                cursor.execute(f"select avg(transaction_amount) as AVERAGE_TRANSACTION_VALUE from agg_trans where state='{select_state}'and year={year} and quarter={quarter}")
                df=pd.DataFrame(cursor.fetchall(),columns=["AVERAGE_TRANSACTION_VALUE"])
                st.dataframe(df,hide_index=True)

               
 #User Tab:           
        with tab4:
            col1, col2, col3 = st.columns(3)
            with col1:
                sel_state = st.selectbox('**Select State**', (
                    'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar',
                    'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                    'haryana', 'himachal-pradesh',
                    'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                    'maharashtra', 'manipur',
                    'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                    'tamil-nadu', 'telangana',
                    'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal'),key='sel_state')
            with col2:
                sel_year = st.selectbox('**Select Year**', ('2018', '2019', '2020', '2021', '2022','2023'),key='sel_year')
            with col3:
                sel_quarter = st.selectbox('**Select Quarter**', ('1', '2', '3', '4'),key='sel_quarter')
 #District wise-Users Count           
            col4,col5=st.columns([15,9])
            with col4:
                cursor.execute(f"select district as District,sum(registeredusers) as Registered_Users from map_users where state='{sel_state}'and year={sel_year} and quarter={sel_quarter} group by district")
                df1 = pd.DataFrame(cursor.fetchall(),columns= ['District', 'Registered_Users'])
                df2 = df1.set_index(pd.Index(range(1, len(df1) + 1)))

                df2['District'] = df2['District'].astype(str)
                df2['Registered_Users'] = df2['Registered_Users'].astype(int)
                df_fig = px.bar(df2, x='District',y='Registered_Users', color='Registered_Users',color_continuous_scale='puor',
                                                        title='User Analysis Chart', height=500, )
                df_fig.update_layout(title_font=dict(size=33), title_font_color='#AD71EF')
                st.plotly_chart(df_fig, use_container_width=True)
                
            with col5:
                st.markdown("## :violet[ALL REGISTERED USERS]")
                cursor.execute(f"select sum(registeredusers) as TOTAL_USERS from map_users where state='{sel_state}'and year={sel_year} and quarter={sel_quarter}")
                df=pd.DataFrame(cursor.fetchall(),columns=["TOTAL_USERS"])
                st.dataframe(df,hide_index=True)
                
                
                st.markdown("## :violet[APP OPENS]")
                cursor.execute(f"select sum(appopens) as APP_OPENS from map_users where state='{sel_state}'and year={sel_year} and quarter={sel_quarter}")
                df=pd.DataFrame(cursor.fetchall(),columns=["APP_OPENS"])
                st.dataframe(df,hide_index=True)

#Menu - TOP CATEGORIES
    if select=="TOP CATEGORIES":
        tab3 ,tab4 = st.tabs(["TRANSACTION","USER"])
#Transaction tab
        with tab3:
            col1,col2=st.columns(2)
            with col1:
                sel_year = st.selectbox('**Select Year**', ('2018', '2019', '2020', '2021', '2022','2023'),key='sel_year')
            with col2:
                sel_quarter = st.selectbox('**Select Quarter**', ('1', '2', '3', '4'),key='sel_quarter')
            col3,col4=st.columns([15,10])
            with col3:
                cursor.execute(f"select state as State,sum(transaction_amount) as Total_Payment from agg_trans where year={sel_year} and quarter={sel_quarter} group by state order by Total_Payment desc limit 10") 
                df1 = pd.DataFrame(cursor.fetchall(),columns= ['State', 'Total_Payment'])
                df2 = df1.set_index(pd.Index(range(1, len(df1) + 1)))
                df2['State'] = df2['State'].astype(str)
                df2['Total_Payment'] = df2['Total_Payment'].astype(float)
                df_fig = px.bar(df2, x='State',y='Total_Payment', color='Total_Payment',color_continuous_scale='puor',
                                                          title='TOP STATES-TRANSACTION AMOUNT', height=500, )
                df_fig.update_layout(title_font=dict(size=33), title_font_color='#AD71EF')
                st.plotly_chart(df_fig, use_container_width=True)
                
            with col4:
                st.markdown("## :violet[TOP 10 STATES]")
                cursor.execute(f"select state as State,sum(transaction_amount) as Transaction_Amount from top_trans group by state order by Transaction_Amount desc limit 10")
                df=pd.DataFrame(cursor.fetchall(),columns=["STATE","TRANSACTION_AMOUNT"])
                st.dataframe(df,hide_index=True)
                
                st.markdown("## :violet[TOP 10 DISTRICTS]")
                cursor.execute(f"select district as District,sum(amount) as Transaction_Amount from map_trans group by district order by Transaction_Amount desc limit 10")
                df=pd.DataFrame(cursor.fetchall(),columns=["STATE","TRANSACTION_AMOUNT"])
                st.dataframe(df,hide_index=True)
 #User Tab               
        with tab4: 
            col1,col2=st.columns([15,10])
            with col1:
                sele_year = st.selectbox('**Select Year**', ('2018', '2019', '2020', '2021', '2022','2023'),key='sele_year')
            with col2:
                sele_quarter = st.selectbox('**Select Quarter**', ('1', '2', '3', '4'),key='sele_quarter')
            col3,col4=st.columns([15,10])
            with col3:
                cursor.execute(f"select state as State,sum(registeredusers) as Total_Users from top_users where year={sele_year} group by state order by Total_Users desc limit 10") 
                df1 = pd.DataFrame(cursor.fetchall(),columns= ['State', 'Total_Users'])
                df2 = df1.set_index(pd.Index(range(1, len(df1) + 1)))
                df2['State'] = df2['State'].astype(str)
                df2['Total_Users'] = df2['Total_Users'].astype(int)
                df_fig = px.bar(df2, x='State',y='Total_Users', color='Total_Users',color_continuous_scale='piyg',
                                                             title='TOP STATES-USERS', height=500, )
                df_fig.update_layout(title_font=dict(size=33), title_font_color='#AD71EF')
                st.plotly_chart(df_fig, use_container_width=True)
            with col4:                
                st.markdown("## :violet[TOP 10 STATES]")
                cursor.execute(f"select state as State,sum(registeredusers) as Total_Users from top_users group by state order by Total_Users desc limit 10")
                df=pd.DataFrame(cursor.fetchall(),columns=["STATE","TOTAL_USERS"])
                st.dataframe(df,hide_index=True)
                
                st.markdown("## :violet[TOP 10 DISTRICTS]")
                cursor.execute(f"select district as District,sum(registeredusers) as Total_Users from map_users group by district order by Total_Users desc limit 10")
                df=pd.DataFrame(cursor.fetchall(),columns=["STATE","TOTAL-USERS"])
                st.dataframe(df,hide_index=True)
                
#Data Visualization Tab:   
if selected=="Data Visualization":
    st.title(':violet[Data Visualization]')
    st.write("Users will be able to access the dashboard from a web browser and easily navigate  the different visualizations and facts and figures displayed. The dashboard will provide valuable insights and information about the data in the Phonepe pulse Github repository, making it a valuable tool for data analysis and decision-making.They are derived from the Analysis of the Phonepe Pulse data. It provides a clear idea about the analysed data.")
    options = ["--select--",
               "Top 10 states based on Transaction-Amount",
               "Top 10 Districts based on the Transaction Amount",
               "Least 10 states based on Transaction-Amount",
               "Least 10 Districts based on the Transaction Amount",
               "Top 10 States and Districts based on Registered Users",
               "Least 10 States and Districts based on Registered Users",
               "Top 10 Districts based on the Transaction count",
               "Least 10 Districts based on the Transaction count",
               "Transaction types based on the Transaction Amount",
               "Top 10 Mobile Brands based on the User count of transaction"]
    select = st.selectbox(":violet[Select the option]",options)
#Q1:       
    if select == "Top 10 states based on Transaction-Amount":
        cursor.execute(
            "SELECT DISTINCT state,SUM(transaction_amount) AS Total_Transaction_Amount FROM top_trans GROUP BY state ORDER BY Total_Transaction_Amount DESC LIMIT 10");

        data = cursor.fetchall()
        columns = ['State', 'Transaction_amount']
        df = pd.DataFrame(data, columns=columns, index=range(1, len(data) + 1))

        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 states")
            st.bar_chart(data=df, x="State", y="Transaction_amount")
#Q2:
    if select == "Top 10 Districts based on the Transaction Amount":
        cursor.execute(
            "SELECT DISTINCT district,SUM(amount) AS Total_Transaction_Amount FROM map_trans GROUP BY district ORDER BY Total_Transaction_Amount DESC LIMIT 10");

        data = cursor.fetchall()
        columns = ['District', 'Transaction_amount']
        df = pd.DataFrame(data, columns=columns, index=range(1, len(data) + 1))

        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Districts")
            st.bar_chart(data=df, x="District", y="Transaction_amount",color="#ffaa00")

#Q3:    
    if select == "Least 10 states based on Transaction-Amount":
        cursor.execute(f"select state,sum(transaction_amount) as Total_Amount from agg_trans group by state order by Total_Amount asc limit 10")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Total_Amount'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            fig = px.pie(df, values='Total_Amount',
                             names='State',
                             color_discrete_sequence=px.colors.sequential.RdBu,
                             hover_data=['Total_Amount'],
                             labels={'Transactions_Amount':'Total_Amount'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
        
#Q4:
    if select=="Least 10 Districts based on the Transaction Amount":
        cursor.execute(
            "SELECT DISTINCT district,SUM(amount) AS Total_Transaction_Amount FROM map_trans GROUP BY district ORDER BY Total_Transaction_Amount ASC LIMIT 10");

        df = pd.DataFrame(cursor.fetchall(), columns=['District', 'Total_Amount'])    
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            fig = px.pie(df, values='Total_Amount',
                             names='District',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             hover_data=['Total_Amount'],
                             labels={'Transactions_Amount':'Total_Amount'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
        
#Q5
    if select=="Top 10 States and Districts based on Registered Users":
            cursor.execute("select state,district,sum(registeredusers) as total from map_users group by state,district  order by total desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['State','District','Total_Users'])    
            col1, col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                fig=px.line(df, x="District", y="Total_Users",width=500,height=500)
                st.plotly_chart(fig, config=dict({'displayModeBar': False}, **{'displaylogo': False}), use_container_width=False, layout=dict({'width': '100%'}, **{'height': '100%'}))
            

#Q6
    if select=="Least 10 States and Districts based on Registered Users":
        cursor.execute("select state,district,sum(registeredusers) as total from map_users group by state,district  order by total asc limit 10")
        df = pd.DataFrame(cursor.fetchall(), columns=['State','District','Total_Users'])    
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            fig=px.line(df, x="District", y="Total_Users",width=500,height=500)
            st.plotly_chart(fig, config=dict({'displayModeBar': False}, **{'displaylogo': False}), use_container_width=False, layout=dict({'width': '100%'}, **{'height': '100%'}))
            
#Q7
    if select == "Top 10 Districts based on the Transaction count":
        cursor.execute(
            "SELECT DISTINCT district,SUM(count) AS Total_Transaction_Count FROM map_trans GROUP BY district ORDER BY Total_Transaction_Count ASC LIMIT 10");

        data = cursor.fetchall()
        columns = ['District', 'Transaction_count']
        df = pd.DataFrame(data, columns=columns, index=range(1, len(data) + 1))

        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Districts")
            st.bar_chart(data=df, x="District", y="Transaction_count")
    
#Q8
    if select == "Least 10 Districts based on the Transaction count":
            cursor.execute(
                "SELECT DISTINCT district,SUM(count) AS Total_Transaction_Count FROM map_trans GROUP BY district ORDER BY Total_Transaction_Count ASC LIMIT 10");

            data = cursor.fetchall()
            columns = ['District', 'Transaction_count']
            df = pd.DataFrame(data, columns=columns, index=range(1, len(data) + 1))

            col1, col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Least 10 Districts")
                st.bar_chart(data=df, x="District", y="Transaction_count")
#Q9
    if select=="Transaction types based on the Transaction Amount":
        cursor.execute("select transaction_type,sum(transaction_amount)as total from agg_trans group by transaction_type order by total asc limit 10")
        data = cursor.fetchall()
        columns = ['Transaction_Type', 'Transaction_Amount']
        df = pd.DataFrame(data, columns=columns, index=range(1, len(data) + 1))

        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Transaction_Type")
            st.bar_chart(data=df, x="Transaction_Type", y="Transaction_Amount")
        
#Q10:
    if select=="Top 10 Mobile Brands based on the User count of transaction":
        cursor.execute("select brand,sum(count)as total from agg_users group by brand order by total desc limit 10")
        df = pd.DataFrame(cursor.fetchall(), columns=['Brand', 'Users_Count'])    
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            fig = px.pie(df, values='Users_Count',
                             names='Brand',
                             color_discrete_sequence=px.colors.sequential.Blugrn,
                             hover_data=['Users_Count'],
                             labels={'Registered Users':'Users_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
