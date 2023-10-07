# Copyright (c) Iris (2023)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import plotly
import plotly.graph_objects as go

st.set_page_config(
    page_title="CEva"
)

## Define functions
# Convert sidebar to numbers and display results
# For ENG version
def ENG_to_num(opt):
   if opt in ['Not at all', 'Not easy', 'Very high', 
              'Difficult', 'Poor', 'Misaligned', 'Very far']:
      num = 1
   elif opt in ['A little bit', 'Maybe not', 'Little', 
                'Requires effort', 'High',  'Not easy', 
                'Doubtful', 'Not bad', 'Barely',
                'Far', 'Below average']:
      num = 2
   elif opt in ['Moderately interested', 'Moderately', 
                 'Have not think about it', 'Not sure', 
                 'Moderate', 'On average']:
      num = 3
   elif opt in ['Very interested', 'Very much', 'Very much aligned', 
                'Maybe', 'Very sure', 'Many',  'Easy', 'Very valuable', 
                'Low', 'Trustworthy', 'Good', 'Will try', 
                'Almost match',  'Close', 'Above average',  'Satisfied']:
      num = 4
   elif opt in ['Could not be more interested', 'Could not be more willing', 
                'Could not be more', 'Could not be more aligned', 
                'Highly likely', 'Could not be more certain', 'Plenty', 
                'Very easy', 'Once in a life time experience', 'Very low', 
                'Very trustworthy', 'Very good',  'Absolutely',  
                'Perfect match',  'Very close', 'Uniquely good', 'Very satisfied']:
      num = 5
   else:
      return "ERROR: No mapping of numbers for the option. Please check."
   
   return num
      

lan = st.sidebar.radio('请选择你的语言 Please select your language:', ["中文", "ENG"])

### Modify the chat function, add avatar and time interval

C_message = st.chat_message("CEva", avatar="😊") # avatar to be changed
C_message.write("你好！我是希娃。请在侧栏中选择你的语言。")
C_message.write("Hello! I am CEva. Please select your preferred language in the sidebar.")

