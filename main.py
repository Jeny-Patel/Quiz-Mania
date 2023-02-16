from tkinter import*
window = Tk()

window.title("Jeny's Quiz Mania")

#size of window 
window.geometry('550x500+420+200')
window.resizable(False,False)

#colour of window
window.config(bg="IndianRed3")

#icon of window
#window.iconbitmap("./pictures/guessing.ico")

#if user pressed exit button 
def end_quiz ():
    
    #displays message box prompting user if they want to exit quiz and saves user ans 
    exit_quiz = messagebox.askquestion("Exit Quiz", "Do you want to exit quiz ?")
    
    #if user pressed yes button 
    if exit_quiz == "yes":
        
        #destroys and closes window 
        global window
        window.destroy()
    
    #if user pressed no button 
    else:
        
        #does nothing just to avoid error goes back to same page 
        to_avoid_error=Label(window,text="",font=("Comic Sans Ms",23),fg="gray4",bg="salmon1")
            

#if user pressed submit button 
def show_score():
    
    #display message box prompting user if they want to submit quiz and saves ans 
    show_score = messagebox.askquestion("Submit", "Do you want to submit ?")
    
    #if user pressed yes button 
    if show_score == "yes":
        
        #destroys and closes old window and makes new window 
        global window
        window.destroy()
        window = Tk()
        
        #size of window 
        window.geometry('590x500+400+200')
        window.resizable(False,False)
        
        #colour of window
        window.config(bg="darkolivegreen3")
        
        title = Label(window,text="Results",font=("Comic Sans Ms",23),fg="gray4",bg="salmon1")
        title.place(relx=0.5,rely=0.10,anchor=CENTER)
        
        #saves user mcq answers in user mcq ans list 
        user_mcq_ans = []
        user_mcq_ans.append(opt_Q1_value.get())
        user_mcq_ans.append(opt_Q2_value.get())
        user_mcq_ans.append(opt_Q3_value.get())
        user_mcq_ans.append(opt_Q4_value.get())
        user_mcq_ans.append(opt_Q5_value.get())
        
        global upper_user_t_f_ans
        
        #saves user t/f answers to user t/f ans list 
        user_t_f_ans = []
        user_t_f_ans= user_t_f_ans + upper_user_t_f_ans
        
        #correct mcq and t/f answers 
        correct_human_mcq_ans =[3,3,1,3,2]
        correct_space_mcq_ans =[1,3,2,1,3]
        correct_human_t_f_ans =['T','T','T','F','T']
        correct_space_t_f_ans = ['F','T','T','T','T']
        
        global user_quiz_form
        global quiz_form_value
        
        score = 0
        
        wrong_questions = []
        correct_questions = []
        
        #if user chose mcq form quiz 
        if quiz_form_value == 1:
            
            #if user chose human body quiz 
            if user_quiz_form.get() == 1:
                
                #compares user's all 5 human body mcq quiz answers to correct answers list 
                for num in range(0,5):
                    
                    #if user's answer is equal to correct ans 
                    if user_mcq_ans[num] == correct_human_mcq_ans[num]:
                        
                        #adds one to score 
                        score = score + 1
                        
                        #adds that question number to correct ans list 
                        correct_questions.append(num+1)
                    
                    #if user's answer is not equal to correct ans 
                    else:
                        
                        #adds that question number to wrong ans list
                        wrong_questions.append(num+1)
                        
            
            #if user chose space quiz 
            else:
                
                #compares user's all 5 space mcq quiz answers to correct answers list
                for num in range(0,5):
                    
                    #if user's answer is equal to correct ans 
                    if user_mcq_ans[num] == correct_space_mcq_ans[num]:
                        
                        #adds one to score   
                        score = score + 1
                        
                        #adds that question number to correct ans list
                        correct_questions.append(num+1)
                        
                    #if user's answer is not equal to correct ans        
                    else:
                        
                        #adds that question number to wrong ans list
                        wrong_questions.append(num+1)
            
        #if user chose true / false form quiz 
        else:
            
            #if user chose human body quiz 
            if user_quiz_form.get() == 1:
                
                #compares user's all 5 t/f ans to correct human body quiz ans 
                for num in range(0,5):
                    
                    #if user ans is equal to correct ans 
                    if user_t_f_ans[num] == correct_human_t_f_ans[num]:
                        
                        #adds 1 to score 
                        score = score + 1
                        
                        #adds that question number to correct question list 
                        correct_questions.append(num+1)
                    
                    #if user's ans is not equal to correct ans 
                    else:
                        
                        #adds that question number to wrong question list 
                        wrong_questions.append(num+1)
            
            #if user chose space quiz 
            else:
                
                #compares user's all 5 t/f ans to correct space quiz ans
                for num in range(0,5):
                    
                    #if user ans is equal to correct ans
                    if user_t_f_ans[num] == correct_space_t_f_ans[num]:
                         
                        #adds 1 to score    
                        score = score + 1
                        
                        #adds that question number to correct question list 
                        correct_questions.append(num+1)
                        
                    #if user's ans is not equal to correct ans        
                    else:
                        
                        #adds that question number to wrong question list 
                        wrong_questions.append(num+1)
        
        #if user got more than zero question right 
        if (len(correct_questions) > 0):
            
           #shows which questions are correct 
            for number in range(len(correct_questions)):
               
                show_correct_questions = Label(window,text="Questions #"+str(correct_questions[number])+" was correct", font=("Comic Sans Ms",15),fg="gray4",bg="khaki1")
                show_correct_questions.place(relx=0.04,rely=0.08*number+0.30)
        
        #if user got less than or equal to zero questions correct 
        else:
            
            #displays none questions were correct 
            show_none_correct_questions = Label(window,text="None", font=("Comic Sans Ms",17),fg="gray4",bg="khaki1")
            show_none_correct_questions.place(relx=0.2,rely=0.3)
       
        #if user got more than zero question incorrect
        if (len(wrong_questions) > 0):
       
           #shows which questions are correct
            for number in range(len(wrong_questions)):
               
                show_incorrect_questions = Label(window,text="Questions #"+str(wrong_questions[number])+" was incorrect", font=("Comic Sans Ms",15),fg="gray4",bg="tan1")
                show_incorrect_questions.place(relx=0.5,rely=0.08*number+0.30)   
        
        #if user got less than or equal to zero questions wrong 
        else:
            
            #displays none questions were incorrect 
            show_none_incorrect_questions = Label(window,text="None", font=("Comic Sans Ms",17),fg="gray4",bg="tan1")
            show_none_incorrect_questions.place(relx=0.68,rely=0.3)
            
        title_correct_questions = Label(window,text="Correct Questions", font=("Comic Sans Ms",15),fg="gray4",bg="peachpuff")
        title_correct_questions.place(relx=0.093,rely=0.20)
        
        title_incorrect_questions = Label(window,text="Incorrect Questions", font=("Comic Sans Ms",15),fg="gray4",bg="peachpuff")
        title_incorrect_questions.place(relx=0.55,rely=0.20)
        
        #displays user's score out of 5
        show_user_result = Label(window,text="Your score is "+str(score)+" out of 5", font=("Comic Sans Ms",22),fg="red",bg="AntiqueWhite1",width=20,height=1)
        show_user_result.place(relx=0.5,rely=0.80,anchor=CENTER)
        
        #displays exit button 
        end = Button(window, text="Exit",font=("Comic Sans Ms",14),fg="ivory2",bg="red3",command=end_quiz,width=10)
        end.place(relx=0.5,rely=0.93,anchor=CENTER)
    
    #if user pressed no button (submit quiz message box)
    else:
        
        #does not show score
        #does nothing just to avoid error 
        to_avoid_error=Label(window,text="",font=("Comic Sans Ms",23),fg="gray4",bg="salmon1")

