import matplotlib.pyplot as plt
import func_val_calc as fncalc


x, y = fncalc.func_val('2*sin(x)', 0, 8, 1., -1, 0.1)

fig = plt.figure()

plt.plot(x,y)

plt.show()




