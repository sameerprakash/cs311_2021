import argparse
import json
parser = argparse.ArgumentParser()
parser.add_argument('--init', help='called when new game')
parser.add_argument('--iterations', help='number of iterations in game')
parser.add_argument('--last_opponent_move', help='last opponent move')

args = parser.parse_args()
movefile = open("mymoves.json")
moves = json.load(movefile)

if(args.init == "true"):
  moves = ["silent", "silent"]
elif(args.last_opponent_move == "zero"):
  print(moves.pop())
  moves.append("silence")
else:
  moves.append(args.last_opponent_move)
  print(moves.pop())
with open("mymoves.json", "w") as output:
  json.dump(moves, output)
