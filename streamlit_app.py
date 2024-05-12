import streamlit as st
from pygame import mixer

mixer.init()

songs = []

for song in songs:
    song_button = st.button(f'{song}')

music = st.file_uploader()

try:
    mixer.load(songs)
except Exception:
    st.write('Please Choose a song')
    
if st.button('Play'):
    mixer.music.play()

if st.button('Pause'):
    mixer.music.pause()

if st.button('Resume'):
    mixer.music.unpause()

if st.button('Stop'):
    mixer.music.stop()