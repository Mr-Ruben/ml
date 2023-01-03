from IPython.display import Audio, display



#-----------------------------------
def download_audio_files(location:str="~/jupyter_sounds") -> None:
    "Downloads the audio files to the specified location"
    
    x="""
    #electricity jet register baby error success
    %mkdir --parents ~/jupyter_sounds
    %cd ~/jupyter_sounds
    !wget -O electricity.wav https://wav-sounds.com/wp-content/uploads/2017/09/Various-08.wav
    !wget -O register-machine.wav https://wav-sounds.com/wp-content/uploads/2017/09/Various-06.wav
    !wget -O jet.wav https://wav-sounds.com/wp-content/uploads/2017/09/Vehicle-08.wav

    # success
    !wget -O sound_success.wav http://soundbible.com/grab.php?id=1795&type=wav

    # baby
    !wget -O sound_baby_cry.wav https://wav-sounds.com/wp-content/uploads/2017/09/Various-02.wav

    # Short Error Beep sound
    !wget -O sound_error_beep.wav  http://soundbible.com/grab.php?id=419&type=wav
    """
    print(x)
    return 

# ----- error sound --------
def play_sound_error(self, etype, value, tb, tb_offset=None):
    self.showtraceback((etype, value, tb), tb_offset=tb_offset)

    v1="http://soundbible.com/grab.php?id=419&type=wav" # Short Error Beep sound
    v2="https://wav-sounds.com/wp-content/uploads/2017/09/Various-02.wav" # Short Baby cry
    #display(Audio(url=v1, autoplay=True))

    v1="../jupyter_sounds/sound_error_beep.wav" # Short Error Beep sound 
    v2="../jupyter_sounds/sound_baby_cry.wav" # Short Baby cry
    #display(Audio(filename=v1, autoplay=True))
    
    play_any_sound(name="error")
    return

# ----- atach it to all Exceptions
get_ipython().set_custom_exc((Exception,), play_sound_error)
  
    
# ----- success sound --------
def play_sound_success():
    #v1='http://soundbible.com/grab.php?id=1795&type=wav'
    #display(Audio(url=v1, autoplay=True))
    #v1='../sound_success.wav'
    #v1='~/lang-tutor-tools-gcs/jupyter_sounds/
    #display(Audio(filename=v1, autoplay=True))
    play_any_sound(name="success")
    return
#-------------------------------------
def play_any_sound(name:str = "any"):
    """One of: electricity jet register baby error success or nothing (random)
    """
    
    sounds={"electricity":'/home/osboxes/lang-tutor-tools-gcs/jupyter_sounds/electricity.wav',
             "jet":'/home/osboxes/lang-tutor-tools-gcs/jupyter_sounds/jet.wav',
             "register":'/home/osboxes/lang-tutor-tools-gcs/jupyter_sounds/register-machine.wav',
             "baby":'/home/osboxes/lang-tutor-tools-gcs/jupyter_sounds/sound_baby_cry.wav',
             "error":'/home/osboxes/lang-tutor-tools-gcs/jupyter_sounds/sound_error_beep.wav',
             "success":'/home/osboxes/lang-tutor-tools-gcs/jupyter_sounds/sound_success.wav'}
        
    #v1='http://soundbible.com/grab.php?id=1795&type=wav'
    #display(Audio(url=v1, autoplay=True))
    s=name.lower()
    if s in sounds:
        file=sounds[s]
    else:
        import random
        file=random.choice(list(sounds.values()))
    
    #v1='../sound_success.wav'    
    display(Audio(filename=file, autoplay=True))
    return
#-------------------------------------------------------
#-------------------------------------------------------
