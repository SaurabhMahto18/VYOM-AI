import tkinter as tk
import math


class VYOMWindow:

    def __init__(self):

        # =====================================================
        # WINDOW
        # =====================================================

        self.root = tk.Tk()

        self.root.title(
            "VYOM — Virtual Yielding Omni Mind"
        )

        self.root.geometry("1100x700")
        self.root.minsize(900, 600)

        self.root.configure(
            bg="#F7F6FA"
        )

        # =====================================================
        # COLORS
        # =====================================================

        self.BG = "#F7F6FA"
        self.WHITE = "#FFFFFF"

        self.PURPLE = "#7654F6"
        self.PURPLE_LIGHT = "#F0ECFF"
        self.PURPLE_SOFT = "#E9E4FF"

        self.TEXT = "#211F2D"
        self.MUTED = "#7A7887"

        self.BORDER = "#E5E1EC"

        self.GREEN = "#35C77A"

        # =====================================================
        # STATE
        # =====================================================

        self.state = "idle"

        self.animation = 0

        self.user_message = (
            "Ask VYOM anything..."
        )

        self.ai_message = (
            "Hello! I'm VYOM.\n\n"
            "I'm ready to listen."
        )

        # =====================================================
        # BUILD
        # =====================================================

        self.build_ui()

        # Start animation
        self.animate()

    # =========================================================
    # BUILD UI
    # =========================================================

    def build_ui(self):

        # -----------------------------------------------------
        # MAIN CONTAINER
        # -----------------------------------------------------

        self.main = tk.Frame(
            self.root,
            bg=self.BG
        )

        self.main.pack(
            fill="both",
            expand=True,
            padx=24,
            pady=24
        )

        # -----------------------------------------------------
        # HEADER
        # -----------------------------------------------------

        self.create_header()

        # -----------------------------------------------------
        # MAIN BODY
        # -----------------------------------------------------

        self.body = tk.Frame(
            self.main,
            bg=self.BG
        )

        self.body.pack(
            fill="both",
            expand=True,
            pady=(20, 0)
        )

        # Left / Core
        self.create_core_panel()

        # Right / Conversation
        self.create_conversation_panel()

        # -----------------------------------------------------
        # BOTTOM INPUT
        # -----------------------------------------------------

        self.create_input_bar()

    # =========================================================
    # HEADER
    # =========================================================

    def create_header(self):

        header = tk.Frame(
            self.main,
            bg=self.WHITE,
            height=70,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        # -----------------------------------------------------
        # LEFT HEADER
        # -----------------------------------------------------

        left = tk.Frame(
            header,
            bg=self.WHITE
        )

        left.pack(
            side="left",
            fill="y",
            padx=18
        )

        # Logo
        logo = tk.Canvas(
            left,
            width=42,
            height=42,
            bg=self.WHITE,
            highlightthickness=0
        )

        logo.pack(
            side="left",
            pady=13
        )

        logo.create_oval(
            3,
            3,
            39,
            39,
            fill=self.PURPLE,
            outline=""
        )

        logo.create_text(
            21,
            21,
            text="V",
            fill="white",
            font=(
                "Segoe UI",
                17,
                "bold"
            )
        )

        # Title container
        title_frame = tk.Frame(
            left,
            bg=self.WHITE
        )

        title_frame.pack(
            side="left",
            padx=10
        )

        tk.Label(
            title_frame,
            text="VYOM",
            bg=self.WHITE,
            fg=self.TEXT,
            font=(
                "Segoe UI",
                16,
                "bold"
            )
        ).pack(
            anchor="w"
        )

        tk.Label(
            title_frame,
            text="Virtual Yielding Omni Mind",
            bg=self.WHITE,
            fg=self.MUTED,
            font=(
                "Segoe UI",
                8
            )
        ).pack(
            anchor="w"
        )

        # -----------------------------------------------------
        # RIGHT HEADER
        # -----------------------------------------------------

        status_container = tk.Frame(
            header,
            bg="#F1FFF7"
        )

        status_container.pack(
            side="right",
            padx=18,
            pady=15
        )

        tk.Label(
            status_container,
            text="●",
            bg="#F1FFF7",
            fg=self.GREEN,
            font=(
                "Segoe UI",
                10
            )
        ).pack(
            side="left",
            padx=(10, 4)
        )

        tk.Label(
            status_container,
            text="ONLINE",
            bg="#F1FFF7",
            fg="#23794C",
            font=(
                "Segoe UI",
                9,
                "bold"
            )
        ).pack(
            side="left",
            padx=(0, 10)
        )

    # =========================================================
    # CORE PANEL
    # =========================================================

    def create_core_panel(self):

        self.core_panel = tk.Frame(
            self.body,
            bg=self.WHITE,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )

        self.core_panel.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        # -----------------------------------------------------
        # CORE CANVAS
        # -----------------------------------------------------

        self.core_canvas = tk.Canvas(
            self.core_panel,
            bg=self.WHITE,
            highlightthickness=0
        )

        self.core_canvas.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        # -----------------------------------------------------
        # STATE
        # -----------------------------------------------------

        self.state_label = tk.Label(
            self.core_panel,
            text="LISTENING",
            bg=self.WHITE,
            fg=self.PURPLE,
            font=(
                "Segoe UI",
                17,
                "bold"
            )
        )

        self.state_label.pack(
            pady=(0, 3)
        )

        # -----------------------------------------------------
        # DETAIL
        # -----------------------------------------------------

        self.detail_label = tk.Label(
            self.core_panel,
            text="Waiting for your command...",
            bg=self.WHITE,
            fg=self.MUTED,
            font=(
                "Segoe UI",
                10
            )
        )

        self.detail_label.pack()

        # -----------------------------------------------------
        # WAVEFORM
        # -----------------------------------------------------

        self.wave_canvas = tk.Canvas(
            self.core_panel,
            height=60,
            bg=self.WHITE,
            highlightthickness=0
        )

        self.wave_canvas.pack(
            fill="x",
            padx=80,
            pady=10
        )

        # -----------------------------------------------------
        # PHILOSOPHY
        # -----------------------------------------------------

        tk.Label(
            self.core_panel,
            text="THINK  •  LEARN  •  ACT",
            bg=self.WHITE,
            fg="#777387",
            font=(
                "Segoe UI",
                9,
                "bold"
            )
        ).pack(
            pady=(0, 15)
        )

    # =========================================================
    # CONVERSATION PANEL
    # =========================================================

    def create_conversation_panel(self):

        self.conversation_panel = tk.Frame(
            self.body,
            bg=self.WHITE,
            width=390,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )

        self.conversation_panel.pack(
            side="right",
            fill="y"
        )

        self.conversation_panel.pack_propagate(
            False
        )

        # -----------------------------------------------------
        # USER MESSAGE
        # -----------------------------------------------------

        self.user_box = tk.Frame(
            self.conversation_panel,
            bg=self.PURPLE_LIGHT
        )

        self.user_box.pack(
            fill="x",
            padx=20,
            pady=(20, 12)
        )

        self.user_text = tk.Label(
            self.user_box,
            text=self.user_message,
            bg=self.PURPLE_LIGHT,
            fg=self.TEXT,
            font=(
                "Segoe UI",
                10
            ),
            justify="left",
            anchor="w",
            wraplength=320
        )

        self.user_text.pack(
            fill="x",
            padx=15,
            pady=14
        )

        # -----------------------------------------------------
        # VYOM TITLE
        # -----------------------------------------------------

        vyom_header = tk.Frame(
            self.conversation_panel,
            bg=self.WHITE
        )

        vyom_header.pack(
            fill="x",
            padx=22,
            pady=(8, 8)
        )

        tk.Label(
            vyom_header,
            text="●",
            bg=self.WHITE,
            fg=self.PURPLE,
            font=(
                "Segoe UI",
                10,
                "bold"
            )
        ).pack(
            side="left"
        )

        tk.Label(
            vyom_header,
            text=" VYOM",
            bg=self.WHITE,
            fg=self.PURPLE,
            font=(
                "Segoe UI",
                10,
                "bold"
            )
        ).pack(
            side="left"
        )

        # -----------------------------------------------------
        # AI RESPONSE
        # -----------------------------------------------------

        self.response_box = tk.Frame(
            self.conversation_panel,
            bg=self.WHITE
        )

        self.response_box.pack(
            fill="both",
            expand=True,
            padx=22
        )

        self.response_text = tk.Label(
            self.response_box,
            text=self.ai_message,
            bg=self.WHITE,
            fg=self.TEXT,
            font=(
                "Segoe UI",
                11
            ),
            justify="left",
            anchor="nw",
            wraplength=330
        )

        self.response_text.pack(
            fill="both",
            expand=True
        )

    # =========================================================
    # INPUT BAR
    # =========================================================

    def create_input_bar(self):

        input_outer = tk.Frame(
            self.main,
            bg=self.WHITE,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )

        input_outer.pack(
            fill="x",
            pady=(14, 0)
        )

        # -----------------------------------------------------
        # PLACEHOLDER
        # -----------------------------------------------------

        tk.Label(
            input_outer,
            text="Ask anything...",
            bg=self.WHITE,
            fg="#898696",
            font=(
                "Segoe UI",
                10
            )
        ).pack(
            side="left",
            padx=18,
            pady=13
        )

        # -----------------------------------------------------
        # MIC BUTTON
        # -----------------------------------------------------

        mic = tk.Label(
            input_outer,
            text="🎤",
            bg="#F6F4FB",
            fg=self.PURPLE,
            font=(
                "Segoe UI",
                13
            )
        )

        mic.pack(
            side="right",
            padx=(5, 8),
            pady=6,
            ipadx=7,
            ipady=5
        )

        # -----------------------------------------------------
        # VOICE WAVE BUTTON
        # -----------------------------------------------------

        voice_button = tk.Label(
            input_outer,
            text="▮▮▮",
            bg=self.PURPLE,
            fg="white",
            font=(
                "Segoe UI",
                12,
                "bold"
            )
        )

        voice_button.pack(
            side="right",
            padx=6,
            pady=6,
            ipadx=10,
            ipady=6
        )

    # =========================================================
    # SET STATE
    # =========================================================

    def set_state(self, state):

        self.state = state

        states = {

            "idle": (
                "LISTENING",
                "Waiting for your command...",
                self.PURPLE
            ),

            "listening": (
                "LISTENING",
                "I'm listening to you...",
                self.PURPLE
            ),

            "thinking": (
                "THINKING",
                "Processing your request...",
                "#8B6CFF"
            ),

            "speaking": (
                "SPEAKING",
                "VYOM is responding...",
                "#5C8EFF"
            ),

            "error": (
                "ERROR",
                "Something went wrong.",
                "#E05252"
            )
        }

        title, detail, color = states.get(
            state,
            states["idle"]
        )

        self.state_label.config(
            text=title,
            fg=color
        )

        self.detail_label.config(
            text=detail
        )

    # =========================================================
    # SET USER MESSAGE
    # =========================================================

    def set_user_text(self, text):

        self.user_message = text

        self.user_text.config(
            text=text
        )

    # =========================================================
    # SET AI RESPONSE
    # =========================================================

    def set_response(self, text):

        self.ai_message = text

        self.response_text.config(
            text=text
        )

    # =========================================================
    # ORB
    # =========================================================

    def draw_orb(self):

        self.core_canvas.delete(
            "all"
        )

        width = self.core_canvas.winfo_width()
        height = self.core_canvas.winfo_height()

        if width <= 0 or height <= 0:
            return

        center_x = width // 2
        center_y = height // 2

        # -----------------------------------------------------
        # Animation
        # -----------------------------------------------------

        pulse = math.sin(
            self.animation * 0.08
        )

        # -----------------------------------------------------
        # Outer rings
        # -----------------------------------------------------

        rings = [
            145,
            120,
            95,
            72
        ]

        for radius in rings:

            radius += pulse * 4

            self.core_canvas.create_oval(
                center_x - radius,
                center_y - radius,
                center_x + radius,
                center_y + radius,
                outline=self.PURPLE_SOFT,
                width=1
            )

        # -----------------------------------------------------
        # Glow circles
        # -----------------------------------------------------

        for radius in [
            65,
            57,
            49
        ]:

            self.core_canvas.create_oval(
                center_x - radius,
                center_y - radius,
                center_x + radius,
                center_y + radius,
                fill="#F1EDFF",
                outline=""
            )

        # -----------------------------------------------------
        # Main Orb
        # -----------------------------------------------------

        self.core_canvas.create_oval(
            center_x - 40,
            center_y - 40,
            center_x + 40,
            center_y + 40,
            fill=self.PURPLE,
            outline=""
        )

        # -----------------------------------------------------
        # V
        # -----------------------------------------------------

        self.core_canvas.create_text(
            center_x,
            center_y,
            text="V",
            fill="white",
            font=(
                "Segoe UI",
                25,
                "bold"
            )
        )

        # -----------------------------------------------------
        # CORE LABEL
        # -----------------------------------------------------

        self.core_canvas.create_text(
            center_x,
            center_y + 82,
            text="VYOM CORE",
            fill=self.PURPLE,
            font=(
                "Segoe UI",
                9,
                "bold"
            )
        )

    # =========================================================
    # WAVEFORM
    # =========================================================

    def draw_waveform(self):

        self.wave_canvas.delete(
            "all"
        )

        width = self.wave_canvas.winfo_width()

        if width <= 0:
            return

        center = width // 2

        # Number of bars
        bars = 31

        spacing = 10

        start_x = (
            center
            - ((bars - 1) * spacing) / 2
        )

        for i in range(bars):

            # Animated value
            value = math.sin(
                self.animation * 0.15
                + i * 0.65
            )

            height = (
                8
                + abs(value) * 28
            )

            x = (
                start_x
                + i * spacing
            )

            self.wave_canvas.create_line(
                x,
                30 - height / 2,
                x,
                30 + height / 2,
                fill=self.PURPLE,
                width=2
            )

    # =========================================================
    # ANIMATION
    # =========================================================

    def animate(self):

        self.animation += 1

        self.draw_orb()

        self.draw_waveform()

        self.root.after(
            50,
            self.animate
        )

    # =========================================================
    # RUN
    # =========================================================

    def run(self):

        self.root.mainloop()