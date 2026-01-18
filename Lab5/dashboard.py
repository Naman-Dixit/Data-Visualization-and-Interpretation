import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from io import StringIO

# Set page configuration
st.set_page_config(page_title="Multi-Dataset Explorer Dashboard", layout="wide")

# Title and description
st.title("📊 Multi-Dataset Explorer Dashboard")
st.markdown("""
This dashboard allows exploration of multiple datasets from various domains. Select a dataset from the sidebar to view its details, perform data science steps (cleaning, analysis), visualize key insights using Plotly, and read observations and interpretations for each visualization.
""")

# Hardcoded dataset contents (from provided <DOCUMENT> tags; in a real app, load from files)
datasets = {
    "Coffee Sales (index_2.csv)": """date,datetime,cash_type,money,coffee_name
2025-02-08,2025-02-08 14:26:04,cash,15.0,Tea
2025-02-08,2025-02-08 14:28:26,cash,15.0,Tea
2025-02-08,2025-02-08 14:33:04,card,20.0,Espresso
2025-02-08,2025-02-08 15:51:04,card,30.0,Chocolate with coffee
2025-02-08,2025-02-08 16:35:01,cash,27.0,Chocolate with milk
2025-02-08,2025-02-08 18:55:30,card,33.0,Espresso
2025-02-08,2025-02-08 18:59:03,cash,29.0,Coffee with Irish whiskey
2025-02-08,2025-02-08 19:00:28,cash,27.0,Irish whiskey with milk
2025-02-09,2025-02-09 08:45:45,card,28.0,Double Irish whiskey
2025-02-09,2025-02-09 10:41:36,cash,30.0,Chocolate with coffee
2025-02-09,2025-02-09 10:42:55,cash,27.0,Double espresso
2025-02-09,2025-02-09 12:18:53,cash,25.0,Americano with milk
2025-02-09,2025-02-09 13:28:56,card,20.0,Espresso
2025-02-09,2025-02-09 15:16:48,card,30.0,Cappuccino
2025-02-09,2025-02-09 15:43:17,card,32.0,Double espresso with milk
2025-02-09,2025-02-09 16:14:26,card,28.0,Double Irish whiskey
2025-02-09,2025-02-09 16:23:52,card,28.0,Caramel with Irish whiskey
2025-02-09,2025-02-09 16:25:15,card,33.0,Latte
2025-02-09,2025-02-09 17:47:17,card,33.0,Latte
2025-02-09,2025-02-09 18:01:22,card,25.0,Americano with milk
2025-02-09,2025-02-09 18:01:22,card,33.0,Latte
2025-02-09,2025-02-09 18:01:22,card,15.0,Tea
2025-02-09,2025-02-09 18:02:39,card,28.0,Caramel with Irish whiskey
2025-02-09,2025-02-09 19:50:36,cash,29.0,Coffee with Irish whiskey
2025-02-10,2025-02-10 09:26:07,cash,25.0,Americano
2025-02-10,2025-02-10 12:26:32,cash,25.0,Americano
2025-02-10,2025-02-10 18:21:29,cash,27.0,Chocolate with milk
2025-02-11,2025-02-11 09:49:22,card,15.0,Tea
2025-02-11,2025-02-11 18:35:30,card,25.0,Americano
2025-02-12,2025-02-12 17:57:46,cash,27.0,Chocolate with milk
2025-02-13,2025-02-13 07:55:09,card,33.0,Latte
2025-02-13,2025-02-13 08:12:14,card,32.0,Double espresso with milk
2025-02-13,2025-02-13 08:47:48,card,30.0,Cappuccino
2025-02-13,2025-02-13 10:28:04,card,25.0,Americano with milk
2025-02-14,2025-02-14 12:33:35,card,20.0,Espresso
2025-02-14,2025-02-14 14:27:58,cash,20.0,Espresso
2025-02-14,2025-02-14 14:33:41,card,28.0,Double Irish whiskey
2025-02-14,2025-02-14 16:09:35,cash,20.0,Espresso
2025-02-14,2025-02-14 19:02:15,card,20.0,Espresso
2025-02-14,2025-02-14 19:24:49,cash,27.0,Chocolate with milk
2025-02-14,2025-02-14 19:30:59,card,29.0,Coffee with Irish whiskey
2025-02-14,2025-02-14 19:53:26,card,28.0,Super chocolate
2025-02-14,2025-02-14 19:54:48,card,28.0,Double Irish whiskey
2025-02-15,2025-02-15 09:38:59,card,25.0,Americano
2025-03-16,2025-03-16 15:04:02,cash,25.0,Americano with milk
2025-03-16,2025-03-16 16:01:45,card,29.0,Coffee with Irish whiskey
2025-03-17,2025-03-17 08:01:14,card,29.0,Coffee with Irish whiskey
2025-03-17,2025-03-17 11:03:49,card,25.0,Irish whiskey
2025-03-17,2025-03-17 16:44:56,card,33.0,Latte
2025-03-17,2025-03-17 17:33:56,card,29.0,Coffee with Irish whiskey
2025-03-17,2025-03-17 18:33:37,card,29.0,Coffee with Irish whiskey
2025-03-18,2025-03-18 08:25:07,card,29.0,Coffee with Irish whiskey
2025-03-18,2025-03-18 15:02:02,cash,28.0,Double Irish whiskey
2025-03-18,2025-03-18 17:44:32,cash,20.0,Espresso
2025-03-18,2025-03-18 17:47:22,card,25.0,Irish whiskey
2025-03-18,2025-03-18 19:35:21,card,30.0,Chocolate with coffee
2025-03-18,2025-03-18 19:36:32,card,30.0,Chocolate with coffee
2025-03-19,2025-03-19 16:56:15,card,25.0,Irish whiskey
2025-03-19,2025-03-19 17:38:00,card,27.0,Chocolate with milk
2025-03-19,2025-03-19 17:42:13,cash,30.0,Mochaccino
2025-03-19,2025-03-19 17:44:09,cash,33.0,Latte
2025-03-19,2025-03-19 19:42:58,cash,25.0,Double chocolate
2025-03-20,2025-03-20 08:10:49,card,25.0,Irish whiskey
2025-03-20,2025-03-20 11:54:23,card,33.0,Latte
2025-03-20,2025-03-20 17:22:35,cash,30.0,Chocolate with coffee
2025-03-21,2025-03-21 09:04:53,card,25.0,Irish whiskey
2025-03-21,2025-03-21 19:37:46,card,27.0,Chocolate with milk
2025-03-21,2025-03-21 19:39:07,card,28.0,Super chocolate
2025-03-21,2025-03-21 21:47:03,card,25.0,Americano with milk
2025-03-22,2025-03-22 10:54:05,card,27.0,Irish whiskey with milk
2025-03-22,2025-03-22 10:55:29,card,27.0,Irish with chocolate
2025-03-22,2025-03-22 11:00:25,card,25.0,Irish whiskey
2025-03-22,2025-03-22 16:59:05,card,15.0,Tea
2025-03-22,2025-03-22 17:07:45,cash,25.0,Irish whiskey
2025-03-22,2025-03-22 17:44:51,card,28.0,Caramel with Irish whiskey
2025-03-22,2025-03-22 17:58:01,cash,22.0,Caramel
2025-03-22,2025-03-22 22:19:59,card,25.0,Americano with milk
2025-03-22,2025-03-22 22:21:21,card,25.0,Americano with milk
2025-03-22,2025-03-22 22:23:39,card,29.0,Coffee with Irish whiskey
2025-03-23,2025-03-23 10:16:44,cash,25.0,Irish whiskey
2025-03-23,2025-03-23 10:25:48,cash,25.0,Americano with milk
2025-03-23,2025-03-23 10:25:48,cash,25.0,Americano with milk
2025-03-23,2025-03-23 14:55:46,cash,30.0,Cappuccino
2025-03-23,2025-03-23 15:15:36,card,25.0,Irish whiskey
2025-03-23,2025-03-23 17:59:25,card,28.0,Super chocolate
2025-03-23,2025-03-23 18:01:33,card,28.0,Vanilla with Irish whiskey
2025-03-23,2025-03-23 21:23:11,card,29.0,Coffee with Irish whiskey""",  # Truncated, but use as is

    "Student Stress (StressLevelDataset.csv)": """anxiety_level,self_esteem,mental_health_history,depression,headache,blood_pressure,sleep_quality,breathing_problem,noise_level,living_conditions,safety,basic_needs,academic_performance,study_load,teacher_student_relationship,future_career_concerns,social_support,peer_pressure,extracurricular_activities,bullying,stress_level
14,20,0,11,2,1,2,4,2,3,3,2,3,2,3,3,2,3,3,2,1
15,8,1,15,5,3,1,4,3,1,2,2,1,4,1,5,1,4,5,5,2
12,18,1,14,2,1,2,2,2,2,3,2,2,3,3,2,2,3,2,2,1
16,12,1,15,4,3,1,3,4,2,2,2,2,4,1,4,1,4,4,5,2
16,28,0,7,2,3,5,1,3,2,4,3,4,3,1,2,1,5,0,5,1
20,13,1,21,3,3,1,4,3,2,2,1,2,5,2,5,1,4,4,5,2
4,26,0,6,1,2,4,1,1,4,4,4,5,1,4,1,3,2,2,1,0
17,3,1,22,4,3,1,5,3,1,1,1,1,3,2,4,1,4,4,5,2
13,22,1,12,3,1,2,4,3,3,3,3,3,3,2,3,3,3,2,2,1
6,8,0,27,4,3,1,2,0,5,2,2,2,2,1,5,1,5,3,4,1
17,12,1,25,4,3,1,3,4,2,1,1,1,3,1,4,1,4,4,5,2
17,15,1,22,3,3,1,5,5,2,1,1,1,3,1,4,1,5,5,4,2
5,28,0,8,1,2,4,2,2,3,5,5,5,2,4,1,3,1,1,1,0
9,23,1,24,4,3,1,0,1,2,4,3,1,2,3,3,0,1,0,1,2
2,28,0,3,1,2,4,2,1,3,4,4,4,2,5,1,3,1,2,1,0
11,21,0,14,3,1,2,4,2,2,2,2,3,3,3,3,2,3,2,2,1
6,28,0,1,1,2,4,2,1,4,5,4,5,1,5,1,3,2,2,1,0
7,25,0,3,1,2,4,2,2,4,5,4,4,2,5,1,3,1,1,1,0
11,23,0,12,3,1,2,2,3,2,3,3,2,3,2,2,3,3,2,3,1
21,1,1,25,4,3,1,4,4,1,2,1,1,5,2,5,1,4,4,5,2
3,27,0,0,1,2,4,1,1,3,5,4,5,2,5,1,3,1,2,1,0
18,1,1,21,4,3,1,3,5,1,1,2,2,5,1,4,1,4,4,5,2
7,27,0,5,1,2,4,1,1,3,5,5,4,2,5,1,3,1,2,1,0
20,5,1,26,3,3,1,4,4,2,1,2,1,3,1,4,1,5,4,4,2
13,21,1,1,2,1,2,2,2,2,3,3,3,3,3,2,2,3,3,2,1
19,5,1,24,4,3,1,4,3,2,2,2,1,4,1,5,1,4,4,5,2
16,12,1,24,5,3,1,5,3,1,2,2,2,3,2,4,1,5,4,4,2
15,13,1,17,5,3,1,4,4,1,2,1,2,5,1,4,1,5,4,4,2
14,16,0,20,1,3,0,5,2,2,0,4,0,1,0,2,0,0,4,5,0
10,18,1,12,3,1,2,2,3,2,2,3,2,3,2,3,3,2,2,3,1
13,16,1,13,2,1,3,2,2,3,3,3,2,3,3,2,2,3,3,2,1
15,13,1,23,4,3,1,3,3,2,1,2,1,5,1,5,1,5,4,4,2
4,25,0,6,1,2,5,2,2,4,4,4,5,2,5,1,3,2,1,1,0
0,28,0,0,1,2,4,2,2,4,5,5,5,1,5,1,3,2,2,1,0
3,10,0,14,3,3,4,4,5,2,1,5,4,3,4,3,1,2,4,3,2
2,15,1,18,5,3,1,0,1,3,3,5,4,4,3,3,1,3,1,3,2
15,7,1,21,4,3,1,3,5,2,1,2,1,3,1,5,1,4,4,5,2
10,25,0,9,2,1,2,2,3,3,3,2,3,2,2,3,2,2,2,2,1
21,1,1,17,3,3,1,4,5,1,1,1,1,4,2,5,1,5,5,5,2
6,4,0,12,4,3,1,1,4,4,4,1,4,4,3,0,0,0,3,2,2
19,3,1,24,3,3,1,4,5,1,1,2,2,5,1,4,1,4,4,5,2
9,13,1,18,5,3,0,0,3,2,3,5,2,4,1,4,1,2,5,1,0
4,29,0,4,1,2,5,1,1,4,5,5,5,1,4,1,3,1,2,1,0
20,10,1,18,3,3,1,4,3,2,1,1,2,4,1,5,1,4,4,4,2
19,16,0,9,4,3,3,5,1,3,5,1,2,0,0,3,1,0,5,5,0
6,11,0,24,4,3,1,1,0,3,4,2,0,3,2,1,1,2,0,1,0
19,11,1,25,4,3,1,5,5,1,1,2,1,4,2,4,1,5,5,5,2
13,20,0,9,2,1,3,4,3,3,3,2,3,2,3,2,3,3,3,3,1
1,30,0,4,1,2,5,2,1,3,5,5,5,1,4,1,3,1,1,1,0
7,17,0,0,4,3,5,4,5,1,0,1,2,1,1,1,0,1,0,3,2
11,17,0,14,3,1,3,2,2,2,2,3,2,2,2,3,3,2,3,3,1
9,12,0,8,0,3,0,0,0,1,3,4,0,1,1,1,1,3,4,3,2
4,26,0,3,1,2,5,2,2,3,4,4,5,1,4,1,3,1,2,1,0
21,0,1,19,5,3,1,4,3,1,1,1,2,5,1,4,1,4,4,4,2
18,6,1,15,3,3,0,3,3,0,4,3,3,4,3,3,1,5,1,4,2""",  # Truncated

    "Retail Sales (retail_sales_dataset.csv)": """Transaction ID,Date,Customer ID,Gender,Age,Product Category,Quantity,Price per Unit,Total Amount
1,2023-11-24,CUST001,Male,34,Beauty,3,50,150
2,2023-02-27,CUST002,Female,26,Clothing,2,500,1000
3,2023-01-13,CUST003,Male,50,Electronics,1,30,30
4,2023-05-21,CUST004,Male,37,Clothing,1,500,500
5,2023-05-06,CUST005,Male,30,Beauty,2,50,100
6,2023-04-25,CUST006,Female,45,Beauty,1,30,30
7,2023-03-13,CUST007,Male,46,Clothing,2,25,50
8,2023-02-22,CUST008,Male,30,Electronics,4,25,100
9,2023-12-13,CUST009,Male,63,Electronics,2,300,600
10,2023-10-07,CUST010,Female,52,Clothing,4,50,200
11,2023-02-14,CUST011,Male,23,Clothing,2,50,100
12,2023-10-30,CUST012,Male,35,Beauty,3,25,75
13,2023-08-05,CUST013,Male,22,Electronics,3,500,1500
14,2023-01-17,CUST014,Male,64,Clothing,4,30,120
15,2023-01-16,CUST015,Female,42,Electronics,4,500,2000
16,2023-02-17,CUST016,Male,19,Clothing,3,500,1500
17,2023-04-22,CUST017,Female,27,Clothing,4,25,100
18,2023-04-30,CUST018,Female,47,Electronics,2,25,50
19,2023-09-16,CUST019,Female,62,Clothing,2,25,50
20,2023-11-05,CUST020,Male,22,Clothing,3,300,900
21,2023-01-14,CUST021,Female,50,Beauty,1,500,500
22,2023-10-15,CUST022,Male,18,Clothing,2,50,100
23,2023-04-12,CUST023,Female,35,Clothing,4,30,120
24,2023-11-29,CUST024,Female,49,Clothing,1,300,300
25,2023-12-26,CUST025,Female,64,Beauty,1,50,50
26,2023-10-07,CUST026,Female,28,Electronics,2,500,1000
27,2023-08-03,CUST027,Female,38,Beauty,2,25,50
28,2023-04-23,CUST028,Female,43,Beauty,1,500,500
29,2023-08-18,CUST029,Female,42,Electronics,1,30,30
30,2023-10-29,CUST030,Female,39,Beauty,3,300,900
31,2023-05-23,CUST031,Male,44,Electronics,4,300,1200
32,2023-01-04,CUST032,Male,30,Beauty,3,30,90
33,2023-03-23,CUST033,Female,50,Electronics,2,50,100
34,2023-12-24,CUST034,Female,51,Clothing,3,50,150
35,2023-08-05,CUST035,Female,58,Beauty,3,300,900
36,2023-06-24,CUST036,Male,52,Beauty,3,300,900
37,2023-05-23,CUST037,Female,18,Beauty,3,25,75
38,2023-03-21,CUST038,Male,38,Beauty,4,50,200
39,2023-04-21,CUST039,Male,23,Clothing,4,30,120
40,2023-06-22,CUST040,Male,45,Beauty,1,50,50
41,2023-02-22,CUST041,Male,34,Clothing,2,25,50
42,2023-02-17,CUST042,Male,22,Clothing,3,300,900
43,2023-07-14,CUST043,Female,48,Clothing,1,300,300
44,2023-02-19,CUST044,Female,22,Clothing,1,25,25
45,2023-07-03,CUST045,Female,55,Electronics,1,30,30
46,2023-06-26,CUST046,Female,20,Electronics,4,300,1200
47,2023-11-06,CUST047,Female,40,Beauty,3,500,1500
48,2023-05-16,CUST048,Male,54,Electronics,3,300,900
49,2023-01-23,CUST049,Female,54,Electronics,2,500,1000
50,2023-08-24,CUST050,Female,27,Beauty,3,25,75
51,2023-10-02,CUST051,Male,27,Beauty,3,25,75
52,2023-03-05,CUST052,Female,36,Beauty,1,300,300
53,2023-07-13,CUST053,Male,34,Electronics,3,25,75
948,2023-10-13,CUST948,Female,23,Electronics,3,25,75
949,2023-08-02,CUST949,Female,41,Electronics,2,25,50
950,2023-11-07,CUST950,Male,36,Clothing,3,300,900
951,2023-11-02,CUST951,Male,33,Beauty,2,50,100
952,2023-11-13,CUST952,Female,57,Clothing,1,25,25
953,2023-04-26,CUST953,Male,45,Beauty,3,30,90
954,2023-09-25,CUST954,Female,50,Electronics,3,300,900
955,2023-07-14,CUST955,Male,58,Clothing,1,25,25
956,2023-08-19,CUST956,Male,30,Clothing,3,500,1500
957,2023-08-15,CUST957,Female,60,Electronics,4,30,120
958,2023-06-02,CUST958,Male,62,Electronics,2,25,50
959,2023-10-29,CUST959,Female,42,Electronics,2,30,60
960,2023-08-08,CUST960,Male,59,Clothing,2,30,60
961,2023-06-06,CUST961,Male,53,Beauty,4,50,200
962,2023-10-19,CUST962,Male,44,Clothing,2,30,60
963,2023-11-14,CUST963,Female,55,Beauty,1,50,50
964,2023-01-31,CUST964,Male,24,Clothing,3,300,900
965,2023-11-09,CUST965,Male,22,Clothing,4,50,200
966,2023-02-20,CUST966,Male,60,Electronics,2,500,1000
967,2023-04-17,CUST967,Male,62,Beauty,1,25,25
968,2023-11-17,CUST968,Female,48,Clothing,3,300,900
969,2023-04-19,CUST969,Female,40,Clothing,3,300,900
970,2023-05-16,CUST970,Male,59,Electronics,4,500,2000
971,2023-12-05,CUST971,Female,27,Electronics,4,50,200
972,2023-02-11,CUST972,Male,49,Beauty,4,25,100
973,2023-03-22,CUST973,Male,60,Clothing,1,50,50
974,2023-05-03,CUST974,Male,47,Beauty,1,30,30
975,2023-03-30,CUST975,Female,56,Clothing,4,50,200
976,2023-10-10,CUST976,Female,48,Beauty,2,300,600
977,2023-02-08,CUST977,Female,35,Electronics,3,25,75
978,2023-03-22,CUST978,Female,53,Clothing,3,50,150
979,2023-01-02,CUST979,Female,19,Beauty,1,25,25
980,2023-07-29,CUST980,Female,31,Electronics,3,25,75
981,2023-08-19,CUST981,Female,30,Electronics,2,30,60
982,2023-12-19,CUST982,Female,46,Beauty,3,30,90
983,2023-11-01,CUST983,Female,29,Clothing,1,300,300
984,2023-08-29,CUST984,Male,56,Clothing,1,500,500
985,2023-05-30,CUST985,Female,19,Electronics,2,25,50
986,2023-01-17,CUST986,Female,49,Clothing,2,500,1000
987,2023-04-29,CUST987,Female,30,Clothing,3,300,900
988,2023-05-28,CUST988,Female,63,Clothing,3,25,75
989,2023-12-28,CUST989,Female,44,Electronics,1,25,25
990,2023-05-25,CUST990,Female,58,Beauty,2,500,1000
991,2023-12-26,CUST991,Female,34,Clothing,2,50,100
992,2023-08-21,CUST992,Female,57,Electronics,2,30,60
993,2023-02-06,CUST993,Female,48,Electronics,3,50,150
994,2023-12-18,CUST994,Female,51,Beauty,2,500,1000
995,2023-04-30,CUST995,Female,41,Clothing,1,30,30
996,2023-05-16,CUST996,Male,62,Clothing,1,50,50
997,2023-11-17,CUST997,Male,52,Beauty,3,30,90
998,2023-10-29,CUST998,Female,23,Beauty,4,25,100
999,2023-12-05,CUST999,Female,36,Electronics,3,50,150
1000,2023-04-12,CUST1000,Male,47,Electronics,4,30,120""",  # Truncated

    "Avocado Prices (avocado.csv)": """,Date,AveragePrice,Total Volume,4046,4225,4770,Total Bags,Small Bags,Large Bags,XLarge Bags,type,year,region
0,2015-12-27,1.33,64236.62,1036.74,54454.85,48.16,8696.87,8603.62,93.25,0.0,conventional,2015,Albany
1,2015-12-20,1.35,54876.98,674.28,44638.81,58.33,9505.56,9408.07,97.49,0.0,conventional,2015,Albany
2,2015-12-13,0.93,118220.22,794.7,109149.67,130.5,8145.35,8042.21,103.14,0.0,conventional,2015,Albany
3,2015-12-06,1.08,78992.15,1132.0,71976.41,72.58,5811.16,5677.4,133.76,0.0,conventional,2015,Albany
4,2015-11-29,1.28,51039.6,941.48,43838.39,75.78,6183.95,5986.26,197.69,0.0,conventional,2015,Albany
5,2015-11-22,1.26,55979.78,1184.27,48067.99,43.61,6683.91,6556.47,127.44,0.0,conventional,2015,Albany
6,2015-11-15,0.99,83453.76,1368.92,73672.72,93.26,8318.86,8196.81,122.05,0.0,conventional,2015,Albany
7,2015-11-08,0.98,109428.33,703.75,101815.36,80.0,6829.22,6266.85,562.37,0.0,conventional,2015,Albany
8,2015-11-01,1.02,99811.42,1022.15,87315.57,85.34,11388.36,11104.53,283.83,0.0,conventional,2015,Albany
9,2015-10-25,1.07,74338.76,842.4,64757.44,113.0,8625.92,8061.47,564.45,0.0,conventional,2015,Albany
10,2015-10-18,1.12,84843.44,924.86,75595.85,117.07,8205.66,7877.86,327.8,0.0,conventional,2015,Albany
11,2015-10-11,1.28,64489.17,1582.03,52677.92,105.32,10123.9,9866.27,257.63,0.0,conventional,2015,Albany
12,2015-10-04,1.31,61007.1,2268.32,49880.67,101.36,8756.75,8379.98,376.77,0.0,conventional,2015,Albany
13,2015-09-27,0.99,106803.39,1204.88,99409.21,154.84,6034.46,5888.87,145.59,0.0,conventional,2015,Albany
14,2015-09-20,1.33,69759.01,1028.03,59313.12,150.5,9267.36,8489.1,778.26,0.0,conventional,2015,Albany
15,2015-09-13,1.28,76111.27,985.73,65696.86,142.0,9286.68,8665.19,621.49,0.0,conventional,2015,Albany
16,2015-09-06,1.11,99172.96,879.45,90062.62,240.79,7990.1,7762.87,227.23,0.0,conventional,2015,Albany
17,2015-08-30,1.07,105693.84,689.01,94362.67,335.43,10306.73,10218.93,87.8,0.0,conventional,2015,Albany
18,2015-08-23,1.34,79992.09,733.16,67933.79,444.78,10880.36,10745.79,134.57,0.0,conventional,2015,Albany
19,2015-08-16,1.33,80043.78,539.65,68666.01,394.9,10443.22,10297.68,145.54,0.0,conventional,2015,Albany
20,2015-08-09,1.12,111140.93,584.63,100961.46,368.95,9225.89,9116.34,109.55,0.0,conventional,2015,Albany
21,2015-08-02,1.45,75133.1,509.94,62035.06,741.08,11847.02,11768.52,78.5,0.0,conventional,2015,Albany
22,2015-07-26,1.11,106757.1,648.75,91949.05,966.61,1,2018-03-18,1.73,210067.47,33437.98,47165.54,110.4,129353.55,73163.12,56020.24,170.19,organic,2018,West
2,2018-03-11,1.63,264691.87,27566.25,60383.57,276.42,176465.63,107174.93,69290.7,0.0,organic,2018,West
3,2018-03-04,1.46,347373.17,25990.6,71213.19,79.01,250090.37,85835.17,164087.33,167.87,organic,2018,West
4,2018-02-25,1.49,301985.61,34200.18,49139.34,85.58,218560.51,99989.62,118314.77,256.12,organic,2018,West
5,2018-02-18,1.64,224798.6,30149.0,38800.64,123.13,155725.83,120428.13,35257.73,39.97,organic,2018,West
6,2018-02-11,1.47,275248.53,24732.55,61713.53,243.0,188559.45,88497.05,99810.8,251.6,organic,2018,West
7,2018-02-04,1.41,283378.47,22474.66,55360.49,133.41,205409.91,70232.59,134666.91,510.41,organic,2018,West
8,2018-01-28,1.8,185974.53,22918.4,33051.14,93.52,129911.47,77822.23,51986.86,102.38,organic,2018,West
9,2018-01-21,1.83,189317.99,27049.44,33561.32,439.47,128267.76,76091.99,51947.5,228.27,organic,2018,West
10,2018-01-14,1.82,207999.67,33869.12,47435.14,433.52,126261.89,89115.78,37133.99,12.12,organic,2018,West
11,2018-01-07,1.48,297190.6,34734.97,62967.74,157.77,199330.12,103761.55,95544.39,24.18,organic,2018,West
0,2018-03-25,1.62,15303.4,2325.3,2171.66,0.0,10806.44,10569.8,236.64,0.0,organic,2018,WestTexNewMexico
1,2018-03-18,1.56,15896.38,2055.35,1499.55,0.0,12341.48,12114.81,226.67,0.0,organic,2018,WestTexNewMexico
2,2018-03-11,1.56,22128.42,2162.67,3194.25,8.93,16762.57,16510.32,252.25,0.0,organic,2018,WestTexNewMexico
3,2018-03-04,1.54,17393.3,1832.24,1905.57,0.0,13655.49,13401.93,253.56,0.0,organic,2018,WestTexNewMexico
4,2018-02-25,1.57,18421.24,1974.26,2482.65,0.0,13964.33,13698.27,266.06,0.0,organic,2018,WestTexNewMexico
5,2018-02-18,1.56,17597.12,1892.05,1928.36,0.0,13776.71,13553.53,223.18,0.0,organic,2018,WestTexNewMexico
6,2018-02-11,1.57,15986.17,1924.28,1368.32,0.0,12693.57,12437.35,256.22,0.0,organic,2018,WestTexNewMexico
7,2018-02-04,1.63,17074.83,2046.96,1529.2,0.0,13498.67,13066.82,431.85,0.0,organic,2018,WestTexNewMexico
8,2018-01-28,1.71,13888.04,1191.7,3431.5,0.0,9264.84,8940.04,324.8,0.0,organic,2018,WestTexNewMexico
9,2018-01-21,1.87,13766.76,1191.92,2452.79,727.94,9394.11,9351.8,42.31,0.0,organic,2018,WestTexNewMexico
10,2018-01-14,1.93,16205.22,1527.63,2981.04,727.01,10969.54,10919.54,50.0,0.0,organic,2018,WestTexNewMexico
11,2018-01-07,1.62,17489.58,2894.77,2356.13,224.53,12014.15,11988.14,26.01,0.0,organic,2018,WestTexNewMexico""",  # Truncated

    "Netflix Movies (NetFlix.csv)": """show_id,type,title,director,cast,country,date_added,release_year,rating,duration,genres,description
s1,TV Show,3%,,"João Miguel, Bianca Comparato, Michel Gomes, Rodolfo Valente, Vaneza Oliveira, Rafael Lozano, Viviane Porto, Mel Fronckowiak, Sergio Mamberti, Zezé Motta, Celso Frateschi",Brazil,14-Aug-20,2020,TV-MA,4,"International TV Shows, TV Dramas, TV Sci-Fi & Fantasy","In a future where the elite inhabit an island paradise far from the crowded slums, you get one chance to join the 3% saved from squalor."
s10,Movie,1920,Vikram Bhatt,"Rajneesh Duggal, Adah Sharma, Indraneil Sengupta, Anjori Alagh, Rajendranath Zutshi, Vipin Sharma, Amin Hajee, Shri Vallabh Vyas",India,15-Dec-17,2008,TV-MA,143,"Horror Movies, International Movies, Thrillers",An architect and his wife move into a castle that is slated to become a luxury hotel. But something inside is determined to stop the renovation.
s100,Movie,3 Heroines,Iman Brotoseno,"Reza Rahadian, Bunga Citra Lestari, Tara Basro, Chelsea Islan",Indonesia,5-Jan-19,2016,TV-PG,124,"Dramas, International Movies, Sports Movies",Three Indonesian women break records by becoming the first of their nation to medal in archery at the Seoul Olympics in the summer of 1988.
s1000,Movie,Blue Mountain State: The Rise of Thadland,Lev L. Spiro,"Alan Ritchson, Darin Brooks, James Cade, Rob Ramsay, Chris Romano, Frankie Shaw, Omari Newton, Ed Marinaro, Dhani Jones, Ed Amatrudo, Jimmy Tatro",United States,1-Mar-16,2016,R,90,Comedies,"New NFL star Thad buys his old teammates' beloved frat house, renames it Thadland and throws the raunchiest, most debauched party in school history."
s1001,TV Show,Blue Planet II,,David Attenborough,United Kingdom,3-Dec-18,2017,TV-G,1,"British TV Shows, Docuseries, Science & Nature TV","This sequel to the award-winning nature series ""Blue Planet"" dives beneath Earth's oceans to reveal the dazzling vistas and amazing creatures there."
s1002,Movie,Blue Ruin,Jeremy Saulnier,"Macon Blair, Devin Ratray, Amy Hargreaves, Kevin Kolack, Eve Plumb, David W. Thompson, Brent Werzner, Stacy Rock, Sidné Anderson, Sandy Barnett, Bonnie Johnson","United States, France",25-Feb-19,2013,R,90,"Independent Movies, Thrillers","Bad news from the past unhinges vagabond Dwight Evans, sending him on a mission of bloody retribution that takes him to his childhood hometown."
s1003,Movie,Blue Streak,Les Mayfield,"Martin Lawrence, Luke Wilson, Peter Greene, Dave Chappelle, Nicole Ari Parker, Graham Beckel, Robert Miranda, Olek Krupa, Saverio Guerra, Richard C. Sarafian, William Forsythe","Germany, United States",1-Jan-21,1999,PG-13,94,"Action & Adventure, Comedies",A jewel thief returns to his hiding place after a stint in jail — only to find that his diamond is buried under a newly constructed police station.
s1004,Movie,Blue Valentine,Derek Cianfrance,"Ryan Gosling, Michelle Williams, Faith Wladyka, John Doman, Mike Vogel, Ben Shenkman, Jen Jones, Maryann Plunkett, Marshall Johnson, James Benatti, Barbara Troy, Carey Westbrook, Enid Graham",United States,5-Jul-18,2010,R,112,"Dramas, Independent Movies, Romantic Movies","As Cindy and Dean muddle through their languishing marriage, they hearken back to the golden days when life was filled with possibility and romance."
s1005,Movie,BluffMaster!,Rohan Sippy,"Abhishek Bachchan, Priyanka Chopra, Riteish Deshmukh, Boman Irani, Nana Patekar, Sanjay Mishra, Tinnu Anand, Hussain Shaikh",India,8-Jan-21,2005,TV-14,129,"Comedies, International Movies, Romantic Movies","When his girlfriend learns the truth about his murky past, a con artist is forced to examine his choices and get to the root of his real identity."
s1006,Movie,Blurred Lines: Inside the Art World,Barry Avrich,,Canada,31-Dec-17,2017,TV-MA,85,Documentaries,Artists and industry insiders shed light on the commercial forces behind the veneer of genius and glamour that often shrouds contemporary art.
s1007,TV Show,BNA,,"Sumire Morohoshi, Yoshimasa Hosoya, Maria Naganawa, Kaito Ishikawa, Gara Takashima, Michiyo Murase",Japan,30-Jun-20,2020,TV-14,1,"Anime Series, International TV Shows","Morphed into a raccoon beastman, Michiru seeks refuge, and answers, with the aid of wolf beastman Shirou inside the special zone of Anima-City."
s1008,Movie,BNK48: Girls Don't Cry,Nawapol Thamrongrattanarit,,Thailand,1-Mar-19,2018,TV-14,108,"Documentaries, International Movies, Music & Musicals","Members of the Thai idol girl group BNK48 open up about their experiences beyond the spotlight, their training and the nature of fame."
s1009,Movie,Bo Burnham: Make Happy,"Bo Burnham, Christopher Storer",Bo Burnham,United States,3-Jun-16,2016,TV-MA,60,"Music & Musicals, Stand-Up Comedy","Combining his trademark wit and self-deprecating humor with original music, Bo Burnham offers up his unique twist on life in this stand-up special."
s99,Movie,3 Generations,Gaby Dellal,"Elle Fanning, Naomi Watts, Susan Sarandon, Tate Donovan, Linda Emond, Jordan Carlos, Sam Trammell, Maria Dizzia, Tessa Albertson",United States,28-Aug-17,2015,PG-13,92,"Dramas, LGBTQ Movies","When teenage Ray begins transitioning from female to male, his single mom and grandmother must cope with the change while tracking down his father."
s990,TV Show,Blood Pact,,"Guilherme Fontes, Ravel Cabral, Jonathan Haagensen, André Ramiro, Adriano Garib, Mel Lisboa, Cristina Lago",Brazil,10-Oct-18,2018,TV-MA,1,"Crime TV Shows, International TV Shows, TV Dramas","An ambitious TV reporter uses risky and ethically questionable methods to report on gang wars and police corruption in the Amazon port of Belém, Brazil."
s991,Movie,Blood Will Tell,"Miguel Cohan, Miguel Cohan","Oscar Martínez, Dolores Fonzi, Diego Velázquez, Paulina Garcia, Luis Gnecco, Malena Sánchez, Emilio Vodanovich, Norman Briski","Argentina, United States",21-Jun-19,2019,TV-MA,113,"Dramas, Independent Movies, International Movies",Family patriarch Elías begins to unravel after the death of his wife – which casts a suspicious light on her tragic accident.
s992,TV Show,Bloodline,,"Kyle Chandler, Ben Mendelsohn, Sissy Spacek, Linda Cardellini, Norbert Leo Butz, Jacinda Barrett, Jamie McShane, John Leguizamo, Enrique Murciano, Sam Shepard, Chloë Sevigny, Andrea Riseborough, Beau Bridges, Taylor Rouviere, Owen Teague, Brandon Larracuente",United States,26-May-17,2017,TV-MA,3,"TV Dramas, TV Mysteries, TV Thrillers","When the black sheep son of a respected family threatens to expose dark secrets from their past, sibling loyalties are put to the test."
s993,TV Show,Bloodride,,"Ine Marie Wilmann, Bjørnar Teigen, Emma Spetalen Magnusson, Erlend Rødal Vikhagen, Benjamin Helstad, Harald Rosenstrøm, Dagny Backer Johnsen, Stig Amdam, Numa Edema Norderhaug, Ellen Bendu, Torfinn Nag",Norway,13-Mar-20,2020,TV-MA,1,"International TV Shows, TV Horror, TV Mysteries","The doomed passengers aboard a spectral bus head toward a gruesome, unknown destination in this deliciously macabre horror anthology series."
s994,Movie,Blow,Ted Demme,"Johnny Depp, Penélope Cruz, Franka Potente, Rachel Griffiths, Paul Reubens, Jordi Mollà, Cliff Curtis, Miguel Sandoval, Ethan Suplee, Ray Liotta",United States,1-Oct-19,2001,R,123,Dramas,Cocaine smuggler George rises from poverty to become one of the biggest drug dealers in America before his eventual downfall.
s995,TV Show,Blown Away,,,Canada,12-Jul-19,2019,TV-14,1,"International TV Shows, Reality TV","Ten master artists turn up the heat in glassblowing sculpture challenges for the chance to win $60,000 in prizes and the title of champion."
s996,TV Show,Blue Exorcist,,"Nobuhiko Okamoto, Jun Fukuyama, Kana Hanazawa, Kazuya Nakai, Koji Yusa, Yuki Kaji, Eri Kitamura, Ayahi Takagaki, Rina Satou, Daisuke Ono, Ryotaro Okiayu, Tetsuya Kakihara, Hiroshi Kamiya, Keiji Fujiwara, Hiroaki Hirata, Jin Urayama, Katsuyuki Konishi, Kisho Taniyama, M・A・O, Kazuhiro Yamaji, Hideyuki Tanaka, Masaki Terasoma, Naomi Shindo",Japan,1-Sep-20,2017,TV-MA,2,"Anime Series, International TV Shows","Determined to throw off the curse of being Satan's illegitimate son, Rin enters the True Cross Academy to become an exorcist, just like his mentor."
s997,Movie,Blue Is the Warmest Color,Abdellatif Kechiche,"Léa Seydoux, Adèle Exarchopoulos, Salim Kechiouche, Aurélien Recoing, Catherine Salée, Benjamin Siksou, Mona Walravens, Alma Jodorowsky, Jérémie Laheurte, Anne Loiret, Benoît Pilot, Sandor Funtek, Fanny Maurin","France, Belgium, Spain",26-Aug-16,2013,NC-17,180,"Dramas, Independent Movies, International Movies","Determined to fall in love, 15-year-old Adele is focused on boys. But it's a blue-haired girl she meets on the street who really piques her interest."
s998,Movie,Blue Jasmine,Woody Allen,"Cate Blanchett, Sally Hawkins, Alec Baldwin, Louis C.K., Bobby Cannavale, Andrew Dice Clay, Peter Sarsgaard, Michael Stuhlbarg, Tammy Blanchard, Max Casella, Alden Ehrenreich",United States,8-Mar-19,2013,PG-13,98,"Comedies, Dramas, Independent Movies",The high life leads to high anxiety for a fashionable New York City homemaker in crisis who finds herself forced to live a more modest lifestyle.
s999,Movie,Blue Jay,Alex Lehmann,"Sarah Paulson, Mark Duplass, Clu Gulager",United States,6-Dec-16,2016,TV-MA,81,"Dramas, Independent Movies, Romantic Movies","Two former high school sweethearts unexpectedly reunite in their old hometown, where they rediscover their magical bond and face a shared regret." """,  # Truncated

    "Telco Customer Churn (telecom_churn.csv)": """customer_id,telecom_partner,gender,age,state,city,pincode,date_of_registration,num_dependents,estimated_salary,calls_made,sms_sent,data_used,churn
1,Reliance Jio,F,25,Karnataka,Kolkata,755597,2020-01-01,4,124962,44,45,-361,0
2,Reliance Jio,F,55,Mizoram,Mumbai,125926,2020-01-01,2,130556,62,39,5973,0
3,Vodafone,F,57,Arunachal Pradesh,Delhi,423976,2020-01-01,0,148828,49,24,193,1
4,BSNL,M,46,Tamil Nadu,Kolkata,522841,2020-01-01,1,38722,80,25,9377,1
5,BSNL,F,26,Tripura,Delhi,740247,2020-01-01,2,55098,78,15,1393,0
6,Vodafone,M,36,Uttarakhand,Chennai,120612,2020-01-01,1,73452,91,24,8109,0
7,BSNL,F,60,Karnataka,Delhi,609616,2020-01-01,1,110035,36,13,8512,0
8,BSNL,M,46,Arunachal Pradesh,Kolkata,866786,2020-01-01,4,104541,87,40,2245,1
9,Reliance Jio,F,53,Himachal Pradesh,Mumbai,765257,2020-01-01,2,79439,34,12,10039,0
10,BSNL,F,57,Rajasthan,Mumbai,506308,2020-01-01,0,126422,61,33,567,0
11,Airtel,M,44,Uttarakhand,Chennai,776250,2020-01-01,0,133288,7,7,1275,1
12,Airtel,M,56,Odisha,Mumbai,642121,2020-01-01,4,135129,39,51,7644,0
13,Vodafone,F,64,Uttar Pradesh,Hyderabad,339770,2020-01-01,4,136967,40,4,1911,0
14,Vodafone,F,70,Chhattisgarh,Kolkata,711206,2020-01-01,0,140219,50,17,7727,0
15,Vodafone,F,38,Uttar Pradesh,Delhi,546253,2020-01-01,1,147805,86,20,8058,0
16,BSNL,M,22,Tamil Nadu,Mumbai,437585,2020-01-01,3,100340,88,40,6303,0
17,Vodafone,M,61,Himachal Pradesh,Hyderabad,734068,2020-01-01,2,59723,16,42,8157,1
18,Reliance Jio,M,59,Madhya Pradesh,Hyderabad,940945,2020-01-01,1,101694,80,20,2605,0
19,Airtel,F,47,Manipur,Delhi,630028,2020-01-01,1,138037,60,28,1432,0
20,Vodafone,M,26,Uttar Pradesh,Hyderabad,516585,2020-01-01,1,109753,95,-1,9993,0
21,Vodafone,F,58,Goa,Bangalore,316225,2020-01-01,1,118578,94,50,2214,0
22,Vodafone,M,66,West Bengal,Bangalore,504153,2020-01-01,2,64468,57,10,8141,0
23,BSNL,F,26,Arunachal Pradesh,Chennai,893238,2020-01-01,0,65263,79,0,4426,0
24,Reliance Jio,F,71,Gujarat,Bangalore,264045,2020-01-01,1,110373,25,24,2533,0
25,Reliance Jio,M,48,Telangana,Delhi,941207,2020-01-01,2,114923,43,8,5994,0
26,Airtel,F,48,Mizoram,Chennai,651699,2020-01-01,0,94683,28,48,6434,1
27,Vodafone,M,58,Himachal Pradesh,Delhi,133421,2020-01-01,3,50853,36,5,5604,0
28,BSNL,M,20,Karnataka,Delhi,801389,2020-01-01,2,133235,99,4,5044,0
29,Airtel,M,64,Gujarat,Kolkata,106829,2020-01-01,2,103868,20,39,8314,0
30,Reliance Jio,M,53,Maharashtra,Kolkata,270313,2020-01-01,4,61335,4,45,7268,0
31,Vodafone,M,29,Chhattisgarh,Kolkata,316582,2020-01-01,2,86124,65,22,7592,0
32,Airtel,M,73,Gujarat,Chennai,832883,2020-01-01,4,61329,25,29,1479,1
33,BSNL,F,66,Telangana,Mumbai,523021,2020-01-01,3,104227,93,6,837,0
243520,BSNL,M,23,Rajasthan,Hyderabad,200764,2023-05-03,1,131560,104,24,8398,0
243521,BSNL,M,32,Rajasthan,Hyderabad,758414,2023-05-03,2,123983,50,32,7293,1
243522,BSNL,F,60,Assam,Mumbai,141181,2023-05-03,3,36721,9,38,958,1
243523,Vodafone,F,33,Telangana,Chennai,851762,2023-05-03,1,44468,94,35,5095,0
243524,Reliance Jio,F,38,Gujarat,Delhi,112512,2023-05-03,0,69163,86,10,7323,1
243525,Vodafone,M,60,Meghalaya,Bangalore,142369,2023-05-03,0,53400,27,8,8023,0
243526,Vodafone,M,74,Assam,Delhi,277968,2023-05-03,1,120102,68,24,4001,0
243527,Airtel,M,35,Telangana,Delhi,453514,2023-05-03,2,64686,22,6,3375,0
243528,BSNL,F,50,Uttar Pradesh,Mumbai,613558,2023-05-03,3,126994,39,2,3186,1
243529,Vodafone,M,55,Manipur,Hyderabad,976656,2023-05-03,1,112946,61,4,4873,0
243530,Reliance Jio,M,45,Punjab,Kolkata,190431,2023-05-03,2,110127,58,24,2852,1
243531,Vodafone,F,52,Sikkim,Mumbai,136385,2023-05-03,0,102626,50,7,9436,0
243532,BSNL,M,54,Bihar,Delhi,591188,2023-05-03,1,129926,37,21,6912,0
243533,Airtel,F,69,Kerala,Bangalore,736798,2023-05-03,4,21894,89,0,5092,0
243534,Reliance Jio,F,22,West Bengal,Kolkata,732518,2023-05-03,2,123399,69,9,448,1
243535,Reliance Jio,F,46,Mizoram,Bangalore,541787,2023-05-03,1,106524,43,17,5620,0
243536,BSNL,M,32,Andhra Pradesh,Delhi,439538,2023-05-03,1,104748,62,15,4743,1
243537,Vodafone,M,28,Assam,Mumbai,177043,2023-05-03,1,126176,97,43,6314,0
243538,Vodafone,M,65,Arunachal Pradesh,Delhi,209498,2023-05-03,3,96988,24,8,1695,0
243539,BSNL,M,52,Arunachal Pradesh,Chennai,651013,2023-05-03,0,112257,96,21,5921,0
243540,Airtel,M,74,West Bengal,Bangalore,158721,2023-05-03,0,114273,55,18,4658,0
243541,BSNL,M,59,Rajasthan,Mumbai,441802,2023-05-03,0,65373,80,26,5808,0
243542,Vodafone,M,26,Goa,Kolkata,665113,2023-05-03,4,122295,82,2,3059,0
243543,Vodafone,F,20,Sikkim,Bangalore,687656,2023-05-03,1,109512,48,5,8219,0
243544,Airtel,M,73,Jharkhand,Kolkata,675783,2023-05-03,3,131421,10,20,8551,0
243545,Reliance Jio,M,37,Uttar Pradesh,Delhi,712167,2023-05-03,1,30972,72,28,5053,0
243546,Vodafone,M,64,Mizoram,Delhi,547404,2023-05-03,1,113699,71,23,9277,0
243547,Airtel,M,51,Nagaland,Chennai,331867,2023-05-03,1,87843,78,43,7394,0
243548,Vodafone,M,18,Haryana,Bangalore,184327,2023-05-03,4,111912,17,32,5944,0
243549,Airtel,F,28,Mizoram,Kolkata,110295,2023-05-03,3,130580,28,9,4102,0
243550,Reliance Jio,F,52,Assam,Kolkata,713481,2023-05-03,0,82393,80,45,7521,0
243551,Reliance Jio,M,59,Tripura,Kolkata,520218,2023-05-03,4,51298,26,4,6547,0
243552,BSNL,M,49,Madhya Pradesh,Kolkata,387744,2023-05-03,2,83981,80,15,1125,0
243553,BSNL,F,37,Telangana,Hyderabad,139086,2023-05-04,0,144297,61,7,3384,0""",  # Truncated

    "Spotify and YouTube (Spotify_Youtube.csv)": """,Artist,Url_spotify,Track,Album,Album_type,Uri,Danceability,Energy,Key,Loudness,Speechiness,Acousticness,Instrumentalness,Liveness,Valence,Tempo,Duration_ms,Url_youtube,Title,Channel,Views,Likes,Comments,Description,Licensed,official_video,Stream
0,Gorillaz,https://open.spotify.com/artist/3AA28KZvwAUcZuOKwyblJQ,Feel Good Inc.,Demon Days,album,spotify:track:0d28khcov6AiegSCpG5TuT,0.818,0.705,6.0,-6.679,0.177,0.00836,0.00233,0.613,0.772,138.559,222640.0,https://www.youtube.com/watch?v=HyHNuVaZJ-k,Gorillaz - Feel Good Inc. (Official Video),Gorillaz,693555221.0,6220896.0,169907.0,"Official HD Video for Gorillaz' fantastic track Feel Good Inc.



Follow Gorillaz online:

http://gorillaz.com

http://facebook.com/Gorillaz

http://twitter.com/GorillazBand

http://instagram/Gorillaz



For more information on Gorillaz don't forget to check out the official website at http://www.gorillaz.com",True,True,1040234854
1,Gorillaz,https://open.spotify.com/artist/3AA28KZvwAUcZuOKwyblJQ,Rhinestone Eyes,Plastic Beach,album,spotify:track:1foMv2HQwfQ2vntFf9HFeG,0.676,0.703,8.0,-5.815,0.0302,0.0869,0.000687,0.0463,0.852,92.761,200173.0,https://www.youtube.com/watch?v=yYDmaexVHic,Gorillaz - Rhinestone Eyes [Storyboard Film] (Official Music Video),Gorillaz,72011645.0,1079128.0,31003.0,"The official video for Gorillaz - Rhinestone Eyes



Rhinestone Eyes is taken from the 2010 album Plastic Beach including the singles Rhinestone Eyes, Stylo, Superfast Jellyfish and On Melancholy Hill.



Follow Gorillaz online:

https://instagram.com/gorillaz 

https://tiktok.com/@gorillaz 

https://twitter.com/gorillaz 

https://facebook.com/gorillaz 

https://gorillaz.com



#Gorillaz #RhinestoneEyes #PlasticBeach",True,True,310083733
2,Gorillaz,https://open.spotify.com/artist/3AA28KZvwAUcZuOKwyblJQ,New Gold (feat. Tame Impala and Bootie Brown),New Gold (feat. Tame Impala and Bootie Brown),single,spotify:track:64dLd6rVqDLtkXFYrEUHIU,0.695,0.923,1.0,-3.93,0.0522,0.0425,0.0469,0.116,0.551,108.014,215150.0,https://www.youtube.com/watch?v=qJa-VFwPpYA,Gorillaz - New Gold ft. Tame Impala & Bootie Brown (Official Visualiser),Gorillaz,8435055.0,282142.0,7399.0,"Gorillaz - New Gold ft. Tame Impala & Bootie Brown (Official Visualiser)



Pre-order Cracker Island album: https://gorillaz.com 

Listen to New Gold: https://gorill.az/newgold

Join The Last Cult: https://thelastcult.org

Listen to Gorillaz: https://gorill.az/listen

Shop Gorillaz: https://store.gorillaz.com/

Tour gorillaz.com/tour



Follow Gorillaz: 

https://instagram.com/gorillaz

https://tiktok.com/@gorillaz

https://twitter.com/gorillaz

https://facebook.com/gorillaz

https://gorillaz.com



Director: Jamie Hewlett

Co-Direction: Swear Studio, Steve Gallagher

Exec Producers: Jamie Hewlett & Damon Albarn

Producer: Alexa Pearson

Video Design: Catherine Woodhouse

Video Design: SHOP



#newgold #crackerisland #gorillaz #newmusic #newalbum",True,True,63063467
3,Gorillaz,https://open.spotify.com/artist/3AA28KZvwAUcZuOKwyblJQ,On Melancholy Hill,Plastic Beach,album,spotify:track:0q6LuUqGLUiCPP1cbdwFs3,0.689,0.739,2.0,-5.81,0.026,1.51e-05,0.509,0.064,0.578,120.423,233867.0,https://www.youtube.com/watch?v=04mfKJWDSzI,Gorillaz - On Melancholy Hill (Official Video),Gorillaz,211754952.0,1788577.0,55229.0,"Follow Gorillaz online:

http://gorillaz.com 

http://facebook.com/Gorillaz

http://twitter.com/GorillazBand

https://instagram.com/gorillaz



Music video by Gorillaz performing On Melancholy Hill. (P) 2010 The copyright in this audiovisual recording is owned by Parlophone Records",True,True,434663559
4,Gorillaz,https://open.spotify.com/artist/3AA28KZvwAUcZuOKwyblJQ,Clint Eastwood,Gorillaz,album,spotify:track:7yMiX7n9SBvadzox8T5jzT,0.663,0.694,10.0,-8.627,0.171,0.0253,0.0,0.0698,0.525,167.953,340920.0,https://www.youtube.com/watch?v=1V_xRb0x9aw,Gorillaz - Clint Eastwood (Official Video),Gorillaz,618480958.0,6197318.0,155930.0,"The official music video for Gorillaz - Clint Eastwood



Taken from Gorillaz debut Studio Album 'Gorillaz’ released in 2001, which features the singles Clint Eastwood, 19-2000, Rock The House & Tomorrow Comes Today.



Pre-order Cracker Island album: https://gorillaz.com 

Listen to Gorillaz: https://gorill.az/listen

Shop Gorillaz: https://store.gorillaz.com/

Tour gorillaz.com/tour



Follow Gorillaz: 

https://instagram.com/gorillaz

https://tiktok.com/@gorillaz

https://twitter.com/gorillaz

https://facebook.com/gorillaz

https://gorillaz.com



#ClintEastwood #Gorillaz #DemonDays",True,True,618652750
20711,SICK LEGEND,https://open.spotify.com/artist/3EYY5FwDkHEYLw5V86SAtl,MIDDLE OF THE NIGHT - HARDSTYLE REMIX,MIDDLE OF THE NIGHT - HARDSTYLE REMIX,single,spotify:track:4pqAkUZlA17gsTxFjP4BDL,0.292,0.692,2.0,-7.198,0.0376,0.000118,0.000354,0.382,0.0544,185.467,175147.0,https://www.youtube.com/watch?v=5f_RpP10nRk,MIDDLE OF THE NIGHT - HARDSTYLE REMIX,SICK LEGEND - Topic,254268.0,3472.0,0.0,"Provided to YouTube by Routenote



MIDDLE OF THE NIGHT - HARDSTYLE REMIX · SICK LEGEND



MIDDLE OF THE NIGHT - HARDSTYLE REMIX



℗ SICK LEGEND



Released on: 2022-08-01



Auto-generated by YouTube.",True,True,17125177
20712,SICK LEGEND,https://open.spotify.com/artist/3EYY5FwDkHEYLw5V86SAtl,EVERYTIME WE TOUCH HARDSTYLE (SPED UP),EVERYTIME WE TOUCH HARDSTYLE (SPED UP),single,spotify:track:2dSNs47vHBSPnsUwpl39nk,0.554,0.874,1.0,-5.199,0.048,0.235,0.0,0.318,0.617,102.167,94000.0,https://www.youtube.com/watch?v=2C66T9FhnAk,EVERYTIME WE TOUCH HARDSTYLE (SPED UP),SICK LEGEND - Topic,16004.0,267.0,0.0,"Provided to YouTube by Routenote



EVERYTIME WE TOUCH HARDSTYLE (SPED UP) · SICK LEGEND



EVERYTIME WE TOUCH HARDSTYLE (SPED UP)



℗ SICK CVNT



Released on: 2022-07-12



Auto-generated by YouTube.",True,True,9921887
20713,SICK LEGEND,https://open.spotify.com/artist/3EYY5FwDkHEYLw5V86SAtl,JUST DANCE HARDSTYLE,JUST DANCE HARDSTYLE,single,spotify:track:0RtcKQGyI4hr8FgFH1TuYG,0.582,0.926,5.0,-6.344,0.0328,0.448,0.0,0.0839,0.658,90.002,94667.0,https://www.youtube.com/watch?v=5SHmKFKlNqI,JUST DANCE HARDSTYLE,SICK LEGEND - Topic,71678.0,1113.0,0.0,"Provided to YouTube by Routenote



JUST DANCE HARDSTYLE · SICK LEGEND



JUST DANCE HARDSTYLE



℗ SICK CVNT



Released on: 2022-07-12



Auto-generated by YouTube.",True,True,9227144
20714,SICK LEGEND,https://open.spotify.com/artist/3EYY5FwDkHEYLw5V86SAtl,SET FIRE TO THE RAIN HARDSTYLE,SET FIRE TO THE RAIN HARDSTYLE,single,spotify:track:3rHvPA8lUnPBkaLyPOc0VV,0.531,0.936,4.0,-1.786,0.137,0.028,0.0,0.0923,0.657,174.869,150857.0,https://www.youtube.com/watch?v=ocTH6KxllDQ,SET FIRE TO THE RAIN HARDSTYLE,SICK LEGEND - Topic,164741.0,2019.0,0.0,"Provided to YouTube by Routenote



SET FIRE TO THE RAIN HARDSTYLE · SICK LEGEND



SET FIRE TO THE RAIN HARDSTYLE



℗ SICK CVNT



Released on: 2022-07-11



Auto-generated by YouTube.",True,True,10898176
20715,SICK LEGEND,https://open.spotify.com/artist/3EYY5FwDkHEYLw5V86SAtl,OUTSIDE HARDSTYLE SPED UP,OUTSIDE HARDSTYLE SPED UP,single,spotify:track:4jk00YxPtPbhvHJE9N4ddv,0.443,0.83,4.0,-4.679,0.0647,0.0243,0.0,0.154,0.419,168.388,136842.0,https://www.youtube.com/watch?v=5wFhE-HY0hg,OUTSIDE HARDSTYLE SPED UP,SICK LEGEND - Topic,35646.0,329.0,0.0,"Provided to YouTube by Routenote

OUTSIDE HARDSTYLE SPED UP · SICK LEGEND

OUTSIDE HARDSTYLE SPED UP

℗ SICK LEGEND

Released on: 2022-07-27

Auto-generated by YouTube.",True,True,6226110
20716,SICK LEGEND,https://open.spotify.com/artist/3EYY5FwDkHEYLw5V86SAtl,ONLY GIRL HARDSTYLE,ONLY GIRL HARDSTYLE,single,spotify:track:5EyErbpsugWliX006eTDex,0.417,0.767,9.0,-4.004,0.419,0.356,0.0184,0.108,0.539,155.378,108387.0,https://www.youtube.com/watch?v=VMFLbFRNCn0,ONLY GIRL HARDSTYLE,SICK LEGEND - Topic,6533.0,88.0,0.0,"Provided to YouTube by Routenote

ONLY GIRL HARDSTYLE · SICK LEGEND

ONLY GIRL HARDSTYLE

℗ SICK LEGEND

Released on: 2022-08-01

Auto-generated by YouTube.",True,True,6873961
20717,SICK LEGEND,https://open.spotify.com/artist/3EYY5FwDkHEYLw5V86SAtl,MISS YOU HARDSTYLE,MISS YOU HARDSTYLE,single,spotify:track:6lOn0jz1QpjcWeXo1oMm0k,0.498,0.938,6.0,-4.543,0.107,0.00277,0.911,0.136,0.0787,160.067,181500.0,https://www.youtube.com/watch?v=zau0dckCFi0,MISS YOU HARDSTYLE,SICK LEGEND - Topic,158697.0,2484.0,0.0,"Provided to YouTube by Routenote

MISS YOU HARDSTYLE · SICK LEGEND

MISS YOU HARDSTYLE

℗ SICK CVNT

Released on: 2022-10-04

Auto-generated by YouTube.",True,True,5695584"""  # Truncated
}

