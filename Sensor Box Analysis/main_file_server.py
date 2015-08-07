import data_analysis_server
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import dates as mdates
from matplotlib.ticker import LinearLocator

def get_link():
    ns5min=5*60*1e9
    
    end = pd.Timestamp("now", tz="UTC")
    end = pd.Timestamp(end.value//ns5min*ns5min) #round to nearest 5min
    
    start = end-pd.Timedelta(minutes=10)
    
    print start,end
    
    link = "http://109.237.25.161/particle/measurements?device={}&measurement={}&start_date={}&end_date={}".format("{}","{}",start,end)

    return link

def line_plot(df_k,df_l):
    levels = df_k.columns.values
    lev_cols = {
        "day_night":"slategray",
        "down_time":"lightgray",
        
        "day_high":"orange",
        "day_low":"wheat",
        "night_high":"lightcyan",
        "night_low":"paleturquoise"
    }
    hfmt = mdates.DateFormatter('%d/%m %H:%M') #display format of date
    
    fig, axs = plt.subplots(2, 1, sharex=True, figsize=(10,5))
    
    proxys=[]
    for i in range(len(levels)):
        axs[0].fill_between(df_k.index,0,df_k[levels[i]].values,color=lev_cols[levels[i]],alpha=1)
        axs[1].fill_between(df_l.index,0,df_l[levels[i]].values,color=lev_cols[levels[i]],alpha=1)
        proxys.append(plt.Rectangle((0,0),0,0,facecolor=lev_cols[levels[i]],edgecolor="black",label=levels[i]))

    axs[0].xaxis.set_major_locator(mdates.HourLocator(tz=timezone("Europe/London")))
    axs[0].xaxis.set_major_formatter(hfmt)
    
    axs[0].set_ylim(0,1)
    axs[1].set_ylim(0,1)

    axs[0].yaxis.set_visible(False)
    axs[1].yaxis.set_visible(False)
    
    axs[0].set_title("Kitchen")
    axs[1].set_title("Living Room")

    #axs[0].set_xlim("2015-08-03 00:00","2015-08-04 13:15")
    
    fig.legend(handles=proxys,labels=levels)
    
    fig.autofmt_xdate()
    fig.show()

def main():
    
    link = get_link()
    
    kitchen = data_analysis_server.main(room="kitchen",api_link=link)
    living_room = data_analysis_server.main(room="living_room",api_link=link)
    
    #print kitchen.tail(), "\n", living_room.tail()
    #line_plot(kitchen,living_room)
    
    #print "Hit Enter to exit..."
    #raw_input()

# call main
if __name__ == '__main__':
    main()