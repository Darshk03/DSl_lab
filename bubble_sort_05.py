#selection sorting  and bubble sorting 
#AsSignment 5 
# Function for Selection Sort of elements

def Selection_Sort(marks):
    for i in range(len(marks)):

        # Find the minimum element in remain unsorted array
        min_idx = i
        for j in range(i + 1, len(marks)):
            if marks[min_idx] > marks[j]:
                min_idx = j

        #swap the min elem with the first element
        marks[i], marks[min_idx] = marks[min_idx], marks[i]

    print("Marks of students after doing  selection sort on the list : ")
    for i in range(len(marks)):
        print(marks[i])

# Function for Bubble Sort of elements

def Bubble_Sort(marks):
    n = len(marks)
    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(0, n - i - 1):

        
            # Swap if the elem found is great than the next element
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]

    print("Marks of students after performing Bubble Sort on the list :")
    for i in range(len(marks)):
        print(marks[i])


marks=[]
n = int(input("Enter number of students whose marks are to be displayed : "))
print("Enter marks for",n,"students (Press Enter after every students marks): ")
for i in range(0, n):
    ele = int(input())
    marks.append(ele)  # ad

print("The marks of",n,"students are : ")
print(marks)

flag=1;
while flag==1:
    print("\nMENU")
    print("1. Selection Sort of the marks")
    print("2. Bubble Sort of the marks")
    print("3. Exit")
    ch=int(input("\n\nEnter your choice (from 1 to 3) : "))

    if ch==1:
        Selection_Sort(marks)

    elif ch==2:
        Bubble_Sort(marks)
        
    elif ch==3:
        print("\nExit ")
        

    else:
        print("\nEnter a right choice ")
        


