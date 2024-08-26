import tkinter as tk
from tkinter import ttk
from aila import get_chatbot_response  # aila.py dosyasındaki get_chatbot_response fonksiyonu
import time
from customtkinter import *

def select_style():
    tool = var.get()
    style = style_var.get()
    focus = focus_var.get()
    composition = composition_var.get()
    lighting = lighting_var.get()

    # Chatbotun cevabını al
    chatbot_response = get_chatbot_response(tool, style, focus, composition, lighting)

    # Cevabı arayüzde göster
    text_output.delete(1.0, tk.END)
    typewriter_effect(chatbot_response)

def clear_selection():
    var.set(0)
    style_var.set("dummy")
    focus_var.set("dummy")
    composition_var.set("dummy")
    lighting_var.set("dummy")
    text_output.delete(1.0, tk.END)
    print("Seçimler temizlendi.")

def typewriter_effect(text):
    for char in text:
        text_output.insert(tk.END, char)
        text_output.update()
        time.sleep(0.01)  # Karakterler arasında bekleme süresi

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(text_output.get(1.0, tk.END))
    root.update()  # Clipboardu güncelleyecek 

def handle_enter(event):
    user_input = text_output.get("1.0", tk.END).strip()
    if user_input:
        chatbot_response = get_chatbot_response(user_input, "", "", "", "")
        text_output.delete(1.0, tk.END)
        typewriter_effect(chatbot_response)

# Arayüz
root = tk.Tk()
root.title("Yapay Zeka Uygulaması")

# Arka plan resmi
background_image = tk.PhotoImage(file="bgimg.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

canvas = tk.Canvas(root, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Yapay Zeka Aracı Seçim Menüsü
frame_tool = tk.Frame(canvas)
frame_tool.grid(row=0, column=0, padx=10, pady=10)

tk.Label(frame_tool, text="Yapay Zeka Aracı Seçin:", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky=tk.W)

var = tk.IntVar()

tk.Radiobutton(frame_tool, text="Midjourney(stability.ai)", variable=var, value=1, anchor=tk.W).grid(row=1, column=0, sticky=tk.W)
tk.Radiobutton(frame_tool, text="Leonardo.ai", variable=var, value=2, anchor=tk.W).grid(row=2, column=0, sticky=tk.W)

# Tarz Seçim Menüsü
frame_style = tk.Frame(canvas)
frame_style.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame_style, text="Tarz Seçin:", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky=tk.W)

style_var = tk.StringVar(value="dummy")  

styles = ["Gerçekçi", "Anime", "3D animasyon", "Pastel", "Sanatsal", "Sinematik"]

row_index = 1
for style in styles:
    tk.Radiobutton(frame_style, text=style, variable=style_var, value=style, anchor=tk.W).grid(row=row_index, column=0, sticky=tk.W)
    row_index += 1

# Odak Noktası Seçim Menüsü
frame_focus = tk.Frame(canvas)
frame_focus.grid(row=0, column=2, padx=10, pady=10)

tk.Label(frame_focus, text="Odak Noktası Seçin:", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky=tk.W)

focus_var = tk.StringVar(value="dummy")  # Dummy değer olarak kullanılacak

focus_options = ["İnsan", "Hayvan", "Nesne", "Manzara"]

row_index = 1
for focus in focus_options:
    tk.Radiobutton(frame_focus, text=focus, variable=focus_var, value=focus, anchor=tk.W).grid(row=row_index, column=0, sticky=tk.W)
    row_index += 1

# Kompozisyon ve Açılar Seçim Menüsü
frame_composition = tk.Frame(canvas)
frame_composition.grid(row=0, column=3, padx=10, pady=10)

tk.Label(frame_composition, text="Kompozisyon ve Açılar Seçin:", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky=tk.W)

composition_var = tk.StringVar(value="dummy")  # Dummy değer olarak kullanılacak

composition_options = ["Merkezi Kompozisyon", "Geniş Açı", "Yakın Plan", "Portre", "Selfie", "Kuş Bakışı", "Alçak Plan", "Yüksek Plan"]

row_index = 1
for composition in composition_options:
    tk.Radiobutton(frame_composition, text=composition, variable=composition_var, value=composition, anchor=tk.W).grid(row=row_index, column=0, sticky=tk.W)
    row_index += 1

# Işıklandırma Seçim Menüsü
frame_lighting = tk.Frame(canvas)
frame_lighting.grid(row=0, column=4, padx=10, pady=10)

tk.Label(frame_lighting, text="Işıklandırma Seçin:", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky=tk.W)

lighting_var = tk.StringVar(value="dummy")  # Dummy değer olarak kullanılacak

lighting_options = ["Stüdyo Işığı", "Yumuşak (Loş) Aydınlatma", "Doğal(Gün) Işığı", "Neon Işıklar", "Şehir Işıkları", "Mum Işığı"]

row_index = 1
for lighting in lighting_options:
    tk.Radiobutton(frame_lighting, text=lighting, variable=lighting_var, value=lighting, anchor=tk.W).grid(row=row_index, column=0, sticky=tk.W)
    row_index += 1

# Seç ve Temizle 
button_select = ttk.Button(root, text="Seç", command=select_style)
button_select.grid(row=1, column=1, pady=10, padx=(50, 5), sticky="E")

button_clear = ttk.Button(root, text="Temizle", command=clear_selection)
button_clear.grid(row=1, column=2, pady=10, padx=(5, 50), sticky="W")

# Chatbotun cevabını göstermek için bir metin kutusu
text_output = tk.Text(root, wrap=tk.WORD, width=60, height=10, fg="green2", bg="black")
text_output.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Kopyalama butonu
button_copy = ttk.Button(root, text="Kopyala", command=copy_to_clipboard)
button_copy.grid(row=2, column=3, padx=5, pady=10)

# Enter tuşuna basıldığında handle_enter işlevini çağırma
text_output.bind("<Return>", handle_enter)

root.mainloop()
