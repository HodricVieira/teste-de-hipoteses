import numpy as np
import pandas as pd
from scipy import stats

from scipy.stats import norm, ksone
import numpy as np
from scipy.stats import t, chi2
def kolmogorov_smirnov(data_values, alpha):

    # media e desvio
    sample_mean = np.mean(data_values)
    sample_standard_deviation = np.std(data_values)
    # Sorting the list of values without duplicates
    sorted_data = sorted(data_values)
    Xi = sorted(set(sorted_data))
    # Calculating the absolute frequency of each value
    freq_abs = [sorted_data.count(i) for i in Xi]
    # Calculating the cumulative frequency
    freq_cumulative = []
    for i in range(len(freq_abs)):
        if i == 0:
            freq_cumulative.append(freq_abs[i])
        else:
            freq_cumulative.append(freq_abs[i] + freq_cumulative[i-1])
   
    # Calculating the relative frequency
    freq_rel = [x / freq_cumulative[-1] for x in freq_abs]
    # Calculating the cumulative relative frequency
    freq_rel_cumulative = []
    for i in range(len(freq_abs)):
            freq_rel_cumulative.append(freq_cumulative[i] / freq_cumulative[-1])
    # Calculating the values of Zi
    Zi = [(x - sample_mean) / sample_standard_deviation for x in Xi]
    # Calculating the expected frequency Fwaited
    freq_expected = [norm.cdf(z) for z in Zi]
    # Calculating |Fwaited(Xi) - Frac(Xi)| for each value of Xi
    Fwaited_minus_Frac = [abs(freq_expected[i] - freq_rel_cumulative[i]) for i in range(len(Xi))]
    # Calculating |Fwaited(Xi) - Frac(Xi-1)| for each value of Xi
    Fwaited_minus_Frac_1 = [freq_expected[0]] + [abs(freq_expected[i] - freq_rel_cumulative[i-1]) for i in range(1, len(Xi))]
    # Calculating Dcalc
    max_Fwaited_minus_Frac = max(Fwaited_minus_Frac)
    max_Fwaited_minus_Frac_1 = max(Fwaited_minus_Frac_1)
    Dcalc = max(max_Fwaited_minus_Frac, max_Fwaited_minus_Frac_1)

    # Calculating Dtabela (critical D)
    if len(sorted_data) <= 35:
        Dtab = ksone.ppf(1 - alpha/2, len(sorted_data))
        #values table
    else:

        if alpha == 0.2:   
            
            Dtab = 1.63 / np.sqrt(len(sorted_data))
        elif alpha == 0.15:
            
            
            Dtab = 1.36 / np.sqrt(len(sorted_data))
        elif alpha == 0.10:
            
            
            Dtab = 1.22 / np.sqrt(len(sorted_data))
        elif alpha == 0.05:
            
            
            Dtab = 1.14 / np.sqrt(len(sorted_data))
        elif alpha == 0.01:
            
            
            Dtab = 1.07 / np.sqrt(len(sorted_data))

    if Dcalc < Dtab:
        print("Accept the null hypothesis that the sample follows a normal distribution. Dcalc = %.4f < Dtab = %.4f" % (Dcalc, Dtab))
        test_result = "Accept the null hypothesis that the sample follows a normal distribution. Dcalc = %.4f < Dtab = %.4f" % (Dcalc, Dtab)
        result = True
    else:
        print("Reject the null hypothesis that the sample follows a normal distribution Dcalc = %.4f > Dtab = %.4f" % (Dcalc, Dtab))
        test_result = "Reject the null hypothesis that the sample follows a normal distribution Dcalc = %.4f > Dtab = %.4f" % (Dcalc, Dtab)
        result = False
    # Creating a pandas dataframe with all frequency columns
    df = pd.DataFrame({'Xi': Xi, 'FreqAbs': freq_abs,"FreqRelative":freq_rel, 'FreqCumulative': freq_cumulative, 'FreqRelCumulative': freq_rel_cumulative, 'Zi': Zi, 'Fwaited': freq_expected,
                       '(Fwaited - Frac': Fwaited_minus_Frac, 'Fwaited - Frac-1': Fwaited_minus_Frac_1})
    #print(df)
    return test_result , df, result


################################################################################################

# Leitura e tratamento das tabelas de coeficientes de Wcrit
coefficients_Ain = pd.read_csv('Coeficientes_ain.csv', sep=';', decimal=',')
critical_values_table = pd.read_csv('tabela_Wcrit.csv', sep=';', decimal=',')
critical_values_table = critical_values_table.drop(['Unnamed: 10'], axis=1)
critical_values_table = critical_values_table.drop(28)
# Convert the "tamanho n" column to integer type
critical_values_table["tamanho n"] = critical_values_table["tamanho n"].astype(int)

