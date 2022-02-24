# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

number_of_times_letters_of_true_appeared = 0
number_of_times_letters_of_love_appeared = 0

name1_to_lowercase = name1.lower()
name2_to_lowercase = name2.lower()

name_of_girl_and_boy = {name1_to_lowercase,name2_to_lowercase}
#considering only 2 partners
girl_and_boy = 2

characters_to_compare_in_true = {"t","r","u","e"}
characters_to_compare_in_love = {"l","o","v","e"}

for name in name_of_girl_and_boy:
    for true_characters in characters_to_compare_in_true:

    # here we calculate number of times t r u e letters appeared in girl and boy and add them
        number_of_times_letters_of_true_appeared += name.count(true_characters)

    # here we calculate number of times l o v e letters appeared in girl and boy and add them
    for love_characters in characters_to_compare_in_love:
        number_of_times_letters_of_love_appeared += name.count(love_characters)
    
     
#love score is the sum of number_of_times_letters_of_true_appeared * 10 + number_of_times_letters_of_love_appeared
love_score = number_of_times_letters_of_true_appeared * 10 + number_of_times_letters_of_love_appeared

#categoring according to the love score
if(love_score <10 or love_score>90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")

elif(love_score>40 and love_score<50):
     print(f"Your score is {love_score}, you are alright together.")

else:
    print(f"Your score is {love_score}.")


