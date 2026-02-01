import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Be my valentine", page_icon="❤️", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    
    .pixel-text {
        font-family: 'Press Start 2P', cursive;
        color: #ff4b4b;
        text-align: center;
        line-height: 1.6;
    }
    </style>
    <div class="pixel-text">
        <h1>LEVEL 99 ROMANCE</h1>
        <p>will you be my valentine?</p>
    </div>
""", unsafe_allow_html=True)

# runaway button
st.image("heart.png", width=300)

proposal_html = """
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
    }
    
    #yesBtn { background-color: #00aa00; position: absolute; left: 20%; top: 40%; }
    #noBtn { background-color: #aa0000; position: absolute; left: 60%; top: 40%; transition: 0.1s ease-out; }
    
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
        
        // Ensure it stays within the black box
        const maxX = container.clientWidth - btn.clientWidth - 20;
        const maxY = container.clientHeight - btn.clientHeight - 20;
        
        const newX = Math.floor(Math.random() * maxX);
        const newY = Math.floor(Math.random() * maxY);
        
        btn.style.left = newX + 'px';
        btn.style.top = newY + 'px';
    }

    function celebrate() {
        window.parent.postMessage({type: 'streamlit:setComponentValue', value: 'YES'}, '*');
    }
</script>
"""

response = components.html(proposal_html, height=350)

if response == "YES":
    st.balloons()
    st.markdown("<h2 class='pixel-text'>PLAYER 1 JOINED THE GAME! ❤️</h2>", unsafe_allow_html=True)
    