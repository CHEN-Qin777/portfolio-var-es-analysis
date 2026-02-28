# -*- coding: utf-8 -*-
"""Calcul de la VaR historique et de l'Expected Shortfall."""
import numpy as np

def var_historique(rendements, niveau_confiance=0.95):
    """
    Calcule la VaR historique.
    Paramètres:
        rendements (array): Série des rendements du portefeuille
        niveau_confiance (float): Niveau de confiance (ex: 0.95)
    Retour:
        float: VaR (valeur négative)
    """
    var = np.percentile(rendements, 100 * (1 - niveau_confiance))
    return var

def es_historique(rendements, niveau_confiance=0.95):
    """Expected Shortfall (ES) au même niveau."""
    var = var_historique(rendements, niveau_confiance)
    es = rendements[rendements <= var].mean()
    return es

def var_glissante(rendements, fenetre=252, niveau_confiance=0.95):
    """Calcule la VaR glissante sur une fenêtre."""
    vars_ = []
    for i in range(fenetre, len(rendements)):
        var = var_historique(rendements[i-fenetre:i], niveau_confiance)
        vars_.append(var)
    return np.array(vars_)