#if user pressed mcq button displays mcq questions and options 
def show_MCQ_page():
    
    #colour of window
    window.config(bg="navajo white2")
    
    #size of window 
    window.geometry('700x590+360+160')
    
    
    #destroys mcq, true/false button and title from screen 
    form.destroy()
    mcq_form.destroy()
    t_or_f_form.destroy()
    
    global quiz_form_value
    
    #quiz form value is equal to 1 if user chose mcq form quiz 
    quiz_form_value = 1
    
    global user_quiz_form
    
    #saves which quiz user chose human body or space 
    quiz_form = user_quiz_form.get()
    
    title = Label(window,text="Choose The Correct Option",font=("Comic Sans Ms",23),fg="gray4",bg="palevioletred1")
    title.place(relx=0.5,rely=0.10,anchor=CENTER)
    
    #positions mcq questions options 
    opt1_Q1.place(relx=0.03,rely = 0.29)
    opt2_Q1.place(relx=0.20,rely = 0.29)
    opt3_Q1.place(relx=0.37,rely = 0.29)
    opt1_Q2.place(relx=0.03,rely = 0.43)
    opt2_Q2.place(relx=0.20,rely = 0.43)
    opt3_Q2.place(relx=0.37,rely = 0.43)
    opt1_Q3.place(relx=0.03,rely = 0.57)
    opt2_Q3.place(relx=0.20,rely = 0.57)
    opt3_Q3.place(relx=0.37,rely = 0.57)
    opt1_Q4.place(relx=0.03,rely = 0.71)
    opt2_Q4.place(relx=0.20,rely = 0.71)
    opt3_Q4.place(relx=0.37,rely = 0.71)
    opt1_Q5.place(relx=0.03,rely = 0.85)
    opt2_Q5.place(relx=0.20,rely = 0.85)
    opt3_Q5.place(relx=0.37,rely = 0.85)
    
    #if user chose human body quiz 
    if quiz_form == 1:
        
        global human_mcq_qus
        
        qus_num = 0
        
        #displays all the 5 mcq questions 
        for num in range(1,6,1):
            
            mcq_question = Label(window, text=str(num)+". "+ human_mcq_qus[qus_num],font=("Comic Sans Ms",17),fg="gray4",bg="springgreen3")
            mcq_question.place(relx=0.02,rely=0.08+num*0.14)
            qus_num = qus_num + 1
        
        
        #displays human body mcq options 
        opt1_Q1.config(text="+O")
        opt2_Q1.config(text="+AB")
        opt3_Q1.config(text="-AB")
        opt1_Q2.config(text="30 %")
        opt2_Q2.config(text="60 %")
        opt3_Q2.config(text="70 %")
        opt1_Q3.config(text="28,800")
        opt2_Q3.config(text="30,000")
        opt3_Q3.config(text="25,000")
        opt1_Q4.config(text="3 liters")
        opt2_Q4.config(text="2 liters")
        opt3_Q4.config(text="1 liter")
        opt1_Q5.config(text="Heart")
        opt2_Q5.config(text="Tongue")
        opt3_Q5.config(text="Ear")
    
    #if user chose space quiz 
    else:
        
        global space_mcq_question
        
        qus_num = 0
        
        #displays all 5 space quiz questions 
        for num in range(1,6,1):
            
            question = Label(window, text=str(num)+". "+ space_mcq_qus[qus_num],font=("Comic Sans Ms",17),fg="gray4",bg="springgreen3")
            question.place(relx=0.02,rely=0.08+num*0.14)
            qus_num = qus_num + 1
        
        #displays space quiz options 
        opt1_Q1.config(text="Twelve")
        opt2_Q1.config(text="Five")
        opt3_Q1.config(text="Eight")
        opt1_Q2.config(text="Mars")
        opt2_Q2.config(text="Venus")
        opt3_Q2.config(text="Mercury")
        opt1_Q3.config(text="Moon")
        opt2_Q3.config(text="Sun")
        opt3_Q3.config(text="Jupiter")
        opt1_Q4.config(text="4.6 Billion",width=7)
        opt2_Q4.config(text="1.3 Billion",width=7)
        opt3_Q4.config(text="3 Billion",width=7)
        opt1_Q5.config(text="Saturn")
        opt2_Q5.config(text="Mars")
        opt3_Q5.config(text="Jupiter")
    
    #displays submit button
    submit = Button(window, text="Submit",font=("Comic Sans Ms",14),fg="ivory2",bg="red3",command=show_score,width=10)
    submit.place(relx=0.87,rely=0.93,anchor=CENTER)
    
    #displays exit button 
    end = Button(window, text="Exit",font=("Comic Sans Ms",14),fg="ivory2",bg="red3",command=end_quiz,width=10)
    end.place(relx=0.68,rely=0.93,anchor=CENTER)