if lan == "ENG":
  C_message.write("OK. Let's talk in English.")
  
  start = C_message.radio('Are you ready to start?', ["No", "Yes"])
  
  # if yes, start the survey
  if start == "Yes":
    job_title = C_message.text_input("Which position would you like to evaluate?") 
    if job_title:
      C_message.write(f"OK. Let's try to evaluate the position: **{job_title}**.")
      C_message.write("""Please complete the 20 questions below. 
                    All questions are on a 5-point scale.""") 
      
      with st.form("CEva_questionnaire"):

        pa1 = st.select_slider(
        '1. Are you interested in this area?',
        options=['Not at all', 'A little bit', 'Moderately interested', 'Very interested', 'Could not be more interested'],
        )

        pa1_sc = ENG_to_num(pa1)
        
        pa2 = st.select_slider(
        '2. Are you willing to contribute the next 5 years to this area?',
        options=['Not at all', 'A little bit', 'Moderately', 'Very much', 'Could not be more willing'],
        )

        pa2_sc = ENG_to_num(pa2)

        pa3 = st.select_slider(
        '3. Are there any opportunities of innovation in this area and are you willing to contribute to the innovation process?',
        options=['Not at all', 'A little bit', 'Moderately', 'Very much', 'Could not be more'],
        )

        pa3_sc = ENG_to_num(pa3)

        pa4 = st.select_slider(
        '4. Does this area match your education?',
        options=['Not at all', 'A little bit', 'Moderately', 'Very much aligned', 'Could not be more aligned'],
        )

        pa4_sc = ENG_to_num(pa4)

        pa5 = st.select_slider(
        '5. Will you pursue further education in this area?',
        options=['Not at all', 'Maybe not', 'Have not think about it', 'Maybe', 'Highly likely'],
        )

        pa5_sc = ENG_to_num(pa5)

        d1 = st.select_slider(
        '6. Are you sure about the career path?',
        options=['Not at all', 'A little bit', 'Moderately', 'Very sure', 'Could not be more certain'],
        )

        d1_sc = ENG_to_num(d1)
        
        d2 = st.select_slider(
        '7. Are there any opportunities for knowledge acquisition?',
        options=['Not at all', 'Little', 'Not sure', 'Many', 'Plenty'],
        )

        d2_sc = ENG_to_num(d2)

        d3 = st.select_slider(
        '8. Is it easy to switch jobs after 5 years?',
        options=['Not easy', 'Requires effort', 'Not sure', 'Easy', 'Very easy'],
        )

        d3_sc = ENG_to_num(d3)

        d4 = st.select_slider(
        '9. Is the experience valuable?',
        options=['Not at all', 'A little bit', 'Moderately', 'Very valuable', 'Once in a life time experience'],
        )

        d4_sc = ENG_to_num(d4)

        d5 = st.select_slider(
        '10. What is the risk level in being in this industry? (Think about the cyclicity of industry)',
        options=['Very high', 'High', 'Moderate', 'Low', 'Very low'],
        )

        d5_sc = ENG_to_num(d5)

        wl1 = st.select_slider(
        '11. Will life be easy if you work in this industry?',
        options=['Difficult', 'Not easy', 'Not sure', 'Easy', 'Very easy'],
        )

        wl1_sc = ENG_to_num(wl1)
        
        wl2 = st.select_slider(
        '12. What is the level of pressure in working in this industry? ',
        options=['Very high', 'High', 'Moderate', 'Low', 'Very low'],
        )

        wl2_sc = ENG_to_num(wl2)

        wl3 = st.select_slider(
        '13. Are team members trustworthy?',
        options=['Not at all', 'Doubtful', 'Not sure', 'Trustworthy', 'Very trustworthy'],
        )

        wl3_sc = ENG_to_num(wl3)

        wl4 = st.select_slider(
        '14. What about the welfare provided by the company?',
        options=['Poor', 'Not bad', 'Moderately', 'Good', 'Very good'],
        )

        wl4_sc = ENG_to_num(wl4)

        wl5 = st.select_slider(
        '15. Can I have positive influence on the team?',
        options=['Not at all', 'Little', 'Not sure', 'Will try', 'Absolutely'],
        )

        wl5_sc = ENG_to_num(wl5)

        p1 = st.select_slider(
        '16. Does the compensation match your capabilities?',
        options=['Misaligned', 'Barely', 'Not sure', 'Almost match', 'Perfect match'],
        )

        p1_sc = ENG_to_num(p1)
        
        p2 = st.select_slider(
        '17. What is the distance from the company to your home?',
        options=['Very far', 'Far', 'Moderate', 'Close', 'Very close'],
        )

        p2_sc = ENG_to_num(p2)

        p3 = st.select_slider(
        '18. What about the working environment?',
        options=['Poor', 'Below average', 'On average', 'Above average', 'Uniquely good'],
        )

        p3_sc = ENG_to_num(p3)

        p4 = st.select_slider(
        '19. Are you satisfied with the organization structure?',
        options=['Not at all', 'A little bit', 'Moderately', 'Satisfied', 'Very satisfied'],
        )

        p4_sc = ENG_to_num(p4)

        p5 = st.select_slider(
        '20. What about the promotion opportunities & bonus?',
        options=['Not at all', 'Little', 'On average', 'Above average', 'Plenty'],
        )

        p5_sc = ENG_to_num(p5)
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Thank you for completing the questionnaire. Below are the results.")
        
      if submitted:
        pa_total = pa1_sc + pa2_sc+ pa3_sc + pa4_sc + pa5_sc
        d_total = d1_sc + d2_sc + d3_sc + d4_sc + d5_sc
        wl_total = wl1_sc + wl2_sc + wl3_sc + wl4_sc + wl5_sc
        p_total = p1_sc + p2_sc + p3_sc + p4_sc + p5_sc
        total = pa_total+d_total+wl_total+p_total

        if total > 80:
           total_eva = f"which is above or equals to 80. **It fits you well.**"
        elif total > 70:
           total_eva = f"which is above or equals to 70. **It is a good opportunity.**"
        elif total > 60:
           total_eva = f"which is above or equals to 60. **It is acceptable.**"
        else:
           total_eva = f"which is below 60. **Maybe you would like to think twice.**"
        
        C_message_re = st.chat_message("CEva", avatar="😊") 
        C_message_re.write("""Let's see the results.""") 

        col_tl = st.columns(1)

        with col_tl:
           fig = go.Figure(go.Indicator(
              mode = "gauge+number",
              value = total,
              gauge = {'axis':{'range':[20,100]},
                       'bar': {'color': "#9eb9f3"}},
              domain = {'x': [0, 1], 'y': [0, 1]},
              title = {'text': "Total Score"}))

           st.plotly_chart(fig, use_container_width=True)

        col_pa, col_d = st.columns(2)

