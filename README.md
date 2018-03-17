# 2nd_law
thermo simulations

Make a simulation with many particles moving in space. 
Replicate Maxwells demon setup.  
* Chamber
* Wall
* Door
* Particles

## Particles
```
def next(board, x0, x1):
    particle = board[x0, x1]
    target = board[x0+particle.v0, x1+particle.v1]
    particle.v0, target.v0 = collision(particle.m, particle.v0, target.m, target.v0)
    particle.v1, target.v1 = collision(particle.m, particle.v1, target.m, target.v1)
    board[x0, x1] = None
    board[x0 + particle.v0, x1 + particle.v1] = particle
    
def collision(m_0, v_0, m_1, v_1):
  # m_0*v_0+m_1*v_1=m_0*v_0_+m_1*v_1_
  # m_0*v_0^2+m_1*v_1^2=m_0*v_0_^2+m_1*v_1_^2
  # v_0_*v_1_=v_0*v_1
  # m_0*v_0+m_1*v_1=m_0*v_0_+m_1*v_0*v_1/v_0_
  # 0=m_0*v_0_^2+2*(m_0*v_0+m_1*v_1)*v_0_+m_1*v_0*v_1
  a = m_0
  b = 2*(m_0*v_0+m_1*v_1)
  c = m_1*v_0*v_1
  v_0_ = (-b±sqrt(b**2-4*a*c))/2*a
  v_1_ = v_0*v_1/v_0_
  return v_0_, v_1_

class particle(object):
  def __init__(this, m, x0, x1, v0, v1):
    this.m = m
    this.v0 = v0
    this.v1 = v1

for i in range(MAX_X):
  for j in range(MAX_Y):
    # door
     if i == MAX_X/2 and j == MAX_X/2:
      board[i][j] = particle(10**-10, 0, 0)
      continue
    # walls
    if i == 0 or j == 0 or i == MAX_X-1 or j == MAX_Y-1 or i == MAX_X/2:
      board[i][j] = particle(10**10, 0, 0)
      continue
    # particle
    if i == randint(0,MAX_X) and j == randint(0,MAX_J):
      board[i][j] = particle(10**0, randint(0, MAX_X), randint(0, MAX_Y))
      continue
    

while(true):
  for i in range(MAX_X):
    for j in range(MAX_Y):
        next(board, i, j)
        print(board)

```
One sided door. 
A door that opens to one side. 
All the particles