#checks if user entered t/f for true or false ans if user presses submit button 
def find_entry_error():
    
    global entry_box
    
    #user's ans list 
    user_answers = []
    

    entry_num = 0
    
    #saves all 5 user t/f answers into user answers list 
    for i in range(1,6):
        
        user_answers.append(entry_box[entry_num].get())
        entry_num = entry_num + 1
    
    global upper_user_t_f_ans
    
    #converts user's all 5 t/f ans into upper case and saves it in new upper case list 
    for ans in range(0,5):
        upper_user_t_f_ans.append(user_answers[ans].upper())
    
    error_at = 0
    
    #list of invalid input
    invalid_input_at = []
    
    #list of quesitons where user entered invalid input 
    show_invalid_input_at = []
    
    #checks if user entered t/f for all 5 t/f question ans 
    for ans_num in range(0,5):
        
        #if user didn't enter t/f 
        if upper_user_t_f_ans[ans_num] != "T" and upper_user_t_f_ans[ans_num] != "F":
            
            #adds question number for which user entered invalid ans to list
            invalid_input_at.append(ans_num)
            show_invalid_input_at.append(ans_num+1)
        
        #if user entered t/f 
        else:
            
            #does nothing avoids error 
            text = Label(window,text="")
    
    #if user entered any other input for t/f answers except for t/f 
    if len(invalid_input_at)>0:
        
        #displays message box with error message box to user and prompts user to enter t/f only 
        messagebox.showerror("Invalid Input", "Please enter only T or F for Question"+str(show_invalid_input_at))
        
        #clears all the invalid user answers from t/f answer entry box 
        for num in range(len(invalid_input_at)):
            
            entry_box[invalid_input_at[num]].delete(0, END)
        
        #clears user answers list 
        user_answers.clear()
        upper_user_t_f_ans.clear()
        
        #sets cursor back to 1 entry box where user didn't enter t/f 
        entry_box[invalid_input_at[0]].focus()
    
    #if user entered t/f for t/f answers 
    else:
        
        #calls show score function 
        show_score()
    

