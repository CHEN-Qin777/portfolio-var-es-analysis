import unittest
import numpy as np
from src.var_historique import var_historique, es_historique

class TestVar(unittest.TestCase):
    def test_var_historique(self):
        rend = np.array([-0.1, -0.05, 0, 0.02, 0.03])
        var = var_historique(rend, 0.95)
        self.assertAlmostEqual(var, -0.1)
    
    def test_es_historique(self):
        rend = np.array([-0.1, -0.05, 0, 0.02, 0.03])
        es = es_historique(rend, 0.95)
        self.assertAlmostEqual(es, -0.1)

if __name__ == '__main__':
    unittest.main()
