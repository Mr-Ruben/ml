from IPython.display import Audio, display

# ----- error sound --------
def play_sound_error(self, etype, value, tb, tb_offset=None):
    self.showtraceback((etype, value, tb), tb_offset=tb_offset)

    v1="http://soundbible.com/grab.php?id=419&type=wav" # Short Error Beep sound
    v2="https://wav-sounds.com/wp-content/uploads/2017/09/Various-02.wav" # Short Baby cry
    #display(Audio(url=v1, autoplay=True))

    v1="../sound_error_beep.wav" # Short Error Beep sound 
    v2="../sound_baby_cry.wav" # Short Baby cry
    display(Audio(filename=v1, autoplay=True))

# ----- atach it to all Exceptions
get_ipython().set_custom_exc((Exception,), play_sound_error)
  
    
# ----- success sound --------
def play_sound_success():
    #v1='http://soundbible.com/grab.php?id=1795&type=wav'
    #display(Audio(url=v1, autoplay=True))
    v1='../sound_success.wav'    
    display(Audio(filename=v1, autoplay=True))
