import subprocess

comando = "iwr -useb https://raw.githubusercontent.com/spicetify/cli/main/install.ps1 | iex"

process = subprocess.Popen(["powershell", "-Command", comando],
                           stdin=subprocess.PIPE, # Permite enviar comandos para o processo
                           stdout=subprocess.PIPE, # Permite capturar a saída do processo
                           stderr=subprocess.PIPE, # Permite capturar erros do processo
                           text=True) # configura o processo para usar String em vez de bytes

process.communicate(input="y") # envia o "y" para confirmar a instalação
process.close() # fecha o processo após a instalação

