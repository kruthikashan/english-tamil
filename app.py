import streamlit as st
from googletrans import Translator

def translate_text(text, target_language='ta'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def main():
    st.title("English to Tamil Translator")

    # Input text box
    input_text = st.text_area("Enter English Text:", "Hello, how are you?")

    if st.button("Translate"):
        # Perform translation
        translated_text = translate_text(input_text)
        
        # Display translated text
        st.success(f"Translated Text (Tamil): {translated_text}")

if __name__ == "__main__":
    main()
