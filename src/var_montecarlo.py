# -*- coding: utf-8 -*-
"""VaR par simulation Monte Carlo (approche multivariée)."""
import numpy as np

def var_montecarlo(rendements, poids, n_sim=10000, horizon=1, niveau=0.95):
    """
    Simulation Monte Carlo de la VaR (méthode multivariée).
    - rendements : DataFrame des rendements historiques (lignes = dates, colonnes = actifs)
    - poids : vecteur des poids du portefeuille
    - n_sim : nombre de simulations
    - horizon : horizon en jours (1 = 1 jour)
    - niveau : niveau de confiance (ex: 0.95)
    Retourne (VaR, ES)
    """
    mu = rendements.mean().values  # vecteur des moyennes par actif
    cov = rendements.cov().values  # matrice de covariance

    # Génération des rendements simulés pour chaque actif
    rendements_sim = np.random.multivariate_normal(mu * horizon, cov * horizon, n_sim)

    # Rendement du portefeuille = somme pondérée
    rendements_portefeuille = rendements_sim @ poids  # produit matriciel

    var = np.percentile(rendements_portefeuille, 100 * (1 - niveau))
    es = rendements_portefeuille[rendements_portefeuille <= var].mean()
    return var, es
