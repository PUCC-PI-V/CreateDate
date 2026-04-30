import customtkinter as ctk
from getData import GetData



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Criador de dados")
        self.geometry("820x520")
        self.minsize(820, 520)
        self.configure(fg_color="#111827")
        self._center_window()
        self.iconbitmap("icon.ico")

        self._build_ui()

    def _center_window(self):
        self.update_idletasks()
        width = 820
        height = 520
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        pos_x = int((screen_width / 2) - (width / 2))
        pos_y = int((screen_height / 2) - (height / 2))
        self.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

    def _build_ui(self):
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=28, pady=28)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(1, weight=1)

        header_card = ctk.CTkFrame(
            container,
            corner_radius=22,
            fg_color="#1F2937",
            border_width=1,
            border_color="#374151",
        )
        header_card.grid(row=0, column=0, sticky="ew", pady=(0, 18))
        header_card.grid_columnconfigure(0, weight=1)

        badge_label = ctk.CTkLabel(
            header_card,
            text="Painel principal",
            fg_color="#7C2D12",
            corner_radius=999,
            padx=14,
            pady=7,
            font=("Arial", 13, "bold"),
            text_color="#FFF7ED",
        )
        badge_label.grid(row=0, column=0, sticky="w", padx=26, pady=(24, 12))

        title_label = ctk.CTkLabel(
            header_card,
            text="Gerador de descricoes para tatuagem",
            font=("Arial", 30, "bold"),
            text_color="#F9FAFB",
        )
        title_label.grid(row=1, column=0, sticky="w", padx=26)

        description_label = ctk.CTkLabel(
            header_card,
            text="Abra o gerador, receba uma sugestao criada por IA e registre a dificuldade tecnica junto da justificativa.",
            justify="left",
            wraplength=700,
            font=("Arial", 15),
            text_color="#D1D5DB",
        )
        description_label.grid(row=2, column=0, sticky="w", padx=26, pady=(12, 22))

        content_card = ctk.CTkFrame(
            container,
            corner_radius=22,
            fg_color="#172033",
        )
        content_card.grid(row=1, column=0, sticky="nsew")
        content_card.grid_columnconfigure((0, 1), weight=1)

        info_frame = ctk.CTkFrame(content_card, fg_color="transparent")
        info_frame.grid(row=0, column=0, sticky="nsew", padx=(26, 14), pady=26)

        section_label = ctk.CTkLabel(
            info_frame,
            text="Fluxo rapido",
            font=("Arial", 15, "bold"),
            text_color="#F97316",
        )
        section_label.pack(anchor="w")

        steps_label = ctk.CTkLabel(
            info_frame,
            justify="left",
            text=(
                "1. Gere uma descricao detalhada.\n"
                "2. Avalie a dificuldade tecnica.\n"
                "3. Salve tudo no historico local."
            ),
            font=("Arial", 20, "bold"),
            text_color="#F9FAFB",
        )
        steps_label.pack(anchor="w", pady=(12, 12))

        action_frame = ctk.CTkFrame(
            content_card,
            corner_radius=18,
            fg_color="#0F172A",
            border_width=1,
            border_color="#334155",
        )
        action_frame.grid(row=0, column=1, sticky="nsew", padx=(14, 26), pady=26)

        action_title = ctk.CTkLabel(
            action_frame,
            text="Acoes",
            font=("Arial", 24, "bold"),
            text_color="#F8FAFC",
        )
        action_title.pack(anchor="w", padx=24, pady=(24, 8))

        action_text = ctk.CTkLabel(
            action_frame,
            text="Escolha o que deseja fazer agora.",
            font=("Arial", 14),
            text_color="#94A3B8",
        )
        action_text.pack(anchor="w", padx=24, pady=(0, 24))

        self.button = ctk.CTkButton(
            action_frame,
            text="Gerar descricao",
            command=self.open_new_window,
            width=220,
            height=44,
            corner_radius=14,
            fg_color="#C2410C",
            hover_color="#9A3412",
            font=("Arial", 16, "bold"),
        )
        self.button.pack(anchor="w", padx=24)

        self.button_exit = ctk.CTkButton(
            action_frame,
            text="Sair",
            command=self.getOut,
            width=220,
            height=44,
            corner_radius=14,
            fg_color="#334155",
            hover_color="#475569",
            font=("Arial", 16, "bold"),
        )
        self.button_exit.pack(anchor="w", padx=24, pady=(14, 0))

        footer_label = ctk.CTkLabel(
            action_frame,
            text="Seu tempo de uso continua sendo registrado em `tempo_execucao.txt`.",
            justify="left",
            wraplength=260,
            font=("Arial", 12),
            text_color="#64748B",
        )
        footer_label.pack(anchor="w", padx=24, pady=(18, 24))

    def open_new_window(self):
        GetData(self)
    
    def getOut(self):
        self.destroy()
    
if __name__ == "__main__":
    app = App()
    app.mainloop()