from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import *

import bs4  # Beautiful Soup - for parsing html content
import googlesearch  # for accessing Google search
import googletrans  # for accessing Google translate
import html_text  # for extracting visible text from html content
import requests  # for downloading a web page
import wikipedia  # for accessing Wikipedia pages


def google_search(event=None):
    query = query_txt.get()
    search_results = []
    for search_result in googlesearch.search(query, stop=5, num=1, pause=2):
        print(search_result)
        search_results.append(search_result)
    combo["values"] = search_results
    combo.current(0)
    load_combobox_selection(None)


def load_combobox_selection(event=None):
    url = combo.get()
    url_output.set(url)
    load_webpage_text(url)


def wikipedia_lookup():
    query = query_txt.get()
    url = wikipedia.page(query).url
    url_output.set(url)
    results = wikipedia.summary(query, sentences=2)
    update_output_txt(results)


def load_url_text(event):
    url = url_txt.get()
    if not url.startswith("http"):
        url = "https://" + url  # guess at https
        url_output.set(url)
    load_webpage_text(url)


def load_webpage_text(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    text = html_text.extract_text(str(soup))
    update_output_txt(text)


def update_output_txt(text):
    output_txt.delete(1.0, END)
    output_txt.insert(1.0, text)


def google_translate():
    text = output_txt.get(1.0, END)
    if len(text) > 5000:
        messagebox.showwarning("Warning", "Google translate character limit exceeded - trimming to 5000.")
        text = text[:5000]
    translator = googletrans.Translator()
    input_language = translator.detect(text).lang
    input_lang.set(googletrans.LANGUAGES[input_language])
    translation_language = trans_lang.get()
    translation = translator.translate(text, src=input_language, dest=translation_language)
    update_output_txt(translation.text)


window = Tk()
window.geometry("520x430")
window.title("Web inSite")

row_counter = 0

lbl = Label(window, text="Search", font=("Arial Bold", 16))
lbl.grid(column=0, row=row_counter, columnspan=3, sticky="W")

row_counter += 1

lbl = Label(window, text="Query:", font=("Arial Bold", 10))
lbl.grid(column=0, row=row_counter, sticky="E", padx=5, pady=5)

query_txt = Entry(window, width=65)
query_txt.bind('<Return>', google_search)
query_txt.grid(column=1, columnspan=6, row=row_counter, sticky="W", padx=5, pady=5)

row_counter += 1

toolbar = Frame(window)
toolbar.grid(column=1, row=row_counter, columnspan=6)

btn = Button(toolbar, text="Google", command=google_search)
btn.grid(column=0, row=0, padx=5, pady=5)

combo = Combobox(toolbar)
combo.bind("<<ComboboxSelected>>", load_combobox_selection)
combo["values"] = [""]
combo.current(0)
combo.grid(column=1, row=0, padx=5, pady=5)

btn = Button(toolbar, text="Wikipedia", command=wikipedia_lookup)
btn.grid(column=2, row=0, padx=5, pady=5)

row_counter += 1

lbl = Label(window, text="URL:", font=("Arial Bold", 10))
lbl.grid(column=0, row=row_counter, sticky="E", padx=5, pady=5)

url_output = StringVar()

url_txt = Entry(window, width=65, textvariable=url_output)
url_txt.bind('<Return>', load_url_text)
url_txt.grid(column=1, columnspan=6, row=row_counter, sticky="W", padx=5, pady=5)

row_counter += 1

lbl = Label(window, text="Content", font=("Arial Bold", 16))
lbl.grid(column=0, row=row_counter, columnspan=3, sticky="W")

row_counter += 1

output_txt = scrolledtext.ScrolledText(window, width=60, height=10, wrap=WORD)
output_txt.grid(column=0, row=row_counter, columnspan=7, sticky="W", padx=5, pady=5)

row_counter += 1

lbl = Label(window, text="Processing", font=("Arial Bold", 16))
lbl.grid(column=0, row=row_counter, columnspan=3, sticky="W")

row_counter += 1

btn = Button(window, text="Translate", command=google_translate)
btn.grid(column=0, row=row_counter, sticky="W", padx=5, pady=5)

languages = list(googletrans.LANGUAGES.values())

input_lang = Combobox(window, values=languages, width=25, state="disabled")
input_lang.grid(column=1, columnspan=3, row=row_counter, padx=5, pady=5)
input_lang.set("detected input language")

trans_lang = Combobox(window, values=languages, width=25)
trans_lang.grid(column=4, columnspan=3, row=row_counter, padx=5, pady=5)
trans_lang.set("choose output language")

window.mainloop()
