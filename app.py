import streamlit as st
from PIL import Image
import altair as alt
import pandas as pd
import numpy as np
from chart_assembler import AssembleCharts

df = pd.DataFrame()
np.random.seed(42)

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
    share_rework = str2num(st.text_input("Procent påslag för rättningar", value="10"))


def calc_uniform_simulation(no_of_stories, min_for_story, max_for_story):
    return np.sum(np.random.uniform(min_for_story, max_for_story, int(no_of_stories)))

factor_rework = 1 + (share_rework/100)

@st.cache(allow_output_mutation=True)
def simulate(no_of_stories, min_for_story, max_for_story, factor_rework):
    df["value"] = [calc_uniform_simulation(int(no_of_stories), min_for_story, max_for_story) for i in range(4000)]
    df["value"] = df["value"] * factor_rework
    return df

if no_of_stories > 0.0 and min_for_story > 0.0 and max_for_story > 0.0:
    df = simulate(no_of_stories, min_for_story, max_for_story, factor_rework)

    p85th = df.value.quantile(0.85)
    p50th = df.value.quantile(0.5)

    # set label_str to p85th rounded to 0 decimals
    label_str_85 = "{:.0f}".format(p85th)
    label_str_50 = "{:.0f}".format(p50th)
    st.subheader("Sammanlagt tid för alla User Stories")
    st.write(f'Under {label_str_85} med 85% sannolikhet')
    st.write(f'Under {label_str_50} med 50% sannolikhet')
  

    histogram = alt.Chart(df).transform_density(
        'value',
        as_=['value', 'Sannolikhet'],
        ).mark_area(color='lightgrey').encode(
            x = alt.X('value:Q', title="Sammanlagd tid", scale=alt.Scale(domain=[0, max_for_story*no_of_stories*factor_rework])),
            y='Sannolikhet:Q',
        )


    quantiler = (
        alt.Chart(df)
        .transform_quantile('value', probs=[0.50, 0.85], as_=['Procentil', 'value'])
        .mark_rule(size=2, opacity=0.85)
        .encode(

            x = alt.X('value:Q'),
     
            color = alt.Color(
                    "Procentil:N",
                    legend=alt.Legend(orient='top'),
                )
        )
    )

    c_expr = (histogram + quantiler)
    ass = AssembleCharts(c_expr)
    c_complete = ass.get_assembled_charts()
    
    st.altair_chart(c_complete, use_container_width=True)
    

