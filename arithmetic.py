from manim import *

import numpy as np
import pandas as pd
import sympy.ntheory as nt
from sympy import igcd

# table for showing the Euler theorem in modular arithmetic

class EulerTheoremTable(Scene):
    def construct(self):
        n = 7
        vals = np.array([[str((a**k) % n) for k in range(1, n)] for a in range(1, n)])
        table = Table(
            vals.tolist(),
            col_labels=[MathTex(f"k={k}") for k in range(1, n)],
            row_labels=[MathTex(f"a={a}") for a in range(1, n)],
            include_outer_lines=True
        ).scale_to_fit_width(config.frame_width - 1)
        self.play(Create(table))
        self.wait(3)
        rect = SurroundingRectangle(table.get_columns()[6], color=RED, buff=0.1)
        self.play(Create(rect))
        self.wait(3)