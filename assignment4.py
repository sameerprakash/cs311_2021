import string
import random

nodeCount = [4,3,2]

class Node:
  def __init__(self):
    self.weights = []
    self.children = []
    
    self.node_name = ''
    random_letters = []
    for i in range(3):
      random_letters.append( random.choice(string.ascii_letters) ) # generates random set of 3 characters
    self.node_name = ''.join(random_letters)
   
  def create_children(self, current, node_map):
    if current >= len(node_map):
      return
    
    for i in range( node_map[current] ):
      self.children.append( Node() )
      
    self.children[0].create_children( current + 1, node_map)
    
    for i in range(1, len(self.children) ):
      self.children[i].children = self.children[0].children[:]

  def output(self, current, node_map):
    indent = '   ' * current
    
    if current >= len(node_map):
      print(f"{indent} {self.node_name}")
      return
    
    print(f"{indent} {self.node_name} is connected to: ")
    for i in range( len(self.children) ):
      try:
        print(f"{indent} Weight of {self.weight[i]}")
      except:
        pass
      
      self.children[i].output(current + 1, node_map)
      
    return
  
  def set_random_weights(self, current, node_map):
    if current >= len(node_map):
      return
    self.weights = [0,0] * len(self.children)
    for i in range( len(self.children) ):
      self.weights[i] = random.uniform(0,1)
      self.children[i].set_random_weights(current + 1, node_map)
      
    return

new_node = Node()
new_node.create_children(0, nodeCount)
new_node.output(0, nodeCount)
print("After Weights")
new_node.set_weights(0, nodeCount)
new_node.output(0, nodeCount)
