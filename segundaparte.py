import tkinter as tk
import numpy as np
import testes_de_hipotese as th
from tkinter import messagebox

def z_test_window():
    def run_test():
        try:
            alpha = float(alpha_entry.get())
            media_sup = float(media_sup_entry.get())
            media_par = float(media_par_entry.get())
            desvio_par = float(desvio_par_entry.get())
            data_values = np.random.normal(media_par, desvio_par, 29)
            info = th.z_test(data_values, media_sup, alpha, two_tailed=True)
            result_label.config(text=f"Resultado: {info}")
        except:
            messagebox.showerror("Erro", "Dados inválidos")

    window = tk.Toplevel()
    window.title("Teste Z")
    window.geometry("400x300")

    media_par_label = tk.Label(window, text="Média para random.normal:")
    media_par_label.pack()
    media_par_entry = tk.Entry(window)
    media_par_entry.pack()

    desvio_par_label = tk.Label(window, text="Desvio para random.normal:")
    desvio_par_label.pack()
    desvio_par_entry = tk.Entry(window)
    desvio_par_entry.pack()

    media_sup_label = tk.Label(window, text="Média Suposta:")
    media_sup_label.pack()
    media_sup_entry = tk.Entry(window)
    media_sup_entry.pack()

    alpha_label = tk.Label(window, text="Alpha:")
    alpha_label.pack()
    alpha_entry = tk.Entry(window)
    alpha_entry.pack()

    run_button = tk.Button(window, text="Executar", command=run_test)
    run_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

########################################################################################

def independent_ttest_window():
    def run_test():
        try:
            alpha = float(alpha_entry.get())
            media_par1 = float(media_par_entry1.get())
            desvio_par1 = float(desvio_par_entry1.get())
            media_par2 = float(media_par_entry2.get())
            desvio_par2 = float(desvio_par_entry2.get())
            data_values1 = np.random.normal(media_par1, desvio_par1, 50)
            data_values2 = np.random.normal(media_par2, desvio_par2, 50)
            info, df = th.independent_ttest(data_values1, data_values2, alpha)
            result_label.config(text=f"Resultado: {info} \n {df}")
        except:
            messagebox.showerror("Erro", "Dados inválidos")

    window = tk.Toplevel()
    window.title("Teste T de independência de médias")
    window.geometry("400x400")

    media_par_label1 = tk.Label(window, text="Média para random.normal 1:")
    media_par_label1.pack()
    media_par_entry1 = tk.Entry(window)
    media_par_entry1.pack()

    desvio_par_label1 = tk.Label(window, text="Desvio para random.normal 1:")
    desvio_par_label1.pack()
    desvio_par_entry1 = tk.Entry(window)
    desvio_par_entry1.pack()

    media_par_label2 = tk.Label(window, text="Média para random.normal 2:")
    media_par_label2.pack()
    media_par_entry2 = tk.Entry(window)
    media_par_entry2.pack()

    desvio_par_label2 = tk.Label(window, text="Desvio para random.normal 2:")
    desvio_par_label2.pack()
    desvio_par_entry2 = tk.Entry(window)
    desvio_par_entry2.pack()

    alpha_label = tk.Label(window, text="Alpha:")
    alpha_label.pack()
    alpha_entry = tk.Entry(window)
    alpha_entry.pack()

    run_button = tk.Button(window, text="Executar", command=run_test)
    run_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

###################################################################################

def t_test_single_sample_window():
    def run_test():
        try:
            alpha = float(alpha_entry.get())
            mu = float(mu_entry.get())
            media_par = float(media_par_entry.get())
            desvio_par = float(desvio_par_entry.get())
            data_values = np.random.normal(media_par, desvio_par, 50)
            info = th.t_test_single_sample(data_values, mu, alpha)
            result_label.config(text=f"Resultado: {info}")
        except:
            messagebox.showerror("Erro", "Dados inválidos")

    window = tk.Toplevel()
    window.title("Teste T de uma Amostra")
    window.geometry("400x300")

    media_par_label = tk.Label(window, text="Média para random.normal:")
    media_par_label.pack()
    media_par_entry = tk.Entry(window)
    media_par_entry.pack()

    desvio_par_label = tk.Label(window, text="Desvio para random.normal:")
    desvio_par_label.pack()
    desvio_par_entry = tk.Entry(window)
    desvio_par_entry.pack()

    mu_label = tk.Label(window, text="Média Suposta:")
    mu_label.pack()
    mu_entry = tk.Entry(window)
    mu_entry.pack()

    alpha_label = tk.Label(window, text="Alpha:")
    alpha_label.pack()
    alpha_entry = tk.Entry(window)
    alpha_entry.pack()

    run_button = tk.Button(window, text="Executar", command=run_test)
    run_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

#######################################################################################

