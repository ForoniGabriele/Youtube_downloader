import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import threading
from download import download 

def select_folder():
    folder = filedialog.askdirectory()

    if folder:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder)

def start_download_thread():
    url = url_entry.get()
    dir = folder_entry.get()

    if not url:
        messagebox.showerror("Errore", 'Inserire un URL!')
        return

    if not dir:
        messagebox.showerror("Errore", 'Inserire una cartella')
        return
    
    progress_bar['value'] = 0
    go_button.config(state=tk.DISABLED, text='Scaricando...')

    progress_callback_ui = lambda percent: root.after(0, update_progress, percent) # <-- AGGIUNTA

    download_thread = threading.Thread(
        target=lambda: actual_download_task(url, dir, progress_callback_ui)
    )
    download_thread.start()

def actual_download_task(url, dir, progress_callback=None):
    result = download(url, dir, progress_callback=progress_callback)

    if result is True:
        root.after(0, lambda:messagebox.showinfo("Successo", f"Download comletato! Salvato in {dir}"))
    else:
        root.after(0, lambda: messagebox.showerror("Errore di download", f"Impossibile scaricare. Errore: {result}"))
    
    root.after(0, lambda: go_button.config(state=tk.NORMAL, text='Go!'))

def update_progress(percent):
    """Aggiorna la progress bar sulla GUI (chiamato tramite root.after)."""
    progress_bar['value'] = percent
    root.update_idletasks()


root = tk.Tk()
root.title('Youtube downloader')
frm = ttk.Frame(root, padding="10 10 10 10")
frm.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

ttk.Label(frm, text="URL:").grid(column=0, row=0, sticky=tk.W, pady=5)
ttk.Label(frm, text="Cartella:").grid(column=0, row=1, sticky=tk.W, pady=5)

url_entry = ttk.Entry(frm, width=70) # Larghezza regolata
url_entry.grid(column=1, row=0, sticky=(tk.W, tk.E), padx=10)

folder_entry = ttk.Entry(frm, width=70)
folder_entry.insert(0, os.path.join(os.getcwd(), 'Yt_downloader')) 
folder_entry.grid(column=1, row=1, sticky=(tk.W, tk.E), padx=10)

go_button = ttk.Button(frm, text="Go!", command=start_download_thread)
go_button.grid(column=2, row=0, sticky=tk.W, padx=5)

browse_button = ttk.Button(frm, text="Sfoglia", command=select_folder)
browse_button.grid(column=2, row=1, sticky=tk.W, padx=5)

progress_bar = ttk.Progressbar(
    frm, 
    orient='horizontal', 
    length=300, 
    mode='determinate' # Uso 'determinate' per mostrare la percentuale precisa
)
progress_bar.grid(column=0, row=2, columnspan=3, pady=10, sticky=(tk.W, tk.E))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frm.columnconfigure(1, weight=1) # Permetti alla colonna dell'Entry di espandersi
root.mainloop()