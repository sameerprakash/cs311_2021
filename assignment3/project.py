import argparse
import json
parser = argparse.ArgumentParser()
parser.add_argument('--init', help='called when new game')
parser.add_argument('--iterations', help='number of iterations in game')
parser.add_argument('--last_opponent_move', help='last opponent move')

args = parser.parse_args()
mymoves = open("mymoves.json")
moves = json.load(mymoves)

if(args.init == "true"):
  moves = ["silent"]
elif(args.last_opponent_move == "zero"):
  print(moves.pop())
else:
  moves.append(args.last_opponent_move)
  moves.pop()
json.dump(moves,mymoves)
