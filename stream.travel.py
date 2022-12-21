import pickle
import streamlit as st

travel_model = pickle.load(open('travel_model.sav', 'rb'))



st.title('Data Mining Prediksi Customer Travel')
st.title('Fadlie Muhammad Agustien 191351029')

Age = st.text_input ('Input nilai Age')

FrequentFlyer = st.text_input ('Input nilai Frequent Flyer')

AnnualIncomeClass = st.text_input ('Input nilai Annual Income Class')

ServicesOpted = st.text_input ('Input nilai Services Opted')

AccountSyncedToSocialMedia = st.text_input ('Input nilai Account Synced To Social Media')

BookedHotelOrNot = st.text_input ('Input nilai Booked Hotel Or Not')

trav_travel = ''

if st.button('Test Prediksi Customer') :
    trav_prediction = travel_model.predict([[Age, FrequentFlyer, AnnualIncomeClass, ServicesOpted, AccountSyncedToSocialMedia, BookedHotelOrNot]]) 

    if(trav_prediction[0] == 1):
        trav_travel = 'Customer bukan target'
    else :
        trav_travel = 'Customer adalah target'
    st.success(trav_travel)



