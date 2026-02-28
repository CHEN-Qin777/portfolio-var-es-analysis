# -*- coding: utf-8 -*-
"""Visualisations avancées."""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

def tracer_histogramme_rendements(rendements, var, es, titre="Distribution des rendements"):
    """Histogramme avec lignes VaR et ES."""
    plt.figure(figsize=(10,6))
    sns.histplot(rendements, bins=50, kde=True, stat='density')
    plt.axvline(var, color='red', linestyle='--', label=f'VaR {var:.4f}')
    plt.axvline(es, color='orange', linestyle='--', label=f'ES {es:.4f}')
    plt.xlabel('Rendement')
    plt.ylabel('Densité')
    plt.title(titre)
    plt.legend()
    plt.show()

def tracer_var_glissante(rendements, vars_glissantes, dates, titre="VaR glissante (fenêtre 1 an)"):
    """Trace la VaR glissante avec les périodes de stress."""
    plt.figure(figsize=(12,6))
    plt.plot(rendements.index, rendements, alpha=0.5, label='Rendements quotidiens')
    plt.plot(dates, vars_glissantes, color='red', linewidth=2, label='VaR 95% glissante')
    # Marquer les crises (exemples)
    crises = [('2008-09-15', '2009-03-01'), ('2020-02-20', '2020-04-01')]
    for debut, fin in crises:
        plt.axvspan(pd.to_datetime(debut), pd.to_datetime(fin), alpha=0.2, color='gray')
    plt.xlabel('Date')
    plt.ylabel('Rendement / VaR')
    plt.title(titre)
    plt.legend()
    plt.show()
