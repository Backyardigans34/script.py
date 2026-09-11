import os, subprocess

print(f"diretorioatual: ", os.getcwd())

print(f"Processo atual: ", os.getpid())

subprocess.run("notepad")

subprocess.run("calc")

#criar um arquivo
with open("arquivo_aula.txt", "w") as arquivo:
    arquivo.write("sistemas de informação, sistemasoperacionais")