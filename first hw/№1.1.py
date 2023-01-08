import time
from cvxopt.modeling import variable, op

start = time.time()
x = variable(25, "x")
z = (4*x[0]+5*x[1]+2*x[2]+4*x[3]+3*x[4]+3*x[5]+1*x[6]+3*x[7]+5*x[8]+2*x[9]+2*x[10]+7*x[11]+6*x[12]+8*x[13]+6*x[14]+3*x[15]+3*x[16]+1*x[17]+4*x[18]+9*x[19]+1*x[20]+6*x[21]+9*x[22]+2*x[23]+7*x[24])
mass1 =(x[0]+x[1]+x[2]+x[3]+x[4]<=20)
mass2 =(x[5]+x[6]+x[7]+x[8]+x[9]<=40)
mass3 =(x[10]+x[11]+x[12]+x[13]+x[14]<=80)
mass4 =(x[15]+x[16]+x[17]+x[18]+x[19]<=40)
mass5 =(x[20]+x[21]+x[22]+x[23]+x[24]<=20)
mass6 =(x[0]+x[5]+x[10]+x[15]+x[20]==20)
mass7 =(x[1]+x[6]+x[11]+x[16]+x[21]==20)
mass8 =(x[2]+x[7]+x[12]+x[17]+x[22]==40)
mass9 =(x[3]+x[8]+x[13]+x[18]+x[23]==40)
mass10 =(x[4]+x[9]+x[14]+x[19]+x[24]==40)
x_non_negative = (x>=0)
problem = op(z,[mass1,mass2,mass3,mass4,mass5,mass6,mass7,mass8,mass9,mass10,x_non_negative])
problem.solve(solver="glpk")
problem.status
print("Result: {}".format(x.value))
print("Price: {}".format(problem.objective.value()[0]))
stop = time.time()
print(stop-start)