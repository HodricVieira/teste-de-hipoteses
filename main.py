import testes_de_hipotese as th
import pandas as pd

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
                    '(5) Mudar os dados de entrada;\n'
                    '(6) Trocar o alpha;\n'
                    '(7) sair do programa\n')
    resposta = int(input("Digite o número correspondente à operação desejada: "))
    
    # Essa parte ta repetindo durante a execução
    if primeira_execucao == True:
        #endereco = input("Digite o endereço do arquivo de dados: ")
        #data_values = pd.read_csv(f'{endereco}', sep=';', decimal=',')
        data_values = [4,6,2,10,10,12,14,16,18,20]
        alpha = float(input("Digite o valor para alpha: "))
        primeira_execucao == False

    match resposta:  
        case 1:
            print("_________________________________________________________________\n")
            th.kolmogorov_smirnov(data_values, alpha)
            #Funcionou
        
        case 2:
            print("_________________________________________________________________\n")
            th.shapiro_wilk(data_values, alpha, critical_values_table, coefficients_Ain)
            #Deu erro

        case 3:
            print("_________________________________________________________________\n")
            th.z_test(data_values, alpha, two_tailed=True)

        case 4:
            print("_________________________________________________________________\n")
            #endereco2 = input("Digite o endereço do segundo arquivo de dados: ")
            #data_values2 = pd.read_csv(f'{endereco2}', sep=';', decimal=',')
            data_values2 = [6,3,1,18,10,15,18,16,21,20]
            th.independent_ttest(data_values, data_values2, alpha)
            #Funcionou
        
        case 5:
            endereco = input("Digite o endereço do arquivo de dados: ")
            data_values = pd.read_csv(f'{endereco}', sep=';', decimal=',')

        case 6:
            alpha = float(input("Digite o valor para alpha: "))

        case 7:
            print("Programa finalizado.")
            print("_________________________________________________________________\n")
            break

        case _:
            print("insira uma opção valida")

#Ainda tem que ver como faz um sistem out para os graficos