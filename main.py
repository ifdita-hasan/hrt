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

# 2. The Logic: Listen for the "Yes" signal from JS
if st.query_params.get("accepted") == "true":
    st.balloons()
    st.markdown("<h2 class='pixel-text'>Yay! BEST DECISION EVER! ❤️</h2>", unsafe_allow_html=True)
    if st.button("Reset"):
        st.query_params.clear()
        st.rerun()
else:
    # 3. The HTML: Both buttons in one box
    # Using window.parent.postMessage is the most reliable way to talk to Streamlit
    proposal_html = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
        #box { height: 300px; width: 100%; background: #000; border: 4px solid #fff; position: relative; overflow: hidden; }
        .btn { font-family: 'Press Start 2P', cursive; padding: 10px 20px; border: 4px solid #fff; color: white; cursor: pointer; position: absolute; }
        #yes { background: #00aa00; left: 20%; top: 40%; }
        #no { background: #aa0000; left: 60%; top: 40%; transition: 0.1s; }
    </style>

    <div id="box">
        <button id="yes" class="btn" onclick="sayYes()">YES</button>
        <button id="no" class="btn" onmouseover="moveNo()">NO</button>
    </div>

    <script>
        function moveNo() {
            const btn = document.getElementById('no');
            const box = document.getElementById('box');
            btn.style.left = Math.random() * (box.clientWidth - btn.clientWidth - 20) + 'px';
            btn.style.top = Math.random() * (box.clientHeight - btn.clientHeight - 20) + 'px';
        }

        function sayYes() {
            // This is the "magic" that works in 2026 browsers:
            // It modifies the parent URL directly via top navigation
            window.top.location.href = window.parent.location.href.split('?')[0] + "?accepted=true";
        }
    </script>
    """
    components.html(proposal_html, height=350)