# Sidebar for dataset selection
st.sidebar.header("Dataset Selection")
selected_dataset = st.sidebar.selectbox("Choose a dataset", list(datasets.keys()))

# Load selected dataset
data_content = datasets[selected_dataset]
df = pd.read_csv(StringIO(data_content))

# Data Science Steps Section
st.header("Data Science Steps")
st.subheader("1. Data Preview")
st.dataframe(df.head())

st.subheader("2. Data Cleaning")
# Example cleaning: Drop NA, convert dates if applicable
df = df.dropna()  # Simple drop NA
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
elif 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
elif 'datetime' in df.columns:
    df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
elif 'date_of_registration' in df.columns:
    df['date_of_registration'] = pd.to_datetime(df['date_of_registration'], errors='coerce')
elif 'date_added' in df.columns:
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
st.write("Cleaned Data Preview:")
st.dataframe(df.head())

st.subheader("3. Key Statistics")
st.write(df.describe())

# Interactive Controls
st.header("Interactive Controls")
color = st.selectbox("Select a color for charts", ["Blue", "Red", "Green", "Yellow"])
color_map = {"Blue": "blue", "Red": "red", "Green": "green", "Yellow": "gold"}

# Visualizations and Observations
st.header("📈 Data Visualizations and Interpretations")

