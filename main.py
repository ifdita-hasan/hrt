import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Be my valentine", page_icon="❤️", layout="centered")

# Custom CSS to make the native Streamlit button look like the pixel-art one
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    
    .pixel-text {
        font-family: 'Press Start 2P', cursive;
        color: #ff4b4b;
        text-align: center;
        line-height: 1.6;
    }
    
    .img-container {
        display: flex;
        justify-content: center;
        padding: 20px;
    }

    /* Styling the Streamlit button to match the black box theme */
    div.stButton > button:first-child {
        font-family: 'Press Start 2P', cursive;
        background-color: #00aa00;
        color: white;
        border: 4px solid #fff;
        height: 300px;
        font-size: 20px;
        box-shadow: 4px 4px 0px #555;
    }
    
    div.stButton > button:hover {
        background-color: #008800;
        color: white;
        border: 4px solid #fff;
    }
    </style>
    <div class="pixel-text">
        <p>will you be my valentine?</p>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="img-container">', unsafe_allow_html=True)
st.image("heart.png", width=300)
st.markdown('</div>', unsafe_allow_html=True)

# The HTML for the "NO" button only
no_button_html = """
<div id="game-container">
    <button id="noBtn" class="pixel-btn" onmouseover="moveNo()">NO</button>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    body { background: transparent; margin: 0; }
    #game-container {
        height: 300px; width: 100%; background: #000;
        border: 4px solid #fff; position: relative; overflow: hidden;
    }
    .pixel-btn {
        font-family: 'Press Start 2P', cursive; padding: 10px 20px;
        border: 4px solid #fff; color: white; cursor: pointer;
        position: absolute; font-size: 14px; background-color: #aa0000;
        left: 40%; top: 40%; transition: 0.1s ease-out;
    }
</style>

<script>
    function moveNo() {
        const btn = document.getElementById('noBtn');
        const container = document.getElementById('game-container');
        const maxX = container.clientWidth - btn.clientWidth - 20;
        const maxY = container.clientHeight - btn.clientHeight - 20;
        btn.style.left = Math.floor(Math.random() * maxX) + 'px';
        btn.style.top = Math.floor(Math.random() * maxY) + 'px';
    }
</script>
"""

# Logic Handling
if st.query_params.get("accepted") == "true":
    st.balloons()
    st.markdown("<h2 class='pixel-text'>Yay! BEST DECISION EVER! ❤️</h2>", unsafe_allow_html=True)
    if st.button("Start Over"):
        st.query_params.clear()
        st.rerun()
else:
    # This creates the side-by-side look
    col1, col2 = st.columns(2)
    
    with col1:
        # Native button that bypasses iframe security
        if st.button("YES", use_container_width=True):
            st.query_params["accepted"] = "true"
            st.rerun()
            
    with col2:
        # HTML component for the "moving" effect
        components.html(no_button_html, height=310)