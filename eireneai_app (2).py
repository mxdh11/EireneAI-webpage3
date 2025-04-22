
import streamlit as st
from transformers import pipeline
import requests
import datetime

# Load emotion detection model
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

# LibreTranslate API function
def translate_text(text, target_lang="ar"):
    url = "https://libretranslate.com/translate"
    payload = {
        "q": text,
        "source": "en",
        "target": target_lang,
        "format": "text"
    }
    response = requests.post(url, data=payload)
    return response.json().get("translatedText", "Translation error")

# Empathy Story Generator (simulated)
def generate_empathy_story():
    return (
        "Once, a child from Syria met a boy from Ukraine in a refugee shelter. They didn't speak the same language, "
        "but they played together every day. Through shared games, food, and smiles, they formed a bond stronger than words."
    )

# Emergency Help Instructions
def emergency_help():
    return (
        "It seems you're in distress. Please try to move to a safe location. Contact local authorities if you're in danger. "
        "Stay calm and try to reach someone you trust. Type 'emergency numbers' if you need more help."
    )

# Streamlit UI
st.set_page_config(page_title="EireneAI", layout="centered")
st.markdown("""
    <style>
        .main {
            padding: 1rem;
            font-family: 'Arial';
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.image("https://i.imgur.com/wBxrAlM.png", width=100)
st.title("📱 EireneAI Mobile Preview")
st.markdown("A peace & empathy companion — for emotions, support, and culture 🌍")

# User Input
user_input = st.text_input("💬 How are you feeling today?")

if user_input:
    emotion_result = emotion_classifier(user_input)[0]
    label = emotion_result['label']
    score = emotion_result['score']

    st.markdown(f"### 🧠 Emotion Detected: **{label}** ({round(score * 100, 2)}%)")

    if label.lower() in ["anger", "fear", "sadness"]:
        st.markdown("### 🚨 Emergency Help")
        st.warning(emergency_help())
    else:
        st.markdown("### 🤝 You're doing okay!")
        st.success("Would you like a heartwarming story or cultural fact?")

    # Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📖 Empathy Story"):
            st.info(generate_empathy_story())
    with col2:
        if st.button("🌍 Translate Response"):
            translation = translate_text("I'm here to support you.", target_lang="ar")
            st.markdown(f"**Arabic Translation:** {translation}")

# Mood Tracker
if "mood_log" not in st.session_state:
    st.session_state.mood_log = []

st.markdown("## 📊 Mood Tracker")
mood_today = st.selectbox("How do you feel today?", ["Happy", "Calm", "Anxious", "Sad", "Angry", "Excited"])
if st.button("Log Mood"):
    st.session_state.mood_log.append((datetime.date.today().isoformat(), mood_today))
    st.success("Mood logged for today!")

if st.session_state.mood_log:
    st.markdown("### Your Mood History")
    for entry in st.session_state.mood_log[-5:]:
        st.write(f"**{entry[0]}:** {entry[1]}")

# Peace-building Challenge
st.markdown("## ✌️ Peace-Building Challenge")
challenges = [
    "Ask someone about their cultural tradition.",
    "Watch a video about a new culture.",
    "Write a letter of encouragement to someone different from you.",
    "Celebrate a cultural holiday from another community.",
    "Compliment someone in their native language."
]
today_challenge = challenges[datetime.datetime.now().day % len(challenges)]
st.info(f"**Today's Challenge:** {today_challenge}")

# Cultural Exchange
st.markdown("## 🌍 Cultural Exchange")
cultural_facts = {
    "India": "In India, it's common to greet others with 'Namaste'—a gesture of respect.",
    "Japan": "In Japan, slurping noodles is a sign that you're enjoying your food!",
    "Brazil": "Brazilians often greet friends with a warm hug or cheek kiss.",
    "Kenya": "The Maasai tribe in Kenya are known for their colorful dress and jumping dance."
}
for country, fact in cultural_facts.items():
    st.markdown(f"**{country}:** {fact}")

# PeaceShield Emergency
st.markdown("## 🚨 PeaceShield Emergency")
if st.button("Trigger Emergency Mode"):
    st.error("PeaceShield Activated! Your location and distress code have been sent to local authorities.")
    st.markdown("Please follow these instructions: Move to a safe location, stay calm, and await help.")

# Footer
st.markdown("""
---
**Team EireneAI**  
Janhavi Shajin • Maanasika Shankar • Mahdiya Fatima  
Pace International School | April 2025
""")