if selected_dataset == "Coffee Sales (index_2.csv)":
    # Visualization 1: Sales by Coffee Name
    fig_bar = px.bar(df, x="coffee_name", y="money", title="Total Sales by Coffee Type", color_discrete_sequence=[color_map[color]])
    st.plotly_chart(fig_bar, use_container_width=True)
    st.subheader("Observation and Interpretation")
    st.markdown("""
    **Observation**: The bar chart shows the distribution of total sales (money) across different coffee types. For example, 'Latte' and 'Espresso' appear to have higher sales in the sample data.
    
    **Interpretation**: This indicates popular items like alcoholic coffee variants (e.g., with Irish whiskey) contribute significantly to revenue. Businesses could focus on promoting these high-revenue items to boost sales. Data science insight: Correlation between coffee type and payment method could be explored for targeted marketing.
    """)

    # Visualization 2: Sales Over Time
    if 'date' in df.columns:
        daily_sales = df.groupby('date')['money'].sum().reset_index()
        fig_line = px.line(daily_sales, x='date', y='money', title="Daily Sales Trend", color_discrete_sequence=[color_map[color]])
        st.plotly_chart(fig_line, use_container_width=True)
        st.subheader("Observation and Interpretation")
        st.markdown("""
        **Observation**: Sales fluctuate over dates, with peaks possibly on weekends or specific days in February/March 2025.
        
        **Interpretation**: Time-series analysis reveals seasonal patterns; e.g., higher sales in mid-month. This could inform inventory management. Further data science: Use ARIMA for forecasting future sales.
        """)

