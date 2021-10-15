import tkinter as tk
import proj
import time

suaVez = True
count = 0

def iniciar():
  global suaVez, count
  suaVez = True
  count = 0

  initiate.place_forget()
  ongoing.place(relx=0.4, rely=0.1)
  player.place(relx=0.4, rely=0.2)
  play.place(width=100, height=30, relx=0.4, rely=0.3)
  cancel.place(width=100, height=30, relx=0.4, rely=0.9)

def finalizar():
  global suaVez, count

  if suaVez == True:
    player.place_forget()
    machine.place(relx=0.4, rely=0.2)
    # time.sleep(2)
    # proj.main()
    # Executa todos os processos
    suaVez = False
  else:
    machine.place_forget()
    player.place(relx=0.4, rely=0.2)
    suaVez = True
  
  count = count + 1

  if count == 9:
    machine.place_forget()
    player.place_forget()
    play.place_forget()
    ongoing.place_forget()
    cancel.place_forget()
    result.place(relx=0.4, rely=0.2)
    goBack.place(width=100, height=30, relx=0.4, rely=0.9)


def cancelar():
  ongoing.place_forget()
  player.place_forget()
  machine.place_forget()
  play.place_forget()
  cancel.place_forget()
  initiate.place(width=100, height=30, relx=0.4, rely=0.1)

def voltar():
  result.place_forget()
  goBack.place_forget()
  initiate.place(width=100, height=30, relx=0.4, rely=0.1)

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=400, bg="white")
canvas.pack()

initiate = tk.Button(root, text="Iniciar", padx=10, pady=5, fg="black", bg="white", command=iniciar)
initiate.place(width=100, height=30, relx=0.4, rely=0.1)

ongoing = tk.Label(root, text="Jogo em andamento", bg="white")
player = tk.Label(root, text="Sua vez", bg="white")
machine = tk.Label(root, text="Vez da máquina", bg="white")

play = tk.Button(root, text="Finalizar jogada", padx=10, pady=5, fg="black", bg="white", command=finalizar)

cancel = tk.Button(root, text="Cancelar", padx=10, pady=5, fg="black", bg="white", command=cancelar)

result = tk.Label(root, text="Você ganhou ou perdeu", bg="white")
goBack = tk.Button(root, text="Voltar ao início", padx=10, pady=5, fg="black", bg="white", command=voltar)

root.mainloop()