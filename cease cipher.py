alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
def encrypt(plane_txt,Shift_key):
    cipher_txt=" "
    for ch in plane_txt:
        if ch in alphabet:
            position=alphabet.index(ch)
            position_num=(position+Shift_key)%26
            new_position=alphabet[position_num]
            cipher_txt+=new_position
        else: 
            cipher_txt+=ch
    print(f"encrypted text is:{cipher_txt}\n")
def decrypt(cipher_txt,Shift_key):
    plane_txt=" "
    for ch in cipher_txt:
        if ch in alphabet:
            position=alphabet.index(ch)
            position_num=position-Shift_key
            new_position=alphabet[position_num]
            plane_txt+=new_position
        else:
            plane_txt+=ch
    print(f"decrypted text is:{plane_txt}\n")

wanna_end=False
while not wanna_end:
    what_to_do=input("Type to encrypt 'encrypt' or type to decrypt 'decrypt':\n")
    Text=input("Enter the text:\n")
    Shift=int(input("Enter the number of shift:\n"))
    if what_to_do=="encrypt":
        encrypt(plane_txt=Text,Shift_key=Shift)
    elif what_to_do=="decrypt":
     decrypt(cipher_txt=Text,Shift_key=Shift)
    
    play_again=input("Want to play again say 'yes' if not say 'no':\n ")
    if play_again=="no":
        wanna_end=True
        print("The end\n")