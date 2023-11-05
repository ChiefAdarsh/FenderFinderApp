import streamlit as st

# Display the HTML content
st.markdown("<div>Teachable Machine Image Model</div>", unsafe_allow_html=True)

# Create a button to start the webcam
if st.button("Start"):
    st.markdown("<div id='webcam-container'></div>", unsafe_allow_html=True)
    st.markdown("<div id='label-container'></div>", unsafe_allow_html=True)

    # Include JavaScript code
    st.write("""
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/image@latest/dist/teachablemachine-image.min.js"></script>
    <script type="text/javascript">
        // ... (The rest of your JavaScript code)
    </script>
    """, unsafe_allow_html=True)