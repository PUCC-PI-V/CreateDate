import customtkinter as ctk
from getData import GetData
import time
import atexit

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Criador de dados")
        self.geometry("600x300")

        start_time = time.time()
        atexit.register(self.saveTime, start_time)

        self.button = ctk.CTkButton(
            self, text="Gerar descrição", 
            command=self.open_new_window, 
            width=150, height=30, 
            fg_color="#AD2E11", hover_color="#8F250D", font=("Arial", 15)
        )
        self.button.pack(pady=10)

        self.button_exit = ctk.CTkButton(
            self, text="Sair", 
            command=self.getOut, 
            width=150, height=30, 
            fg_color="#AD2E11", hover_color="#8F250D", font=("Arial", 15)
        )
        self.button_exit.pack(pady=10)

    def open_new_window(self):
        GetData(self)
    
    def getOut(self):
        self.destroy()
    
    def saveTime(self, start_time):
        end_time = time.time()
        total_time = end_time - start_time
        with open("tempo_execucao.txt", "a") as f:
            f.write(f"Tempo de execução: {total_time:.2f} segundos\n")
            f.write(f"data: {time.ctime()}\n\n")
    
if __name__ == "__main__":
    app = App()
    app.mainloop()