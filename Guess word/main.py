import random
word_list=['ark','github','javascript','linkedin','python']
chosen_word=random.choice(word_list)
x=list(chosen_word)

display=[]
for letter in range(len(chosen_word)):
    display+='-'
print(display)

remaining_life=6
life=0
while display!=x:
    guess=input('write any word ').lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
        elif letter!=guess:
            life+=1
            print(f'your life is {life}')
    print(display)
    if life==remaining_life:
        break
print('you won')
