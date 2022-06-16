# ###load###

import json

a={"name":"teena","age":19,"gender":"fimale"}
b=open("my dtails.json","r")
c=json.load(a,b)


  

# ###dump###

# import json
# a={"name":"teena","age":19,"gender":"fimale"}
# b=open("my dtails.json","w")
# c=json.dump(a,b,indent=7)


# b=open("dict.json","w")
# c=json.dump(a,b,indent=4)


# a=open("my name.text","w")
# a.write("asdy")
# a.close()


# ##file del hoti ha##

# import os
# os.remove("my name.text")


# ##file del hoti ha##
# import os
# os.remove("/home/chhaya/")


# ##folder delet that method##

# import os
# os.rmdir("teena")































# [0:54 am, 12/06/2022] Megha Ng: import string
# from words import choose_word
# from images import IMAGES

# # End of helper code
# # -----------------------------------

# def is_word_guessed(secret_word, letters_guessed):
#     '''
#     secret_word: ek string word jo ki user ko guess karna hai
#     letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
#     returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
#       False otherwise
#     '''

#     return False

# # Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
# def get_guessed_word(secret_word, letters_guessed):
#     '''
#     secret_word: ek string word jo ki user ko guess kar raha hai
#     letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
#     returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
#     eg agar secret_word = "kindness", letters_guessed = [k,n, s]
#     to hum return karenge "k_n_n_ss"
#     '''

#     index = 0
#     guessed_word = ""
#     while (index < len(secret_word)):
#         if secret_word[index] in letters_guessed:
#             guessed_word += secret_word[index]
#         else:
#             guessed_word += "_"
#         index += 1
    
#     return guessed_word


# def get_available_letters(letters_guessed):
#     '''
#     letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
#     returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
#     eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
#     jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
#     '''
#     import string
#     letters_left = string.ascii_lowercase

#     return letters_left

# def hangman(secret_word):
#     '''
#     secret_word: string, the secret word to guess.

#     Hangman game yeh start karta hai:

#     * Game ki shuruaat mei hi, user ko bata dete hai ki
#       secret_word mei kitne letters hai

#     * Har round mei user se ek letter guess karne ko bolte hai

#     * Har guess ke baad user ko feedback do ki woh guess uss
#       word mei hai ya nahi

#     * Har round ke baar, user ko uska guess kiya hua partial word
#       display karo, aur underscore use kar kar woh letters bhi dikhao
#       jo user ne abhi tak guess nahi kiye hai

#     '''
#     print "Welcome to the game, Hangman!"
#     print "I am thinking of a word that is " + str(len(secret_word)) + " letters long."
#     print ""

#     letters_guessed = []
    
#     available_letters = get_available_letters(letters_guessed)
#     print "Available letters: " + available_letters

#     guess = raw_input("Please guess a letter: ")
#     letter = guess.lower()

#     if letter in secret_word:
#         letters_guessed.append(letter)
#         print "Good guess: " + get_guessed_word(secret_word, letters_guessed)
#         print ""

#         if is_word_guessed(secret_word, letters_guessed) == True:
#             print " * * Congratulations, you won! * * "
#             print ""

#     else:
#         print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
#         letters_guessed.append(letter)
#         print ""
    
# # Load the list of words into the variable wordlist
# # So that it can be accessed from anywhere in the program
# secret_word = choose_word()
# hangman(secret_word)







# a=int(input("enter the num"))
# b=[]
# for i in range(1,a+1):
#     b.append(i)
# print(b)
# k={}
# for i in range(len(b)):
#     if b[i]%2==0:
#         k.update({b[i]:"true"})
#     else:
#         k.update({b[i]:"false"})
# print(k)



# a={"teena":"chouhan","priya":"sharam","manju":"chouhan","riti":"sharma","sonu":"chouhan","monu":"sharma"}
# # for key, value in a.items():
# #     print(key,value)
    
# for key,value in a.items():
#      print(key,a[key])

     
