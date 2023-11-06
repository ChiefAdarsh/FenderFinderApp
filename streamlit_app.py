import streamlit as st

# Display the HTML content
st.markdown("<div>Teachable Machine Image Model</div>", unsafe_allow_html=True)

# Create a button to start the webcam
if st.button("Start"):
    st.markdown("<div id='webcam-container'></div>", unsafe_allow_html=True)
    st.markdown("<div id='label-container'></div>", unsafe_allow_html=True)

    webcam_container = st.empty()
    label_container = st.empty()

    # Include JavaScript code
    st.write("""
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/image@latest/dist/teachablemachine-image.min.js"></script>
    <script type="text/javascript">
        // ... (The rest of your JavaScript code)
    </script>
    """, unsafe_allow_html=True)

# Function to embed the HTML file in an iframe
def st_iframe(url, height=600, width=800):
    return f'<iframe src="{url}" width={width} height={height}></iframe>'

# Display Streamlit content
st.title("Streamlit Webcam App")

# Embed the HTML and JavaScript webcam application using an iframe
st.markdown("Webcam Application:")
st_iframe("webcam_app.html", height=400, width=640)
