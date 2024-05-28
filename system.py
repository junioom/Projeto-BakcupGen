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