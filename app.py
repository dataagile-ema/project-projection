from faulthandler import disable
import streamlit as st
from PIL import Image
from itertools import compress

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame()



def str2num(s):
    try:
        return float(s.replace(",", "."))
    except ValueError:
        st.write("Måste vara ett tal")
        return np.nan
        

# sida
im = Image.open("favicon.ico")
st.set_page_config(page_title="Projektprognos", page_icon=im)
"""
# Projektprognos
"""

left, right = st.columns(2)
with left:
    min_for_story = str2num(st.text_input("Min tid för en User Story", value="5"))
    max_for_story = str2num(st.text_input("Max tid för en User Story", value="40"))
   
with right:
    no_of_stories = str2num(st.text_input("Antal User Stories", value="10", key="text")) 
    share_rework = str2num(st.text_input("Procent av all tid som är rättningar", value="10"))


#st.write(no_of_stories, min_for_story, max_for_story)


def calc_uniform_simulation(no_of_stories, min_for_story, max_for_story):
    return np.sum(np.random.uniform(min_for_story, max_for_story, int(no_of_stories)))

if no_of_stories > 0.0 and min_for_story > 0.0 and max_for_story > 0.0:
    np.random.seed(42)



    df["value"] = [calc_uniform_simulation(int(no_of_stories), min_for_story, max_for_story) for i in range(5000)]

    factor_rework = 1 + (share_rework/100)

    # multiply by factor
    df["value"] = df["value"] * factor_rework


    plt.style.use('ggplot')
    plt.rcParams.update({'font.size': 14})

    fig, ax = plt.subplots()

    # remove scale on y-axis
    #ax.yaxis.set_major_formatter(plt.NullFormatter())

    # remove y-axis
    ax.yaxis.set_visible(False)

    # dist plot without label for 'value'
    ax.hist(df["value"], bins=20, density=True, alpha=0.5)
    #df.plot.kde(ax=ax, legend=False, label="")

    ax.set_xlim(0, max_for_story*no_of_stories)


    # calc 85th percentile
    p85th = df.value.quantile(0.85)
    p50th = df.value.quantile(0.5)

    # set label_str to p85th rounded to 0 decimals
    label_str_85 = "{:.0f}".format(p85th)
    label_str_50 = "{:.0f}".format(p50th)



    ax.axvline(p85th, color='g', linestyle='--', label=f'85:e procentilen: {label_str_85}')

    ax.axvline(p50th, color='b', linestyle='--', label=f'50:e percentile: {label_str_50}')



    ax.legend(loc='upper left')

    # set height of plot
    fig.set_size_inches(10, 5)
    # set font size
  
    st.pyplot(fig)




 






