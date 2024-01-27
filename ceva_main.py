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
import time

st.set_page_config(
    page_title="CEva",
    page_icon = "logo.png"
)

# For CN version
def CN_to_num(opt):
   if opt in ['一点也不', '一点也没有','不容易','非常大','困难','不好','错配', '非常远','非常差']:
      num = 1
   elif opt in ['有一点点', '可能不会', '有点吃力','大','不轻松', '存疑', '不坏', '落差大','远','比较差', '一点点']:
      num = 2
   elif opt in ['中度感兴趣', '中度愿意', '中等', '没想好', '不确定','不远不近','平均水平', '中度满意', '平均水平']:
      num = 3
   elif opt in ['非常感兴趣', '非常愿意', '很多','非常匹配','可能会','确定', '比较多','容易', '有价值','小', '轻松', '低','靠谱', '好','试试看','差不多', '近','比较好','满意']:
      num = 4
   elif opt in ['极度感兴趣', '无条件愿意','不能更多', '不能更匹配', '非常有可能', '不能更确定', '超级多', '非常容易','非常难得的经历', '非常小', '非常轻松', '非常低', '非常靠谱','非常好', '肯定能', '完美匹配', '非常近', '非常满意', '很多']:
      num = 5
   else:
      return "错误：没有对应数字。请检查。"
   
   return num

# for ENG version
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

st.sidebar.image('./logo_rec.png')
lan = st.sidebar.radio('请选择你的语言 Please select your language:', ["😊","中文","ENG"])

### Modify the chat function, add avatar and time interval
time.sleep(0.5)
C_message = st.chat_message("CEva", avatar='avat.png') # avatar to be changed
C_message.write("你好！我是希娃。请在侧栏中选择你的语言。")
C_message.write("Hello! I am CEva. Please select your preferred language in the sidebar.")

time.sleep(0.5)

