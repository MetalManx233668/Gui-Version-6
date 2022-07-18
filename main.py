from tkinter import *
import random
from PIL import Image, ImageTk

names = []
asked = []
score = 0

questions_answers = { #Questions that will be asked
    1: ["What is the biggest continent in the world?", 'South America', 'Asia','Europe', 'Antartica' ,'Asia',2],#Q1
    2: ["Which state is Niagra falls in?",'California','New York','Los Angeles', 'Florida','New York',2],#Q2
    3: ["Where would you find the leaning tower of pisa?", 'Italy','Spain', 'Greece','Sweden','Italy',1],#Q3
    4: ["In which country is cricket the national sport?",'South Africa','India','Australia','England','England',4],#Q4
    5: ["Which pacific nation has suva as their capital?", 'Tonga','Samoa','Fiji','Niue','Fiji',3],#Q5
    6: ["Which ocean surrounds the north pole?",'Arctic Ocean','Atlantic Ocean','Pacific Ocean','Indian Ocean','Arctic Ocean',1],#Q6
    7: ["What is the netherlands also known as?",'Vend','Nether','Holland','Nent','Benfica',3],#Q7
    8: ["What is the official currency of india?",'Peso','Euro','Pound','Rupee','Rupee',4],#Q8
    9: ["How many large islands make up hawaii?",'5','7','6','8','8',4],#Q9
    10: ["What is the largest US state by area?",'California','Texas','Alaska','Arizona','Alaska',3],#Q10




}
def randomQuestions (): #randomises questions
    global qnum
    qnum = random.randint(1,10) # Number of questions
    if qnum not in asked:
      asked.append(qnum)
    elif qnum in asked:
      randomQuestions()
     

class Mainpage:
  def __init__(self, parent):
    background_color="lightgrey"

    self.var1=IntVar()

    self.user_label=Label(window, text="Please Enter your name Below: ", font=( "Times","18","bold"),bg=background_color)
    self.user_label.place(x=10, y=350)#name heading

    self.entry_box=Entry(window)
    self.entry_box.place(x=10, y=400)#entry box

    self.start_button = Button(window, text="Start quiz", font=( "Helvetica","13","bold"), bg="Light green",command=self.name_collection)
    self.start_button.place(x=10, y=440)#start button

  def name_collection(self):
        name=self.entry_box.get()
        names.append(name)
        self.user_label.destroy()
        self.entry_box.destroy()
        self.start_button.destroy()
        Quiz(window)

class Quiz:

  def __init__(self, parent):
    background_color="lightblue"
 
 
    self.quiz_frame = Frame(parent, bg = "lightblue", padx=40, pady=40)
    self.quiz_frame.place(x=10,y=350)

    randomQuestions()

    self.question_label=Label(window, text = questions_answers[qnum][0], font =( "Tw Cen MT","18","bold"))
    self.question_label.place(x=10,y=300)  

    self.var1=IntVar()

    self.rb1 = Radiobutton(window, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
    self.rb1.place(x=20,y=350)

    self.rb2 = Radiobutton(window, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value=2, variable=self.var1, pady=10)
    self.rb2.place(x=20,y=400)

    self.rb3 = Radiobutton(window, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=3, variable=self.var1, pady=10)
    self.rb3.place(x=20,y=450)

    self.rb4 = Radiobutton(window, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color, value=4, variable=self.var1, pady=10)
    self.rb4.place(x=20,y=500)

    self.confirm_button = Button(window, text="Confrim",bg="white",command=self.test_progress)
    self.confirm_button.place(x=200,y=400)
   
    self.leave = Button(window, text='Leave', font=('Helvetica', '13', 'bold'), bg='red', command=self.end_screen)

    self.leave.place(x=900, y=10)  
   
    self.score_label  = Label(window, text ='score')
    self.score_label.place(x=220,y=450)  
     
     
  def questions_setup(self):
     randomQuestions()
     self.var1.set(0)
     self.question_label.config(text=questions_answers[qnum][0])
     self.rb1.config(text=questions_answers[qnum][1])
     self.rb2.config(text=questions_answers[qnum][2])
     self.rb3.config(text=questions_answers[qnum][3])
     self.rb4.config(text=questions_answers[qnum][4])

 
  def test_progress(self):
      global score
      #score = 0
      scr_label=self.score_label
      choice=self.var1.get()
      if len(asked)>9:
        if choice == questions_answers[qnum][6]:
          score +=1
          scr_label.configure(text=score)
          self.confirm_button.config(text="Confirm")
        else:
          score+=0
          scr_label.configure(text="The correct answer was: "+ questions_answers[qnum][5] )
          self.confirm_button.config(text="confirm")
     
      else:
            if choice==0:
              self.confirm_button.config(text="Try Again, you didn't select an option then submit again" )
              choice=self.var1.get()
            else:
              if choice == questions_answers[qnum][6]:
                score+=1
                scr_label.configure(text=score)
                self.confirm_button.config(text="confirm")
                self.questions_setup()
     
              else:
                  score+=0
                  scr_label.configure(text="The correct answer was: " + questions_answers[qnum][5])
                  self.confirm_button.config(text="Confirmn")
                  self.questions_setup()


  def end_screen(self):
    window.destroy()
    name = names[0]
    open_end_object = end()



class end:


  def __init__(self):
      background_color = 'lightblue'
      global window2
      window2 = Tk()
      window2.title('Exit Box')
      window2.geometry('700x600')
      self.end_frame = Frame(window2, width=700, height=600,bg=background_color)
      self.end_frame.grid(row=1)
      self.end_heading = Label(window2,text='Thanks for trying the quiz ', font=('Tw Cen Mt', 22, 'bold'), bg=background_color)
      self.end_heading.place(x=100, y=50)
      self.end_heading2 = Label(window2,text='Hope you had fun ', font=('Tw Cen Mt', 17, 'bold'), 
 bg=background_color)
      self.end_heading2.place(x=200, y=100)
      self.exit_button = Button(
          window2,
          text='Exit',  
          width=10,  
          bg='lightblue',
          font=('Tw Cen Mt', 12, 'bold'),  
          command=self.close_end,  
          )
      self.exit_button.place(x=260, y=200)
      self.list_label = Label(window2, text='Feel no hesitation to Try Again', font=('Tw Cen Mt', 12, 'bold'), width=40, bg=background_color)
      self.list_label.place(x=100, y=140)
 
 
  def close_end(self):
      self.end_frame.destroy()
      self.end_heading.destroy()
      self.exit_button.destroy()
      self.list_label.destroy()
      window2.destroy()
 
 
 
if __name__ == '__main__':
  window = Tk()
  window.title('12CSC Quiz')
  window.geometry('700x600')
  bg_image = Image.open('start_page.jpg')
  bg_image = bg_image.resize((1000, 600), Image.ANTIALIAS)
  bg_image = ImageTk.PhotoImage(bg_image)
  image_label = Label(window, image=bg_image)
  image_label.place(x=0, y=0, relwidth=1, relheight=1)
  start_object = Mainpage(window)
  window.mainloop()