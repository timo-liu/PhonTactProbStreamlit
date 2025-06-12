from PhonTactProb import PhonTactProb
import streamlit as st
import pandas as pd

st.title("English Phonotactic Probability Calculator")
user_input = st.text_input("Enter your input ipa:")

with st.expander("ℹ️ Instructions / Access Guide"):
    st.markdown("""
    **How to use this app:**

    1. Enter a word or space segmented phrase in **IPA** into the text box.
    2. Click the **"Calculate probabilities"** button.
    3. View the resulting **phoneme** and **biphone** probability tables.
    4. You'll have most luck with transciptions from https://tophonetics.com/, American, removing stress markers
    This tool only handles phonemes, and is built for standard American English.

    **Example Input:** `fənɛtɪk`

    **Notes:**
    - Each phoneme must be in IPA format.
    - The app expects space-separated IPA for multi-word input (e.g., `kæt dɔg`).
    
    Many thanks to ChatGPT for liberating me from front-end work (first they came for HTML, then they came for React, then they came for bankend... yadda yadda)
    """)

# initialize instance if PhonTactProb
p = PhonTactProb()

# Placeholder for results
result_placeholder = st.empty()

# Button to trigger calculation
if st.button("Calculate probabilities"):
    if user_input:
        # Example: reverse text and pretend it's a probability
        results = p.compute_phonotactic_probability(user_input)
        for word, data in results.items():
            st.subheader(f"Results for: {word}")

            # Phonemes table
            if 'phonemes' in data:
                phoneme_df = pd.DataFrame(data['phonemes'], columns=["Phoneme", "Probability"])
                st.markdown("### Phonemes")
                st.table(phoneme_df)

            # Biphones table
            if 'biphones' in data:
                biphone_df = pd.DataFrame(data['biphones'], columns=["Biphone", "Probability"])
                st.markdown("### Biphones")
                st.table(biphone_df)
        else:
            st.warning("Please enter a word before calculating.")
    else:
        result = "Please enter some text before calculating."