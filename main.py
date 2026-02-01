import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Be my valentine", page_icon="❤️", layout="centered")

# 1. Pixel Art CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    .pixel-text { font-family: 'Press Start 2P', cursive; color: #ff4b4b; text-align: center; }
    .img-container { display: flex; justify-content: center; padding: 20px; }
    </style>
    <div class="pixel-text"><p>will you be my valentine?</p></div>
""", unsafe_allow_html=True)

st.markdown('<div class="img-container">', unsafe_allow_html=True)
st.image("heart.png", width=300)
st.markdown('</div>', unsafe_allow_html=True)

# 2. The Bridge: HTML + JavaScript
# We use a trick where the iframe sends a message to the parent window
proposal_html = """
<div id="game-container">
    <button id="yesBtn" class="pixel-btn" onclick="sendYes()">YES</button>
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
        position: absolute; font-size: 14px;
    }
    #yesBtn { background: #00aa00; left: 20%; top: 40%; }
    #noBtn { background: #aa0000; left: 60%; top: 40%; transition: 0.1s; }
</style>

<script>
    function moveNo() {
        const btn = document.getElementById('noBtn');
        const container = document.getElementById('game-container');
        btn.style.left = Math.random() * (container.clientWidth - btn.clientWidth - 20) + 'px';
        btn.style.top = Math.random() * (container.clientHeight - btn.clientHeight - 20) + 'px';
    }

    function sendYes() {
        // This sends a signal back to Streamlit without needing a URL change
        window.parent.postMessage({
            isStreamlitMessage: true,
            type: "streamlit:setComponentValue",
            value: "clicked_yes"
        }, "*");
    }
</script>
"""

# 3. Logic: Capture the message from the HTML
# We use the return value of components.html to see if the button was clicked
response = components.html(proposal_html, height=350)

# If the iframe sends the message, the 'response' variable updates
# Note: In standard Streamlit, we check query params or state for persistence
if st.query_params.get("accepted") == "true":
    st.balloons()
    st.markdown("<h2 class='pixel-text'>Yay! BEST DECISION EVER! ❤️</h2>", unsafe_allow_html=True)
    if st.button("Restart"):
        st.query_params.clear()
        st.rerun()

# This script block forces the refresh if the JS message is received
st.markdown(f"""
    <script>
    window.addEventListener('message', (event) => {{
        if (event.data.value === 'clicked_yes') {{
            const url = window.location.href.split('?')[0];
            window.location.href = url + "?accepted=true";
        }}
    }});
    </script>
""", unsafe_allow_html=True)