import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Be my valentine", page_icon="❤️", layout="centered")

# Custom CSS for styling
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

    /* Styling the native Streamlit button to look pixelated */
    .stButton>button {
        font-family: 'Press Start 2P', cursive !important;
        background-color: #00aa00 !important;
        color: white !important;
        border: 4px solid #fff !important;
        box-shadow: 4px 4px 0px #555 !important;
        height: 60px;
        font-size: 14px !important;
    }
    </style>
    <div class="pixel-text">
        <p>will you be my valentine?</p>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="img-container">', unsafe_allow_html=True)
# Ensure heart.png is in the same directory or use a URL
st.image("heart.png", width=300) 
st.markdown('</div>', unsafe_allow_html=True)

# The HTML component now ONLY contains the "NO" button logic
no_button_only_html = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    
    #game-container {
        height: 300px;
        width: 100%;
        position: relative;
        background-color: #000;
        border: 4px solid #fff;
        image-rendering: pixelated;
        overflow: hidden;
    }
    
    .pixel-btn-no {
        font-family: 'Press Start 2P', cursive;
        padding: 10px 20px;
        border: 4px solid #fff;
        color: white;
        cursor: pointer;
        font-size: 14px;
        text-transform: uppercase;
        box-shadow: 4px 4px 0px #555;
        background-color: #aa0000;
        position: absolute;
        left: 50%;
        top: 40%;
        transition: 0.1s ease-out;
    }
</style>

<div id="game-container">
    <button id="noBtn" class="pixel-btn-no" onmouseover="moveNo()">NO</button>
</div>

<script>
    function moveNo() {
        const btn = document.getElementById('noBtn');
        const container = document.getElementById('game-container');
        
        const maxX = container.clientWidth - btn.clientWidth - 20;
        const maxY = container.clientHeight - btn.clientHeight - 20;
        
        const newX = Math.floor(Math.random() * maxX);
        const newY = Math.floor(Math.random() * maxY);
        
        btn.style.left = newX + 'px';
        btn.style.top = newY + 'px';
    }
</script>
"""

# Logic Handling
if st.query_params.get("accepted") == "true":
    st.balloons()
    st.markdown("<h2 class='pixel-text'>Yay! BEST DECISION EVER! ❤️</h2>", unsafe_allow_html=True)
    if st.button("Start Over"):
        st.query_params["accepted"] = "false"
        st.rerun()
else:
    # Creating columns for the buttons
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Native Streamlit button (The "Yes" that actually works)
        if st.button("YES", use_container_width=True):
            st.query_params["accepted"] = "true"
            st.rerun()
            
    with col2:
        # The elusive "No" button
        components.html(no_button_only_html, height=350)