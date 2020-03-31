
def rec_plots_lrfind():
  learn.recorder.plot(suggestion=True)
  plt.grid(True)
  learn.recorder.plot_losses()
  plt.grid(True)
  learn.recorder.plot_lr()
  plt.grid(True)
  #learn.recorder.plot_metrics()

def rec_plots_fit():
  #learn.recorder.plot(suggestion=True)
  learn.recorder.plot_losses()
  plt.grid(True)
  learn.recorder.plot_lr()
  plt.grid(True)
  # Need to check if model has metrics!!!!
  if learn.data.valid_ds.x.items > 0:
    learn.recorder.plot_metrics()
  plt.grid(True)