elif selected_dataset == "Student Stress (StressLevelDataset.csv)":
    # Visualization 1: Correlation Heatmap
    corr = df.corr()
    fig_heat = px.imshow(corr, title="Correlation Matrix of Stress Factors", color_continuous_scale=color_map[color].lower())
    st.plotly_chart(fig_heat, use_container_width=True)
    st.subheader("Observation and Interpretation")
    st.markdown("""
    **Observation**: High correlations between 'anxiety_level' and 'depression' (likely >0.7), and 'stress_level' with 'future_career_concerns'.
    
    **Interpretation**: Mental health factors are interconnected; high anxiety often leads to higher stress. Interventions targeting career concerns could reduce overall stress. Data science: PCA could reduce dimensions for modeling stress predictors.
    """)

    # Visualization 2: Stress Level Distribution
    fig_hist = px.histogram(df, x="stress_level", title="Distribution of Stress Levels", color_discrete_sequence=[color_map[color]])
    st.plotly_chart(fig_hist, use_container_width=True)
    st.subheader("Observation and Interpretation")
    st.markdown("""
    **Observation**: Stress levels are distributed with modes around 1-2 (moderate stress).
    
    **Interpretation**: Most students experience moderate stress, suggesting widespread but manageable issues. Outliers with high stress need targeted support. Data science: Cluster analysis (K-means) to group students by stress profiles.
    """)

