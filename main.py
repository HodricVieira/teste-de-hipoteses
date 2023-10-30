import testes_de_hipotese as th
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox

coefficients_Ain = pd.read_csv('Coeficientes_ain.csv', sep=';', decimal=',')
critical_values_table = pd.read_csv('tabela_Wcrit.csv', sep=';', decimal=',')
critical_values_table = critical_values_table.drop(['Unnamed: 10'], axis=1)
critical_values_table = critical_values_table.drop(28)
# Convert the "tamanho n" column to integer type
critical_values_table["tamanho n"] = critical_values_table["tamanho n"].astype(int)

def kolmogorov_smirnov_window():
    def run_test():
        try:
            alpha = float(alpha_entry.get())
            data_values = np.random.normal(0,1,50)
            info , df = th.kolmogorov_smirnov(data_values, alpha)
            result_label.config(text=f"Resultado: {info},\n {df}")
        except:
            messagebox.showerror("Erro", "Dados inválidos")

    window = tk.Toplevel()
    window.title("Teste de Kolmogorov-Smirnov")
    window.geometry("400x200")



    alpha_label = tk.Label(window, text="Alpha:")
    alpha_label.pack()
    alpha_entry = tk.Entry(window)
    alpha_entry.pack()

    run_button = tk.Button(window, text="Executar", command=run_test)
    run_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

def shapiro_wilk_window():
    def run_test():
        try:
            alpha = float(alpha_entry.get())
            data_values = np.random.normal(0,1,29)
            info, df, df2 = th.shapiro_wilk(data_values, alpha, critical_values_table, coefficients_Ain)
            result_label.config(text=f"Resultado: {info},\n {df}\n {df2}")
        except:
            messagebox.showerror("Erro", "Dados inválidos")

    window = tk.Toplevel()
    window.title("Teste de Shapiro-Wilk")
    window.geometry("400x200")



    alpha_label = tk.Label(window, text="Alpha:")
    alpha_label.pack()
    alpha_entry = tk.Entry(window)
    alpha_entry.pack()

    run_button = tk.Button(window, text="Executar", command=run_test)
    run_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

def z_test_window():
    def run_test():
        try:
            alpha = float(alpha_entry.get())
            data_values = np.random.normal(0,1,29)
            is_normal, df = th.z_test(data_values, alpha, two_tailed=True)
            if is_normal:
                result_label.config(text="Resultado: Dados seguem distribuição normal")
            else:
                result_label.config(text="Resultado: Dados não seguem distribuição normal")
        except:
            messagebox.showerror("Erro", "Dados inválidos")

    window = tk.Toplevel()
    window.title("Teste Z")
    window.geometry("400x200")



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
            #data_values1 = [float(x) for x in data_entry1.get().split(',')]
            #data_values2 = [float(x) for x in data_entry2.get().split(',')]
            data_values1 = np.random.normal(0,1,50)
            data_values2 = np.random.normal(0,1,50)
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

def kolmogorov_smirnov_conf_window():
    def run_test():
        try:
            alpha = float(alpha_entry.get())
            qtd_h0 = 0
            qtd_h1 = 0
            lista_de_testes = []
            for i in range(15):
                data_values = np.random.normal(0, 1,50)
                is_normal , df = th.kolmogorov_smirnov(data_values, alpha)
                if is_normal == 0: #0 referente a H0 é siginifica que é uma dist. normal
                    lista_de_testes.append(0)
                    qtd_h0 += 1
                else:
                    lista_de_testes.append(1)
                    qtd_h1 += 1

            for i in range(15):
                data_values = np.random.poisson(1,29)
                is_normal, df = th.kolmogorov_smirnov(data_values, alpha)
                if is_normal == 0: #0 referente a H0 é siginifica que é uma dist. normal
                    lista_de_testes.append(0)
                    qtd_h0 += 1
                else:
                    lista_de_testes.append(1)
                    qtd_h1 += 1

            result_label.config(text=f"Resultado: {lista_de_testes}\nH0: {qtd_h0}\nH1: {qtd_h1}")
        except:
            messagebox.showerror("Erro", "Dados inválidos")

    window = tk.Toplevel()
    window.title("Teste de confiabilidade de Kolmogorov-Smirnov")
    window.geometry("400x200")

    alpha_label = tk.Label(window, text="Alpha:")
    alpha_label.pack()
    alpha_entry = tk.Entry(window)
    alpha_entry.pack()

    run_button = tk.Button(window, text="Executar", command=run_test)
    run_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