def shapiro_wilk(data_values, alpha, critical_value_table_W, coefficient_table_Ain):
    # Finding the value of n (sample size)
    n = len(data_values)
    if n > 30 or n < 3:
        return 'Error: Sample size greater than 30 or less than 3'
    
    #arredondamento
    arredondados = []
    for i in range(len(data_values)):
        arredondados.append(round(data_values[i]))
    data_values = arredondados
    
    # Sorting the list of values without duplicates
    sorted_data = sorted(data_values)
    Si = sorted(set(sorted_data))
    # Calculating the absolute frequency of each value
    freq_abs = [sorted_data.count(i) for i in Si]
    # Calculating the cumulative frequency
    freq_cumulative = []
    for i in range(len(freq_abs)):
        if i == 0:
            freq_cumulative.append(freq_abs[i])
        else:
            freq_cumulative.append(freq_abs[i] + freq_cumulative[i-1])
   
    # Calculating the relative frequency
    freq_rel = [x / freq_cumulative[-1] for x in freq_abs]
    # Calculating the cumulative relative frequency
    freq_rel_cumulative = []
    for i in range(len(freq_abs)):
            freq_rel_cumulative.append(freq_cumulative[i] / freq_cumulative[-1])

    # Finding the value of i
    i_ = [i for i in range(1, (n // 2) + 1)]
    
    # Finding the value of n - (i - 1)
    n_minus_i_minus_1 = []
    for i in i_:
        n_minus_i_minus_1.append(n - (i - 1))
    
    # Finding the value of Ai,n
    Ain = []
    for i in range(1, (n // 2) + 1):
        Ain.append(coefficient_table_Ain.loc[(i - 1, str(n))])
    # Finding the value of X(n-(i-1)) in the list of values
    X_n_minus_i_minus_1 = []
    for i in range(1, (n // 2) + 1):
        X_n_minus_i_minus_1.append(data_values[n - (i - 1) - 1])

    # Finding the value of Xi in the list of values
    Xi = []
    for i in i_:
        Xi.append(data_values[i - 1])

    # Finding the value of Ai,n times (X(n-(i-1)) - Xi)
    values_Bi = []
    sum_Bi = 0
    for i in range(1, (n // 2) + 1):
        values_Bi.append(Ain[i - 1] * (X_n_minus_i_minus_1[i - 1] - Xi[i - 1]))
        sum_Bi += values_Bi[i - 1]

    # Finding the sample value of squared absolute deviations (or the variance times n-1)
    denominator_Wcalc = np.var(data_values, ddof=1) * (n - 1)

    # Finding the value of W calculated
    Wcalc = (sum_Bi**2) / denominator_Wcalc

    # Finding the critical W value (W critical)
    Wcrit = critical_value_table_W.loc[(n - 3, str(alpha))]


    if Wcrit > Wcalc:
        test_result = "Accept the null hypothesis H0 that the sample follows a normal distribution Wcrit = %.4f > Wcalc = %.4f" % (Wcrit, Wcalc)
        print("Accept the null hypothesis H0 that the sample follows a normal distribution Wcrit = %.4f > Wcalc = %.4f" % (Wcrit, Wcalc))
    else:
        test_result = "Reject the null hypothesis H0 that the sample follows a normal distribution Wcrit = %.4f > Wcalc = %.4f" % (Wcrit, Wcalc)
        print("Reject the null hypothesis H0 that the sample follows a normal distribution Wcrit = %.4f > Wcalc = %.4f" % (Wcrit, Wcalc))

    # Creating a pandas DataFrame with all the columns
    df2 = pd.DataFrame({'i': i_, 'n - (i - 1)': n_minus_i_minus_1, 'Ai,n': Ain, 'X(n-(i-1))': X_n_minus_i_minus_1,
                       'Xi': Xi, 'Bi Values': values_Bi})

    df = pd.DataFrame({'Xsi': Si, 'FreqAbs': freq_abs,"FreqRelative":freq_rel, 'FreqCumulative': freq_cumulative, 'FreqRelCumulative': freq_rel_cumulative})

    return test_result, df, df2

########################################################################################

def z_test(population, media_sup, alpha, two_tailed=True):
    # Calcula estatisticas base
    sample_size = len(population)
    sample_mean = np.mean(population)
    population_std_dev = np.std(population)
    
    # Calculate Zcalc
    numerator_zcalc = sample_mean - media_sup
    denominator_zcalc = population_std_dev / np.sqrt(sample_size)
    Zcalc = numerator_zcalc / denominator_zcalc
    # Find Zcrit
    Zcrit = stats.norm.ppf(1 - alpha/2) if two_tailed else stats.norm.ppf(1 - alpha)

    # Print the results
    print(f"Zcalc = {Zcalc}")
    print(f"Zcrit = {Zcrit}")
    #module of the zcalc - zcrit
    if abs(Zcalc) < abs(Zcrit):
        print(f"|Zcalc| = {abs(Zcalc)} < Zcrit = {abs(Zcrit)}")
        print(f"Accept the null hypothesis that the population mean is {sample_mean}")
        info = "Accept the null hypothesis that the population mean is %.4f\n media amostral = %.4f\n |Zcalc| = %.4f < Zcrit = %.4f" % (media_sup, sample_mean, abs(Zcalc), abs(Zcrit))
    else:
        print(f"|Zcalc| = {abs(Zcalc)} > Zcrit = {abs(Zcrit)}")
        print(f"Reject the null hypothesis that the population mean is {sample_mean}")
        info = "Reject the null hypothesis that the population mean is %.4f\n media amostral = %.4f\n |Zcalc| = %.4f > Zcrit = %.4f" % (media_sup, sample_mean, abs(Zcalc), abs(Zcrit))

    return info


##########################################################################################

# t-test for independent samples
# function for calculating the t-test for two independent samples
def independent_ttest(data1, data2, alpha):
    # calculate means
    mean1, mean2 = np.mean(data1), np.mean(data2)
    # calculate standard errors
    se1, se2 = stats.sem(data1), stats.sem(data2)
    # standard error on the difference between the samples
    sed = np.sqrt(se1**2.0 + se2**2.0)
    # calculate the t statistic
    t_stat = (mean1 - mean2) / sed
    # degrees of freedom
    df = len(data1) + len(data2) - 2
    # calculate the critical value
    cv = stats.t.ppf(1.0 - alpha, df)
    # calculate the p-value
    p = (1.0 - stats.t.cdf(abs(t_stat), df)) * 2.0
    
    # calculate the t test
    print('t=%.3f, df=%d, cv=%.3f, p=%.3f' % (t_stat, df, cv, p))
    # interpret via critical value
    if abs(t_stat) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')
    # interpret via p-value
    if p > alpha:
        print('Accept null hypothesis that the means are equal.')
        info = "Accept null hypothesis that the means are equal. \n Media 1: %.3f     Media 2: %.3f \n P_valor: %.3f > alpha %.3f" % (mean1, mean2, p, alpha)
    else:
        print('Reject the null hypothesis that the means are equal.')
        info = "Reject the null hypothesis that the means are equal. \n Media 1: %.3f     Media 2: %.3f \n P_valor: %.3f < alpha %.3f" % (mean1, mean2, p, alpha)

    # return everything
    # return t_stat, df, cv, p
    return info


#############################################################################################

def t_test_single_sample(data, mu, alpha):
    n = len(data)
    x_bar = np.mean(data)
    s = np.sqrt(np.sum((data - x_bar)**2) / (n - 1))
    sem = s / np.sqrt(n)
    t_stat = (x_bar - mu) / sem
    p_value = 2 * t.sf(abs(t_stat), n - 1)
    
    if p_value > alpha:
        print(f"Accept the null hypothesis that the population mean is {x_bar}")
        info = "Accept the null hypothesis that the population mean is %.3f\n media amostral = %.3f\n p_valor = %.3f > alpha = %.3f" % (mu, x_bar, p_value, alpha)
    else:
        print(f"Reject the null hypothesis that the population mean is {x_bar}")
        info = "Reject the null hypothesis that the population mean is %.3f\n media amostral = %.3f\n p_valor = %.3f < alpha = %.3f" % (mu, x_bar, p_value, alpha)

    #return t_stat, p_value, p_value < alpha
    return info

############################################################################################

def t_test_two_independent_samples(data1, data2, alpha):
    n1, n2 = len(data1), len(data2)
    x_bar1, x_bar2 = np.mean(data1), np.mean(data2)
    s1, s2 = np.sqrt(np.sum((data1 - x_bar1)**2) / (n1 - 1)), np.sqrt(np.sum((data2 - x_bar2)**2) / (n2 - 1))
    sed = np.sqrt(s1**2 / n1 + s2**2 / n2)
    t_stat = (x_bar1 - x_bar2) / sed
    df = n1 + n2 - 2
    p_value = 2 * t.sf(abs(t_stat), df)
    return t_stat, p_value, p_value < alpha

##############################################################################################

def bartlett_test(alpha, sample1, sample2, *more_samples):
    # Combine all samples into a list
    all_samples = [sample1, sample2, *more_samples]

    # Calculate the sample sizes and sample means
    n = [len(sample) for sample in all_samples]
    means = [np.mean(sample) for sample in all_samples]

    # Calculate the sum of squared differences for each sample
    ssd = [np.sum((sample - mean) ** 2) for sample, mean in zip(all_samples, means)]

    # Calculate the degrees of freedom and the chi-squared statistic
    k = len(all_samples)
    df = k - 1
    chi_squared = (np.sum([(ni - 1) * ssi for ni, ssi in zip(n, ssd)]) / (np.sum(n) - k))

    # Calculate the p-value using the chi-squared distribution
    from scipy.stats import chi2
    p_value = 1 - chi2.cdf(chi_squared, df)

    variance1 = np.var(sample1)
    variance2 = np.var(sample2)

    if p_value > alpha:
        print('Accept null hypothesis that the variance are homogeneous.')
        info = "Accept null hypothesis that the variance are homogeneous. \n variance 1: %.3f     variance 2: %.3f \n P_valor: %.3f > alpha %.3f" % (variance1, variance2, p_value, alpha)
    else:
        print('Reject the null hypothesis that the variance are homogeneous.')
        info = "Reject the null hypothesis that the variance are homogeneous. \n variance 1: %.3f     variance 2: %.3f \n P_valor: %.3f < alpha %.3f" % (variance1, variance2, p_value, alpha)
    

    #return chi_squared, p_value
    return info