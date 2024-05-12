import streamlit as st
import pygame
import os

#pygame.mixer.init()

songs = [file for file in os.listdir('Songs') if file.endswith('.mp3')]
covers = [file for file in os.listdir('Covers') if file.endswith('.png')]

song_and_art = {}
for song in songs:
    song_title = os.path.splittext(song)[0]
    for cover in covers:
        if song_title in cover:
            song_and_art[song] = cover

# def play_song(song_path):
#     pygame.mixer.music.load(song_path)
#     pygame.mixer.music.play()
    

def main():
    st.title('Music Player :)')
    st.sidebar.title('Songs:')
    
    st.header('All Songs')
    current_song_index = st.session_state.get('current_song_index', 0)
    
    st.sidebar.title('Playlist')
    song_selection = st.radio('Select Song', songs, index=current_song_index)
    
    st.sidebar.audio(f'Songs/{song_selection}', format='audio/mp3', start_time=0)
    
    current_song = songs[current_song_index]
    cover_art = song_and_art.get(current_song, 'cover.png')
    cover_path = f'Covers/{cover_art}'
    st.sidebar.image(cover_art, use_column_width=True)
    
    st.success(f'Now Playing: {song_selection}')
    
    if st.button('Previous') and current_song_index > 0:
        current_song_index -= 1
    if st.button('Next') and current_song_index < len(songs) - 1:
        current_song_index += 1
        
    st.session_state.current_song_index = current_song_index
    
if __name__ == '__main__':
    main()