import streamlit as st
import os

songs = [file for file in os.listdir('Songs') if file.endswith('.mp3')]
song_titles = [file.split('.')[0].title() for file in os.listdir('Songs') if file.endswith('.mp3')].sort()
cover = [file for file in os.listdir('Covers') if file.endswith('.png')]

song_and_art = {}
for song in songs:
    song_title = os.path.splitext(song)[0]
    song_and_art[song] = cover

def main():
    st.title('Music Player :)')
    
    current_song_index = st.session_state.get('current_song_index', 0)
    
    song_selection = st.radio('Select Song', song_titles, index=current_song_index)
    
    st.audio(f'Songs/{song_selection}', format='audio/mp3', start_time=0)
    
    current_song = songs[current_song_index]
    cover_path = 'Covers/cover.png'
    st.image(cover_path, use_column_width=True)
    
    if st.button('Previous') and current_song_index > 0:
        current_song_index -= 1
    if st.button('Next') and current_song_index < len(songs) - 1:
        current_song_index += 1
        
    st.session_state.current_song_index = current_song_index
    
if __name__ == '__main__':
    main()