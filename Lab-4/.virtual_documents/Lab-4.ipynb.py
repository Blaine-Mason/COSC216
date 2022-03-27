import numpy as np
import matplotlib.pyplot as plt


def normal_pdf(x, m, s):
    return (1/(np.sqrt(2*np.pi)*s))*np.exp(-(1/2)*(((x-m)/s)**2))


max_ = 100
min_ = -max_
x = [i for i in np.arange(min_,max_,.1)]
y = [normal_pdf(i,0,1) for i in np.arange(min_,max_,.1)]
y_1 = [normal_pdf(i,0,3) for i in np.arange(min_,max_,.1)]
y_2 = [normal_pdf(i,0,5) for i in np.arange(min_,max_,.1)]
y_3 = [normal_pdf(i,0,10) for i in np.arange(min_,max_,.1)]


plt.xlim(-30,30)
plt.ylim(0,.5)
plt.title("Blaine Mason Normal PDF")
plt.plot(x, y, label="std = 1")
plt.plot(x, y_1, label="std = 3")
plt.plot(x, y_2, label="std = 5")
plt.plot(x, y_3, label="std = 10")
plt.legend()
plt.show()


−1,−3,0,5,10


max_ = 100
min_ = -max_
x = [i for i in np.arange(min_,max_,.1)]
y_list = [[normal_pdf(i,m,1) for i in np.arange(min_,max_,.1)] for m in [-1,-3,0,5,10]]
plt.xlim(-11,13)
plt.ylim(0,.5)
plt.title("Blaine Mason Normal PDF")
plt.plot(x, y_list[0], label="mean = -1")
plt.plot(x, y_list[1], label="mean = -3")
plt.plot(x, y_list[2], label="mean = 0")
plt.plot(x, y_list[3], label="mean = 5")
plt.plot(x, y_list[4], label="mean = 10")
plt.legend()
plt.show()


max_ = 10
min_ = -max_
x = [i for i in np.arange(min_,max_,.1)]
y_ = [normal_pdf(i,0,1) for i in np.arange(min_,max_,.1)]
plt.xlim(-5,5)
plt.ylim(0,.5)
plt.fill_between(-1.75,1.75)
plt.title("Blaine Mason Normal PDF")
plt.plot(x, y_)
plt.legend()
plt.show()



