import streamlit as st
import os
import sys
import importlib.util



if len(sys.argv) > 1:
    folder = os.path.abspath(sys.argv[1])
else:
    folder = os.path.abspath(os.getcwd())
this_file = os.path.abspath(__file__)
fnames = []

for basename in os.listdir(folder):
    fname = os.path.basename(basename)
    if fname.endswith('.py') and fname != this_file:
        
        if fname == 'app.py':
            continue
        print(fname)
        
        fnames.append(fname)

st.sidebar.title("Car Analysis")
st.sidebar.markdown("Welcome!! This is my project on car analysis for Engage 2022")
st.sidebar.image("car.jpg")
fname_to_run = st.sidebar.selectbox('Select an app', fnames)
fake_module_count = 0

def load_module(filepath):
    global fake_module_count

    modulename = '_dont_care_%s' % fake_module_count
    spec = importlib.util.spec_from_file_location(modulename, filepath)
    module = importlib.util.module_from_spec(spec)
    sys.modules[modulename] = module

    fake_module_count += 1


with open(fname_to_run) as f:
    load_module(fname_to_run)
    filebody = f.read()

exec(filebody, {})