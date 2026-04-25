import customtkinter as ctk
import time
import atexit
from CreateData import App as CreateDataApp


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ViboraInk - Criador de dados")
        self.geometry("760x460")
        self.minsize(760, 460)
        self.configure(fg_color="#111827")

        self._center_window()
        self._build_ui()

        start_time = time.time()
        atexit.register(self.saveTime, start_time)

    def _center_window(self):
        self.update_idletasks()
        width = 760
        height = 460
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        pos_x = int((screen_width / 2) - (width / 2))
        pos_y = int((screen_height / 2) - (height / 2))
        self.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

    def _build_ui(self):
        outer_frame = ctk.CTkFrame(self, fg_color="transparent")
        outer_frame.pack(fill="both", expand=True, padx=24, pady=24)
        outer_frame.grid_columnconfigure((0, 1), weight=1)
        outer_frame.grid_rowconfigure(0, weight=1)

        left_card = ctk.CTkFrame(
            outer_frame,
            corner_radius=22,
            fg_color="#7C2D12",
        )
        left_card.grid(row=0, column=0, sticky="nsew", padx=(0, 12))

        right_card = ctk.CTkFrame(
            outer_frame,
            corner_radius=22,
            fg_color="#1F2937",
            border_width=1,
            border_color="#374151",
        )
        right_card.grid(row=0, column=1, sticky="nsew", padx=(12, 0))

        brand_label = ctk.CTkLabel(
            left_card,
            text="ViboraInk Studio",
            font=("Arial", 16, "bold"),
            text_color="#FED7AA",
        )
        brand_label.pack(anchor="w", padx=28, pady=(28, 10))

        title_label = ctk.CTkLabel(
            left_card,
            text="Crie descricoes de tatuagem\ncom um visual mais elegante.",
            justify="left",
            font=("Arial", 28, "bold"),
            text_color="#FFF7ED",
        )
        title_label.pack(anchor="w", padx=28)

        subtitle_label = ctk.CTkLabel(
            left_card,
            text="Uma experiencia mais bonita para iniciar, gerar ideias e salvar referencias com rapidez.",
            justify="left",
            wraplength=280,
            font=("Arial", 15),
            text_color="#FFEDD5",
        )
        subtitle_label.pack(anchor="w", padx=28, pady=(16, 0))

        status_chip = ctk.CTkLabel(
            left_card,
            text="Pronto para gerar",
            fg_color="#9A3412",
            corner_radius=999,
            padx=14,
            pady=8,
            font=("Arial", 13, "bold"),
            text_color="#FFFBEB",
        )
        status_chip.pack(anchor="w", padx=28, pady=(22, 28))

        info_card = ctk.CTkFrame(
            left_card,
            corner_radius=18,
            fg_color="#6B210A",
            border_width=1,
            border_color="#C2410C",
        )
        info_card.pack(fill="both", expand=True, padx=28, pady=(0, 28))

        info_title = ctk.CTkLabel(
            info_card,
            text="Como funciona",
            font=("Arial", 15, "bold"),
            text_color="#FED7AA",
        )
        info_title.pack(anchor="w", padx=18, pady=(18, 10))

        steps_label = ctk.CTkLabel(
            info_card,
            text=(
                "1. Abra o painel principal.\n"
                "2. Gere uma nova descricao.\n"
                "3. Avalie a dificuldade tecnica.\n"
                "4. Salve o resultado no historico."
            ),
            justify="left",
            font=("Arial", 18, "bold"),
            text_color="#FFF7ED",
        )
        steps_label.pack(anchor="w", padx=18, pady=(0, 12))

        info_caption = ctk.CTkLabel(
            info_card,
            text="Uma entrada simples, sem imagens decorativas, com foco no fluxo da aplicacao.",
            wraplength=250,
            justify="left",
            font=("Arial", 13),
            text_color="#FFEDD5",
        )
        info_caption.pack(anchor="w", padx=18, pady=(0, 18))

        eyebrow_label = ctk.CTkLabel(
            right_card,
            text="Bem-vinda",
            font=("Arial", 14, "bold"),
            text_color="#F97316",
        )
        eyebrow_label.pack(anchor="w", padx=28, pady=(32, 8))

        welcome_label = ctk.CTkLabel(
            right_card,
            text="Ola Barbara, seja bem-vinda!",
            justify="left",
            font=("Arial", 26, "bold"),
            text_color="#F9FAFB",
        )
        welcome_label.pack(anchor="w", padx=28)

        description_label = ctk.CTkLabel(
            right_card,
            text="Organize sua criacao em poucos cliques e abra o gerador com uma interface mais clara e moderna.",
            justify="left",
            wraplength=290,
            font=("Arial", 15),
            text_color="#D1D5DB",
        )
        description_label.pack(anchor="w", padx=28, pady=(14, 24))

        button = ctk.CTkButton(
            right_card,
            text="Iniciar",
            command=self.open_window,
            width=190,
            height=44,
            corner_radius=14,
            fg_color="#C2410C",
            hover_color="#9A3412",
            font=("Arial", 16, "bold"),
        )
        button.pack(anchor="w", padx=28)

        helper_label = ctk.CTkLabel(
            right_card,
            text="Clique para abrir o painel principal.",
            font=("Arial", 13),
            text_color="#9CA3AF",
        )
        helper_label.pack(anchor="w", padx=28, pady=(10, 0))

    def cleanFrame(self):
        self.destroy()

    def open_window(self):
        self.cleanFrame()
        new_window = CreateDataApp()
        new_window.mainloop()
    
    def saveTime(self, start_time):
        end_time = time.time()
        total_time = end_time - start_time
        with open("tempo_execucao.txt", "a", encoding="utf-8") as f:
            f.write(f"Tempo de execução: {total_time:.2f} segundos\n")
            f.write(f"data: {time.ctime()}\n\n")

if __name__ == "__main__":
    app = App()
    app.mainloop()