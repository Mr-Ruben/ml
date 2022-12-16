# Call this file with
# !wget --no-clobber --quiet "https://raw.githubusercontent.com/Mr-Ruben/ml/master/_jupyter_display.py"
# %run _jupyter_display.py

import sys

# Adapted to the differences in library paths from Python 3.7

if sys.version_info.minor<=7:
    from IPython.core.interactiveshell import InteractiveShell
else:
    from IPython import InteractiveShell

# To print the output of all commands (except those ending in ; )
InteractiveShell.ast_node_interactivity = "all"


# To change the width of the current notebook you're working on,
# you can enter the following into a cell:
if sys.version_info.minor<=7:
    from IPython.core.display import display, HTML
else:
    from IPython.display import display, HTML
    
display(HTML("<style>.container { width:100% !important; }</style>"))



## To print the output of all commands (except those ending in ; )
#from IPython.core.interactiveshell import InteractiveShell
#InteractiveShell.ast_node_interactivity = "all"

## To change the width of the current notebook you're working on, you can enter the following into a cell:
#from IPython.core.display import display, HTML
#display(HTML("<style>.container { width:100% !important; }</style>"))



# ---------------------- v3 ---------------------------
# import sys

# if sys.version_info.minor<=7:
#     from IPython.core.interactiveshell import InteractiveShell
# else:
#     from IPython.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"

# # To change the width of the current notebook you're working on, you can enter the following into a cell:
# from IPython.core.display import display, HTML
# display(HTML("<style>.container { width:100% !important; }</style>"))

