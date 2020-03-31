
# Usage: from   _xload_xsave import *
# Or     import _xload_xsave

import inspect
try:
   import cPickle as pickle
except:
   import pickle


#---------------------
def retrieve_name(var):
        """
        Gets the name of var. Does it from the out most frame inner-wards.
        :param var: variable to get name from.
        :return: string
        """
        for fi in reversed(inspect.stack()):
            names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
            if len(names) > 0:
                return names[0]
#---------------------
def xsave(input_var,file_name=""):
  """
  usage:  xsave(data)  
          xsave(input_var=data,file_name="file_name")"""
  var_name=file_name if file_name  else retrieve_name(input_var)

  with open(var_name+".pkl", "wb") as f:
      pickle.dump(input_var, f)
#---------------------
def xload(var_name):
  """usage:   data=xload("data")
  returns None if file not found
  so you can do:
  data=xload("data"); if not data: ...
  """

  into=None
  # Check if file exists
  if (Path(".") / (var_name+".pkl")).is_file():
    # Open it and load
    with open(var_name+".pkl", "rb") as f:
      into = pickle.load(f)
  return(into)
#---------------------