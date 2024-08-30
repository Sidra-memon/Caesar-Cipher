from Art import logo
print(logo)
alphabet = "abcdefghijklmnopqrstuvwxyz"
End_game= True
while End_game is True:
  user_input = input("Enter a word Encrypt/ Decrpyt: Type Enc or Dec:")
  word = input("Enter a word:").lower()
  key = int(input("Enter a shift key: "))
  new_word = ""
  if user_input=="Dec":
    key *=-1
  def cipher(new_word, key):
    """This fuction encrypt/ dencrypts a word using a shift key"""
    if user_input=="Dec":
      key *=-1
  for letter in word:
    if letter in alphabet:
      letter_index=alphabet.find(letter)
      new_index=(letter_index+key)%26
      new_word+=alphabet[new_index]
    else:
      new_word+=letter
  print(new_word)
  try_again=input("Do you want to try again? Type Y or N: ")
  if try_again=="Y":
    cipher(new_word, key)  
  else:
    End_game=False
    print("Goodbye")