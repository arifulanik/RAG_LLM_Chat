import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from doc_loader import load_and_index_document
from rag_chain import build_rag_chain
from llm_model import load_flan_model

def launch_tkinter_ui():
    hf_pipeline = None
    vectordb = None
    rag_chain = None

    chat_history = []  # list of (speaker, text) tuples

    def upload_pdf():
        nonlocal vectordb, rag_chain
        filepath = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if filepath:
            try:
                vectordb = load_and_index_document(filepath)
                messagebox.showinfo("Success", "PDF loaded and indexed successfully!")

                if hf_pipeline is not None:
                    rag_chain = build_rag_chain(vectordb, hf_pipeline)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to process PDF:\n{str(e)}")

    def run_query():
        nonlocal vectordb, hf_pipeline, rag_chain, chat_history

        query = query_entry.get("1.0", tk.END).strip()
        if not query:
            messagebox.showwarning("Warning", "Please enter a query.")
            return

        if hf_pipeline is None:
            try:
                response_text.config(state=tk.NORMAL)
                response_text.delete("1.0", tk.END)
                response_text.insert(tk.END, "🔄 Loading model, please wait...\n")
                window.update_idletasks()

                hf_pipeline = load_flan_model()
                response_text.insert(tk.END, "✅ Model loaded successfully!\n")

                rag_chain = build_rag_chain(vectordb, hf_pipeline)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load LLM model:\n{str(e)}")
                return

        if rag_chain is None:
            rag_chain = build_rag_chain(vectordb, hf_pipeline)

        try:
            response = rag_chain.invoke({"question": query})
            answer = response["answer"]

            chat_history.append(("You", query))
            chat_history.append(("Bot", answer))

            response_text.config(state=tk.NORMAL)
            response_text.delete("1.0", tk.END)

            for speaker, text in chat_history:
                if speaker == "You":
                    response_text.insert(tk.END, f"You: {text}\n")
                else:
                    response_text.insert(tk.END, f"Bot: {text}\n\n")

            response_text.config(state=tk.DISABLED)

            query_entry.delete("1.0", tk.END)
            response_text.see(tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process query:\n{str(e)}")

    def clear_query():
        query_entry.delete("1.0", tk.END)

    window = tk.Tk()
    window.title("RAG + LLM Desktop Chat")
    window.geometry("800x600")

    upload_button = tk.Button(window, text="📄 Upload PDF", command=upload_pdf)
    upload_button.pack(pady=10)

    query_label = tk.Label(window, text="Enter your question:")
    query_label.pack()
    query_entry = scrolledtext.ScrolledText(window, height=4, width=100)
    query_entry.pack()

    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)
    ask_button = tk.Button(button_frame, text="🚀 Ask", command=run_query)
    ask_button.pack(side=tk.LEFT, padx=10)
    clear_button = tk.Button(button_frame, text="❌ Clear", command=clear_query)
    clear_button.pack(side=tk.LEFT, padx=10)

    response_label = tk.Label(window, text="Conversation:")
    response_label.pack()
    response_text = scrolledtext.ScrolledText(window, height=20, width=100, state=tk.DISABLED)
    response_text.pack()

    window.mainloop()
