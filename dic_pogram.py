from turtle import goto
from click import option


dic = {
    "harry" : "is a coder",
    "fan" : "pankha"
}
print("\t***Hey, This is a dictionary***\t")
print("\t***for see the meaning of any word. type 0***\t")
print("\t***for add words in dictionary. type 1***\t")
print("\t***for remove the word and meaning in dictionary. type 2***\t")

choose = int(input("\nchoose the one option : "))

if choose == 0 :
    print("\t***you can see the meaning of these words***\t")
    print(list(dic))
    choice = input("Enter the word you want to see the meaning : ")
    mean = dic[choice]
    print(mean)
    pass

elif choose == 1 :
    
    print("\t***you can add words in dictionary***\t")
    word = input("Enter the word : ")
    meaning = input("Enter the meaning of word : ")
    print(f"your word are {word} and your meaning of word are {meaning}.")
    print("\t***for yes then type (0) and for no then type (1)")
    option = int(input("Enter your choice : "))
    if option == 0 :
        dic[word] = meaning
        print(dic)
        pass

    elif option == 1 :
       
        pass

    else :
        print("choose correct option")
        
        pass

elif choose == 2 :
    print("you choose the remove the word")
    print(dic)
    remove = input("Enter the you want to remove : ")
    del dic[remove]
    print(dic)


else :
    print("Please enter valid choice")
   
    pass

