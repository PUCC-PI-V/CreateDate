import customtkinter as ctk
from CreateData import App as CreateDataApp


class App(ctk.CTk):
    def cleanFrame(self):
        self.destroy()
    
    def open_window(self):
        self.cleanFrame()
        new_window = CreateDataApp()
        new_window.mainloop()

    
    def __init__(self):
        super().__init__()

        self.title("ViboraInk - Criador de dados")
        self.geometry("600x300")

        self.label = ctk.CTkLabel(self, text="Olá Barbara, seja bem-vinda!", font=("Arial", 17))
        self.label.pack(pady=20)

        self.button = ctk.CTkButton(self, text="Iniciar", command=self.open_window, width=150, height=30, fg_color="#AD2E11", hover_color="#8F250D", font=("Arial", 15))
        self.button.pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()