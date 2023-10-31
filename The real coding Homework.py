import time
lives = 3
while lives >0:

    def introduction():
        print("Welcome to the CyberSafe Adventure!")
        time.sleep(1)
        print("You find yourself in a virtual world filled with dangers and opportunities.")
        time.sleep(1)
        print("Your mission is to navigate this digital realm safely, making the right choices to protect your online identity and privacy.")
        time.sleep(1)
        print("Are you ready to begin?\n")

    def game_over(reason):
        print("\n" + reason)
        print("Game Over! Do you want to play again? (yes/no)")
        choice = input()
        if choice.lower() == "yes":
            start_game()
        else:
            print("Thank you for playing CyberSafe Adventure!")


        print("Chapter 1: The Virtual World Awaits")
        time.sleep(1)
        print("You're about to create your online presence. What will you do?\n")
        time.sleep(1)
        print("1. Use your full name as your username.")
        time.sleep(1)
        print("2. Create a unique username that doesn't reveal your real identity.")
        choice = input()
        if choice == "1":
            game_over("Using your full name as your username was not a safe choice. You've revealed your real identity.")
            lives = lives -1
        elif choice == "2":
            print("Great choice! Your online identity is secure.")
            
        else:
            game_over("Invalid choice. Please select 1 or 2.")

    
        print("\nChapter 2: Choosing Friends")
        time.sleep(1)
        print("You've received a friend request from someone you don't know. What will you do?\n")
        time.sleep(1)
        print("1. Accept the request. More friends are always good, right?")
        time.sleep(1)
        print("2. Decline the request. You don't want to connect with strangers.")
        choice = input()
        if choice == "1":
            game_over("Accepting requests from strangers is not safe. You've made a risky choice.")
            lives = lives -1
        elif choice == "2":
            print("Smart move! You've protected your privacy.")
            
        else:
            game_over("Invalid choice. Please select 1 or 2.")

    
        print("\nChapter 3: Password Predicament")
        time.sleep(1)
        print("Time that you set up your password what will it be?\n ")
        time.sleep(1)
        print("1. Choose a strong Password like 65lLM<v7HI~£ which can be hard to remember. ")
        time.sleep(1)
        print("2. Use a soft password like FroggyBane which is easy to remeember. ")
        choice = input()
        if choice == "1":
            print("Very good you wont be hacked so easily and you will be able to feel secure. ")
            
        elif choice == "2":
            game_over("Thats not good the password is to easy to get into. ")
            lives = lives -1
        else:
            game_over("Thats not good please redo that and choose a number between 1 and 2! ")

    
        print("\nChapter 4: Social Media Share ")
        time.sleep(1)
        print("Yor really excited about your achievement and want to share it on soical media, what will you includ ein this share?\n")
        time.sleep(1)
        print("1. Share your achievement and include your personal information? ")
        time.sleep(1)
        print("2. Share your achievement and do not include any personal information? ")
        choice = input()
        if choice == "1":
            game_over("Thats not good you will get stranger stealing your information. ")
            lives = lives -1
        elif choice == "2":
            print("Very good man I am proud that you're learning! ")
            
        else:
            game_over("You need to choose an option please and thank you (1 or 2) ")

    
        print("\nChapter 5: Online Bullying ")
        time.sleep(1)
        print("You was surfing the web and then you saw that there is a comment that is bulling someone what, what will you do?\n ")
        time.sleep(1)
        print("1. Get yourself involved and start bullying him/her with the stranger? ")
        time.sleep(1)
        print("2. Get yourself involved and spam report the person thats bullying and offer support to the person being bullied? ")
        choice = input()
        if choice == "1":
            game_over("Nah cause thats not nice, what kind of human being are you? ")
            lives = lives -1
        elif choice == "2":
            print("Now thats a very nice samarathon and you might even get a gold star now good job! ")
            
        else:
            game_over("I mean by this point you should know to choose 1 or 2! ")

   
        print("\nChapter 6: Pishing Email ")
        time.sleep(1)
        print("One day you recieve an email claiming that you won a prize, You think it look suspicious though, What will you do?\n")
        time.sleep(1)
        print("1. Click and use the link and provide them with you information? ")
        time.sleep(1)
        print("2. Dispose of the email and spam repoort it? ")
        choice = input()
        if choice == "1":
            game_over("Thats not good you got you details out there and they spent all your life savings! ")
            lives = lives -1
        elif choice == "2":
            print("Good choice you saved your money for another day! ")
            chapter7()
        else:
            game_over("Choose the options 1 or 2! ")
        
    
        print("\nChapter 7: Gaming Dilemma")
        time.sleep(1)
        print("Your trying to enjoy your sunday and play your favourtite game but there is someone trying to pressure you in sharing your information, What will you do?\n ")
        time.sleep(1)
        print("1. Share the information because of presure? ")
        time.sleep(1)
        print("2. Refuse to share anything and block them? ")
        choice = input()
        if choice == "1":
            game_over("Thats gonna get your information stolen and cause you to potentially lose your money! ")
            lives = lives -1
        elif choice == "2":
            print("Nice your learning leave him and tell him off! ")
            
        else: 
            game_over("Choose the appropriate number 1 or 2! ")

    
        print("\nChapter 8: Safe Surfing ")
        time.sleep(1)
        print("You are looking for a new game to download on your mobile app, Where will you download it from?\n")
        time.sleep(1)
        print("1. Download it from a trusted website? ")
        time.sleep(1)
        print("2. Download it from a random website? ")
        choice = input()
        if choice == "1":
            print("Good job, do not fall for fake websites! ")
           
        elif choice == "2":
            game_over("Nope thats how you get a virus. ")
            lives = lives -1
        else:
            game_over("Choose a number BRO 1 OR 2 ")
        
    
        print("\nChapter 9: Final Chapter ")
        time.sleep(1)
        print("This is the final Challenge and all you needed to do is complete the cyber space safety adventure game! ")
        time.sleep(1)
        print("If you made it here good job and i am proud of you and remember always stay safe when your browsing the web! ")
        

    def start_game():
        introduction()
        chapter1()

    if __name__ == "__main__":
        start_game()