import os
import wave
import pyaudio


SAMPLE_RATE = 16000
CHANNELS = 1
FORMAT = pyaudio.paInt16

DURATION = 2

OUTPUT_DIR = "wakeword_data/positive"


def record_sample(index):

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    filename = os.path.join(
        OUTPUT_DIR,
        f"hello_v_{index:03d}.wav"
    )

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=SAMPLE_RATE,
        input=True,
        frames_per_buffer=1024
    )

    print("\n🎤 Recording...")
    print("Say: HELLO V")

    frames = []

    for _ in range(
        int(SAMPLE_RATE / 1024 * DURATION)
    ):

        data = stream.read(
            1024,
            exception_on_overflow=False
        )

        frames.append(data)

    print("✅ Saved:", filename)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(filename, "wb") as wf:

        wf.setnchannels(CHANNELS)
        wf.setsampwidth(
            audio.get_sample_size(FORMAT)
        )
        wf.setframerate(SAMPLE_RATE)

        wf.writeframes(
            b"".join(frames)
        )


def main():

    print("=" * 50)
    print("       VYOM - HELLO V WAKE WORD")
    print("=" * 50)

    print("\nWe will record 30 samples.")
    print("For each sample:")
    print("Press ENTER → Say 'Hello V'")
    print("The recording lasts 2 seconds.")

    input("\nPress ENTER to start...")

    for index in range(1, 31):

        print(f"\n--- Sample {index}/30 ---")

        input("Press ENTER and say 'Hello V'...")

        record_sample(index)

    print("\n🎉 Recording complete!")
    print("Samples saved in:")
    print(OUTPUT_DIR)


if __name__ == "__main__":
    main()