import streamlit as st
import os

songs = [file for file in os.listdir('Songs') if file.endswith('.mp3')]
cover = [file for file in os.listdir('Covers') if file.endswith('.png')]

song_and_art = {}
for song in songs:
    song_title = os.path.splitext(song)[0]
    song_and_art[song] = cover

def main():
    st.title('Music Player :)')
    
    current_song_index = st.session_state.get('current_song_index', 0)
    
    song_selection = st.radio('scroll for a surprise maybe who knows', songs, index=current_song_index)
    
    st.audio(f'Songs/{song_selection}', format='audio/mp3', start_time=0)
    
    current_song = songs[current_song_index]
    cover_path = 'Covers/cover.png'
    st.image(cover_path, use_column_width=True)
    
    st.write('Woah look at him!')
    st.markdown('![He be dancin](https://media.tenor.com/yRSnf6wABQ4AAAAi/pato-duck.gif)')
        
    st.session_state.current_song_index = current_song_index
    
if __name__ == '__main__':
    main()