from flask import Flask,render_template,request
from average import Average
from graph import Graph
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

app.secret_key = 'CS106A'

@app.route('/',methods = ['GET','POST'])
def average():
        form1 = Average()
        form2 = Graph()
        if request.method == 'GET':
                return render_template('base.html',form1=form1,form2=form2,ch='First')
        elif request.method == 'POST':
                if request.form['submit'] == 'PlotTheGraph':
                    class Interpolate:
                        S, Q, R = [], [], []
                        # for finding limits, polynomials
                        x = sp.Symbol('x')
                        def Lag_Poly(self, L, M):
                            # X for storing x coordinates
                            # Y for storing f(x)
                            self.Q, self.R = L, M
                            for i in range(len(L)):
                                u, j = 1, 0
                                # forming list of polynomials
                                # summation of which is Lagrange Polynomial
                                while j < len(L):
                                    if i != j:
                                        u *= (self.x-L[j])/(L[i]-L[j])
                                    j += 1
                                u*= M[i] 
                                self.S.append(u)   
                            # plot Lagrange Polynomial
                            self.plot_Poly()     
                            
                        def plot_Poly(self, var = []):     
                            a = np.arange(0,max(self.Q)+0.2,0.1)
                            pol_sum = 0
                            # plot function in the list
                            for  i in self.S:   
                                pol_sum += i
                                for j in a:   
                                    var.append(sp.limit(i,self.x,j))
                                plt.plot(a, var)             
                                var = [] 
                            # plot Lagrange Polynomial in Black Color
                            for j in a:
                                var.append(sp.limit(pol_sum,self.x,j))
                            plt.plot(a, var,'k')
                            # plot node points
                            plt.plot(self.Q,self.R,'ro')
                            plt.title('INTERPOLATING POLYNOMIAL IS BLACK')
                            plt.xlabel('X-AXIS')
                            plt.ylabel('Y-AXIS')
                            plt.savefig('C:\Users\hp\Desktop\NA\static\img\graph.png')
                            plt.clf()     
                    ob = Interpolate()
                    x = form2.x_cor.data
                    y = form2.y_cor.data
                    L = [float(i) for i in x.split(' ')]
                    R= [float(i) for i in y.split(' ')]
                    ob.Lag_Poly(L,R)
                    return render_template('base.html',form1=form1,form2=form2,ch='Second')                                   
                else:
                        num = form1.message.data
                        num, sum = num.split(' '), 0
                        for i in num:                           
                                sum += float(i)
                        return render_template('base.html',form1=form1,form2=form2,avg = (sum*1.0)/len(num),ch='Third')
if __name__ == '__main__':
        app.run(debug = True)
