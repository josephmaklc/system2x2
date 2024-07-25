import matplotlib.pyplot as plt
import numpy as np
import math

"""
Simple little 2x2 system example:
 x + 2y = 1
 3x + 5y = 2
 
 This can be written as matrix form [A][x] = [B]:
 
 [1 2][x] =  [1]
 [3 5][y]    [2]
"""
A = np.array([[1, 2], 
              [3, 5]])
B = np.array([1, 2])

XMIN, XMAX = -5, 5
YMIN, YMAX = -5, 5
GRIDSIZE = 1

# linear equations requires only 2 points because 2 points determines a line
# use higher numbers to graph other functions so more points used
STEPS = 2  


a11 = A[0][0];
a12 = A[0][1];
a21 = A[1][0];
a22 = A[1][1];
b11 = B[0];
b12 = B[1];

def f(x):
    return (-a11*x+b11)/a12

def g(x):
    return (-a21*x+b12)/a22

x = np.linspace(XMIN,XMAX,STEPS)
plt.axis([XMIN,XMAX,YMIN,YMAX]) 

y1v = np.zeros(len(x))
y2v = np.zeros(len(x))
for i in range(len(x)):
    try: 
        y1v[i] = f(x[i])
        y2v[i] = g(x[i])
    except:
        pass

try:
    solution = np.linalg.solve(A, B)
    print("Solution")
    print(solution)
    solutionpoint =  "(${0:.2f}, ${1:.2f})".format(solution[0], solution[1]);
    plt.plot(solution[0],solution[1],'bo'); # blue circle
    plt.annotate( solutionpoint,(solution[0],solution[1]));
except:
    print("No solution")
    
eq1 = "{0}x+{1}y={2}".format(a11,a12,b11);
eq2 = "{0}x+{1}y={2}".format(a21,a22,b12);
plt.plot(x,y1v, color='r',label=eq1)
plt.plot(x,y2v, color='g',label=eq2)


# make axes
plt.axhline(y=0, color='k') # 'k' means black
plt.axvline(x=0, color='k')
# gca is get current axes 
plt.gca().set_aspect('equal')
plt.gca().set_xticks(np.arange(XMIN,XMAX,GRIDSIZE))
plt.gca().set_yticks(np.arange(YMIN,YMAX,GRIDSIZE))
plt.grid(True)
plt.legend() 
plt.show()