#if user chose true or false form quiz displays true or false quesitons 
def show_t_f_page():
    
    global user_quiz_form
    
    #saves which quiz user chose 
    quiz_form = user_quiz_form.get()
    
    global quiz_form_value
    
    #quiz form value is equal to 2 as user chose true or false quiz form 
    quiz_form_value = 2
    
    #colour of window 
    window.config(bg="rosybrown")
    
    #size of window 
    window.geometry('700x590+360+160')
    
    #destroys mcq button, true/false button and title from screen 
    form.destroy()
    mcq_form.destroy()
    t_or_f_form.destroy()
    
    #prompts user to enter true or false 
    title = Label(window,text="Enter T for True or F for False",font=("Comic Sans Ms",23),fg="gray4",bg="salmon")
    title.place(relx=0.5,rely=0.10,anchor=CENTER)
    
    #if user chose human body quiz 
    if quiz_form == 1:
        
        global human_t_f_qus
        
        qus_num = 0
        
        #displays all 5 human body true or false quiz questions 
        for num in range(1,6,1):
            
            t_f_question = Label(window, text=str(num)+". "+ human_t_f_qus[qus_num],font=("Comic Sans Ms",14),fg="gray4",bg="darkseagreen2")
            t_f_question.place(relx=0.02,rely=0.11+num*0.13)
            qus_num = qus_num + 1
        
        
    #if user chose space quiz     
    else:
        
        global space_t_f_qus
        
        qus_num = 0
        
        #displays all the 5 space quiz true or false questions 
        for num in range(1,6,1):
            
            t_f_question = Label(window, text=str(num)+". "+ space_t_f_qus[qus_num],font=("Comic Sans Ms",17),fg="gray4",bg="darkseagreen2")
            t_f_question.place(relx=0.02,rely=0.11+num*0.13)
            qus_num = qus_num + 1
    
    entry_box_num = 0
    global entry_box
    
    #displays all 5 true or false answers entry boxes 
    for number in range(1,6):
        
        entry_box[entry_box_num] = Entry(window,fg="gray6",font=("Merriweather",17),bg="ivory1",width=6)
        entry_box[entry_box_num].place(relx=0.85,rely=0.11+number*0.13)
        entry_box_num = entry_box_num + 1
    
    #displays submit button #if user presses submit button calls find entry error function that checks user's t/f ans 
    submit = Button(window, text="Submit",font=("Comic Sans Ms",14),fg="ivory2",bg="red3",command=find_entry_error,width=10)
    submit.place(relx=0.63,rely=0.92,anchor=CENTER)
    
    #displays exit button 
    end = Button(window, text="Exit",font=("Comic Sans Ms",14),fg="ivory2",bg="red3",command=end_quiz,width=10)
    end.place(relx=0.37,rely=0.92,anchor=CENTER)
    
