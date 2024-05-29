import pandas

#Create a dict in this format {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(data)
new_dict = {row.letter:row.code for (index,row) in df.iterrows()}


#create a list of the photetic code words from a word form an input ("Enter a word:  ")
def generate_phonetic():
    word = input("Enter a word: ").upper()
    new_list= [char for char in word]

    try:
        result = [new_dict[letter] for letter in new_list]
    except:
        print("Sorry, only letters in the alphabet, please")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()