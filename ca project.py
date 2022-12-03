import random

name=input("Enter your name: ")
resd = int(input("Enter your Registration number: "))
Q1 = "Sharks are mammals."
A1 = "False"
#False: Sharks are fishes.
Q2 = "Bats are blind."
A2 = "False"
#False: Bats use ultrasonic waves to find their direction, but the are not blind.
Q3 = "An ant can lift 1000 times its body weight."
A3 = "False"
#False: they can lift upto 5000 times their weight.
Q4 = "Mount Everest is the tallest mountain in the world."
A4 = "True"
#True: 8,850 m OR 29,035 ft
Q5 = "There are 4 oceans in the world."
A5 = "True"
#True: Arctic, Indian, Antarctic, Pacific
Q6 = "The 2 longest rivers are Mississippi and Nile."
A6 = "False"
#False: They are Nile and Amazon.
Q7 = "Vatican city is the smallest country in the World."
A7 = "True"
#True: measuring a mere 0.2 square miles, it is almost 120 times smaller than Manhattan in New York.
Q8 = "There are 300 bones in an average adult human."
A8 = "False"
#False: A human baby has 300 bones whereas human adult has 206.
Q9 = "Heart is the largest internal organ in the human body."
A9 = "False"
#False: It is Liver.
Q10 = "India has won the World Cup (50 overs) 2 times."
A10 = "True"
#True: Yes, in 1983 and 2011.
Q11 = "French fries originated from France."
A11 = "False"
#False: Thanks to Germany, we have french fries.
Q12 = "Christopher Columbus found America from India."
A12 = "True"
#True: He came to India in 3 August,1492.
Q13 = "George Washington is the 1st President of America."
A13 = "True"
#True: He was the 1st and John Adams is the 2nd.
Q14 = "The maximum length for a video posted on TikTok is 45 seconds."
A14 = "False"
#False: No, it is 60 seconds.
Q15 = "People who are afraid of crowd are called Cynophobic."
A15 = "False"
#False: They are called Agorophobic. Cynophobia is the fear of dogs.
dict = { Q1 : A1, Q2 : A2, Q3: A3, Q4: A4, Q5 : A5, Q6 : A6,Q7 : A7, Q8 : A8, Q9 :
A9, Q10 : A10, Q11 : A11, Q12: A12, Q13: A13, Q14 : A14, Q15 : A15}
score = 0
print("Given Questions are True/False questions. Answer the following in the form of True/False only.")
n = 1
while n<=5:
    key,val=random.choice(list(dict.items()))
    print(str(key))
    g=str(val)
    a=input("Enter Your Answer (True/False):")
    if a == g:
        print("Congratulations, it's correct")
        score +=1
        n += 1
    elif a != g:
            print ("Sorry, that's incorrect.")
            n += 1
print("End of Quiz")
print("NAME: ",name)
print("Registration number: ",resd)
print("You Obtained:",score,"/5", sep="")
print("Thank you for participating")