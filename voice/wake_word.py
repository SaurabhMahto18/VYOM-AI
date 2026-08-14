import time

import numpy as np
import pyaudio
from openwakeword.model import Model


SAMPLE_RATE = 16000
CHUNK_SIZE = 1280

WAKE_THRESHOLD = 0.5


def wait_for_wake_word():

    print("\n🔵 VYOM is in standby.")
    print("🎤 Say: Hello V")

    model = Model(
        wakeword_models=[
            "models/hello_v.onnx"
        ]
    )

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=SAMPLE_RATE,
        input=True,
        frames_per_buffer=CHUNK_SIZE
    )

    try:

        while True:

            audio_data = stream.read(
                CHUNK_SIZE,
                exception_on_overflow=False
            )

            audio_frame = np.frombuffer(
                audio_data,
                dtype=np.int16
            )

            prediction = model.predict(
                audio_frame
            )

            score = prediction.get(
                "hello_v",
                0
            )

            if score >= WAKE_THRESHOLD:

                print("\n🟢 Hello V detected!")

                return True

            time.sleep(0.01)

    finally:

        stream.stop_stream()
        stream.close()
        audio.terminate()