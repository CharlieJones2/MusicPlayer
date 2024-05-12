import streamlit as st
import pygame

pygame.mixer.init()

songs = []

for song in songs:
    song_button = st.button(f'{song}')

music = st.file_uploader()

try:
    pygame.mixer.load(songs)
except Exception:
    st.write('Please Choose a song')
    
if st.button('Play'):
    pygame.mixer.music.play()

if st.button('Pause'):
    pygame.mixer.music.pause()

if st.button('Resume'):
    pygame.mixer.music.unpause()

if st.button('Stop'):
    pygame.mixer.music.stop()