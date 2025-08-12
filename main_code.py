from tkinter import *  #used to create GUI
from PIL import ImageTk, Image #loading and proccesing images
from shutil import *#to move folders from one location to another location (foder::Tesseract-OCR => current directory to  C Drive  and bring from C Drive to  current directory)
from atexit import * #used to perform operations when exit button is clicked before exit operation is performed
from os import *#used in our program to get current directory path
from pack.image_to_hw import img_to_hw#image to handwriting module
from pack.image_to_speech import img_to_spech#image to speech module
from pack.image_to_text import img_txt  #image to text module
from pack.text_to_hw import txt_to_hw # text to handwriting module
from pack.text_to_speech import txt_to_speech #text to speech module
from pack.textbox_to_speech import tb_to_speech #text in text box to speech module
import tkinter.filedialog #it is used to perform file operations dynamically
from pywhatkit import *
root=Tk()
#making window non-resizable
root.resizable(0,0)
#adding  image as icon
icon=PhotoImage(file=r'main files\icon.png')
root.iconphoto(True,icon)
#setting title
root.title('VERSATILE CONVERTER')
'''
DONT TOUCH THIS CODE 
#___________________moving tesseract-OCR folder to C Drive_______________________
def cd_to_c():
    move(r'Tesseract-OCR',r'C:\Program Files')
cd_to_c() #calling above function
#________________________moving tesseract-OCR folder from C drive to current directory________________________________________
def c_to_cd():
    move(r'C:\Program Files\Tesseract-OCR',cwdstr)    
register(c_to_cd) #registering  above function to call when exit button is clicked 
DONT TOUCH THIS CODE
'''
root.geometry('1000x600')
#opening a image to set as background in canvas
im=Image.open(r'main files\bg.png')
#resizing image to window size
rim=im.resize((1000,600))
#loading resized image
bg=ImageTk.PhotoImage(rim)
#creating canvas to hold image as background
can=Canvas(root,width=1000,height=600)
can.pack(expand=YES,fill=BOTH)

def win():  
     
   b.destroy()
  
   can.create_image(0,0,anchor=NW,image=bg)#setting background image on canvas
