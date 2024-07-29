import streamlit as st


st.set_page_config(page_title='Attendence System', layout='wide')

st.header('Attendance System Using Face Recognition')
st.warning('If You find any Technical error in any Page please refresh the page')
with st.spinner('Loading Model And Connecting to Database'):
    import face_rec

# st.success('Model loaded and Database Connected to successfully')
# st.success('Database Connected to successfully')

# Instruction For Using App
url = "https://www.youtube.com/watch?v=b6AK9L6lb7c"
# st.markdown("Check out this [Demo](%s)" % url)

st.info('For any Suggestion or Problem contact me -----> prashankm5@gmail.com')

st.subheader('📝📝Registration Process [Demo](%s)' % url)
st.write('Step1.  Enter Your Name and Roll Number')
st.write('Step2.  Click on start button and give samples (Recommended more than 200 samples)')
st.write('Step3.  Click on Submit button)')
st.write('Step4.  Visit report page and click on "refresh data"')
st.write('Step5.  If You Data is available then You are registerd')
st.write('Step6.  If You Data is not available, Follow this process again')
st.image(r'image/reg.jpg')

st.subheader('📝📝Attendance Process')
st.write('Step1.  Visit Attendance page and Recheck Your data')
st.write('Step2.  Click on Submit button and hold for 30 seconds')
st.write('Step3.  Visit Report page and click on "Refresh log"')
st.info('Attendance will be taken every 30 seconds')
st.image(r'image/Pred.jpg')

st.subheader('📝📝Report')
st.write('Step1.  Visit Report page')
st.write('Step2.  Click on Register Data For check registration log')
st.write('Step2.  Click on Log For check Attendance')
st.write('Step3.  Click on "Refresh log" or Refresh Data')

st.image(r'image/report.jpg')

st.balloons()
