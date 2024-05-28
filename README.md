# Backup Generator

Backup Generator é um projeto desenvolvido para automatizar o processo de backup de arquivos e diretórios. Este projeto foi criado como parte do meu aprendizado em Python e suas bibliotecas. Ele representa o meu primeiro projeto prático usando Python.

## Descrição

O Backup Generator permite selecionar um diretório e criar um backup de seus arquivos e subdiretórios, excluindo outros backups existentes. A estrutura de backup é organizada com base na data e hora da execução, facilitando a gestão e a recuperação dos arquivos.

## Funcionalidades

- Seleção de diretório para backup.
- Criação de um diretório de backup com a data e hora atuais.
- Cópia de arquivos e subdiretórios (excluindo outros backups) para o diretório de backup.

## Tecnologias Utilizadas

- Python 3
- Biblioteca `tkinter` para interface gráfica de seleção de diretório.
- Biblioteca `os` para manipulação de diretórios e arquivos.
- Biblioteca `shutil` para operações de cópia de arquivos e diretórios.
- Biblioteca `datetime` para manipulação de datas e horas.

## Como Usar

1. **Clone o repositório**:
   ```sh
   git clone <URL_DO_REPOSITÓRIO>
   cd <NOME_DO_REPOSITÓRIO>
   ```

2. **Instale as dependências** (se necessário):
   - Certifique-se de ter o Python 3 instalado.
   - Instale a biblioteca `tkinter` se não estiver disponível.

3. **Execute o script**:
   ```sh
   python backup_generator.py
   ```

4. **Selecione o diretório**:
   - Uma janela pop-up permitirá que você selecione o diretório para backup.

5. **Verifique o backup**:
   - O backup será criado em um subdiretório chamado `backup` dentro do diretório selecionado, com um nome baseado na data e hora atuais.

## Código

```python
import os
import shutil as sh
import datetime as dt
from tkinter.filedialog import askdirectory

date_now = str(dt.datetime.today().strftime('%d-%m-%y %H_%M_%S'))

directory_selected = askdirectory()
list_file_backup = os.listdir(directory_selected)
backup_directory = os.path.join(directory_selected, 'backup')

if not os.path.exists(backup_directory):
    os.mkdir(backup_directory)

final_directory = os.path.join(backup_directory, date_now)
if not os.path.exists(final_directory):
    os.mkdir(final_directory)

for file in list_file_backup:
    file_name = f'{directory_selected}/{file}'
    if os.path.isfile(file_name):
        sh.copy2(file_name, final_directory)
    elif 'backup' != file and os.path.isdir(file_name):
        destination = os.path.join(final_directory, file)
        sh.copytree(file_name, destination)
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias ou correções.

## Contato

Se você tiver dúvidas ou sugestões, sinta-se à vontade para me contatar.

## Conecte-se comigo

[![Gmail](https://img.shields.io/badge/Gmail-333333?style=for-the-badge&logo=gmail&logoColor=red)](mailto:juniorbmelo12@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alexsandro-junior-576719297/)
[![Instagram](https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/juniorbm.wn/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/junioom)
```

