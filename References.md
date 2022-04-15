# Skapa miljö
conda create --name pp_app python=3.9
conda activate pp_app
pip3 install streamlit==0.89.0
conda install -c conda-forge matplotlib
conda install -c anaconda scipy
pip3 install jsonschema==3.2
(när bugg i jsonshcema är fixad räcker det att installera senaste streamlit)


   chart= alt.Chart(df).mark_bar().encode(
        alt.X("value:Q", bin=True),
        y='count()',
    )
    # plot line for 85:th percentile in chart




    st.altair_chart(chart)