if lan == "ENG":
  C_message_en = st.chat_message("CEva", avatar='avat.png') 
  C_message_en.write("OK. Let's talk in English.")
  
  time.sleep(0.5)
  C_message_st = st.chat_message("CEva", avatar='avat.png') 
  start = C_message_st.radio('Are you ready to start?', ["No", "Yes"])
  
  # if yes, start the survey
  if start == "Yes":
    time.sleep(0.5)
    job_title = C_message_st.text_input("Which position would you like to evaluate?") 
    if job_title:
      time.sleep(0.5)
      C_message_pos = st.chat_message("CEva", avatar='avat.png') 
      C_message_pos.write(f"OK. Let's try to evaluate the position: **{job_title}**.")
      
      time.sleep(0.5)
      C_message_q = st.chat_message("CEva", avatar='avat.png') 
      C_message_q.write("""Please complete the 20 questions below. 
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
        '15. Can you have positive influence on the team?',
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

        if total >= 80:
           total_eva = f"which is above or equals to 80. **It fits you well.**"
        elif total >= 70:
           total_eva = f"which is above or equals to 70. **It is a good opportunity.**"
        elif total >= 60:
           total_eva = f"which is above or equals to 60. **It is acceptable.**"
        else:
           total_eva = f"which is below 60. **Maybe you would like to think twice.**"
        
        time.sleep(0.5)
        C_message_re = st.chat_message("CEva", avatar='avat.png') 
        C_message_re.write("""Let's see the results.""") 

        fig = go.Figure(go.Indicator(
         mode = "gauge+number",
         value = total,
         gauge = {'axis':{'range':[20,100]},
                  'bar': {'color': "#A67EB7"}},
         domain = {'x': [0, 1], 'y': [0, 1]},
         title = {'text': "Total Score"}))

        st.plotly_chart(fig, use_container_width=True)

        col_pa, col_d = st.columns(2)

        with col_pa:
           fig = go.Figure(go.Indicator(
              mode = "gauge+number",
              value = pa_total,
              gauge = {'axis':{'range':[5,25]},
                       'bar': {'color': "#F18F60"}},
              domain = {'x': [0, 1], 'y': [0, 1]},
              title = {'text': "Passion"}))

           st.plotly_chart(fig, use_container_width=True)

        with col_d:
           fig = go.Figure(go.Indicator(
              mode = "gauge+number",
              value = d_total,
              gauge = {'axis':{'range':[5,25]},
                       'bar': {'color': "#C3D94E"}},
              domain = {'x': [0, 1], 'y': [0, 1]},
              title = {'text': "Development"}))

           st.plotly_chart(fig, use_container_width=True)

        col_wl, col_p = st.columns(2)

        with col_wl:
           fig = go.Figure(go.Indicator(
              mode = "gauge+number",
              value = wl_total,
              gauge = {'axis':{'range':[5,25]},
                       'bar': {'color': "#6F94CD"}},
              domain = {'x': [0, 1], 'y': [0, 1]},
              title = {'text': "Work-life Balance"}))

           st.plotly_chart(fig, use_container_width=True)

        with col_p:
           # st.metric("Practicality", p_total)
           fig = go.Figure(go.Indicator(
              mode = "gauge+number",
              value = p_total,
              gauge = {'axis':{'range':[5,25]},
                       'bar': {'color': "#FFEE6F"}},
              domain = {'x': [0, 1], 'y': [0, 1]},
              title = {'text': "Practicality"}))

           st.plotly_chart(fig, use_container_width=True)
        
        C_message_con = st.chat_message("CEva", avatar='avat.png') 
        C_message_con.write(f"Your total score for the position {job_title} is **{total}**, "+total_eva)
        C_message_sug = st.chat_message("CEva", avatar='avat.png') 
        C_message_sug.markdown("""Suggestions from me:  
                              :star: If a position scores less than 60, you might want to think twice.  
                              :star: There are **no absolute cutoffs** for a good/bad job.  
                              :star: My evaluation works best at comparing different options.  
                              :star: Pay close attention to which area scores the most. Weigh it against what matters the most to you.  
                              :star: There is usually a trade-off.  
                              :star: :rainbow[**Follow your passion.**]""") 
        
        C_message_end = st.chat_message("CEva", avatar='avat.png') 
        C_message_end.markdown(""":confetti_ball: Wish you all the best in your job hunting/career development.:sparkles:  
                               If you would like to share your results or just feel stressed out and need a listening ear, please feel free to email to Iris at shiqimeng_1@163.com.""")
        

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
      **C**areer **EVa**luation. 
      """
    )
  with st.sidebar.expander("Background"):
      st.markdown("""
      ### How did CEva come into existence?
      The creator has encountered the 
      difficult moment of making a career decision. She created a 
                  20-question score system to evaluate different options. 
                  Yet, biased by other concerns, she chose the one with the 
                  lowest score, which unsurprisingly sent her to hell. :weary: Fortunately, 
                  she was able to overturn the bad decision and come back to a right track. 
                  This time, the score for the new opportunity surpasses all previous ones. 
                  From that point, the idea of creating CEva began to sprout: there should be 
                  some rational framework out there to help make rational decisions. :four_leaf_clover:  
      ### How does CEva work?
      - CEva uses a 20-question score system. All questions are on a 5-point scale. So the maximum score is 100, minimum 20.     
      - There are no absolute cutoffs for a good/bad job. So CEva is best used as a comparison tool between options.
      - If a position scores less than 60, which means it **fails** the test. :warning: You should be cautious.
      - Use CEva when you are uncertain about your career choice.
      """
    )
  with st.sidebar.expander("User Manual"):
      st.markdown("""
      - **Step 1**: Follow the instructions of CEva and complete the questionnaire.
      - **Step 2**: The scores will be shown in gauge charts.
      - **Step 3**: You can see the breakdown for 4 areas: Passion, Development, Work-life Balance, 
                  and Practicality. Aside from the total score, think about which area matters the most to you.
      - **Step 4**: If you still feel messy, find someone to talk to. :blossom: 
      - For methodology, please see the following chart:
    """
    )
      st.image("metho.png")
elif lan == "中文":   # 中文版
  C_message_en = st.chat_message("CEva", avatar='avat.png') 
  C_message_en.write("好的。让我们用中文聊天。")
  
  time.sleep(0.5)
  C_message_st = st.chat_message("CEva", avatar='avat.png') 
  start = C_message_st.radio('你准备好开始了吗?', ["否", "是"])
  
  # if yes, start the survey
  if start == "是":
    time.sleep(0.5)
    job_title = C_message_st.text_input("你想要评估哪个职位?") 
    if job_title:
      time.sleep(0.8)
      C_message_pos = st.chat_message("CEva", avatar='avat.png') 
      C_message_pos.write(f"好的，让我们来评估这个职位: **{job_title}**.")
      
      time.sleep(0.8)
      C_message_q = st.chat_message("CEva", avatar='avat.png') 
      C_message_q.write("""请完成下面的问卷。所有的问题都是5分制。""") 
      
      with st.form("CEva_questionnaire"):

        pa1 = st.select_slider(
        '1. 你是否对这个领域感兴趣?',
        options=['一点也不', '有一点点', '中度感兴趣', '非常感兴趣', '极度感兴趣'],
        )

        pa1_sc = CN_to_num(pa1)
        
        pa2 = st.select_slider(
        '2. 你是否愿意在这个领域连续工作五年？',
        options=['一点也不', '有一点点', '中度愿意', '非常愿意', '无条件愿意'],
        )

        pa2_sc = CN_to_num(pa2)

        pa3 = st.select_slider(
        '3. 这个领域创新的机会多不多？你是否愿意参与创新？',
        options=['一点也不', '有一点点', '中等', '很多', '不能更多'],
        )

        pa3_sc = CN_to_num(pa3)

        pa4 = st.select_slider(
        '4. 这个领域是否与你的专业匹配？',
        options=['一点也不', '有一点点', '中等', '非常匹配', '不能更匹配'],
        )

        pa4_sc = CN_to_num(pa4)

        pa5 = st.select_slider(
        '5. 你会不会在这个领域继续深造？',
        options=['一点也不', '可能不会', '没想好', '可能会', '非常有可能'],
        )

        pa5_sc = CN_to_num(pa5)

        d1 = st.select_slider(
        '6. 你是否对这一职业的发展路径有把握？',
        options=['一点也不', '有一点点', '中等', '确定', '不能更确定'],
        )

        d1_sc = CN_to_num(d1)
        
        d2 = st.select_slider(
        '7. 这个职位上有没有很多学习机会？',
        options=['一点也没有', '有一点点', '不确定', '比较多', '超级多'],
        )

        d2_sc = CN_to_num(d2)

        d3 = st.select_slider(
        '8. 五年后，是否容易跳槽？',
        options=['不容易', '有点吃力', '不确定', '容易', '非常容易'],
        )

        d3_sc = CN_to_num(d3)

        d4 = st.select_slider(
        '9. 这个职位上的工作经验是否有价值？',
        options=['一点也不', '有一点点', '中等', '有价值', '非常难得的经历'],
        )

        d4_sc = CN_to_num(d4)

        d5 = st.select_slider(
        '10. 从行业周期的角度考虑，这个行业的风险大不大？',
        options=['非常大', '大', '中等', '小', '非常小'],
        )

        d5_sc = CN_to_num(d5)

        wl1 = st.select_slider(
        '11. 在这个行业工作，生活会不会很轻松？',
        options=['困难', '不轻松', '不确定', '轻松', '非常轻松'],
        )

        wl1_sc = CN_to_num(wl1)
        
        wl2 = st.select_slider(
        '12. 这个行业的工作压力大不大？',
        options=['非常大', '大', '中等', '低', '非常低'],
        )

        wl2_sc = CN_to_num(wl2)

        wl3 = st.select_slider(
        '13. 团队成员是否靠谱？',
        options=['一点也不', '存疑', '不确定', '靠谱', '非常靠谱'],
        )

        wl3_sc = CN_to_num(wl3)

        wl4 = st.select_slider(
        '14. 公司福利好不好？',
        options=['不好', '不坏', '中等', '好', '非常好'],
        )

        wl4_sc = CN_to_num(wl4)

        wl5 = st.select_slider(
        '15. 你能否给团队带来正面影响？',
        options=['一点也不', '有一点点', '不确定', '试试看', '肯定能'],
        )

        wl5_sc = CN_to_num(wl5)

        p1 = st.select_slider(
        '16. 薪酬是否和你的技能匹配？',
        options=['错配', '落差大', '不确定', '差不多', '完美匹配'],
        )

        p1_sc = CN_to_num(p1)
        
        p2 = st.select_slider(
        '17. 公司离你的住所远不远？',
        options=['非常远', '远', '不远不近', '近', '非常近'],
        )

        p2_sc = CN_to_num(p2)

        p3 = st.select_slider(
        '18. 工作环境怎么样？',
        options=['非常差', '比较差', '平均水平', '比较好', '非常好'],
        )

        p3_sc = CN_to_num(p3)

        p4 = st.select_slider(
        '19. 你对公司的组织架构是否满意？',
        options=['一点也不', '一点点', '中度满意', '满意', '非常满意'],
        )

        p4_sc = CN_to_num(p4)

        p5 = st.select_slider(
        '20. 升值空间大不大？奖金多不多？',
        options=['一点也没有', '有一点点', '平均水平', '比较多', '很多'],
        )

        p5_sc = CN_to_num(p5)
        
        submitted = st.form_submit_button("提交")
        if submitted:
            st.write("谢谢你完成问卷。")
        
      if submitted:
        pa_total = pa1_sc + pa2_sc+ pa3_sc + pa4_sc + pa5_sc
        d_total = d1_sc + d2_sc + d3_sc + d4_sc + d5_sc
        wl_total = wl1_sc + wl2_sc + wl3_sc + wl4_sc + wl5_sc
        p_total = p1_sc + p2_sc + p3_sc + p4_sc + p5_sc
        total = pa_total+d_total+wl_total+p_total

        if total >= 80:
           total_eva = f"高于（等于）80分。**这个职位非常适合你。**"
        elif total >= 70:
           total_eva = f"高于（等于）70分。**这是个好机会。**"
        elif total >= 60:
           total_eva = f"高于（等于）60分。**这个机会还行。**"
        else:
           total_eva = f"低于60分。**你可能要好好想想。**"
        
        time.sleep(0.8)
        C_message_re = st.chat_message("CEva", avatar='avat.png') 
        C_message_re.write("""让我们一起来看看结果吧。""") 

        fig = go.Figure(go.Indicator(
         mode = "gauge+number",
         value = total,
         gauge = {'axis':{'range':[20,100]},
                  'bar': {'color': "#A67EB7"}},
         domain = {'x': [0, 1], 'y': [0, 1]},
         title = {'text': "总分"}))

        st.plotly_chart(fig, use_container_width=True)

        col_pa, col_d = st.columns(2)

        with col_pa:
           fig = go.Figure(go.Indicator(
              mode = "gauge+number",
              value = pa_total,
              gauge = {'axis':{'range':[5,25]},
                       'bar': {'color': "#F18F60"}},
              domain = {'x': [0, 1], 'y': [0, 1]},
              title = {'text': "热爱度"}))

           st.plotly_chart(fig, use_container_width=True)

        with col_d:
           fig = go.Figure(go.Indicator(
              mode = "gauge+number",
              value = d_total,
              gauge = {'axis':{'range':[5,25]},
                       'bar': {'color': "#C3D94E"}},
              domain = {'x': [0, 1], 'y': [0, 1]},
              title = {'text': "成长性"}))

           st.plotly_chart(fig, use_container_width=True)

        col_wl, col_p = st.columns(2)

        with col_wl:
           fig = go.Figure(go.Indicator(
              mode = "gauge+number",
              value = wl_total,
              gauge = {'axis':{'range':[5,25]},
                       'bar': {'color': "#6F94CD"}},
              domain = {'x': [0, 1], 'y': [0, 1]},
              title = {'text': "工作与生活之间的平衡度"}))

           st.plotly_chart(fig, use_container_width=True)

        with col_p:
           # st.metric("Practicality", p_total)
           fig = go.Figure(go.Indicator(
              mode = "gauge+number",
              value = p_total,
              gauge = {'axis':{'range':[5,25]},
                       'bar': {'color': "#FFEE6F"}},
              domain = {'x': [0, 1], 'y': [0, 1]},
              title = {'text': "现实度"}))

           st.plotly_chart(fig, use_container_width=True)
        
        C_message_con = st.chat_message("CEva", avatar='avat.png') 
        C_message_con.write(f"{job_title}的评估总分是**{total}**分，"+total_eva)
        C_message_sug = st.chat_message("CEva", avatar='avat.png') 
        C_message_sug.markdown("""我的建议:  
                              :star: 如果一个职位低于60分，你可能要好好想一想。    
                              :star: 职位好坏**没有绝对的分数界限**。   
                              :star: 我的评估最适合用于比较多个职位。  
                              :star: 注意那些得分高的维度，它们是否恰好是你所看重的？   
                              :star: 通常，鱼和熊掌不可兼得。   
                              :star: :rainbow[**追求你所热爱的.**]""") 
        
        C_message_end = st.chat_message("CEva", avatar='avat.png') 
        C_message_end.markdown(""":confetti_ball: 祝你在求职/发展路上一切顺利。:sparkles:  
                               如果你压力太大了，想找个人聊聊，请发邮件至毛毛的邮箱（shiqimeng_1@163.com）。""")
        

      else:
        st.warning("请记得提交你的回答。")
        
  # If no, display message.
  if start == "否":
    st.warning("""准备好后，点击“是”开始评估。""")  
  
  # sidebar configuration
  with st.sidebar.expander("关于希娃"):
      st.markdown("""
      希娃（CEva）是一个专门用于职业评估（**C**areer **EVa**luation）的开源软件。
      """
    )
  with st.sidebar.expander("背景故事"):
      st.markdown("""
      ### 灵感来源
      人生怎么会没有弯路？曾经，有4条路摆在毛毛面前，毛毛搭出希娃，给自己做了一次评估。
                  最后选择了得分最低的那条路，事实证明那条路通向天坑。:weary: 好在，毛毛幸运地爬出了坑。这一次，新机会的希娃得分超过了前面所有机会。  
                  “柳暗花明又一村”，但是最好不要有前面的“峰回路转”。   
                  希娃是一个基于打分的评估模型，希望可以给职业规划带来一个理性视角。:four_leaf_clover:  
      ### 工作机制
      - 希娃的问卷包括20个五分制问题。总分100分，最低分20。    
      - 好坏职业没有绝对的分界线。希娃最适合用于比较多个职位。
      - 如果一个职位低于60分，就说明它**不及格**。:warning: 你要小心！
      - 当你对自己的选择感到不确定时，试试希娃。
      """
    )
  with st.sidebar.expander("说明书"):
      st.markdown("""
      - **第一步**：跟着希娃，完成问卷。
      - **第二步**：结果将显示在仪表图里。
      - **第三步**：你可看到4个维度的独立分数：热爱度，成长性，工作与生活之间的平衡度，现实度。除了看总分，你也要考虑一下自己最在意哪个维度。
      - **第四步**：如果你还是感觉很迷茫，可以找个人聊聊。:blossom: 
      - 方法论见下表（中文版待更新）：
    """
    )
      st.image("metho.png")