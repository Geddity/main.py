import tkinter as tk
from tkinter import filedialog
import os
import json
import pandas as pd
import subprocess
import re
import cv2
from openpyxl.styles import Alignment


# путь к файлу конфигурации
config_file = 'config.txt'

# сохранение/загрузка пути
def read_selected_folder():
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return f.read().strip()
    return ''

def save_selected_folder(folder_path):
    with open(config_file, 'w') as f:
        f.write(folder_path)

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        save_selected_folder(folder_path)
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)

# поиск видео
def find_video_files(folder_path):
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv']
    video_files = []

    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            _, ext = os.path.splitext(filename.lower())
            if ext in video_extensions:
                video_files.append(os.path.join(folder_path, filename))

    return video_files

# подсчет кадров
def count_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    frames_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames_count += 1
    cap.release()
    return frames_count

# вывод инфо
def show_video_info(folder_path):
    video_files = find_video_files(folder_path)

    info_text.delete('1.0', tk.END)

    if not video_files:
        info_text.insert(tk.END, "В папке не найдены видеофайлы.")
    else:
        for file in video_files:
            frames_count = count_frames(file)
            if frames_count:
                info_text.insert(tk.END, f"{os.path.basename(file)}: {frames_count} кадров\n")
            else:
                info_text.insert(tk.END, f"{file}: Не удалось подсчитать количество кадров\n")

# создание таблицы
def create_excel_report():
    folder_path = folder_entry.get()
    if not folder_path:
        print("Пожалуйста, выберите папку.")
        return

    video_files = find_video_files(folder_path)

    if not video_files:
        print("Видеофайлы не найдены.")
        return

    folder_name = os.path.basename(os.path.normpath(folder_path))

    report_name = filedialog.asksaveasfilename(defaultextension=f".xlsx",
                                               initialdir=os.path.normpath(folder_path),
                                               title="Сохранить отчет")
    if not report_name:
        print("Отмена создания отчета.")
        return

    frames_count_list = []

    for video_file in video_files:
        file_name = os.path.splitext(os.path.basename(video_file))[0]
        frames_count = count_frames(video_file)
        if frames_count:
            frames_count_list.append([folder_name, file_name, frames_count])
        else:
            frames_count_list.append([folder_name, file_name, "Не удалось подсчитать"])

    df = pd.DataFrame(frames_count_list, columns=['Серия', 'Номер шота', 'Кол-во кадров'])

    with pd.ExcelWriter(report_name) as writer:
        df.to_excel(writer, index=False, header=True, startrow=0)
        worksheet = writer.sheets['Sheet1']

        for row in range(1, len(df) + 2):
            for col in range(len(df.columns)):
                cell = worksheet.cell(row=row, column=col + 1)
                cell.alignment = Alignment(horizontal='center')

        for col in range(len(df.columns)):
            worksheet.column_dimensions[chr(ord('A') + col)].width = len(str(df.columns[col])) + 4

    print(f"Отчет '{report_name}' сохранен.")
    show_video_info(folder_path)


# настройки окна
window = tk.Tk()
window.title('Frame Counter')
window.geometry('420x300')
window.resizable(False, True)

# выбор папки
input_frame = tk.Frame(window)
input_frame.pack(side=tk.TOP, padx=10, pady=20)

folder_label = tk.Label(input_frame, text="Video Folder :")
folder_label.pack(side=tk.LEFT)

folder_entry = tk.Entry(input_frame, width=40)
folder_entry.insert(0, read_selected_folder())
folder_entry.pack(side=tk.LEFT)

button_browse = tk.Button(input_frame, text='Browse', width=6, height=1, command=browse_folder)
button_browse.pack(side=tk.RIGHT, padx=10)

# вывод данных
output_frame = tk.Frame(window)
output_frame.pack(side=tk.TOP, padx=20, pady=10)

text_area_frame = tk.Frame(output_frame)
text_area_frame.pack(fill=tk.BOTH, expand=True)

# Configure the nested frame to expand
output_frame.pack_configure(fill=tk.BOTH, expand=True)
text_area_frame.pack_configure(fill=tk.BOTH, expand=True)

info_text = tk.Text(text_area_frame, width=50, height=4)
info_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# кнопки управления
bottom_frame = tk.Frame(window)
bottom_frame.pack(side=tk.BOTTOM, padx=10, pady=20)

button_calculate = tk.Button(bottom_frame, text='Calculate', width=9, height=1, command=lambda: show_video_info(folder_entry.get()))
button_calculate.pack(side=tk.LEFT, padx=5)

button_create_xls = tk.Button(bottom_frame, text='Create XLS', width=9, height=1, command=create_excel_report)
button_create_xls.pack(side=tk.LEFT, padx=5)

current_folder = read_selected_folder()

window.minsize(420, 260)
window.mainloop()