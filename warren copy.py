import os
import random
import time

def speak():
    phrases = ["Naomi", "Naomi watch","hydrate", "watch", "evidently", "quote unquote"]
    for x in range(30):
        os.system("say "+(phrases[random.randint(0,len(phrases)-1)]))
        