#prompts user if they want their quiz in mcq form or true/false form     
def page2():
    
    #colour of window
    window.config(bg="salmon")
    
    #destroys human body and space quiz buttons and welcome title 
    body_quiz.destroy()
    space_quiz.destroy()
    welcome.destroy()
    choose_quiz.destroy()
    
    #prompts user what quiz form they want to choose 
    form.config(text="What form you want your Quiz to be in ?",bg="mediumpurple1")
    
    #displays mcq quiz form button 
    mcq_form.config(text="Multiple Choice Question")
    mcq_form.place(relx=0.5,rely=0.4,anchor=CENTER)
    
    #displays true or false form button 
    t_or_f_form.config(text="True / False")
    t_or_f_form.place(relx=0.5,rely=0.53,anchor=CENTER)
    
#creat prompting text,empty for now, for user asking which form they want their quiz to be 
form = Label(window,text="",font=("Comic Sans Ms",19),fg="gray4",bg="IndianRed3")
form.place(relx=0.5,rely=0.18,anchor=CENTER)

#creats mcq button 
mcq_form = Button(window, text="",font=("Comic Sans Ms",14),fg="gray4",bg="burlywood1",padx=-200,command=show_MCQ_page)

#creats true or false button
t_or_f_form = Button(window, text="",font=("Comic Sans Ms",14),fg="gray4",bg="burlywood1",padx=-200,command=show_t_f_page)

quiz_form_value = 0

welcome = Label(window,text="Welcome to Jeny's Quiz Mania",font=("Comic Sans Ms",22),fg="gray4",bg="cornsilk2")
welcome.place(relx=0.5,rely=0.1,anchor=CENTER)

choose_quiz = Label(window,text="Choose your Quiz",font=("Comic Sans Ms",18),fg="gray4",bg="navajowhite")
choose_quiz.place(relx=0.5,rely=0.22,anchor=CENTER)

user_quiz_form = IntVar()

#creats and positions human body quiz button
body_quiz = Radiobutton(window, text="Human Body Quiz",font=("Comic Sans Ms",14),fg="gray4",bg="lemon chiffon", value=1, variable=user_quiz_form, padx=-200,command=page2)
body_quiz.place(relx=0.5,rely=0.4,anchor=CENTER)

#creats and positions space quiz button
space_quiz = Radiobutton(window, text="Space Quiz",font=("Comic Sans Ms",14),fg="gray4",bg="lemon chiffon", value=2, variable=user_quiz_form, padx=-200,command=page2)
space_quiz.place(relx=0.5,rely=0.53,anchor=CENTER)

#list of human body mcq function
human_mcq_qus = ["Which is the rarest blood type ? ","What percentage of our body is water ?","On average, how many times you blink in a day ?","How much saliva does your mouth make each day ?","What is the most flexible muscle in human body ?"]

