import pickle 
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Tahun Mobil')
mileage = st.number_input('KM Mobil')
tax = st.number_input('Pajak Mobil')
mpg = st.number_input('Konsumsi BBM Mobil')
engineSize = st.number_input('Engine Size')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
        )
    st.write('Estimasi Harga Mobil Bekas dalam Ponds : ', predict)
    st.write('Estimasi Harga Mobil Bekas dalam IDR (Juta) :', predict*19000)
