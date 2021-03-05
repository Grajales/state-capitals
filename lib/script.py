from capitals import states
import random
num_states=len(states)
index=list(range(num_states))
random.shuffle(index)
for i in range(0,num_states):
    picked_state = states[index[i]]["name"]
    capital=input('What is the capital of '+ picked_state + '?')
    if (capital == states[index[i]]["capital"]):
        print("great job!")
    else:
        print("keep working at it, try another one")



# print(states)