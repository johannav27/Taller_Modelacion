from cProfile import label
import matplotlib.pyplot as plt
def habitat(B_0, R_0, B_c, R_c, R_d, B_d, N):
    Buhos, Ratones = [B_0], [R_0]
    for i in range(N-1):
        Buhos.append(B_c*Buhos[i]+(B_d*Buhos[i]*Ratones[i]))
        Ratones.append(R_c*Ratones[i]+(R_d*Buhos[i]*Ratones[i]))
    plt.plot(Buhos, label="Buhos")
    plt.plot(Ratones, label="Ratones")
    plt.legend()
    plt.show()
    return Buhos, Ratones
#CasoA
#habitat(150, 200, 0.8, 1.5, -0.001, 0.002, 45)
#Caso B
#habitat(150, 300, 0.8, 1.5, -0.001, 0.002, 45)
#Caso C
#habitat(100, 200, 0.8, 1.5, -0.001, 0.002, 45)
#Caso D
#habitat(10, 20, 0.8, 1.5, -0.001, 0.002, 15)

#Experimentos
#habitat(150, 200, 1.5, 0.8, -0.001, 0.002, 10)
#habitat(150, 200, 0.8, 1.5, -0.001, 0.001,30)
habitat(200, 150, 1.5, 0.8, -0.001, 0.002, 10)
habitat(200, 150, 0.8, 1.5, -0.001, 0.001,40)