### change the color tune
### Add overall score and suggestion

        with col_pa:
           fig = go.Figure(go.Indicator(
              mode = "gauge+number",
              value = pa_total,
              gauge = {'axis':{'range':[5,25]},
                       'bar': {'color': "#9eb9f3"}},
              domain = {'x': [0, 1], 'y': [0, 1]},
              title = {'text': "Passion"}))

           st.plotly_chart(fig, use_container_width=True)

        with col_d:
           fig = go.Figure(go.Indicator(
              mode = "gauge+number",
              value = d_total,
              gauge = {'axis':{'range':[5,25]},
                       'bar': {'color': "#f6cf71"}},
              domain = {'x': [0, 1], 'y': [0, 1]},
              title = {'text': "Development"}))

           st.plotly_chart(fig, use_container_width=True)

        col_wl, col_p = st.columns(2)

        with col_wl:
           fig = go.Figure(go.Indicator(
              mode = "gauge+number",
              value = wl_total,
              gauge = {'axis':{'range':[5,25]},
                       'bar': {'color': "#8be0a4"}},
              domain = {'x': [0, 1], 'y': [0, 1]},
              title = {'text': "Work-life Balance"}))

           st.plotly_chart(fig, use_container_width=True)

        with col_p:
           # st.metric("Practicality", p_total)
           fig = go.Figure(go.Indicator(
              mode = "gauge+number",
              value = p_total,
              gauge = {'axis':{'range':[5,25]},
                       'bar': {'color': "#dcb0f2"}},
              domain = {'x': [0, 1], 'y': [0, 1]},
              title = {'text': "Practicality"}))

           st.plotly_chart(fig, use_container_width=True)
        
        C_message_con = st.chat_message("CEva", avatar="😊") 
        C_message_con.write(f"Your total score for the position {job_title} is **{total}**, "+total_eva)
        C_message_sug = st.chat_message("CEva", avatar="😊") 
        C_message_sug.markdown("""Suggestions from me:
                              * If a position scores less than 60, you might want to think twice.
                              * There is **no absolute cutoffs** of a good/bad job.
                              * My evaluation works best at comparing different options.
                              * Pay close attention to which area scores the most. Weigh it against what matters the most to you.
                              * There is usually a trade-off.
                              * **Follow your passion.**""") 
        
        C_message_end = st.chat_message("CEva", avatar="😊") 
        C_message_end.markdown("""Wish you all the best in your job hunting/career development.
                               
                               If you would like to share your results or just feel stressed out 
                               and need a listening ear, please feel free to email to Iris at shiqimeng_1@163.com.""")

      else:
        st.warning("Please remember to submit your answers.")

        
  # If no, display message.
  if start == "No":
    st.warning("""Just click "Yes" when you are ready and 
                    the evaluation will start.""")  
  
  # sidebar configuration
  with st.sidebar.expander("About"):
      st.markdown("""
      CEva is an open-source app built specifically for
      career evaluation. 
      """
    )
  with st.sidebar.expander("Background"):
      st.markdown("""
      ### How does CEva come into existence?
      The creator has encountered the 
      difficult moment of making a career choice.
      ### How does CEva work?
      - Check out [streamlit.io](https://streamlit.io)
      - Jump into our [documentation](https://docs.streamlit.io)
      - Ask a question in our [community
        forums](https://discuss.streamlit.io)
      ### How can CEva help?
      - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
      - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )
  with st.sidebar.expander("User Manual"):
      st.markdown("""
      ### How does CEva work?
      - Check out [streamlit.io](https://streamlit.io)
      - Jump into our [documentation](https://docs.streamlit.io)
      - Ask a question in our [community
        forums](https://discuss.streamlit.io)
      ### How can CEva help?
      - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
      - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )