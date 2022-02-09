import string
program_running = True

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] * 2
key = 0



def encrypt(message):
  length = len(message)
  final_word = ''
  for i in range(length):
    if message[i] == ' ':
      message[i] = ' '
    else:
      sum = message[i]
      if sum in alphabet:
        new_sum = alphabet.index(sum)
        new_letter = alphabet[new_sum + key]
        final_word = final_word + new_letter
  return final_word



def dencrypt(message):
  length = len(message)

  final_word = ''
  for i in range(length):
    if message[i] == ' ':
      message[i] = ' '
    else:
      sum = message[i]
      if sum in alphabet:
        new_sum = alphabet.index(sum)
        new_letter = alphabet[new_sum - key]
        final_word = final_word + new_letter + '-' 
  return final_word


print('***********************************************************')
print('WELCOME TO THE ENCRYPTOR 8576348756348756348756384756348756')
print('***********************************************************')

while program_running:


  question = int(input('Would you like to 1: Set a key? Or 2: encode a message? Or 3: Decode a message? or 4: End the program '))

  if question == 1:
    
    key = int(input('Please enter your key: '))
    
  elif question == 2:
    
    plaintext = list(input('Please enter your message: '))
    ciphertext = encrypt(plaintext)
    print(ciphertext)
    
  elif question == 3:
    
    new_cipher = list(input('Please enter your message: '))
    new_plaintext = dencrypt(new_cipher)
    print(new_plaintext)

  elif question == 4:
    program_running = False

  else:
    print('Please enter either 1,2,3 or 4')

print('Thank you for using my cipher!')
print('©Noah Perrott 2022')
