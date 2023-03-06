import streamlit as st
import sklearn
import pickle
import pandas as pd
import datetime
import time
random_date = '2019-02-02 01:01:01'
# This is where the issue occurs



model = pickle.load(open("flight_rf.pkl", "rb"))
df = pd.read_csv('Data_Train.csv')


st.title("Flight Fare Prediction")


#One
# st.subheader("Select Departure")
# m = pd.to_datetime("today").month
# d = pd.to_datetime("today").day
# y = pd.to_datetime("today").year
#
# dep = st.date_input("Day", datetime.date(y, m, d))
# if dep is not None:
#     mon_d = dep.month
#     day_d = dep.day
#
#     hour_1 = st.selectbox("Hour", list(range(1, 25)))
#     minute_1 = st.selectbox("Minute", list(range(0, 61)))
#
# st.subheader("Departure Time :")
# x = "2020" + "/" + str(mon_d) + "/" + str(day_d) + " " + str(hour_1) + ":" + str(minute_1)
# if x is not None:
#     op = pd.to_datetime([x])
#     if op is not None:
#         st.write(op.item())
#
#
# #Two
# st.subheader("Select Arrival")
# arr = st.date_input("Day.", datetime.date(y, m, d + 1))
#
# if arr is not None:
#     mon_a = arr.month
#     day_a = arr.day
#
#     hour_2 = st.selectbox("Hour.", list(range(1, 25)), 2)
#     minute_2 = st.selectbox("Minute.", list(range(0, 61)))
#
# st.subheader("Arrival Time :")
# x1 = "2020" + "/" + str(mon_a) + "/" + str(day_a) + " " + str(hour_2) + ":" + str(minute_2)
# if x1 is not None:
#
#     op1 = pd.to_datetime([x1])
#     if op1 is not None:
#         st.write(op1.item())
#
Journey_Day = st.number_input('Select Journey Date:')
Journey_month = st.number_input('Select Journey month:')
Dep_Hour=st.number_input('Enter Departure Hour:')
Dep_minute=st.number_input('Enter Departure Minute:')
Arr_hour=st.number_input('Enter Arrival Hour:')
Arr_minute=st.number_input('Enter Arrival minute:')
Duration_hours=st.number_input('Enter Duration hours:')
Duration_minutes=st.number_input('Enter Duration minutes:')


