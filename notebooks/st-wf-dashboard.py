import streamlit as st
import pandas as pd
import numpy as np
import time 

from wf_script import Population

st.title('Simple Wright-Fisher Simulation of Genetic Drift')

tab1, tab2 = st.tabs(["wf skel", "wf fancy"])

with tab1:
    st.write("The base wf model with no fancy")

    # Create a new Population
    # As a reminder these are the default values for population size (N)
    # and initial derived allele frequency (f).
    #   N=10, f=0.2
    p = Population()

    # Initialize the chart with the initial allele frequency of the derived
    # allele. `line_chart` expects a list, so we must wrap `p.f` in square
    # brackets to pass a list
    chart = st.line_chart([p.f])

    # Initially we'll run a loop 50 times
    for i in range(1, 50):
        # Step 1 wf generation
        p.step(ngens=1)
        # Calculate the current derived allele frequency
        freq = np.sum(p.pop)/len(p.pop)
        # Update the chart to add the current allele frequency
        chart.add_rows([freq])
        # sleep for a small amount of time so you can watch the animation
        time.sleep(0.05)

with tab2:
    st.write("The whole enchilada wf model with fancy")

    generations = st.slider("Generations", 1, 1000, 50, 10)
    N = st.slider("N", 10, 10000, 10, 10)
    f = st.slider("f", 0.0, 1.0, 0.2, 0.01)
    nsims = st.slider("Number of simulations", 1, 10, 1, 1)

    sims = {}
    for idx in range(nsims):
        sims[idx] = Population(N=N, f=f)

    chart = st.line_chart(pd.DataFrame([p.f] * nsims),
                            x_label="Generations",
                            y_label="Derived allele freq",
                            color='#ffaa00')

    for i in range(1, generations):
        freq = []
        for p in sims.values():
            p.step(ngens=1)
            freq.append(np.sum(p.pop)/len(p.pop))
        chart.add_rows(pd.DataFrame(freq))
        time.sleep(0.05)


# Add a button to rerun the simulation
st.button("Rerun")