#_________________________________________loading all the image files to set images on widgets in the program___________________________________________________________________________________________   
   img=PhotoImage(file=r'main files\image.png')  
   img2=PhotoImage(file=r'main files\text.png')
   img3=PhotoImage(file=r'main files\back.png')
   img4=PhotoImage(file=r'main files\i_v.png')
   img5=PhotoImage(file=r'main files\i_h.png')
   img6=PhotoImage(file=r'main files\i_t.png')
   img7=PhotoImage(file=r'main files\t_v.png')
   img8=PhotoImage(file=r'main files\t_h.png')
   img9=PhotoImage(file=r'main files\save.png')
   img10=PhotoImage(file=r'main files\select_file.png')
   img11=PhotoImage(file=r'main files\say.png')
   img12=PhotoImage(file=r'main files\info.png')
   img13=PhotoImage(file=r'main files\convert.png')

   def tab1():   #first  page of project contains info,image,text buttons
      def tab2():  #2nd page of project contains all image processing functions
          b1.destroy()
          b2.destroy()
          b18.destroy()
          def tab_hand():  
              l6.config(text='')
              filename = tkinter.filedialog.askopenfilename()# returns name of a file selected
              try:
                img=Image.open(filename)# identifies image and retuns an image object
              except:
                l6.config(text='open a image file')   
              else:    
              
                 b3.destroy()
                 b4.destroy()
                 b5.destroy()
                 b6.destroy()
                
                 e1=Entry(root, width=15, font=('Arial',24),bg='#d2d2d2')
                 e1.t.place(x=340,y=300)
                 l7=Label(root,text='Save as:',bg='#f8f7f7',font=('Arial',14))
                 l7.place(x=340,y=260)
                 
                 def op():
                     img_to_hw(img,e1.get())# calling function that procceses image to handwriting
                     e1.delete(0,END)
                     
                 def dest3():
                     b17.destroy()
                     b10.destroy()
                     e1.destroy()
                     l7.destroy()
                     tab2()
                     
                 b10=Button(root,image=img9,command=op,background='#f8f7f7',borderwidth=0)
                 b10.place(x=380,y=420)
                 b17=Button(root,image=img3,command=dest3,background='#88ffa2',borderwidth=0)
                 b17.place(x=40,y=50)
          def des1():
              b3.destroy()
              b4.destroy()
              b5.destroy()
              b6.destroy()
              l6.destroy()
              tab1()
              
          def i_to_sp():  
               l6.config(text='')
               filename =tkinter.filedialog.askopenfilename()# for selecting image file and return image filename
               try:
                 img=Image.open(filename)#identifies image and retuns an image object
             
               except:
                  l6.config(text='open a image file')   
               else:    
                 img_to_spech(img)  #calling image_to_speech function to extract image and give output as voice 
                 
          def i_T():  
              l6.config(text='')
              filename =tkinter.filedialog.askopenfilename()
              try:
                 img=Image.open(filename)#identifies image and retuns an image object
             
              except:
                   l6.config(text='open a image file')  
              else:    
                  img_txt(img) #calling img_to_txt function to save text file extracted
          l6=Label(root,bg='#f8f7f7',font=('Arial',20),fg='red')  
          l6.place(x=400,y=530)    
          b3=Button(root,image=img3,command=des1,borderwidth=0,bg="#88ffa2")
          b3.place(x=40,y=50)
          b4=Button(root,image=img4,command=i_to_sp,borderwidth=0,bg='#f8f7f7')
          b4.place(x=375,y=200)
          b5=Button(root,image=img5,command=tab_hand,borderwidth=0,bg='#f8f7f7')
          b5.place(x=375,y=300)
          b6=Button(root,image=img6,command=i_T,borderwidth=0,bg='#f8f7f7')
          b6.place(x=375,y=400)
      def tab3():  #__________text processing page contains text to voice and text to handwriting
          def tab_vo():  # page that contains file and textbox options to convert to speech
              b7.destroy()
              b8.destroy()
              b9.destroy()
             
              def dest4():
                  t1.destroy()
                  b11.destroy()
                  b12.destroy()
                  b13.destroy()
                  l4.destroy()
                  l5.destroy()
                  tab3()
              def t_to_sp(): 
                  l5.config(text='')
                  try:
                      txt_to_speech()# this function converts text from text to voice
                  except:
                      l5.config(text='Select Text File Only')  
                      
              def tbtosp(): # convert text in textbox to voice
                  l5.config(text='')
                  tb_to_speech(t1.get(1.0,'end-1c'))# takes text box input and convert to speech
                  t1.delete(1.0,'end')        
              t1=Text(root,width=21,height=5,font=('Arial',16),bg='#d2d2d2')
              t1.place(x=470,y=230)
            
              b11=Button(root,image=img10,command=t_to_sp,background='#f8f7f7',borderwidth=0)
              b11.place(x=160,y=330)
             
              b12=Button(root,image=img11,command=tbtosp,background='#f8f7f7',borderwidth=0)
              b12.place(x=500,y=410)
              
              b13=Button(root,image=img3,command=dest4,background='#88ffa2',borderwidth=0)
              b13.place(x=40,y=50)
              
              l4=Label(root,text='Enter Text:',bg='#f8f7f7',font=('Arial',14))
              l4.place(x=470,y=195)
              
              l5=Label(root,bg='#f8f7f7',font=('Arial',20),fg='red')
              l5.place(x=400,y=530)
              
          def tab_hwr(): # this contains file and text box options to convert the given input as handwriting image file
              
              def tab_fh(): 
                  stri=''  
                  l3.config(text='')
                  filename =tkinter.filedialog.askopenfile(mode='r')
                  try:
                    if filename == '':
                      raise UnicodeDecodeError
                    else: 
                       stri=filename.read()
                       print(stri)
                  except UnicodeDecodeError:
                      l3.config(text='Select Text File') 
                  else:     
                      b14.destroy()
                      t2.destroy()
                      e2.destroy()
                      b15.destroy()
                      b16.destroy()
                      l1.destroy()
                      l2.destroy()
                      l3.destroy()
                      def dest6():
                          e3.destroy()
                          b17.destroy()
                          b18.destroy()
                          l.destroy()
                          tab_hwr()
                      e3=Entry(root,width=15,font=('Arial',24),bg='#d2d2d2')
                      e3.place(x=340,y=300)
                      
                      def fi():
                         txt_to_hw(stri,e3.get())# this function takes text and saving file name as parameters and converts to handwriting
                         e3.delete(0,END)
                       
                      l=Label(root,text='Save as:',bg='#f8f7f7',font=('Arial',14))
                      l.place(x=340,y=260)  
                      b17=Button(root,image=img9,command=fi,borderwidth=0,background='#f8f7f7')
                      b17.place(x=380,y=420)
                      b18=Button(root,image=img3,command=dest6,borderwidth=0,background='#88ffa2')
                      b18.place(x=40,y=50)
              def dest5():
                  b14.destroy()
                  t2.destroy()
                  e2.destroy()
                  b15.destroy()
                  b16.destroy()
                  l1.destroy()
                  l2.destroy()
                  l3.destroy()
                  tab3()
                  
              b7.destroy()
              b8.destroy()
              b9.destroy()
              b14=Button(root,image=img10,command=tab_fh,borderwidth=0,background='#f8f7f7')
              b14.place(x=170,y=300)
              l1=Label(root,text='Enter Text:',bg='#f8f7f7',font=('Arial',14))
              l1.place(x=500,y=140)
              l2=Label(root,text='Save as:',bg='#f8f7f7',font=('Arial',14))
              l2.place(x=500,y=310)
              l3=Label(root,bg="#f8f7f7",font=('Arial',20),fg='red')
              l3.place(x=400,y=530)
              t2=Text(root,width=20,height=4,font=('Arial',16),bg="#d2d2d2")
              t2.place(x=500,y=170)
              e2=Entry(root,width=14, font=('Arial',24),bg='#d2d2d2')
              e2.place(x=500,y=340)
              def tb(): #this function takes input from text box and converts it to handwriting image file
                  l3.config(text='')
                  if t2.get(1.0,'end-1c') == '':
                      l3.config(text='enter text')                      
                  else:    
                     txt_to_hw(t2.get(1.0,'end-1c'),e2.get())
                  e2.delete(0,END)
                  t2.delete('1.0','end')
              b15=Button(root,image=img3,command=dest5,borderwidth=0,background='#88ffa2')
              b15.place(x=40,y=50)
              b16=Button(root,image=img13,command=tb,borderwidth=0,background='#f8f7f7')
              b16.place(x=525,y=425)
              
          b1.destroy()
          b2.destroy()
          b18.destroy()
          
          def des2():
              b7.destroy()
              b8.destroy()
              b9.destroy()
              tab1()
          b7=Button(root,image=img3,command=des2,bg='#88ffa2',borderwidth=0)
          b7.place(x=40,y=50)
          b8=Button(root,image=img7,command=tab_vo,bg='#f8f7f7',borderwidth=0)
          b8.place(x=375,y=250)
          b9=Button(root,image=img8,command=tab_hwr,bg='#f8f7f7',borderwidth=0)
          b9.place(x=375,y=375)
      
      def tab_info():# this contains information about the creators of this project
          b1.destroy()
          b2.destroy()
          b18.destroy()
          def dest():
              b.destroy()
              can.delete(ct)
              can.delete(ct1)
              can.delete(ct2)
              can.delete(ct3)
              can.delete(ct4)
              can.delete(ct5)
              can.delete(ct6)
              can.delete(ct7)
              can.delete(ct8)
              can.delete(ct9)
              can.delete(ct10)
              can.delete(ct11)
             # can.delete(ct12)
              tab1()
          
          b=Button(root,image=img3,command=dest,bg='#88ffa2',borderwidth=0)
          b.place(x=40,y=50)
          ct= can.create_text(270,100,text="Guide-",font=('Arial',17,' bold'),fill='#545454')
          ct1= can.create_text(420,130,text="MISS.B.KavyaSri",font=('Arial',15,' bold'),fill='red')
          ct2= can.create_text(530,150,text="(B.Tech)",font=('Arial',8,'bold '),fill='blue')
          ct3= can.create_text(270,180,text="Group-",font=('Arial',17,'bold'),fill='#545454')
          ct4= can.create_text(370,220,text="V.Ushasree",font=('Arial',15,' bold'),fill='green4')
          ct5= can.create_text(398,256,text="K.Poojitha",font=('Arial',15,' bold'),fill='green4')
          ct6= can.create_text(370,290,text="P.Kiranmai",font=('Arial',15,' bold'),fill='green4')
          ct7= can.create_text(364,324,text="G.Deekshitha",font=('Arial',15,' bold'),fill='green4')
          ct8= can.create_text(373,355,text="K.Nikhil",font=('Arial',15,' bold'),fill='green4')
          ct9= can.create_text(407,388,text="CH.Sampreeth",font=('Arial',15,' bold'),fill='green4')
          ct10= can.create_text(357,420,text="A.Tharun",font=('Arial',15,' bold'),fill='green4')
          ct11= can.create_text(350,455,text="M.Maniratnam",font=('Arial',15,' bold'),fill='green4')
    
      b1=Button(root,image=img,command=tab2,bg='#f8f7f7',borderwidth=0)
      b1.place(x=375,y=200)
      b2=Button(root,image=img2,command=tab3,borderwidth=0,bg='#f8f7f7')
      b2.place(x=375,y=347)
      b18=Button(root,image=img12,borderwidth=0,background='#88ffa2',command=tab_info)
      b18.place(x=40,y=50)
   tab1()
img=PhotoImage(file=r'main files\front.png')
b=Button(root,image=img,borderwidth=0,command=win)
b.pack(pady=30)
bb=can.create_window(500,300,window=b)
       
root.mainloop()# this runs the window continuously