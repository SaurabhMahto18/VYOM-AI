import tkinter as tk
import math


class VYOMWindow:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("VYOM — Virtual Yielding Omni Mind")
        self.root.geometry("1100x700")
        self.root.configure(bg="#050A12")
        self.root.resizable(False, False)

        self.state = "idle"
        self.animation_time = 0

        self.canvas = tk.Canvas(
            self.root,
            width=1100,
            height=700,
            bg="#050A12",
            highlightthickness=0
        )

        self.canvas.pack()

        self.create_background()
        self.create_header()
        self.create_core()
        self.create_status()
        self.create_waveform()
        self.create_footer()

        self.animate()

    # --------------------------------------------------
    # BACKGROUND
    # --------------------------------------------------

    def create_background(self):

        # Top subtle line
        self.canvas.create_line(
            40,
            105,
            1060,
            105,
            fill="#14263A",
            width=1
        )

        # Side panels
        self.canvas.create_rectangle(
            35,
            130,
            260,
            550,
            outline="#102033",
            width=1
        )

        self.canvas.create_rectangle(
            840,
            130,
            1065,
            550,
            outline="#102033",
            width=1
        )

        # Left information
        self.canvas.create_text(
            65,
            160,
            text="SYSTEM",
            anchor="w",
            fill="#5D7894",
            font=("Segoe UI", 9, "bold")
        )

        self.canvas.create_text(
            65,
            195,
            text="VYOM CORE",
            anchor="w",
            fill="#DCEBFA",
            font=("Segoe UI", 11, "bold")
        )

        self.canvas.create_text(
            65,
            225,
            text="AI ENGINE",
            anchor="w",
            fill="#6E8AA5",
            font=("Segoe UI", 9)
        )

        self.canvas.create_text(
            65,
            255,
            text="VOICE SYSTEM",
            anchor="w",
            fill="#6E8AA5",
            font=("Segoe UI", 9)
        )

        self.canvas.create_text(
            65,
            285,
            text="MEMORY",
            anchor="w",
            fill="#6E8AA5",
            font=("Segoe UI", 9)
        )

        # Right information
        self.canvas.create_text(
            870,
            160,
            text="STATUS",
            anchor="w",
            fill="#5D7894",
            font=("Segoe UI", 9, "bold")
        )

        self.canvas.create_text(
            870,
            195,
            text="MICROPHONE",
            anchor="w",
            fill="#6E8AA5",
            font=("Segoe UI", 9)
        )

        self.canvas.create_text(
            870,
            225,
            text="ONLINE",
            anchor="w",
            fill="#DCEBFA",
            font=("Segoe UI", 11, "bold")
        )

        self.canvas.create_text(
            870,
            270,
            text="PRIVACY",
            anchor="w",
            fill="#6E8AA5",
            font=("Segoe UI", 9)
        )

        self.canvas.create_text(
            870,
            300,
            text="LOCAL FIRST",
            anchor="w",
            fill="#DCEBFA",
            font=("Segoe UI", 11, "bold")
        )

    # --------------------------------------------------
    # HEADER
    # --------------------------------------------------

    def create_header(self):

        self.canvas.create_text(
            55,
            45,
            text="VYOM",
            anchor="w",
            fill="#EAF6FF",
            font=("Segoe UI", 27, "bold")
        )

        self.canvas.create_text(
            55,
            78,
            text="VIRTUAL YIELDING OMNI MIND",
            anchor="w",
            fill="#5F7C98",
            font=("Segoe UI", 9)
        )

        # Online indicator
        self.canvas.create_oval(
            995,
            43,
            1005,
            53,
            fill="#00AEEF",
            outline=""
        )

        self.canvas.create_text(
            1018,
            48,
            text="ONLINE",
            anchor="w",
            fill="#8FB2CC",
            font=("Segoe UI", 9, "bold")
        )

    # --------------------------------------------------
    # AI CORE
    # --------------------------------------------------

    def create_core(self):

        self.core_center_x = 550
        self.core_center_y = 315

        # Outer rings
        self.ring1 = self.canvas.create_oval(
            390,
            155,
            710,
            475,
            outline="#0E334C",
            width=2
        )

        self.ring2 = self.canvas.create_oval(
            420,
            185,
            680,
            445,
            outline="#0A2538",
            width=1
        )

        self.ring3 = self.canvas.create_oval(
            450,
            215,
            650,
            415,
            outline="#123B55",
            width=1
        )

        # Main core
        self.core = self.canvas.create_oval(
            480,
            245,
            620,
            385,
            outline="#00AEEF",
            width=3
        )

        self.inner_core = self.canvas.create_oval(
            505,
            270,
            595,
            360,
            outline="#55D9FF",
            width=2
        )

        # Center
        self.center = self.canvas.create_oval(
            530,
            295,
            570,
            335,
            outline="#B8F2FF",
            width=2
        )

        self.canvas.create_text(
            550,
            410,
            text="VYOM CORE",
            fill="#66849E",
            font=("Segoe UI", 9, "bold")
        )

    # --------------------------------------------------
    # STATUS
    # --------------------------------------------------

    def create_status(self):

        self.status_text = self.canvas.create_text(
            550,
            500,
            text="READY",
            fill="#DDF7FF",
            font=("Segoe UI", 15, "bold")
        )

        self.user_text = self.canvas.create_text(
            550,
            530,
            text="Waiting for your command...",
            fill="#607C96",
            font=("Segoe UI", 10),
            width=650
        )

    # --------------------------------------------------
    # WAVEFORM
    # --------------------------------------------------

    def create_waveform(self):

        self.wave_lines = []

        start_x = 440

        for i in range(23):

            x = start_x + (i * 10)

            line = self.canvas.create_line(
                x,
                590,
                x,
                590,
                fill="#00AEEF",
                width=2
            )

            self.wave_lines.append(line)

    # --------------------------------------------------
    # FOOTER
    # --------------------------------------------------

    def create_footer(self):

        self.canvas.create_text(
            550,
            650,
            text="THINK  •  LEARN  •  ACT",
            fill="#314A61",
            font=("Segoe UI", 9, "bold")
        )

    # --------------------------------------------------
    # STATE
    # --------------------------------------------------

    def set_state(self, state):

        self.state = state

        states = {
            "idle": "READY",
            "listening": "LISTENING",
            "thinking": "THINKING",
            "speaking": "SPEAKING",
            "error": "ERROR"
        }

        self.canvas.itemconfig(
            self.status_text,
            text=states.get(state, "READY")
        )

    # --------------------------------------------------
    # USER TEXT
    # --------------------------------------------------

    def set_user_text(self, text):

        self.canvas.itemconfig(
            self.user_text,
            text=f'"{text}"'
        )

    # --------------------------------------------------
    # ANIMATION
    # --------------------------------------------------

    def animate(self):

        self.animation_time += 0.08

        # ---------------------------------------------
        # Core animation
        # ---------------------------------------------

        if self.state == "idle":

            pulse = math.sin(
                self.animation_time
            ) * 4

            speed = 1

        elif self.state == "listening":

            pulse = math.sin(
                self.animation_time * 5
            ) * 13

            speed = 4

        elif self.state == "thinking":

            pulse = math.sin(
                self.animation_time * 8
            ) * 8

            speed = 7

        elif self.state == "speaking":

            pulse = math.sin(
                self.animation_time * 11
            ) * 17

            speed = 10

        else:

            pulse = 0
            speed = 1

        # Main core
        self.canvas.coords(
            self.core,
            480 - pulse,
            245 - pulse,
            620 + pulse,
            385 + pulse
        )

        # Inner core
        inner = pulse * 0.5

        self.canvas.coords(
            self.inner_core,
            505 - inner,
            270 - inner,
            595 + inner,
            360 + inner
        )

        # ---------------------------------------------
        # Rotating ring effect
        # ---------------------------------------------

        ring_offset = math.sin(
            self.animation_time * speed
        ) * 5

        self.canvas.coords(
            self.ring3,
            450 - ring_offset,
            215 - ring_offset,
            650 + ring_offset,
            415 + ring_offset
        )

        # ---------------------------------------------
        # Waveform
        # ---------------------------------------------

        for i, line in enumerate(self.wave_lines):

            if self.state == "idle":

                height = 3

            else:

                height = (
                    abs(
                        math.sin(
                            self.animation_time * speed
                            + i * 0.5
                        )
                    ) * 25
                )

            x = 440 + i * 10

            self.canvas.coords(
                line,
                x,
                590 - height,
                x,
                590 + height
            )

        self.root.after(
            30,
            self.animate
        )

    # --------------------------------------------------
    # RUN
    # --------------------------------------------------

    def run(self):

        self.root.mainloop()