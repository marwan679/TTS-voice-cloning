## 🎤 Clone My Voice: Coqui TTS & XTTS v2

Ever wanted to turn text into speech using a specific voice? This project does exactly that\! It's a fun, straightforward demonstration of **voice cloning** using the powerful **Coqui TTS** library, specifically tapping into the **XTTS v2** model. Think of it as teaching an AI to speak in your (or any) voice\!

### 🛠️ What You Need to Get Started

Before you run the script, make sure your Python environment has the right ingredients. These are listed in `requirements.txt`:

```
torch==2.1.0
torchaudio==2.1.0
TTS==0.22.0
numpy==1.22.0
scipy==1.11.2
scikit-learn==1.3.0
librosa==0.10.0
pandas==1.5.3
soundfile
```

You can set everything up with one simple command:

```bash
pip install -r requirements.txt
```

#### Project Contents

You'll find these files doing the heavy lifting:

  * `Voice_Cloning.py`: The heart of the operation—this Python script handles the cloning.
  * `requirements.txt`: The shopping list for Python packages.
  * `input.wav`: The crucial **reference audio**. This is the voice the AI will learn from and try to mimic.
  * `output.wav`: The final result\! The text converted to speech, spoken in the cloned voice.

### 🧠 Behind the Scenes: How the Cloning Works

The `Voice_Cloning.py` script is quite smart. Here's what it does step-by-step:

1.  **Prep & Setup**: It loads all the necessary Coqui TTS and PyTorch tools. It even checks your system to see if you have a **GPU (`cuda`)**—if so, it uses it for speed; if not, it happily runs on your **CPU**.
2.  **Model Mastery**: It loads the **XTTS v2 model**, which is trained to handle multiple languages and voice types.
3.  **The Cloning Magic**: It runs the main function, telling the model three things:
      * **What to say**: `"Hello, this is a voice cloning test. Nice to meet you!"`.
      * **Whose voice to use**: The voice heard in **`input.wav`**.
      * **What language it is**: **English (`en`)**.
4.  **Save the Output**: The synthesized speech is saved directly into a new file, **`output.wav`**.

### 🎧 Listen to the Difference

#### The Reference Voice (`input.wav`)

This is the original audio, containing six short, distinct phrases, which the model uses to learn the tone, rhythm, and texture of the speaker's voice:

> "The stale smell of old beer lingers. It takes heat to bring out the odor. A cold dip restores health and zest. A salt pickle tastes fine with ham. Tacos al pastor are my favorite. A zestful food is the hot cross bun."

#### The Cloned Result (`output.wav`)

This is the AI speaking the new text in the voice it just learned:

> "Hello, this is a voice cloning test. Nice to meet you\!"
