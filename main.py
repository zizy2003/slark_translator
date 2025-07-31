import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random
from slark_translator import LeetTransliterator
from PIL import Image, ImageTk
from itertools import count



class SlarkTranslatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🐟 Slark Translator v1.0 🐟")
        self.root.geometry("1080x1080")
        self.root.configure(bg="#0a1428")
        self.root.resizable(False, False)
        self.fullscreen = False
        self.current_lang = "en"
        self.root.bind("<Escape>", lambda event: self.exit_fullscreen())
        self.quotes_eng = [
            "\"I'll gut them like fish!\" - Slark",
            "\"The deep calls.\" - Slark",
            "\"From the depth I come!\" - Slark",
            "\"Dark waters run deep.\" - Slark",
            "\"Design and code by Alexey Irnapasenko. Structure borrowed from Alexey Xiaomi.\""
        ]
        
        self.quotes_ru = [
            
            "\"Slark положил на тебя глаз.\" - Slark",
            "\"Узник пучины.\" - Slark",
            "\"Лучше бы я остался в Тёмном рифе.\" - Slark",
            "\"О-хо-хо-хо нет, меня на крючок не возьмёшь!\" - Slark",
            "\"Дизайн и код написан Алексеем Ирнапасенко. Структура позаимствована у Алексея Ксяоми. \""
        ]
        self.translations = {
    "en": {
        "title": "🐟 SLARK_TRANSLATOR 🐟",
        "subtitle": "\"Dark Reef Prison can't hold my nickname\" - Slark, 2025",
        "enter_nickname": "Enter a nickname for translation:",
        "generate": "⚔️ GENERATE COMBINATIONS ⚔️",
        "clear": "🗑️ CLEAR",
        "results": "Translation results:",
        "ready": "Slark ready to work!",
        "cleared": "Cleared!",
        "warning": "Enter your nickname for translation!",
        "info": "Better works with russian nicknames!",
        "generated": "✅ Generated {count} epic combinations!",
        "switch_lang": "🌍 EN ↔ RU",
        "warning_title": "Attention!",
        "advice": "💡 Advice: use Ctrl+A to higlight all options!",
        "options": "🎮 Options for:",
        "fullscreen_option" : "🖥 Fullscreen"
    },
    "ru": {
        "title": "🐟 СЛАРК_ТРАНСЛИТ 🐟",
        "subtitle": "\"Темница Глубокой Пучины не удержит мой ник\" – Сларк, 2025",
        "enter_nickname": "Введите никнейм для перевода:",
        "generate": "⚔️ СГЕНЕРИРОВАТЬ ВАРИАНТЫ ⚔️",
        "clear": "🗑️ ОЧИСТИТЬ",
        "results": "Результаты перевода:",
        "ready": "Сларк готов к работе!",
        "cleared": "Очищено. Человек.",
        "warning": "Введите никнейм для перевода!",
        "info": "Лучше работает с русскими никами!",
        "generated": "✅ Сгенерировано {count} эпичных т̷р̴а̶н̴с̵л̵и̴т̶о̷в̴",
        "switch_lang": "🌍 RU ↔ EN",
        "warning_title": "Внимание!",
        "advice": "💡 Подсказка: используйте Ctrl+A чтобы выделить все возможные варианты!",
        "options": "🎮 Варианты для:",
        "fullscreen_option" : "🖥 Полноэкранный режим"

    }
}
  

    






        self.slark_translator = LeetTransliterator()
        
        self.setup_gui()
    def fullscreen_toggle(self):
        self.fullscreen = not self.fullscreen
        self.root.attributes("-fullscreen", self.fullscreen)    
        self.reposition_button()
    
        if not self.fullscreen:
            self.root.geometry('1080x1080')
            
    def reposition_button(self):
        if self.fullscreen:
            self.fullscreen_button.place(x=self.root.winfo_screenwidth() - 250, y=20)
        else:
            self.fullscreen_button.place(x=840, y=20)
        
        
    
    def exit_fullscreen(self):
        if self.fullscreen:
            self.fullscreen = False
            self.root.attributes("-fullscreen", False)
            self.root.geometry('1080x1080')
            self.reposition_button()
    
    def toggle_language(self):
        self.current_lang = "ru" if self.current_lang == "en" else "en"
        self.refresh_ui()
        
    def setup_gui(self):
     self.bg_anim = AnimatedGIF(self.root, "slark_background.gif", 1080, 1080)
     main_frame = tk.Frame(self.root, bg="#0a1428")
     main_frame.pack(fill="both", expand=True, padx=20, pady=20)

     self.lang_button = tk.Button(
        self.root,
        text=self.tr("switch_lang"),
        font=("Arial", 12, "bold"),
        bg="#444444",
        fg="#FFFFFF",
        activebackground="#666666",
        command=self.toggle_language
     )
     self.lang_button.place(x=20, y=20)
     
     self.fullscreen_button = tk.Button(
       self.root,
       text = self.tr("fullscreen_option"),
       font=("Arial", 12, "bold"),
       bg="#444444",
       fg="#FFFFFF",
       activebackground="#666666",
       command=self.fullscreen_toggle
         
         
     )
     self.reposition_button()

     self.title_label = tk.Label(
        main_frame,
        text=self.tr("title"),
        font=("Arial Black", 20, "bold"),
        fg="#FFD700",
        bg="#0a1428"
     )
     self.title_label.pack(pady=(0, 20))

     self.subtitle_label = tk.Label(
        main_frame,
        text=self.tr("subtitle"),
        font=("Arial", 10, "italic"),
        fg="#87CEEB",
        bg="#0a1428"
     )
     self.subtitle_label.pack(pady=(0, 30))

     input_frame = tk.Frame(main_frame, bg="#0a1428")
     input_frame.pack(fill="x", pady=(0, 20))

     self.input_label = tk.Label(
        input_frame,
        text=self.tr("enter_nickname"),
        font=("Arial", 12, "bold"),
        fg="#FFFFFF",
        bg="#0a1428"
     )
     self.input_label.pack(anchor="w")

     self.input_entry = tk.Entry(
        input_frame,
        font=("Arial", 14),
        bg="#1e3a5f",
        fg="#FFFFFF",
        insertbackground="#FFD700",
        relief="solid",
        bd=2,
        width=50
     )
     self.input_entry.pack(fill="x", pady=(5, 0))
     self.input_entry.bind("<Return>", lambda e: self.generate_variants())

     button_frame = tk.Frame(main_frame, bg="#0a1428")
     button_frame.pack(pady=20)

     self.generate_button = tk.Button(
        button_frame,
        text=self.tr("generate"),
        font=("Arial Black", 12, "bold"),
        bg="#2E8B57",
        fg="#FFFFFF",
        activebackground="#32CD32",
        activeforeground="#FFFFFF",
        relief="raised",
        bd=3,
        command=self.generate_variants,
        cursor="hand2"
     )
     self.generate_button.pack(side="left", padx=10)

     self.clear_button = tk.Button(
        button_frame,
        text=self.tr("clear"),
        font=("Arial", 10, "bold"),
        bg="#8B0000",
        fg="#FFFFFF",
        activebackground="#FF0000",
        activeforeground="#FFFFFF",
        relief="raised",
        bd=2,
        command=self.clear_all,
        cursor="hand2"
     )
     self.clear_button.pack(side="left", padx=10)

     self.results_label = tk.Label(
        main_frame,
        text=self.tr("results"),
        font=("Arial", 12, "bold"),
        fg="#FFFFFF",
        bg="#0a1428"
     )
     self.results_label.pack(anchor="w", pady=(10, 0))
     self.results_text = scrolledtext.ScrolledText(
        main_frame,
        height=15,
        font=("Courier New", 11),
        bg="#1e3a5f",
        fg="#00FF00",
        insertbackground="#FFD700",
        selectbackground="#FFD700",
        selectforeground="#000000",
        relief="solid",
        bd=2,
        wrap="word"
     )
     self.results_text.pack(fill="both", expand=True, pady=(0, 10))

     self.stats_label = tk.Label(
        main_frame,
        text=self.tr("ready"),
        font=("Arial", 10),
        fg="#87CEEB",
        bg="#0a1428"
     )
     self.stats_label.pack()

     self.add_easter_eggs()
        
    def add_easter_eggs(self):
        self.root.after(5000,self.random_quote)
    def random_quote(self):
            quotes = self.quotes_ru if self.current_lang == 'ru' else self.quotes_eng
            quote = random.choice(quotes)
            self.stats_label.config(text=quote)
            self.root.after(10000, self.random_quote)  
            

    def generate_variants(self):
        nickname = self.input_entry.get().strip()
    
        if not nickname:
         messagebox.showwarning(self.tr("warning_title"), self.tr("warning"))
         return

        if not any(ord(char) >= 1040 and ord(char) <= 1103 for char in nickname):
         messagebox.showinfo("Info", self.tr("info"))

        self.generate_button.config(state="disabled", text=self.tr("generate"))
        self.root.update()

        try:
         variants = self.slark_translator.generate_all_variants(nickname)

         self.results_text.delete(1.0, tk.END)
         self.results_text.insert(tk.END, f"{self.tr('options')}'{nickname}':\n\n")

         for i, variant in enumerate(variants, 1):
            self.results_text.insert(tk.END, f"{i:3d}. {variant}\n")

         self.results_text.insert(tk.END, f"\n{self.tr('generated', count=len(variants))}\n")
         self.results_text.insert(tk.END, f"{self.tr('advice')}\n")

         self.stats_label.config(text=self.tr("generated", count=len(variants)))

        except Exception as e:
         messagebox.showerror("Error", f"An error occurred: {str(e)}")

        finally:
         self.generate_button.config(state="normal", text=self.tr("generate"))
    
    def clear_all(self):
     self.input_entry.delete(0, tk.END)
     self.results_text.delete(1.0, tk.END)
     self.stats_label.config(text=self.tr("cleared"))

    def tr(self, key, **kwargs):
         text = self.translations[self.current_lang].get(key, key)
         return text.format(**kwargs) if kwargs else text 
    
    def refresh_ui(self):
     self.lang_button.config(text=self.tr("switch_lang"))
     self.title_label.config(text=self.tr("title"))
     self.subtitle_label.config(text=self.tr("subtitle"))
     self.input_label.config(text=self.tr("enter_nickname"))
     self.generate_button.config(text=self.tr("generate"))
     self.clear_button.config(text=self.tr("clear"))
     self.results_label.config(text=self.tr("results"))
     self.stats_label.config(text=self.tr("ready"))
     self.fullscreen_button.config(text=self.tr("fullscreen_option"))
     self.random_quote()

    def toggle_language(self):
        self.current_lang = "ru" if self.current_lang == "en" else "en"
        self.refresh_ui()

