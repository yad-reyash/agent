import heapq

class node:
  def __init__(self, state ,parent=None, move = None , g=0,h=0):
    self.state=state
    slef.parent=parent
    slef.move=move
    slef.g=g
    slef.h=h
    slef.f=g+h
  def __lt__(self, other):
    return slef.f<other.f
  class PuzzleSolver:
    def __inti__(self,start_state,goal_state):
      self.start_state=start_state
      slef.goal_state=goal_state
      self.grid_size=3
    def get_distance(self,state):
      distance =0
      for i, tile in enumerate(state):
        if tile==0:
          continue
        current_row,current_col=i // self.grid_size , i% self.grid_size

        goal_index = self.goal_state.index(tile)
        goal_row,goal_col =goal_index // self.grid_size, goal_index % self.grid_size

        distance += abs(current_row- goal_row) + abs(current_col goal_col)
      return distance
   def get_neighbours(self_node):
     neghbours =[]
     state = list (node.state)
     zero_index =state.index(0)

     row ,col =zero_index // self.grid_size, zero_index % slef.grid_size
     moves=[(-1,0,"UP"), (1, 0, "DOWN"), (0, -1, "LEFT"), (0, 1, "RIGHT")]

     for dr, dc , move_name in moves:
       new_row,new_col =row+dr,col+dc
       new_state = state[:]
       new_state[zero_index],new_state[new_index] =new_state[inew_ndex],new_state[zero_index]
    return neghbours


   def slove(self):
     open_list =[]
     close_set= set()




  


       
     
     
          
