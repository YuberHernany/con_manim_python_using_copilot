from manim import *

class VectorSubspaces(Scene):
    def construct(self):
        plane = NumberPlane().add_coordinates()
        plane.set_color(GRAY_C)
        self.play(Create(plane), run_time=0.2)
        self.wait(0.5)
        first_quadrant = Polygon(
            plane.c2p(0, 0), plane.c2p(8, 0), plane.c2p(8, 8), plane.c2p(0, 8),
            fill_color=YELLOW, fill_opacity=0.4, stroke_width=0
        )
        third_quadrant = Polygon(
            plane.c2p(0, 0), plane.c2p(-8, 0), plane.c2p(-8, -8), plane.c2p(0, -8),
            fill_color=YELLOW, fill_opacity=0.4, stroke_width=0
        )
        self.play(FadeIn(first_quadrant), FadeIn(third_quadrant))

        self.wait(1)

        first_quadrant_label = MathTex(r"\{(x, y) \in \mathbb{R}^2 \mid x \geq 0, y \geq 0\}")
        first_quadrant_label.to_corner(UR)
        self.play(Write(first_quadrant_label))

        third_quadrant_label = MathTex(r"\{(x, y) \in \mathbb{R}^2 \mid x \leq 0, y \leq 0\}")
        third_quadrant_label.to_corner(DL)
        self.play(Write(third_quadrant_label))
        self.wait(1)

        vector1 = Arrow(start=plane.c2p(0, 0), end=plane.c2p(0, 2), color=BLUE, buff=0)
        vector2 = Arrow(start=plane.c2p(0, 0), end=plane.c2p(-2, 0), color=BLUE, buff=0)
        self.play(GrowArrow(vector1), GrowArrow(vector2))
        self.wait(1)

        parallelogram = Polygon(
            plane.c2p(0, 0), plane.c2p(0, 2), plane.c2p(-2, 2), plane.c2p(-2, 0),
            fill_color=BLUE, fill_opacity=0.2, stroke_color=BLUE
        )
        self.play(Create(parallelogram))
        self.wait(1)

        result_vector = Arrow(start=plane.c2p(0, 0), end=plane.c2p(-2, 2), color=GREEN, buff=0)
        self.play(GrowArrow(result_vector))
        self.wait(1)

        result_label = MathTex(r"(-2, 2)").next_to(result_vector.get_end(), UP)
        self.play(Write(result_label))
        self.wait(1)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(1)
