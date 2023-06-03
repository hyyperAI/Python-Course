    #CIPHER PROJECT

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z''/n','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input('do you want to "encode" or "decode":\n')
#asking user to put value
text=input('write the text you want to encode\n')
text=text.lower()
#making this value according to the alphabets list
shift=int(input('how much you want to shift \n'))
# to known how much we have to change our code

def encrypt(put_text=text,put_shift=shift):
    #asking for the function,,, his input= text which is then equal to put_text this is because our function on put_text
            cipher=""
            for letters in text:
    #converting every alphabets of text and assingning its name to letter one by one
                position=alphabets.index(letters)
    # as we assign every letter to letter so, in order to know the index of every letter we use this function
                new_position=position+put_shift
    # this help to assigining the new position and add it to shift in order to change the word place and save it in a variable called as new_position
                cipher+=alphabets[new_position]
    # we add each value one by one in cipher, if we only use = operator this save only one letter one by one don't add it
            print (f'the encrypt code is {cipher}')
    # this just print the given state ment and end it

    #SAME AS ENCRYPT

def decrypt(put_text,put_shift):
            cipher=''
            for letters in put_text:
                position=alphabets.index(letters)
                new_position=position-put_shift
                cipher+=alphabets[new_position]
            print (f'the decode word is {cipher}')
    # this is use to call the functions of different kinds


if direction=='encode':
    encrypt(put_text=text,put_shift=shift)

elif direction=='decode':
    decrypt(put_text=text,put_shift=shift)

