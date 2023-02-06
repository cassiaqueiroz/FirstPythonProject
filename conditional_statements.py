# Input Type Number
print("Write your age and press Enter:")
age = int(input())
if age > 75:
    print("--Priority Group For Vaccination--")
    print("Schedule your drive-thru.")
else:
    print("Wait your turn for the vaccine.")

# Input Type String
print("\nNow write a text containing at least 10 words with no punctuation and press Enter:")
text = input()
split_by_words = text.split(" ")
number_of_characters = len(split_by_words)
print("Number of words in the text:", number_of_characters)
if number_of_characters < 10:
    print("You typed less than 10 words.")
else:
    print("The last 3 words typed were:", split_by_words[-3:])

