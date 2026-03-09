import tkinter as tk
from tkinter import messagebox
from CRC_calculator import crc_generic

def compute_crc():
    data_bits = data_entry.get().strip()
    poly_bits = poly_entry.get().strip()
    if not data_bits or not poly_bits:
        messagebox.showerror("Error", "Please enter both data and polynomial")
        return
    if any(c not in '01' for c in data_bits+poly_bits):
        messagebox.showerror("Error", "Only binary digits (0 or 1) allowed")
        return
    crc = crc_generic(data_bits, poly_bits)
    result_var.set(crc)

root = tk.Tk()
root.title("CRC Calculator")

tk.Label(root, text="Data (binary):").grid(row=0, column=0, sticky="w")
data_entry = tk.Entry(root, width=30)
data_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Polynomial (binary):").grid(row=1, column=0, sticky="w")
poly_entry = tk.Entry(root, width=30)
poly_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Compute CRC", command=compute_crc).grid(row=2, column=0, columnspan=2, pady=10)

tk.Label(root, text="CRC Remainder:").grid(row=3, column=0, sticky="w")
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=30, state="readonly").grid(row=3, column=1, padx=5, pady=5)

root.mainloop()