import threading
import customtkinter as ctk

from ai import ProgrammingAI


class ChatbotUI:
    def __init__(self):
        self.ai = None

        # =========================
        # WINDOW
        # =========================

        self.root = ctk.CTk()
        self.root.title("Programming AI Assistant")
        self.root.geometry("900x650")
        self.root.minsize(700, 500)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # =========================
        # TITLE
        # =========================

        self.title_label = ctk.CTkLabel(
            self.root,
            text="Programming AI Assistant",
            font=("Arial", 24, "bold")
        )

        self.title_label.pack(
            padx=20,
            pady=(20, 5)
        )

        self.subtitle_label = ctk.CTkLabel(
            self.root,
            text="Programming • IT • Software Engineering • Computer Science",
            font=("Arial", 12)
        )

        self.subtitle_label.pack(
            padx=20,
            pady=(0, 15)
        )

        # =========================
        # API KEY AREA
        # =========================

        self.api_frame = ctk.CTkFrame(
            self.root
        )

        self.api_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 10)
        )

        self.api_label = ctk.CTkLabel(
            self.api_frame,
            text="Gemini API Key:"
        )

        self.api_label.pack(
            side="left",
            padx=(10, 5),
            pady=10
        )

        self.api_entry = ctk.CTkEntry(
            self.api_frame,
            placeholder_text="Masukkan Gemini API Key",
            show="*"
        )

        self.api_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=5,
            pady=10
        )

        self.connect_button = ctk.CTkButton(
            self.api_frame,
            text="Connect",
            width=100,
            command=self.connect_ai
        )

        self.connect_button.pack(
            side="right",
            padx=(5, 10),
            pady=10
        )

        # =========================
        # CHAT AREA
        # =========================

        self.chat_box = ctk.CTkTextbox(
            self.root,
            wrap="word",
            font=("Consolas", 14)
        )

        self.chat_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.chat_box.configure(
            state="disabled"
        )

        # =========================
        # INPUT AREA
        # =========================

        self.input_frame = ctk.CTkFrame(
            self.root
        )

        self.input_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        self.message_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Tanyakan sesuatu tentang Programming / IT..."
        )

        self.message_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(10, 5),
            pady=10
        )

        self.message_entry.bind(
            "<Return>",
            self.send_message
        )

        self.send_button = ctk.CTkButton(
            self.input_frame,
            text="Send",
            width=100,
            command=self.send_message
        )

        self.send_button.pack(
            side="right",
            padx=(5, 10),
            pady=10
        )

        # =========================
        # STATUS
        # =========================

        self.status_label = ctk.CTkLabel(
            self.root,
            text="Belum terhubung ke Gemini",
            anchor="w"
        )

        self.status_label.pack(
            fill="x",
            padx=20,
            pady=(0, 10)
        )

    # ==================================================
    # CONNECT AI
    # ==================================================

    def connect_ai(self):
        api_key = self.api_entry.get().strip()

        if not api_key:
            self.set_status(
                "API Key belum dimasukkan."
            )
            return

        try:
            self.ai = ProgrammingAI(api_key)

            self.set_status(
                "Connected to Gemini."
            )

            self.add_message(
                "SYSTEM",
                "Gemini berhasil terhubung.\n"
                "Saya hanya menjawab pertanyaan Programming / IT / Software."
            )

        except Exception as error:
            self.set_status(
                f"Connection failed: {error}"
            )

    # ==================================================
    # SEND MESSAGE
    # ==================================================

    def send_message(self, event=None):
        message = self.message_entry.get().strip()

        if not message:
            return

        if self.ai is None:
            self.add_message(
                "SYSTEM",
                "Hubungkan Gemini API terlebih dahulu."
            )
            return

        self.message_entry.delete(
            0,
            "end"
        )

        self.add_message(
            "YOU",
            message
        )

        self.send_button.configure(
            state="disabled"
        )

        self.message_entry.configure(
            state="disabled"
        )

        self.set_status(
            "Gemini sedang berpikir..."
        )

        thread = threading.Thread(
            target=self.process_ai,
            args=(message,),
            daemon=True
        )

        thread.start()

    # ==================================================
    # PROCESS AI
    # ==================================================

    def process_ai(self, message):
        response = self.ai.send_message(
            message
        )

        self.root.after(
            0,
            self.display_ai_response,
            response
        )

    # ==================================================
    # DISPLAY AI RESPONSE
    # ==================================================

    def display_ai_response(self, response):
        self.add_message(
            "GEMINI",
            response
        )

        self.send_button.configure(
            state="normal"
        )

        self.message_entry.configure(
            state="normal"
        )

        self.message_entry.focus()

        self.set_status(
            "Ready"
        )

    # ==================================================
    # ADD MESSAGE
    # ==================================================

    def add_message(self, sender, message):
        self.chat_box.configure(
            state="normal"
        )

        self.chat_box.insert(
            "end",
            f"\n{sender}\n"
        )

        self.chat_box.insert(
            "end",
            f"{message}\n"
        )

        self.chat_box.insert(
            "end",
            "\n" + "=" * 80 + "\n"
        )

        self.chat_box.see(
            "end"
        )

        self.chat_box.configure(
            state="disabled"
        )

    # ==================================================
    # STATUS
    # ==================================================

    def set_status(self, text):
        self.status_label.configure(
            text=text
        )

    # ==================================================
    # RUN
    # ==================================================

    def run(self):
        self.root.mainloop()