class AnimatedGIF:
    def __init__(self, parent, gif_path, width, height, alpha=0.5):
        self.parent = parent
        self.gif = Image.open(gif_path)
        self.frames = []
        self.alpha = alpha

        try:
            for i in count(0):
                self.gif.seek(i)
                frame = self.gif.copy().convert("RGBA").resize((width, height), Image.Resampling.LANCZOS)
                frame = self.apply_alpha(frame, self.alpha)
                self.frames.append(ImageTk.PhotoImage(frame))
        except EOFError as F:
            print(f"En error occured:{F}")

        self.label = tk.Label(parent, bg="#0a1428")
        self.label.place(x=0, y=0, relwidth=1, relheight=1)

        self.index = 0
        self.animate()

    def apply_alpha(self, img, alpha):
        r, g, b, a = img.split()
        a = a.point(lambda p: int(p * alpha))
        return Image.merge('RGBA', (r, g, b, a))

    def animate(self):
        if self.frames:
            self.label.configure(image=self.frames[self.index])
            self.index = (self.index + 1) % len(self.frames)
            self.parent.after(100, self.animate)
def main():
    root = tk.Tk()
    app = SlarkTranslatorGUI(root)
    
    try:
        root.iconbitmap(default="slark.ico")  
    except:
        pass 
        
    root.mainloop()

if __name__ == "__main__":
    main()
