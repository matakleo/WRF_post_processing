import numpy as np
eta_lvls=[]

a = np.linspace(1.000,0,num=63)
#b = np.linspace(0.725, 0, num=(63-35))
for num in a:
    formatted_string = "{:.3f}".format(num)
    num=float(formatted_string)
    eta_lvls.append(num)

# for num in b:
#     formatted_string = "{:.3f}".format(num)
#     num=float(formatted_string)
#     eta_lvls.append(num)
print(eta_lvls)
# for i in range(len(eta_lvls)):
#     print(i)
print(len(eta_lvls))
# idx = np.where(eta_lvls== 0.666)
# eta_lvls2 = [1.000, 0.985, 0.970, 0.955, 0.940,
#             0.925, 0.910, 0.895, 0.880, 0.865,
#             0.850, 0.835, 0.820, 0.805, 0.790,
#             0.775, 0.760, 0.745, 0.730, 0.715,
#             0.700, 0.685, 0.670, 0.655, 0.640,
#             0.610, 0.580, 0.550, 0.520, 0.490,
#             0.450, 0.410, 0.370, 0.330, 0.280,
#             0.230, 0.180,0.130,0.080,0.050,
#             0.020, 0.000]
# beta=[]
# print(len(eta_lvls2))
# print(len(eta_lvls))
# for i in range(len(eta_lvls)-1):
#     a=eta_lvls[i]
#     b=eta_lvls2[i]

#     beta.append(a-b)
#     formatted_string = "{:.3f}".format(beta[i])
#     beta[i]=float(formatted_string)
#     beta.append(beta[i])
# print(beta)