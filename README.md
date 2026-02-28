
```markdown
# Analyse VaR et ES d'un portefeuille multi-actifs

Ce projet implémente le calcul de la Value-at-Risk (VaR) et de l'Expected Shortfall (ES) pour un portefeuille diversifié en utilisant deux méthodes : **historique** et **Monte Carlo**. Il comprend le téléchargement de données réelles, le nettoyage, la visualisation avancée et l'analyse comparative.

## 🎯 Objectifs

- Collecter des données financières historiques (Yahoo Finance) ou générer des données synthétiques.
- Construire un portefeuille équipondéré d'actions, d'ETF et de matières premières.
- Calculer la VaR et l'ES historiques (95% et 99%).
- Calculer la VaR et l'ES par simulation Monte Carlo (approche multivariée).
- Visualiser la distribution des rendements et la VaR glissante dans le temps.
- Identifier les périodes de stress de marché (2008, 2020).
- Comparer les résultats des deux méthodes.

## 📊 Résultats obtenus

Les résultats ci‑dessous ont été obtenus avec un portefeuille composé de `AAPL`, `MSFT`, `GLD` et `TLT` sur la période 2015–2023.

### VaR et ES historiques

| Mesure          | 95%         | 99%         |
|------------------|-------------|-------------|
| **VaR**          | –0.022648   | –0.074315   |
| **ES**           | –0.080870   | –0.258970   |

### VaR Monte Carlo (95%, 50 000 simulations)

- **VaR Monte Carlo 95%** : –0.075468  
- **ES Monte Carlo 95%**  : –0.094868

### Comparaison des méthodes (VaR 95%)

| Méthode     | VaR 95%    |
|-------------|------------|
| Historique  | –0.022648  |
| Monte Carlo | –0.075468  |

## 📈 Interprétation et analyse

1. **Différence significative** : La VaR Monte Carlo est environ **3,3 fois plus élevée** (en valeur absolue) que la VaR historique. Cela s’explique par le fait que la simulation Monte Carlo génère des rendements extrêmes conformes à une loi normale multivariée, ce qui peut amplifier les queues de distribution par rapport à l’échantillon historique.

2. **Expected Shortfall** : L’ES historique à 95 % (–0.0809) est plus proche de la VaR Monte Carlo (–0.0755) que la VaR historique elle‑même. Cela indique que l’ES historique capte mieux le risque de queue que la VaR historique simple.

3. **Périodes de stress** : Le graphique de VaR glissante (fourni dans le notebook) montre clairement des pics pendant la crise du COVID‑19 (début 2020) et une volatilité accrue en 2022. Ces pics sont plus marqués avec la VaR glissante qu’avec la VaR historique ponctuelle.

4. **Choix de méthode** : En pratique, les banques utilisent souvent la VaR historique pour sa simplicité et sa non‑paramétricité, mais lui adjoignent des simulations Monte Carlo pour les scénarios de stress et les produits non linéaires. Notre résultat illustre bien la prudence accrue qu’apporte la méthode Monte Carlo.

## 🛠️ Installation et utilisation

### Prérequis

- Python 3.8+
- Installer les dépendances :
```bash
pip install -r requirements.txt
```

### Exécution

- **Version locale** : lancez les scripts dans l'ordre ou exécutez les tests.
- **Version Colab** : ouvrez le notebook `notebooks/var_analyse_complete.ipynb` dans Google Colab et exécutez toutes les cellules.

## 📁 Structure des fichiers

- `data/telecharger_donnees.py` : télécharge les données depuis Yahoo Finance.
- `data/traiter_donnees.py` : nettoie les données et calcule les rendements.
- `src/portefeuille.py` : définit la classe `Portefeuille`.
- `src/var_historique.py` : fonctions pour VaR/ES historique et glissante.
- `src/var_montecarlo.py` : fonction pour VaR/ES Monte Carlo (multivariée).
- `src/visualisation.py` : fonctions de tracé (histogramme, VaR glissante).
- `notebooks/var_analyse_complete.ipynb` : notebook Colab complet avec tous les calculs et visualisations.
- `tests/test_var.py` : tests unitaires basiques.

## 📝 Licence

Ce projet est fourni à titre éducatif. Vous êtes libre de l'utiliser et de le modifier.

## 🤝 Auteur

Étudiant en Master 2 Mathématiques Financières – Projet de stage.
```

---

## 📄 Fichiers sources (contenu complet)

### `requirements.txt`
```
numpy
pandas
yfinance
matplotlib
scipy
seaborn
```

