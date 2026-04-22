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

        dificultOptions = ["Fácil", "Médio", "Difícil", "Muito difícil"]
        self.checkboxes = []

        self.title("Gerar descrição")
        self.geometry("600x400")
        self.attributes("-topmost", True) 
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self, 
            width=580, 
            height=450, 
            orientation="vertical" 
        )
        self.scrollable_frame.pack(fill="both", expand=True)

        self.label_status = ctk.CTkLabel(self.scrollable_frame, text="Processando descrição...", font=("Arial", 15))
        self.label_status.pack(pady=10)

        self.progress = ctk.CTkProgressBar(self.scrollable_frame, orientation="horizontal", width=300)
        self.progress.pack(pady=10)
        self.progress.start()

        self.result_box = ctk.CTkTextbox(self.scrollable_frame, width=500, height=200)
        self.result_box.pack(pady=10, padx=20)

        threading.Thread(target=self.fetch_data, daemon=True).start()

        self.dificuldade_label = ctk.CTkLabel(self.scrollable_frame, text="O quão difícil é realizar esse trabalho?", font=("Arial", 15))
        self.dificuldade_label.pack(pady=10)
        for option in dificultOptions:
            radio = ctk.CTkRadioButton(
                self.scrollable_frame, 
                text=option, 
                variable=self.dificuldade_var, 
                value=option,                  
                fg_color="#AD2E11", 
                hover_color="#8F250D"
            )
            radio.pack(pady=10, padx=100, anchor="w")
        
        self.justify_label = ctk.CTkLabel(self.scrollable_frame, text=f"Justifique a dificuldade selecionada", font=("Arial", 15))
        self.justify_label.pack(pady=10)

        self.justify_box = ctk.CTkTextbox(self.scrollable_frame, width=500, height=100)
        self.justify_box.pack(pady=10, padx=20)

        self.submit_button = ctk.CTkButton(
            self.scrollable_frame,
            text="Salvar resposta",
            command=self.saveData,
            width=150, height=30,
            fg_color="#AD2E11", hover_color="#8F250D", font=("Arial", 15)
        )
        self.submit_button.pack(pady=10)

    def fetch_data(self):
        try:
            response = client.models.generate_content(
                model="gemini-1.5-flash", 
                contents="Crie uma descrição detalhada de uma tatuagem artística"
            )
            texto = response.text
        except Exception as e:
            texto = f"Erro ao carregar: {e}"

        self.after(0, lambda: self.update_ui(texto))

    def update_ui(self, texto):
        self.progress.stop()
        self.progress.pack_forget() 
        if "Erro" in texto:
            self.label_status.configure(text="Erro ao gerar descrição.")
        else:
            self.label_status.configure(text="Concluído!")
        self.result_box.insert("0.0", texto)
    
    def saveData(self):
        descricao_ia = self.result_box.get("0.0", "end-1c")
        dificuldade = self.dificuldade_var.get()
        justificativa = self.justify_box.get("0.0", "end-1c")

        arquivo = "tatuagens_geradas.txt"

        try:
            with open(arquivo, "a", encoding="utf-8") as f:
                f.write("-" * 50 + "\n")
                f.write(f"DIFICULDADE TÉCNICA: {dificuldade}\n")
                f.write(f"JUSTIFICATIVA DO ARTISTA: {justificativa}\n\n")
                f.write(f"DESCRIÇÃO DA TATUAGEM:\n{descricao_ia}\n")
                f.write("-" * 50 + "\n\n")
            
            self.submit_button.configure(text="✅ Salvo com Sucesso!", fg_color="#C33617")
            print(f"Dados salvos em {arquivo}")
            
            self.after(2000, lambda: self.submit_button.configure(text="Salvar resposta", fg_color="#AD2E11"))

        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")
            self.submit_button.configure(text="❌ Erro ao Salvar", fg_color="red")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Criador de dados")
        self.geometry("600x300")

        self.label = ctk.CTkLabel(self, text="Seja bem-vinda!\nAqui será gerado alguns exemplos de tatuagem.", font=("Arial", 17))
        self.label.pack(pady=20)

        self.button = ctk.CTkButton(
            self, text="Gerar descrição", 
            command=self.open_new_window, 
            width=150, height=30, 
            fg_color="#AD2E11", hover_color="#8F250D", font=("Arial", 15)
        )
        self.button.pack(pady=10)

    def open_new_window(self):
        GetData(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()