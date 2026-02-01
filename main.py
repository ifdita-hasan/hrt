import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Be my valentine", page_icon="❤️", layout="centered")

# Custom CSS for the text and centering
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
    </style>
    <div class="pixel-text">
        <p>will you be my valentine?</p>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="img-container">', unsafe_allow_html=True)
st.image("heart.png", width=300)
st.markdown('</div>', unsafe_allow_html=True)

# Combined HTML: Both buttons inside the same container
proposal_html = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    
    body { background-color: transparent; margin: 0; padding: 0; overflow: hidden; }

    #game-container {
        height: 300px;
        width: 100%;
        position: relative;
        background-color: #000;
        border: 4px solid #fff;
        image-rendering: pixelated;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .pixel-btn {
        font-family: 'Press Start 2P', cursive;
        padding: 10px 20px;
        border: 4px solid #fff;
        color: white;
        cursor: pointer;
        font-size: 14px;
        text-transform: uppercase;
        box-shadow: 4px 4px 0px #555;
        position: absolute;
    }
    
    #yesBtn { 
        background-color: #00aa00; 
        left: 20%; 
        top: 40%; 
    }
    
    #noBtn { 
        background-color: #aa0000; 
        left: 60%; 
        top: 40%; 
        transition: 0.1s ease-out;
        z-index: 10;
    }
    
    .pixel-btn:active {
        box-shadow: 0px 0px 0px;
        transform: translate(2px, 2px);
    }
</style>

<div id="game-container">
    <button id="yesBtn" class="pixel-btn" onclick="celebrate()">YES</button>
    <button id="noBtn" class="pixel-btn" onmouseover="moveNo()">NO</button>
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

    function celebrate() {
        // This targets the main Streamlit window from inside the iframe
        const currentUrl = window.parent.location.href.split('?')[0];
        window.parent.location.href = currentUrl + "?accepted=true";
    }
</script>
"""

# Handling the response
if st.query_params.get("accepted") == "true":
    st.balloons()
    st.markdown("<h2 class='pixel-text'>Yay! BEST DECISION EVER! ❤️</h2>", unsafe_allow_html=True)
    if st.button("Reset"):
        st.query_params.clear()
        st.rerun()
else:
    components.html(proposal_html, height=350)