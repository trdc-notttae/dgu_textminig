import numpy as np

def max_min_normalization(number_list, round_opt=4, reverse=False):
    this_max=np.max(number_list)
    this_min=np.min(number_list)
    norm_list=[]
    for number in number_list:
        this_norm=(number-this_min)/(this_max-this_min)
        if reverse==True:
            this_norm=1-this_norm
        this_norm=round(this_norm,round_opt)
        norm_list.append(this_norm)
    return(norm_list)
