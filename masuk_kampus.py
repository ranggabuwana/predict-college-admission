import streamlit as st

from joblib import load

trained_models = load('model_admission.pkl')

form = st.form(key='my-form')

gre = form.text_input('Masukkan nilai GRE')
toefl = form.text_input('Masukkan nilai TOEFL')
univ_rating = form.text_input('Masukkan nilai University_Rating')
sop = form.text_input('Masukkan nilai SOP')
lor = form.text_input('Masukkan nilai LOR')
cgpa = form.text_input('Masukkan nilai CGPA')
research = form.text_input('Masukkan nilai Research')

submit = form.form_submit_button('Hitung tingkat kelulusan!')

if submit:
  y_preds = trained_models.predict([[int(gre), int(toefl), int(univ_rating), float(sop), float(lor), float(cgpa), int(research)]])
  st.write('Hasil Perhitungan: ')
  st.write(f'Tingkat Kelulusan {y_preds[0]*100}%')