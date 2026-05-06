import os
import customtkinter as ctk
from dotenv import load_dotenv
from google import genai
import threading

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)


class GetData(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        

        self.dificuldade_var = ctk.StringVar(value="Fácil")
        self.is_fetch_complete = False

        dificultOptions = ["Fácil", "Médio", "Difícil", "Muito difícil"]

        self.title("Gerar descrição")
        self.geometry("860x720")
        self.minsize(860, 720)
        self.configure(fg_color="#111827")
        self.attributes("-topmost", True)
        self._center_window()

        self.scrollable_frame = ctk.CTkScrollableFrame(
            self,
            width=820,
            height=680,
            orientation="vertical",
            fg_color="#111827",
        )
        self.scrollable_frame.pack(fill="both", expand=True)
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        self._build_ui(dificultOptions)
        threading.Thread(target=self.getResponse, daemon=True).start()

    def _center_window(self):
        self.update_idletasks()
        width = 860
        height = 720
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        pos_x = int((screen_width / 2) - (width / 2))
        pos_y = int((screen_height / 2) - (height / 2))
        self.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

    def _build_ui(self, dificultOptions):
        header_card = ctk.CTkFrame(
            self.scrollable_frame,
            corner_radius=22,
            fg_color="#1F2937",
            border_width=1,
            border_color="#374151",
        )
        header_card.pack(fill="x", padx=22, pady=(22, 16))

        title_label = ctk.CTkLabel(
            header_card,
            text="Descricao gerada por IA",
            font=("Arial", 28, "bold"),
            text_color="#F9FAFB",
        )
        title_label.pack(anchor="w", padx=24, pady=(24, 8))

        subtitle_label = ctk.CTkLabel(
            header_card,
            text="Revise a sugestao, selecione a dificuldade tecnica e salve a observacao logo abaixo.",
            justify="left",
            wraplength=760,
            font=("Arial", 14),
            text_color="#CBD5E1",
        )
        subtitle_label.pack(anchor="w", padx=24, pady=(0, 18))

        status_frame = ctk.CTkFrame(
            self.scrollable_frame,
            corner_radius=20,
            fg_color="#172033",
        )
        status_frame.pack(fill="x", padx=22, pady=(0, 16))

        self.label_status = ctk.CTkLabel(
            status_frame,
            text="Processando descricao...",
            font=("Arial", 16, "bold"),
            text_color="#F8FAFC",
        )
        self.label_status.pack(anchor="w", padx=22, pady=(22, 8))

        self.progress = ctk.CTkProgressBar(
            status_frame,
            orientation="horizontal",
            width=760,
            progress_color="#F97316",
        )
        self.progress.pack(anchor="w", padx=22, pady=(0, 22))
        self.progress.start()

        result_frame = ctk.CTkFrame(
            self.scrollable_frame,
            corner_radius=20,
            fg_color="#0F172A",
            border_width=1,
            border_color="#334155",
        )
        result_frame.pack(fill="x", padx=22, pady=(0, 16))

        result_title = ctk.CTkLabel(
            result_frame,
            text="Resultado",
            font=("Arial", 18, "bold"),
            text_color="#F9FAFB",
        )
        result_title.pack(anchor="w", padx=22, pady=(20, 10))

        self.result_box = ctk.CTkTextbox(
            result_frame,
            width=760,
            height=220,
            corner_radius=14,
            fg_color="#111827",
            border_width=1,
            border_color="#374151",
            font=("Arial", 14),
        )
        self.result_box.pack(fill="x", padx=22, pady=(0, 22))

        self.valor_label = ctk.CTkLabel(
            result_frame,
            text="Baseado na descrição, qual o valor aproximado da tatuagem?",
            font=("Arial", 18, "bold"),
            text_color="#F9FAFB",
        )
        self.valor_label.pack(anchor="w", padx=22, pady=(20, 10))

        valor_frame = ctk.CTkFrame(
            result_frame,
            fg_color="#111827",
            corner_radius=14,
            border_width=1,
            border_color="#374151",
        )
        valor_frame.pack(fill="x", padx=22, pady=(0, 8))
        valor_frame.grid_columnconfigure(1, weight=1)

        valor_prefixo = ctk.CTkLabel(
            valor_frame,
            text="R$",
            font=("Arial", 16, "bold"),
            text_color="#F97316",
        )
        valor_prefixo.grid(row=0, column=0, padx=(16, 10), pady=10, sticky="w")

        self.valor = ctk.CTkTextbox(
            valor_frame,
            height=44,
            corner_radius=10,
            fg_color="#111827",
            border_width=0,
            font=("Arial", 14),
        )
        self.valor.grid(row=0, column=1, sticky="ew", padx=(0, 10), pady=4)

        valor_hint = ctk.CTkLabel(
            result_frame,
            text="Digite apenas o numero. Nao precisa adicionar a cifra.",
            font=("Arial", 12),
            text_color="#94A3B8",
        )
        valor_hint.pack(anchor="w", padx=22, pady=(0, 22))

       
        difficulty_frame = ctk.CTkFrame(
            self.scrollable_frame,
            corner_radius=20,
            fg_color="#172033",
        )
        difficulty_frame.pack(fill="x", padx=22, pady=(0, 16))

        self.dificuldade_label = ctk.CTkLabel(
            difficulty_frame,
            text="O quao dificil e realizar esse trabalho?",
            font=("Arial", 17, "bold"),
            text_color="#F8FAFC",
        )
        self.dificuldade_label.pack(anchor="w", padx=22, pady=(22, 10))

        for option in dificultOptions:
            radio = ctk.CTkRadioButton(
                difficulty_frame,
                text=option,
                variable=self.dificuldade_var,
                value=option,
                fg_color="#C2410C",
                hover_color="#9A3412",
                font=("Arial", 14),
                text_color="#E5E7EB",
            )
            radio.pack(pady=8, padx=24, anchor="w")

        justify_frame = ctk.CTkFrame(
            self.scrollable_frame,
            corner_radius=20,
            fg_color="#172033",
        )
        justify_frame.pack(fill="x", padx=22, pady=(0, 16))

        self.justify_label = ctk.CTkLabel(
            justify_frame,
            text="Justifique a dificuldade selecionada",
            font=("Arial", 17, "bold"),
            text_color="#F8FAFC",
        )
        self.justify_label.pack(anchor="w", padx=22, pady=(22, 10))

        self.justify_box = ctk.CTkTextbox(
            justify_frame,
            width=760,
            height=130,
            corner_radius=14,
            fg_color="#111827",
            border_width=1,
            border_color="#374151",
            font=("Arial", 14),
        )
        self.justify_box.pack(fill="x", padx=22, pady=(0, 22))

        footer_frame = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
        footer_frame.pack(fill="x", padx=22, pady=(0, 22))

        self.submit_button = ctk.CTkButton(
            footer_frame,
            text="Salvar resposta",
            command=self.saveData,
            width=220,
            height=44,
            corner_radius=14,
            fg_color="#C2410C",
            hover_color="#9A3412",
            font=("Arial", 16, "bold"),
        )
        self.submit_button.pack(anchor="e")

    def getResponse(self):
        if os.path.exists("data.txt") == False:
            with open("data.txt", "w", encoding="utf-8") as f:
                f.write("")
        
        if os.path.getsize("data.txt") == 0:

            Data = self.fetch_data()
            with open("data.txt", "w", encoding="utf-8") as f:
                f.write(Data)
            
            response = self.pop_first_entry("data.txt")
            
        else:
            response = self.pop_first_entry("data.txt")
        
        self.after(0, lambda: self.update_ui(response))


    def get_context(self):
        if os.path.exists("tatuagens_geradas.txt") == False:
            return ""
        
        with open("tatuagens_geradas.txt", "r", encoding="utf-8") as f:
            return f.list(f.readlines()[:100]) 

    def fetch_data(self):
        
        context = self.get_context()

        try:
            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents="Como agente voce deve realizar a seguinte tarefa de forma direta e objetiva em uma unica resposta sem quebrar o prompt em partes."+
                "Faça: Crie 20 descrições detalhada de uma tatuagem a onde deve"+
                " conter informações sobre a tatuagem, como a localização, o tamanho, o estilo, o tema"+
                "exemplo: Projeto de rosa realista para aplicacao no antebraco, com cerca de 18 cm de extensao, seguindo estilo realismo em black and grey e traco fino a medio com sombras suaves. Uma rosa em estilo realista, com petalas volumosas, sombras suaves, textura organica e acabamento delicado nas folhas. A composicao foi pensada para acompanhar a anatomia da regiao, manter leitura clara de perto e de longe e distribuir melhor volumes, respiros e detalhes, para que a tatuagem fique elegante na sessao, cicatrize bem e continue bonita mesmo com o passar do tempo."+
                "No topo antes da descrição adicione um titulo que resuma a tatuagem e uma ? logo apos o titulo, seguindo o exemplo: Rosa realista?"+
                "do titulo para a descrição não adicione espaços vazios mas separe o titulo da descrição, e quando for colocar a descrição adicione no inicio: Descricao:"+
                " Tente ao maximo possivel se parecer com um humano descrevendo uma tatuagem que deseja realizar"+
                "e evite de enumerar os 20 dados, mande somente as 20 descrições e isso é muito imporntante: Do titulo para a descrição adicione uma quebra de linha e coloque um espaço de uma tatuagem para a outra"+
                "a seguir aqui esta exemplos ja existentes, então evite de repitir: "+context
            )
    
            texto = response.text
        except Exception as e:
            error = f"Erro ao carregar: {e}"
            self.after(0, lambda: self.update_ui(error))
            texto = ""
        
        return texto
    
    def pop_first_entry(self, file_path: str): 
        if not os.path.exists(file_path):
            return None

        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        while lines and not lines[0].strip():
            lines.pop(0)

        if not lines:
            return None

        title = None
        description_lines = []
        next_entry_start = len(lines)

        for i, line in enumerate(lines):
            clean_line = line.strip()
            
            if not clean_line:
                continue

            if title is None:
                title = clean_line
            else:
                if clean_line.endswith("?"):
                    next_entry_start = i
                    break
                description_lines.append(clean_line)

        if title:
            extracted_text = f"{title}\n{' '.join(description_lines)}".strip()
            
            remaining_content = lines[next_entry_start:]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(remaining_content)
                
            return extracted_text

        return None

    def update_ui(self, texto):
        self.progress.stop()
        self.progress.pack_forget()
        if "Erro" in texto:
            self.label_status.configure(text="Erro ao gerar descricao.", text_color="#FCA5A5")
        else:
            self.label_status.configure(text="Descricao pronta para revisar.", text_color="#86EFAC")
            self.is_fetch_complete = True
        self.result_box.insert("0.0", texto)

    def saveData(self):
        descricao_ia = self.result_box.get("0.0", "end-1c")
        dificuldade = self.dificuldade_var.get()
        valor = self.valor.get("0.0", "end-1c").strip()
        justificativa = self.justify_box.get("0.0", "end-1c")

        arquivo = "tatuagens_geradas.txt"

        try:
            with open(arquivo, "a", encoding="utf-8") as f:
                f.write(f"{descricao_ia}\n")
                f.write(f"DIFICULDADE TÉCNICA: {dificuldade}\n")
                f.write(f"VALOR APROXIMADO: R${valor}\n")
                f.write(f"JUSTIFICATIVA DA DIFICULDADE: {justificativa}\n\n\n")

            self.submit_button.configure(
                text="Salvo com sucesso!",
                fg_color="#15803D",
                hover_color="#166534",
            )
            print(f"Dados salvos em {arquivo}")
            self.after(1400, self.destroy)

        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")
            self.submit_button.configure(
                text="Erro ao salvar",
                fg_color="#B91C1C",
                hover_color="#991B1B",
            )