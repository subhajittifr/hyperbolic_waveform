import numpy  as np
import matplotlib.pyplot as plt

res311=np.genfromtxt("Data31.1_20.dat")[:, 1]
res312=np.genfromtxt("Data31.2_20.dat")[:, 1]
res314=np.genfromtxt("Data31.4_20.dat")[:, 1]

res111=np.genfromtxt("Data11.1_20.dat")[:, 1]
res112=np.genfromtxt("Data11.2_20.dat")[:, 1]
res114=np.genfromtxt("Data11.4_20.dat")[:, 1]

resQ11=np.genfromtxt("DataQ1.1_20.dat")[:, 1]
resQ12=np.genfromtxt("DataQ1.2_20.dat")[:, 1]
resQ14=np.genfromtxt("DataQ1.4_20.dat")[:, 1]


l=np.genfromtxt('Data31.1_20.dat')[:, 0]

plt.plot(l,res311,label=r'$e_t^{3PN}=1.1$')
# plt.plot(l,res312,label=r'$e_t^{3PN}=1.2$')
# plt.plot(l,res314,label=r'$e_t^{3PN}=1.4$')

# plt.plot(l,res111,label=r'$e_t^{1PN}=1.1$')
# plt.plot(l,res112,label=r'$e_t^{1PN}=1.2$')
# plt.plot(l,res114,label=r'$e_t^{1PN}=1.4$')

plt.plot(l,resQ11,linestyle='--',label=r'$e_t^{Q}=1.1$')
# plt.plot(l,resQ12,linestyle='--',label=r'$e_t^{Q}=1.2$')
# plt.plot(l,resQ14,linestyle='--',label=r'$e_t^{Q}=1.4$')



plt.grid()
plt.legend()
plt.xlim(min(l),max(l))
plt.xlabel(r"$\ell/{2 \pi}$")
plt.ylabel(r"Resudials")
plt.suptitle(r"$M=2 \times 10^9 \, M_\odot; R=1.2 \times 10^{14} \, w; b=20 w; w=\frac{GM}{c^2}$")
plt.savefig("20_3_1.1.pdf")
plt.show()