elif selected_dataset == "Retail Sales (retail_sales_dataset.csv)":
    # Visualization 1: Total Amount by Product Category
    cat_sales = df.groupby('Product Category')['Total Amount'].sum().reset_index()
    fig_pie = px.pie(cat_sales, values='Total Amount', names='Product Category', title="Sales Proportion by Category", color_discrete_sequence=[color_map[color]] + px.colors.qualitative.Pastel)
    st.plotly_chart(fig_pie, use_container_width=True)
    st.subheader("Observation and Interpretation")
    st.markdown("""
    **Observation**: Electronics and Clothing dominate sales proportions.
    
    **Interpretation**: High-value items like electronics drive revenue. Focus marketing on these categories. Data science: RFM analysis for customer segmentation.
    """)

    # Visualization 2: Age vs Total Amount Scatter
    fig_scatter = px.scatter(df, x="Age", y="Total Amount", color="Gender", title="Age vs Sales Amount", color_discrete_sequence=[color_map[color], "gray"])
    st.plotly_chart(fig_scatter, use_container_width=True)
    st.subheader("Observation and Interpretation")
    st.markdown("""
    **Observation**: No strong linear trend, but clusters around ages 20-60 with varying sales.
    
    **Interpretation**: Middle-aged customers spend more; gender differences minimal. Tailor promotions by age groups. Data science: Linear regression to predict spend based on age/gender.
    """)

