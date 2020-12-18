def calcular_bayes(prior_A, prob_B_dado_A, prob_B):
    return (prior_A * prob_B_dado_A) / prob_B


if __name__ == "__main__":
    prob_cancer = 1 / 100000
    prob_sintoma_dado_cancer = 1
    prob_sintoma_dado_no_cancer = 10/99999
    prob_no_cancer = 1 - prob_cancer

    prob_sintoma = (prob_sintoma_dado_cancer * prob_cancer) + (prob_sintoma_dado_no_cancer * prob_no_cancer)

    prob_cancer_dado_sintoma = calcular_bayes(prob_cancer, prob_sintoma_dado_cancer, prob_sintoma)
    print(f'Probabilidad de tener cancer dado un síntoma: {prob_cancer_dado_sintoma}')