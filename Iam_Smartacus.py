print("Hello, Welcome to 'I am Smartacus'")

ans = input("Are you ready to play (yes/no) : ")
score = 0
total_question = 5

if ans.lower() == "yes" :
    ans = input("1. What is the capital of Poland? ") 
    if ans.lower() == "warsaw" :
        score += 1
        print("Correct")
    else:
        print("Incorrect: Please google it immediately")
           
        
    ans = input("2. Who did create Python language? ") 
    if ans.lower() == "guido van rossum" :
        score += 1
        print("Correct")
    else:
        print("Incorrect: Really!")
        
        
        
    ans = input("3. When do Chinese people say 'good morning'? ") 
    if ans.lower() == "when they learn english" :
        score += 1
        print("Correct")
    else:
        print("Incorrect: Funny haaa!")
        
                
    ans = input("4. What does IT stand for? ") 
    if ans.lower() == "information technology" :
        score += 1
        print("Correct")
    else:
        print("Incorrect")


    ans = input("5. What country did win the last World Cup in 2018 in Russia? ") 
    if ans.lower() == "france" :
        score += 1
        print("Correct")
    else:
        print("Incorrect")
     
        
    print("Thank you for playing, you got", score, "questions correct.")
    mark = (score/total_question) * 100

    print("Your mark is:", str(mark) + "%")
    print("Good bye and see you soon!")


else: 
    mark = (score/total_question) * 100
    print("We hope next time XD")
    print("Your mark is:", str(mark) + "%")
    print("Good bye and see you soon!")