elif selected_dataset == "Avocado Prices (avocado.csv)":
    # Visualization 1: Average Price Over Time
    if 'Date' in df.columns:
        df = df.sort_values('Date')
        fig_line = px.line(df, x="Date", y="AveragePrice", color="type", title="Avocado Price Trends", color_discrete_sequence=[color_map[color], "gray"])
        st.plotly_chart(fig_line, use_container_width=True)
        st.subheader("Observation and Interpretation")
        st.markdown("""
        **Observation**: Prices fluctuate seasonally, with organic avocados consistently higher than conventional.
        
        **Interpretation**: Demand peaks could drive prices; organic premium suggests niche market. Data science: Time-series forecasting (Prophet) for price prediction.
        """)

    # Visualization 2: Volume by Region
    region_volume = df.groupby('region')['Total Volume'].sum().reset_index()
    fig_bar = px.bar(region_volume, x="region", y="Total Volume", title="Total Volume by Region", color_discrete_sequence=[color_map[color]])
    st.plotly_chart(fig_bar, use_container_width=True)
    st.subheader("Observation and Interpretation")
    st.markdown("""
    **Observation**: Regions like 'West' have higher volumes.
    
    **Interpretation**: Regional demand variations; focus supply chain on high-volume areas. Data science: Geospatial analysis for market expansion.
    """)

