import streamlit as st
from mood import get_songs_by_mood

st.title("Welcome to :rainbow[MUSICA] 🎶")
st.markdown(
    """
    We know the feeling when you are feeling a certain way but your daily page doesn't recommend you those kind of tunes.

    Fret not, for we bring to you **:rainbow[MUSICA]!**

    Lets test it out shall we?
    """

)

mood = st.text_input("What mood are you in?")
if st.button("Get Recommendations"):
    result=get_songs_by_mood(mood)
    st.write(result)