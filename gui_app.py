import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from doc_loader import load_and_index_document
from rag_chain import build_rag_chain
from llm_model import load_mistral_model
from llm_model import load_flan_model

#hf_pipeline=load_mistral_model()
hf_pipeline = None

# Global vector DB
vectordb = None

def upload_pdf():
    global vectordb
    filepath = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if filepath:
        try:
            vectordb = load_and_index_document(filepath)
            messagebox.showinfo("Success", "PDF loaded and indexed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process PDF:\n{str(e)}")

def run_query():
    global vectordb, hf_pipeline

    if vectordb is None:
        messagebox.showwarning("Warning", "Please upload a PDF first.")
        return

    query = query_entry.get("1.0", tk.END).strip()
    if not query:
        messagebox.showwarning("Warning", "Please enter a query.")
        return

    # Lazy-load the model only when needed
    if hf_pipeline is None:
        try:
            response_text.delete("1.0", tk.END)
            response_text.insert(tk.END, "🔄 Loading model, please wait...\n")
            window.update_idletasks()

            #hf_pipeline = load_mistral_model()  # or any other model loader
            hf_pipeline= load_flan_model()
            response_text.insert(tk.END, "✅ Model loaded successfully!\n")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load LLM model:\n{str(e)}")
            return

    try:
        chain = build_rag_chain(vectordb, hf_pipeline)
        response = chain.run(query)
        response_text.delete("1.0", tk.END)
        response_text.insert(tk.END, response)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process query:\n{str(e)}")


def clear_query():
    query_entry.delete("1.0", tk.END)

# GUI setup
window = tk.Tk()
window.title("RAG + LLM Desktop App")
window.geometry("800x600")

# Upload PDF button
upload_button = tk.Button(window, text="📄 Upload PDF", command=upload_pdf)
upload_button.pack(pady=10)

# Query textbox
query_label = tk.Label(window, text="Enter your question:")
query_label.pack()
query_entry = scrolledtext.ScrolledText(window, height=4, width=100)
query_entry.pack()

# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)
ask_button = tk.Button(button_frame, text="🚀 Ask", command=run_query)
ask_button.pack(side=tk.LEFT, padx=10)
clear_button = tk.Button(button_frame, text="❌ Clear", command=clear_query)
clear_button.pack(side=tk.LEFT, padx=10)

# Response textbox
response_label = tk.Label(window, text="Answer:")
response_label.pack()
response_text = scrolledtext.ScrolledText(window, height=20, width=100)
response_text.pack()

# Start GUI
window.mainloop()
