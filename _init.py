
# ------- Init ------------------

# Some magic
%matplotlib inline
# Reload an IPython extension (autoreload) by its module name.
%reload_ext autoreload
# Reload all modules (except those excluded by %aimport) every time before executing the Python code typed.
%autoreload 2


# Libraries
import fastai
from fastai.basics import *
from fastai.vision import *
from fastai.metrics import error_rate
from pathlib import Path
from fastai.widgets import *
import torch

import numpy as np

try:
   import cPickle as pickle
except:
   import pickle

# Load the Pandas libraries with alias 'pd' 
import pandas as pd 

# To print the output of all commands (except those ending in ; )
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# To change the width of the current notebook you're working on, you can enter the following into a cell:
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


# Note that minimum prereqs are: pytorch v1. fastai v1.0.11.
# Check versions
print(f"""
I have:                   {fastai.__version__} 
minimum required: fastai v1.0.11

I have:                    {torch.__version__}
minimum required: pytorch v1
""")

#BASE_PWD='/kaggle/working' # Kaggle
#BASE_PWD='/content'			  # Colab
#BASE_PWD='/storage'			  # Paperspace


#home=%pwd
#sys.path.append(home + '/content/cruises/ml')