#list of space quiz mcq questions 
space_mcq_qus = ['Jupiters 1 year is earths how many years ?','Which is the smallest planet within our solar system ?','Which of the following is considered Star ?', 'Sun is how many years old ?','Which planet has highest number of moons ?']

#list of human body quiz true or false questions 
human_t_f_qus = ["Giraffe and Human have same number of neck bone","When you blush, the lining of your stomach also turns red","Human body’s temperature rises slightly during digestion","Human can lick their elbow","12 % of human population dream in black and white"]

#list of space quiz true or false questions 
space_t_f_qus = ["People have walked on the planet Mars","The Moon is an example of a natural satellite","Some people live in outer space","Jupiter is the oldest planet","Colour of the Sun is white"]

entry_box = ['entry_1','entry_2','entry_3','entry_4','entry_5']

#creats mcq option buttons and assing them their values

opt_Q1_value = IntVar()

opt1_Q1= Radiobutton(window,text="",font=("Comic Sans Ms",12),fg="gray4",bg="coral1",value=1, anchor= CENTER,width=6,variable=opt_Q1_value)
opt2_Q1= Radiobutton(window,text="",font=("Comic Sans Ms",12),fg="gray4",bg="coral1",value=2, anchor= CENTER,width=6,variable=opt_Q1_value)
opt3_Q1= Radiobutton(window,text="",font=("Comic Sans Ms",12),fg="gray4",bg="coral1",value=3, anchor= CENTER,width=6,variable=opt_Q1_value)

opt_Q2_value = IntVar()

opt1_Q2= Radiobutton(window,text="",font=("Comic Sans Ms",12),fg="gray4",bg="coral1",value=1, anchor= CENTER,width=6,variable=opt_Q2_value)
opt2_Q2= Radiobutton(window,text="",font=("Comic Sans Ms",12),fg="gray4",bg="coral1",value=2, anchor= CENTER,width=6,variable=opt_Q2_value)
opt3_Q2= Radiobutton(window,text="",font=("Comic Sans Ms",12),fg="gray4",bg="coral1",value=3, anchor= CENTER,width=6,variable=opt_Q2_value)
    
opt_Q3_value = IntVar()

opt1_Q3= Radiobutton(window,text="",font=("Comic Sans Ms",12),fg="gray4",bg="coral1",value=1, anchor= CENTER,width=6,variable=opt_Q3_value)
opt2_Q3= Radiobutton(window,text="",font=("Comic Sans Ms",12),fg="gray4",bg="coral1",value=2, anchor= CENTER,width=6,variable=opt_Q3_value)
opt3_Q3= Radiobutton(window,text="",font=("Comic Sans Ms",12),fg="gray4",bg="coral1",value=3, anchor= CENTER,width=6,variable=opt_Q3_value)

opt_Q4_value = IntVar()

opt1_Q4= Radiobutton(window,text="",font=("Comic Sans Ms",12),fg="gray4",bg="coral1",value=1, anchor= CENTER,width=6,variable=opt_Q4_value)
opt2_Q4= Radiobutton(window,text="",font=("Comic Sans Ms",12),fg="gray4",bg="coral1",value=2, anchor= CENTER,width=6,variable=opt_Q4_value)
opt3_Q4= Radiobutton(window,text="",font=("Comic Sans Ms",12),fg="gray4",bg="coral1",value=3, anchor= CENTER,width=6,variable=opt_Q4_value)

opt_Q5_value = IntVar()

opt1_Q5= Radiobutton(window,text="",font=("Comic Sans Ms",12),fg="gray4",bg="coral1",value=1, anchor= CENTER,width=6,variable=opt_Q5_value)
opt2_Q5= Radiobutton(window,text="",font=("Comic Sans Ms",12),fg="gray4",bg="coral1",value=2, anchor= CENTER,width=6,variable=opt_Q5_value)
opt3_Q5= Radiobutton(window,text="",font=("Comic Sans Ms",12),fg="gray4",bg="coral1",value=3, anchor= CENTER,width=6,variable=opt_Q5_value)

upper_user_t_f_ans = []

window.mainloop()

