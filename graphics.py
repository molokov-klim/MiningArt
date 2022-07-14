import matplotlib.pyplot as plt
import numpy as np

# fig, ax = plt.subplots()
# ax.set_title('График')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.grid()
#
# x = np.linspace(-5, 5, 100)
# y = x**2
# ax.plot(x, y)
#
# plt.show()


# x = [1, 5, 10, 15, 20]
# y1 = [1, 17, 3, 5, 1]
# y2 = [4, 3, 1, 8, 12]
#
# plt.figure(figsize=(12, 7))
#
# plt.plot(x, y1, color='red', alpha=0.7, label="first", lw=5, mec='b', mew=2, ms=5)
# plt.plot(x, y2, color='green', alpha=0.7, label="second", lw=5, mec='b', mew=2, ms=5)
# plt.legend()
# plt.grid(True)
#
# plt.show()

#hardcode - исправить
def show_plot(LIST_OF_FUEL):
    y1 = []
    y2 = []
    for i in LIST_OF_FUEL:
        if(i[0]==992):
            y1.append(i[1])
        else:
            y2.append(i[1])

    if(len(y1)>len(y2)):
        y1 = y1[:len(y2)]
    else:
        y2 = y2[:len(y1)]

    temp = 0
    x = [1, ]
    for i in range(len(y1)):
        if i!=len(y1)-1:
            temp = temp + 5
            x.append(temp)

    plt.figure(figsize=(12, 7))
    plt.plot(x, y1, color='red')
    plt.plot(x, y2, color='green')
    plt.grid(True)

    plt.show()






