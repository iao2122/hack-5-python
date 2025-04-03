import streamlit as st
import pandas as pd
import numpy as np
import time

from wf_script import Population

st.title('Simple Wright-Fisher Simulation of Genetic Drift')

generations = st.sidebar.slider("Generations", 1, 1000, 50, 10)
N = st.sidebar.slider("N", 10, 10000, 10, 10)
f = st.sidebar.slider("f", 0.0, 1.0, 0.2, 0.01)

status_text = st.sidebar.empty()

p = Population(N=N, f=f)

chart = st.line_chart([p.f])

for i in range(1, generations):
    p.step(ngens=1)
    if p.state != "segregating":
    	break
    freq = np.sum(p.pop)/len(p.pop)
    chart.add_rows([freq])
    time.sleep(0.05)
    status_text.text(f"Derived allele: {p.state}")

status_text.text(f"Derived allele: {p.state}")
st.button("Rerun")