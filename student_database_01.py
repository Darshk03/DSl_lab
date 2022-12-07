"""
Write a python program to store marks scored in subject Fundamental of
Data Structure by N students in the class. Write functions to compute following:
a)	The average score of class 
b)	Highest score and lowest score of class 
c)	Count of students who were absent for the test
d)	Display mark with highest frequency

"""

def accept_marks(A):   
   n = int(input("Enter the total no. of student : "))
   for i in range(n) :
      while True :
         x = input("Enter the marks scored in FDS for student %d : "%(i+1))
         if(x == "AB"):
            x = -1   # indicates Absent students
            break
         x = int(x)
         if(x >= 0 and x <= 100) :
            break
         else :
            print("Plz enter valid marks out of 100")      
      A.append(x)
   print("Marks accepted & stored successfully");



def display_marks(A) :
   print("\nMarks Scored in FDS")
   for i in range(len(A)):
      if(A[i] == -1) :
         print("\tStudent %d : AB"%(i+1))
      else :
         print("\tStudent %d : %d"%(i+1,A[i]))



def average(A) :
   sum = 0
   for i in range(len(A)) :
      if(A[i] != -1) :
         sum = sum + A[i]
   avg = sum / len(A)
   display_marks(A)
   print("\nAverage score of class is %.2f\n\n"%avg)
   




def highest_and_lowest(A) :
   min = -1
   max = 101
   for i in range(1,len(A)) :
      if(min < A[i]) :
         min = A[i]
         min_ind = i
      if(max > A[i] and A[i] != -1) :
         max = A[i]
         max_ind = i
   display_marks(A)
   print("Highest Mark Score of class is %d scored by student %d"%(min,min_ind+1))
   print("Lowest Mark Score of class is %d scored by student %d"%(max,max_ind+1))
      
   
   
def absent(A) :
   count = 0
   for i in range(len(A)):
      if(A[i] == -1) :
         count += 1
   display_marks(A)
   print("\tAbsent Student Count = %d"%count)
      


def display_mark_with_highest_frequency(A) :
   freq = 0
   for i in range(len(A)) :
      count = 0
      if(A[i] != -1) :
         for j in range(len(A)):
            if(A[i] == A[j]) :
               count += 1
      if(freq < count) :
         Marks = A[i]
         freq = count
   display_marks(A)
   print("\nMarks with highest frequency is %d (%d)"%(Marks,freq))
   

def main():
   FDS_Marks = []
   while True :
      print ("\t1-> Accept fds Marks")
      print ("\t2-> Count of students who were absent for the test ")
      print ("\t3-> Highest score and lowest score of class")
      print ("\t4-> Average score of class")
      print ("\t5-> Display mark with highest frequency")
      print ("\t6-> Exit")
      ch = int(input("Enter your choice : "))
      if (ch == 6):
         print ("End of Program")
         quit()
      elif (ch == 1) :
         accept_marks(FDS_Marks)
         display_marks(FDS_Marks)
      elif (ch == 2) :
         absent(FDS_Marks)  
      elif (ch == 3) :
         highest_and_lowest(FDS_Marks)
      elif (ch == 4) :
         average(FDS_Marks)
      elif (ch == 5) :
         display_mark_with_highest_frequency(FDS_Marks)
      else :
         print ("INVALID CHOICE !")

main()

        
