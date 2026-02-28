# -*- coding: utf-8 -*-
"""Téléchargement des données historiques depuis Yahoo Finance."""
import yfinance as yf
import pandas as pd

def telecharger_donnees(tickers, debut, fin):
    """
    Télécharge les prix ajustés pour une liste de tickers.
    Paramètres:
        tickers (list): Liste des symboles (ex: ['AAPL', 'MSFT', 'GLD'])
        debut (str): Date de début 'YYYY-MM-DD'
        fin (str): Date de fin 'YYYY-MM-DD'
    Retour:
        DataFrame: Prix de clôture ajustés
    """
    try:
        data = yf.download(tickers, start=debut, end=fin)['Adj Close']
        if data.empty:
            raise ValueError("Aucune donnée reçue. Vérifiez les tickers.")
        return data
    except Exception as e:
        print(f"Erreur de téléchargement : {e}")
        # Données synthétiques de secours
        return generer_donnees_synthetiques(tickers, debut, fin)

def generer_donnees_synthetiques(tickers, debut, fin):
    """Génère des données de prix synthétiques."""
    dates = pd.date_range(start=debut, end=fin, freq='B')
    prix = pd.DataFrame(index=dates)
    for t in tickers:
        prix[t] = 100 * (1 + np.random.randn(len(dates)).cumsum() / 100)
    return prix
