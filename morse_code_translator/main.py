from morse_dict import MORSE_CODE_DICT 
import streamlit as st

MORSE_CODE_DICT_REVERSE = {v: k for k, v in MORSE_CODE_DICT.items()}


def encode_to_morse(text: str) -> str:
    return ' '.join(MORSE_CODE_DICT.get(ch.upper(), ch) for ch in text)

# Function to decode Morse to text
def decode_from_morse(morse_code: str) -> str:
    words = morse_code.split(' / ')  # Split by slash for words
    decoded_text = []
    for word in words:
        decoded_text.append(''.join(MORSE_CODE_DICT_REVERSE.get(symbol, symbol) for symbol in word.split()))
    return ' '.join(decoded_text)

# -------------------- Streamlit UI --------------------
st.title("🔡 Morse Code Translator")
st.markdown("Convert text ↔️ Morse code interactively")

# User mode selection
mode = st.radio("Choose mode:", ["Encode (Text ➡️ Morse)", "Decode (Morse ➡️ Text)"])

if mode == "Encode (Text ➡️ Morse)":
    text_input = st.text_area("Enter text:")
    if st.button("Convert to Morse"):
        result = encode_to_morse(text_input)
        st.success(result)

elif mode == "Decode (Morse ➡️ Text)":
    morse_input = st.text_area("Enter Morse Code (use '/' for spaces):")
    if st.button("Convert to Text"):
        result = decode_from_morse(morse_input)
        st.success(result)