Source = st.selectbox('Source:',['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])
Destination = st.selectbox('Destination:',['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'])
Total_stops = st.selectbox('No.of stops:',[0,1,2,3,4])
airline = st.selectbox('Airline :',['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet','Multiple carriers', 'GoAir', 'Vistara', 'Air Asia','Vistara Premium economy', 'Jet Airways Business','Multiple carriers Premium economy', 'Trujet'])

# prediction=''
# if st.button('Predict'):
#     input = pd.DataFrame([[date_dep, date_arr, Source, Destination, Total_stops,airline]], columns=['journey_day', 'journey_month',  'Source', 'Destination', 'Total_stops', 'Airline'])
#     prediction += str(model.predict(input)[0])
#
# st.success(prediction)

# date_dep = request.form["Dep_Time"]
Jet_Airways = 0
IndiGo = 0
Air_India = 0
Multiple_carriers = 0
SpiceJet = 0
Vistara = 0
GoAir = 0
Multiple_carriers_Premium_economy = 0
Jet_Airways_Business = 0
Vistara_Premium_economy = 0
Trujet = 0


#if st.button('Predict'):
    # airline = request.form['airline']
if (airline == 'Jet Airways'):
    Jet_Airways = 1
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'IndiGo'):
    Jet_Airways = 0
    IndiGo = 1
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'Air India'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 1
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'Multiple carriers'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 1
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'SpiceJet'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 1
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'Vistara'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 1
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'GoAir'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 1
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'Multiple carriers Premium economy'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 1
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'Jet Airways Business'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 1
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'Vistara Premium economy'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 1
    Trujet = 0

elif (airline == 'Trujet'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 1

else:
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

    # print(Jet_Airways,
    #     IndiGo,
    #     Air_India,
    #     Multiple_carriers,
    #     SpiceJet,
    #     Vistara,
    #     GoAir,
    #     Multiple_carriers_Premium_economy,
    #     Jet_Airways_Business,
    #     Vistara_Premium_economy,
    #     Trujet)

    # Source
    # Banglore = 0 (not in column)
    # Source = request.form["Source"]
s_Delhi = 0
s_Kolkata = 0
s_Mumbai = 0
s_Chennai = 0
if (Source == 'Delhi'):
    s_Delhi = 1
    s_Kolkata = 0
    s_Mumbai = 0
    s_Chennai = 0

elif (Source == 'Kolkata'):
    s_Delhi = 0
    s_Kolkata = 1
    s_Mumbai = 0
    s_Chennai = 0

elif (Source == 'Mumbai'):
    s_Delhi = 0
    s_Kolkata = 0
    s_Mumbai = 1
    s_Chennai = 0

elif (Source == 'Chennai'):
    s_Delhi = 0
    s_Kolkata = 0
    s_Mumbai = 0
    s_Chennai = 1

else:
    s_Delhi = 0
    s_Kolkata = 0
    s_Mumbai = 0
    s_Chennai = 0

    # print(s_Delhi,
    #     s_Kolkata,
    #     s_Mumbai,
    #     s_Chennai)

    # Destination
    # Banglore = 0 (not in column)
    # Source = request.form["Destination"]
d_Cochin = 0
d_Delhi = 0
d_New_Delhi = 0
d_Hyderabad = 0
d_Kolkata = 0
if (Destination == 'Cochin'):
    d_Cochin = 1
    d_Delhi = 0
    d_New_Delhi = 0
    d_Hyderabad = 0
    d_Kolkata = 0

elif (Destination == 'Delhi'):
    d_Cochin = 0
    d_Delhi = 1
    d_New_Delhi = 0
    d_Hyderabad = 0
    d_Kolkata = 0

elif (Source == 'New_Delhi'):
    d_Cochin = 0
    d_Delhi = 0
    d_New_Delhi = 1
    d_Hyderabad = 0
    d_Kolkata = 0

elif (Destination == 'Hyderabad'):
    d_Cochin = 0
    d_Delhi = 0
    d_New_Delhi = 0
    d_Hyderabad = 1
    d_Kolkata = 0

elif (Destination == 'Kolkata'):
    d_Cochin = 0
    d_Delhi = 0
    d_New_Delhi = 0
    d_Hyderabad = 0
    d_Kolkata = 1

else:
    d_Cochin = 0
    d_Delhi = 0
    d_New_Delhi = 0
    d_Hyderabad = 0
    d_Kolkata = 0

prediction=0
if st.button('Predict'):
    input=pd.DataFrame([[Total_stops,Journey_Day,Journey_month,Dep_Hour,Dep_minute,Arr_hour,Arr_minute,Duration_hours,Duration_minutes,Air_India,GoAir,IndiGo,Jet_Airways,Jet_Airways_Business,Multiple_carriers,Multiple_carriers_Premium_economy,SpiceJet,Trujet,Vistara,Vistara_Premium_economy,s_Chennai,s_Delhi,s_Kolkata,s_Mumbai,d_Cochin,d_Delhi,d_Hyderabad,d_Kolkata,d_New_Delhi
]],columns=['Total_Stops','Journey_day','Journey_month','Dep_hour','Dep_min','Arrival_hour','Arrival_min','Duration_hours','Duration_mins','Airline_Air India','Airline_GoAir','Airline_IndiGo','Airline_Jet Airways','Airline_Jet Airways Business','Airline_Multiple carriers','Airline_Multiple carriers Premium economy','Airline_SpiceJet','Airline_Trujet','Airline_Vistara','Airline_Vistara Premium economy','Source_Chennai','Source_Delhi','Source_Kolkata','Source_Mumbai','Destination_Cochin','Destination_Delhi','Destination_Hyderabad','Destination_Kolkata','Destination_New Delhi'])
    prediction+=model.predict(input)




    st.success("The Predicted Price is : "+str(prediction[0]))






