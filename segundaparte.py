import tkinter as tk
import numpy as np
import testes_de_hipotese as th
from tkinter import messagebox

def z_test_window():
    def run_test():
        try:
            alpha = float(alpha_entry.get())
            media_sup = float(media_sup_entry.get())
            data_values = np.random.normal(10, 1, 29)  # média = 10
            info = th.z_test(data_values, media_sup, alpha, two_tailed=True)
            result_label.config(text=f"Resultado: {info}")
        except:
            messagebox.showerror("Erro", "Dados inválidos")

    window = tk.Toplevel()
    window.title("Teste Z")
    window.geometry("400x200")

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

def independent_ttest_window():
    def run_test():
        try:
            alpha = float(alpha_entry.get())
            data_values1 = np.random.normal(0, 1, 50)
            data_values2 = np.random.normal(0, 1, 50)
            th.independent_ttest(data_values1, data_values2, alpha)
            result_label.config(text="Resultado: Verificar console")
        except:
            messagebox.showerror("Erro", "Dados inválidos")

    window = tk.Toplevel()
    window.title("Teste T de independência de médias")
    window.geometry("400x300")

    alpha_label = tk.Label(window, text="Alpha:")
    alpha_label.pack()
    alpha_entry = tk.Entry(window)
    alpha_entry.pack()

    run_button = tk.Button(window, text="Executar", command=run_test)
    run_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

def t_test_single_sample_window():
    def run_test():
        try:
            alpha = float(alpha_entry.get())
            mu = float(mu_entry.get())
            data_values = np.random.normal(0, 1, 50)
            t_stat, p_value, result = th.t_test_single_sample(data_values, mu, alpha)
            result_label.config(text=f"t_stat: {t_stat}\n p_value: {p_value}\n Result: {result}")
        except:
            messagebox.showerror("Erro", "Dados inválidos")

    window = tk.Toplevel()
    window.title("Teste T de uma Amostra")
    window.geometry("400x200")

    mu_label = tk.Label(window, text="Média Populacional (μ):")
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

def t_test_two_independent_samples_window():
    def run_test():
        try:
            alpha = float(alpha_entry.get())
            data_values1 = np.random.normal(0, 1, 50)
            data_values2 = np.random.normal(1, 1, 50)
            t_stat, p_value, result = th.t_test_two_independent_samples(data_values1, data_values2, alpha)
            result_label.config(text=f"t_stat: {t_stat}\n p_value: {p_value}\n Result: {result}")
        except:
            messagebox.showerror("Erro", "Dados inválidos")

    window = tk.Toplevel()
    window.title("Teste T de Duas Amostras Independentes")
    window.geometry("400x200")

    alpha_label = tk.Label(window, text="Alpha:")
    alpha_label.pack()
    alpha_entry = tk.Entry(window)
    alpha_entry.pack()

    run_button = tk.Button(window, text="Executar", command=run_test)
    run_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

def bartlett_test_window():
    def run_test():
        try:
            data_values1 = np.random.normal(0, 1, 50)
            data_values2 = np.random.normal(1, 1, 50)
            chi2_stat, p_value = th.bartlett_test(data_values1, data_values2)
            result_label.config(text=f"Chi2_stat: {chi2_stat}\n p_value: {p_value}")
        except:
            messagebox.showerror("Erro", "Dados inválidos")

    window = tk.Toplevel()
    window.title("Teste de Bartlett")
    window.geometry("400x200")


    run_button = tk.Button(window, text="Executar", command=run_test)
    run_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

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