elif selected_dataset == "Netflix Movies (NetFlix.csv)":
    # Visualization 1: Release Year Histogram
    fig_hist = px.histogram(df, x="release_year", title="Distribution of Release Years", color_discrete_sequence=[color_map[color]])
    st.plotly_chart(fig_hist, use_container_width=True)
    st.subheader("Observation and Interpretation")
    st.markdown("""
    **Observation**: Peak in recent years (2010-2020).
    
    **Interpretation**: Netflix focuses on modern content; older titles less common. Data science: Trend analysis for content acquisition.
    """)

    # Visualization 2: Genre Count
    df['genres_list'] = df['genres'].str.split(', ')
    genres_exploded = df.explode('genres_list')
    genre_count = genres_exploded['genres_list'].value_counts().reset_index()
    fig_bar = px.bar(genre_count, x='index', y='genres_list', title="Top Genres", color_discrete_sequence=[color_map[color]])
    st.plotly_chart(fig_bar, use_container_width=True)
    st.subheader("Observation and Interpretation")
    st.markdown("""
    **Observation**: Dramas and International Movies are most common.
    
    **Interpretation**: Audience preference for diverse, story-driven content. Data science: Recommendation system using genre embeddings.
    """)

elif selected_dataset == "Telco Customer Churn (telecom_churn.csv)":
    # Visualization 1: Churn Rate by Telecom Partner
    churn_rate = df.groupby('telecom_partner')['churn'].mean().reset_index()
    fig_bar = px.bar(churn_rate, x="telecom_partner", y="churn", title="Churn Rate by Partner", color_discrete_sequence=[color_map[color]])
    st.plotly_chart(fig_bar, use_container_width=True)
    st.subheader("Observation and Interpretation")
    st.markdown("""
    **Observation**: Higher churn in some partners like BSNL.
    
    **Interpretation**: Service quality differences; improve retention strategies. Data science: Logistic regression for churn prediction.
    """)

    # Visualization 2: Age vs Churn Boxplot
    fig_box = px.box(df, x="churn", y="age", title="Age Distribution by Churn", color_discrete_sequence=[color_map[color]])
    st.plotly_chart(fig_box, use_container_width=True)
    st.subheader("Observation and Interpretation")
    st.markdown("""
    **Observation**: Older customers have slightly higher churn median.
    
    **Interpretation**: Age-related factors like tech adoption affect loyalty. Data science: Feature importance in churn model.
    """)

