import matplotlib.pyplot as plt

def plots(nrow_size,ncol_size,plot_size) :

    ''' input arg : 
                        nrow_size,  
                        ncolumn_size, 
                        plot_size (tuple_type) 
                        
    '''

    fig,graph_list = plt.subplots(nrows=nrow_size,ncols=ncol_size)
    fig.set_size_inches(plot_size)

    return fig,graph_list