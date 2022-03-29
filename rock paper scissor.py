from asyncio.windows_events import PipeServer
from multiprocessing import RLock
import random
from tracemalloc import stop


possible_actions = ["pierre","feuille","scissaux"]
actions_ordinateur = random.choice(possible_actions)
player = input(print("choisir parmis",possible_actions))

if player == actions_ordinateur :
  print("Egalite vous avez joués",player,"et l'ordinateur a joué",actions_ordinateur,)

elif player == ("pierre") :
 if actions_ordinateur == ("scissaux") :
   print("gagné vous avez joué",player,"et l'ordinateur a joué",actions_ordinateur,)
 else :
   print("perdu vous avez joué",player,"et l'ordinateur a joué",actions_ordinateur,)
 
elif player == ("feuille") :
 if actions_ordinateur == ("pierre") :
   print("gagné vous avez joué",player,"et l'ordinateur a joué",actions_ordinateur,)
 else :
   print("perdu vous avez joué",player,"et l'ordinateur a joué",actions_ordinateur,)
 
elif player == ("scissaux") :
 if actions_ordinateur == ("feuille") :
   print("gagné vous avez joué",player,"et l'ordinateur a joué",actions_ordinateur,)
 else :
   print("c'est perdu vous avez joué",player,"et l'ordinateur a joué",actions_ordinateur,)



