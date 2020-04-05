from random import randint

MAX_X = 20
MAX_Y = 20
PARTICLE_MASS = 10**0
WALL_MASS = 10**10
DOOR_MASS = 10**-10

def next(b, x0, x1):
    particle = b[x0][x1]
    if particle is None:
      return
    target = b[x0+int(particle.v0)][x1+int(particle.v1)]
    if target is not None:       
      if particle.v0 != 0:
         particle.v0, target.v0 = collision(particle.m, particle.v0, target.m, target.v0)
      if particle.v1 != 0:
         particle.v1, target.v1 = collision(particle.m, particle.v1, target.m, target.v1)
    b[x0][x1] = None
    b[x0 + int(particle.v0)][x1 + int(particle.v1)] = particle
    
def collision(m_0, v_0, m_1, v_1):
  v_0_ = (v_0*(m_0-m_1)+2*m_1*v_1)/(m_0+m_1)
  v_1_ = (v_1*(m_1-m_0)+2*m_0*v_0)/(m_0+m_1)
  return v_0_, v_1_

class particle(object):
  def __init__(this, m, v0, v1):
    this.m = m
    this.v0 = v0
    this.v1 = v1

def init(MAX_X, MAX_Y):
  board = []
  for i in range(MAX_X):
    board.append([])
    for j in range(MAX_Y):
      # door
      if i == MAX_X/2 and j == MAX_X/2:
        board[i].append(particle(DOOR_MASS, 0, 0))
        continue
      # walls
      if i == 0 or j == 0 or i == MAX_X-1 or j == MAX_Y-1 or i == MAX_X/2:
        board[i].append(particle(WALL_MASS, 0, 0))
        continue
      # particle
      if i == randint(0,MAX_X) and j == randint(0,MAX_Y):
        board[i].append(particle(PARTICLE_MASS, 1, 1))
        continue
      board[i].append(None)
  return board

def step(board):       
  for i in range(MAX_X):
    for j in range(MAX_Y):
      next(board, i, j)

def _print(board): 
    s =""
    info = ""
    for i in range(MAX_X):
      for j in range(MAX_Y):
        p = board[i][j]
        if p is None:
           s += " "
           continue
        if p.m == WALL_MASS:
           s += "X"
        if p.m == PARTICLE_MASS:
           s += "O"
           info += "({},{},{})\n".format(p.m, p.v0, p.v1)
        if p.m == DOOR_MASS:
           s += "+"
      s += "\n"
    print(s)
    print(info)


if __name__ == "__main__":
  b = init(MAX_X, MAX_Y)
  _print(b)
  while(True):
     step(b)
     _print(b)


