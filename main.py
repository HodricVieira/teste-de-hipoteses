import testes_de_hipotese as th
import pandas as pd
import numpy as np

coefficients_Ain = pd.read_csv('Coeficientes_ain.csv', sep=';', decimal=',')
critical_values_table = pd.read_csv('tabela_Wcrit.csv', sep=';', decimal=',')
critical_values_table = critical_values_table.drop(['Unnamed: 10'], axis=1)
critical_values_table = critical_values_table.drop(28)
# Convert the "tamanho n" column to integer type
critical_values_table["tamanho n"] = critical_values_table["tamanho n"].astype(int)

primeira_execucao = True
while True:
    print("_________________________________________________________________\n")
    print("Menu de operações:\n"
                    '(1) Teste de kolmogorov_smirnov;\n'
                    '(2) Teste de shapiro_wilk;\n'
                    '(3) Teste Z;\n'
                    '(4) Teste T de independencia de medias;\n'
                    '(5) Testar confiabilidade de kolmogorov_smirnov;\n'
                    '(6) Testar confiabilidade de Teste de shapiro_wilk;\n'
                    '(7) sair do programa\n')
    resposta = int(input("Digite o número correspondente à operação desejada: "))
    
    # Essa parte ta repetindo durante a execução
    if primeira_execucao == True:
        #endereco = input("Digite o endereço do arquivo de dados: ")
        #endereco = "NumerosAleatorios.xlsm"
        #data_values = pd.read_excel(f'{endereco}')
        data_values = np.random.binomial(n=100, p=0.5, size=29)
        #data_values = [4,6,2,10,10,12,14,16,18,20]
        alpha = float(input("Digite o valor para alpha: "))
        primeira_execucao == False

    match resposta:  
        case 1:
            print("_________________________________________________________________\n")
            info , df = th.kolmogorov_smirnov(data_values, alpha)
            print(df["FreqAbs"])
            #Funcionou
        
        case 2:
            print("_________________________________________________________________\n")
            info = th.shapiro_wilk(data_values, alpha, critical_values_table, coefficients_Ain)
            #Deu erro

        case 3:
            print("_________________________________________________________________\n")
            info = th.z_test(data_values, alpha, two_tailed=True)

        case 4:
            print("_________________________________________________________________\n")
            #endereco2 = input("Digite o endereço do segundo arquivo de dados: ")
            #data_values2 = pd.read_csv(f'{endereco2}', sep=';', decimal=',')
            data_values2 = [6,3,1,18,10,15,18,16,21,20]
            th.independent_ttest(data_values, data_values2, alpha)
            #Funcionou
        
        case 5:
            qtd_h0 = 0
            qtd_h1 = 0
            lista_de_testes = []
            for i in range(15):
                data_values = np.random.normal(0, 50,100)
                add = th.kolmogorov_smirnov(data_values, alpha)
                if add == 0: #0 referente a H0 é siginifica que é uma dist. normal
                    lista_de_testes.append(0)
                    qtd_h0 += 1
                else:
                    lista_de_testes.append(1)
                    qtd_h1 += 1

            for i in range(15):
                data_values = np.random.binomial(100, 0.5, 100)
                add = th.kolmogorov_smirnov(data_values, alpha)
                if add == 0: #0 referente a H0 é siginifica que é uma dist. normal
                    lista_de_testes.append(0)
                    qtd_h0 += 1
                else:
                    lista_de_testes.append(1)
                    qtd_h1 += 1

            print(lista_de_testes)
            print(qtd_h0, qtd_h1)

        case 6:
            qtd_h0 = 0
            qtd_h1 = 0
            lista_de_testes = []
            for i in range(15):
                data_values = np.random.normal(0, 50,24)
                add = th.shapiro_wilk(data_values, alpha, critical_values_table, coefficients_Ain)
                if add == 0: #0 referente a H0 é siginifica que é uma dist. normal
                    lista_de_testes.append(0)
                    qtd_h0 += 1
                else:
                    lista_de_testes.append(1)
                    qtd_h1 += 1

            for i in range(15):
                data_values = np.random.random(24)
                add = th.shapiro_wilk(data_values, alpha, critical_values_table, coefficients_Ain)
                if add == 0: #0 referente a H0 é siginifica que é uma dist. normal
                    lista_de_testes.append(0)
                    qtd_h0 += 1
                else:
                    lista_de_testes.append(1)
                    qtd_h1 += 1

            print(lista_de_testes)
            print(qtd_h0, qtd_h1)

        case 7:
            print("Programa finalizado.")
            print("_________________________________________________________________\n")
            break

        case _:
            print("insira uma opção valida")

#Ainda tem que ver como faz um sistem out para os graficos