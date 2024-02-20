import tkinter as tk
import tkinter.messagebox as messagebox
import requests

def get_kanye():
    # Fazer solicitação GET à API
    response = requests.get('https://api.kanye.rest')
    
    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Extrair a citação de Kanye da resposta JSON
        kanye_quote = response.json()['quote']
        # Exibir a citação em uma caixa de diálogo
        messagebox.showinfo("Citação de Kanye", kanye_quote)
    else:
        # Exibir mensagem de erro se a solicitação falhar
        messagebox.showerror("Erro", "Não foi possível obter a citação de Kanye")

# Criar a interface do usuário
root = tk.Tk()
root.title("Obter Dados da API")

label = tk.Label(root, text="Clique no botão para obter uma citação de Kanye West:")
label.pack()

button = tk.Button(root, text="Obter Kanye", command=get_kanye)
button.pack()

root.mainloop()
