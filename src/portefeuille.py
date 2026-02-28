# -*- coding: utf-8 -*-
"""Construction du portefeuille."""
import numpy as np

class Portefeuille:
    def __init__(self, rendements, poids=None):
        """
        rendements: DataFrame des rendements (lignes: dates, colonnes: actifs)
        poids: tableau des poids (si None, équipondéré)
        """
        self.rendements = rendements
        self.n_actifs = rendements.shape[1]
        if poids is None:
            self.poids = np.ones(self.n_actifs) / self.n_actifs
        else:
            self.poids = np.array(poids)
        self.rendements_portefeuille = rendements.dot(self.poids)

    def rendements_historiques(self):
        return self.rendements_portefeuille
