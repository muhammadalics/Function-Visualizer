import numpy as np
import numexpr as ne

def func_val(str_input, xmin, xmax, ymin, ymax, xstep):

    x= np.aranage(xmin, xmax, xstep)
    y = ne.evaluate(str_input)

    return x,y



