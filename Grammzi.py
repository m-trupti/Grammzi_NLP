import tkinter
import tkinter.messagebox
import customtkinter

from happytransformer import  HappyTextToText
from happytransformer import TTSettings
from spellchecker import SpellChecker

happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
beam_settings =  TTSettings(num_beams=5, min_length=1, max_length=100)
spell = SpellChecker()

customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Grammzi : Grammar Checker")
root.geometry(f"{800}x{520}")
root.resizable(0,0)

root.grid_columnconfigure(1, weight=1)

userentry = customtkinter.CTkEntry(root, placeholder_text="Enter Text to Check for Grammatical Errors")
userentry.grid(row=3, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

def correct_gram():
    input_text = userentry.get()

    misspelled = spell.unknown(input_text.split())
    for word in misspelled:
        corrected_word = spell.correction(word)
        input_text = input_text.replace(word, corrected_word)
    final_input = "grammar: " + input_text

    output_text = happy_tt.generate_text(final_input, args=beam_settings)
    output_text = happy_tt.generate_text(input_text, args=beam_settings)
    output_tbox.insert("0.0",output_text)

def delete_text():
    output_tbox.delete("0.0","end")

main_button_1 = customtkinter.CTkButton(master=root, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Check Grammar", command=correct_gram)
main_button_1.grid(row=3, column=2, padx=(10, 10), pady=(20, 20), sticky="nsew")

del_button = customtkinter.CTkButton(master=root, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Delete Contents of Textbox", command=delete_text)
del_button.grid(row=6, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

output_tbox = customtkinter.CTkTextbox(master=root)
output_tbox.grid(row=5, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

if __name__ == "__main__":
    root.mainloop()