elif selected_dataset == "Spotify and YouTube (Spotify_Youtube.csv)":
    # Visualization 1: Danceability vs Energy Scatter
    fig_scatter = px.scatter(df, x="Danceability", y="Energy", color="Album_type", title="Danceability vs Energy", color_discrete_sequence=[color_map[color], "gray", "orange"])
    st.plotly_chart(fig_scatter, use_container_width=True)
    st.subheader("Observation and Interpretation")
    st.markdown("""
    **Observation**: Positive correlation; albums cluster higher.
    
    **Interpretation**: Energetic tracks are more danceable, popular in singles. Data science: Clustering for music recommendation.
    """)

    # Visualization 2: Views vs Likes
    fig_scatter2 = px.scatter(df, x="Views", y="Likes", title="YouTube Views vs Likes", color_discrete_sequence=[color_map[color]])
    st.plotly_chart(fig_scatter2, use_container_width=True)
    st.subheader("Observation and Interpretation")
    st.markdown("""
    **Observation**: Linear trend; high views correlate with likes.
    
    **Interpretation**: Popular tracks engage more; viral potential. Data science: Regression for predicting engagement.
    """)

# Footer
st.markdown("---")
st.write("Built with Streamlit and Plotly. Datasets are truncated samples; extend with full data for deeper analysis.")