def shapiro_wilk_conf_window():
    def run_test():
        try:
            alpha = float(alpha_entry.get())
            qtd_h0 = 0
            qtd_h1 = 0
            lista_de_testes = []
            for i in range(15):
                data_values1 = np.random.normal(0, 1, 29)
                is_normal = th.shapiro_wilk(data_values1 , alpha, critical_values_table, coefficients_Ain)
                if is_normal: #0 referente a H0 é siginifica que é uma dist. normal
                    lista_de_testes.append(0)
                    qtd_h0 += 1
                else:
                    lista_de_testes.append(1)
                    qtd_h1 += 1

            for i in range(15):

                data_values3 = np.random.poisson(5, 29)
                is_normal = th.shapiro_wilk(data_values3, alpha, critical_values_table, coefficients_Ain)
                if is_normal: #0 referente a H0 é siginifica que é uma dist. normal
                    lista_de_testes.append(0)
                    qtd_h0 += 1
                else:
                    lista_de_testes.append(1)
                    qtd_h1 += 1

            result_label.config(text=f"Resultado: {lista_de_testes}\nH0: {qtd_h0}\nH1: {qtd_h1}")
        except:
            messagebox.showerror("Erro", "Dados inválidos")

    window = tk.Toplevel()
    window.title("Teste de confiabilidade de Shapiro-Wilk")
    window.geometry("400x200")

    alpha_label = tk.Label(window, text="Alpha:")
    alpha_label.pack()
    alpha_entry = tk.Entry(window)
    alpha_entry.pack()

    run_button = tk.Button(window, text="Executar", command=run_test)
    run_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

def main_window():
    def show_kolmogorov_smirnov_window():
        kolmogorov_smirnov_window()

    def show_shapiro_wilk_window():
        shapiro_wilk_window()

    def show_z_test_window():
        z_test_window()

    def show_independent_ttest_window():
        independent_ttest_window()

    def show_kolmogorov_smirnov_conf_window():
        kolmogorov_smirnov_conf_window()

    def show_shapiro_wilk_conf_window():
        shapiro_wilk_conf_window()

    root = tk.Tk()
    root.title("Testes de hipóteses")
    root.geometry("400x400")

    menu_label = tk.Label(root, text="Menu de operações:")
    menu_label.pack()

    kolmogorov_smirnov_button = tk.Button(root, text="Teste de Kolmogorov-Smirnov", command=show_kolmogorov_smirnov_window)
    kolmogorov_smirnov_button.pack()

    shapiro_wilk_button = tk.Button(root, text="Teste de Shapiro-Wilk", command=show_shapiro_wilk_window)
    shapiro_wilk_button.pack()

    z_test_button = tk.Button(root, text="Teste Z", command=show_z_test_window)
    z_test_button.pack()

    independent_ttest_button = tk.Button(root, text="Teste T de independência de médias", command=show_independent_ttest_window)
    independent_ttest_button.pack()

    kolmogorov_smirnov_conf_button = tk.Button(root, text="Teste de confiabilidade de Kolmogorov-Smirnov", command=show_kolmogorov_smirnov_conf_window)
    kolmogorov_smirnov_conf_button.pack()

    shapiro_wilk_conf_button = tk.Button(root, text="Teste de confiabilidade de Shapiro-Wilk", command=show_shapiro_wilk_conf_window)
    shapiro_wilk_conf_button.pack()

    exit_button = tk.Button(root, text="Sair", command=root.quit)
    exit_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

main_window()
