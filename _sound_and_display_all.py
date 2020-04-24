# To print the output of all commands (except those ending in ; )
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from IPython.display import display


# Specific for Colab  (please provide alternative for Jupyter)
from google.colab import output
from IPython.core.ultratb import AutoFormattedTB

# Catch any Exception, play error sound and re-raise the Exception
#-------------------------------------------------
# initialize the formatter for making the tracebacks into strings
itb = AutoFormattedTB(mode = 'Plain', tb_offset = 1)
# this function will be called on exceptions in any cell
def custom_exc(shell, etype, evalue, tb, tb_offset=None):
 # still show the error within the notebook, don't just swallow it
 shell.showtraceback((etype, evalue, tb), tb_offset=tb_offset)
 # Play an audio beep. Any audio URL will do.  
 output.eval_js('new Audio("http://soundbible.com/grab.php?id=419&type=wav").play()')
 # # grab the traceback and make it into a list of strings
 # stb = itb.structured_traceback(etype, evalue, tb)
 # sstb = itb.stb2text(stb)
 # print (sstb) # <--- this is the variable with the traceback string
 # print ("sending mail")
 # send_mail_to_myself(sstb)
 # this registers a custom exception handler for the whole current notebook
get_ipython().set_custom_exc((Exception,), custom_exc)
#------------------------------------------
# Function to play a sound (to put at the end of a long job)
def beep_completed():
#url_sound="http://soundbible.com/grab.php?id=1795&type=mp3";
	output.eval_js('new Audio("http://soundbible.com/grab.php?id=1795&type=mp3").play()')
# Just play it
#beep_completed()