def t_test_two_independent_samples_window():
    def run_test():
        try:
            alpha = float(alpha_entry.get())
            media_par1 = float(media_par_entry1.get())
            desvio_par1 = float(desvio_par_entry1.get())
            media_par2 = float(media_par_entry2.get())
            desvio_par2 = float(desvio_par_entry2.get())
            data_values1 = np.random.normal(media_par1, desvio_par1, 50)
            data_values2 = np.random.normal(media_par2, desvio_par2, 50)
            result, df = th.t_test_two_independent_samples(data_values1, data_values2, alpha)
            result_label.config(text=f"Resultado: {result} \n {df}")
        except:
            messagebox.showerror("Erro", "Dados inválidos")

    window = tk.Toplevel()
    window.title("Teste T de Duas Amostras Independentes")
    window.geometry("400x400")

    media_par_label1 = tk.Label(window, text="Média para random.normal 1:")
    media_par_label1.pack()
    media_par_entry1 = tk.Entry(window)
    media_par_entry1.pack()

    desvio_par_label1 = tk.Label(window, text="Desvio para random.normal 1:")
    desvio_par_label1.pack()
    desvio_par_entry1 = tk.Entry(window)
    desvio_par_entry1.pack()

    media_par_label2 = tk.Label(window, text="Média para random.normal 2:")
    media_par_label2.pack()
    media_par_entry2 = tk.Entry(window)
    media_par_entry2.pack()

    desvio_par_label2 = tk.Label(window, text="Desvio para random.normal 2:")
    desvio_par_label2.pack()
    desvio_par_entry2 = tk.Entry(window)
    desvio_par_entry2.pack()

    alpha_label = tk.Label(window, text="Alpha:")
    alpha_label.pack()
    alpha_entry = tk.Entry(window)
    alpha_entry.pack()

    run_button = tk.Button(window, text="Executar", command=run_test)
    run_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

#################################################################################

def bartlett_test_window():
    def run_test():
        try:
            alpha = float(alpha_entry.get())
            media_par1 = float(media_par_entry1.get())
            desvio_par1 = float(desvio_par_entry1.get())
            media_par2 = float(media_par_entry2.get())
            desvio_par2 = float(desvio_par_entry2.get())
            data_values1 = np.random.normal(media_par1, desvio_par1, 50)
            data_values2 = np.random.normal(media_par2, desvio_par2, 50)
            info, df = th.bartlett_test(alpha, data_values1, data_values2)
            result_label.config(text=f"Resultad0 {info} \n {df}")
        except:
            messagebox.showerror("Erro", "Dados inválidos")

    window = tk.Toplevel()
    window.title("Teste de Bartlett")
    window.geometry("400x400")

    media_par_label1 = tk.Label(window, text="Média para random.normal 1:")
    media_par_label1.pack()
    media_par_entry1 = tk.Entry(window)
    media_par_entry1.pack()

    desvio_par_label1 = tk.Label(window, text="Desvio para random.normal 1:")
    desvio_par_label1.pack()
    desvio_par_entry1 = tk.Entry(window)
    desvio_par_entry1.pack()

    media_par_label2 = tk.Label(window, text="Média para random.normal 2:")
    media_par_label2.pack()
    media_par_entry2 = tk.Entry(window)
    media_par_entry2.pack()

    desvio_par_label2 = tk.Label(window, text="Desvio para random.normal 2:")
    desvio_par_label2.pack()
    desvio_par_entry2 = tk.Entry(window)
    desvio_par_entry2.pack()

    alpha_label = tk.Label(window, text="Alpha:")
    alpha_label.pack()
    alpha_entry = tk.Entry(window)
    alpha_entry.pack()

    run_button = tk.Button(window, text="Executar", command=run_test)
    run_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

#####################################################################################

def main_window():
    root = tk.Tk()
    root.title("Testes de hipóteses")
    root.geometry("400x400")

    menu_label = tk.Label(root, text="Menu de operações:")
    menu_label.pack()

    z_test_button = tk.Button(root, text="Teste Z", command=z_test_window)
    z_test_button.pack()

    independent_ttest_button = tk.Button(root, text="Teste T de independência de médias", command=independent_ttest_window)
    independent_ttest_button.pack()

    t_test_single_sample_button = tk.Button(root, text="Teste T de uma Amostra", command=t_test_single_sample_window)
    t_test_single_sample_button.pack()

    t_test_two_independent_samples_button = tk.Button(root, text="Teste T de Duas Amostras Independentes", command=t_test_two_independent_samples_window)
    t_test_two_independent_samples_button.pack()

    bartlett_test_button = tk.Button(root, text="Teste de Bartlett", command=bartlett_test_window)
    bartlett_test_button.pack()

    exit_button = tk.Button(root, text="Sair", command=root.quit)
    exit_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

main_window()
