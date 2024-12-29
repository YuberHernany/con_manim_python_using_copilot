from manim import *

class CicleWithRoots(Scene):
    def construct(self):
        n = 6
        circle = Circle(radius=3).set_color(YELLOW)
        self.play(Create(circle))
        self.wait(1)
        roots = [[np.cos(2*i*np.pi/n), np.sin(2*i*np.pi/n), 0] for i in range(n)]
        roots = np.array(roots).reshape(-1, 3)
        arrows = VGroup(*[
            Arrow(start=ORIGIN, end=3 * root, buff=0).set_color(WHITE)
            for root in roots
        ])
        self.play(FadeIn(arrows))
        self.wait(1)
        dots = VGroup(*[
            Dot(point=3 * root, color=RED).scale(2)
            for root in roots
        ])
        self.play(FadeOut(arrows), run_time=0.2)
        self.play(FadeIn(dots), run_time=0.2)
        self.wait(1)
        labels_omegas = VGroup(*[
            MathTex(fr"\omega_6^{{{i}}}").scale(0.8).next_to(3 * root, RIGHT)
            for i, root in enumerate(roots)
        ])
        self.play(FadeIn(labels_omegas))
        self.wait(1)
        
        first_roots = VGroup(*[dots, labels_omegas, circle])
        self.play(first_roots.animate.to_edge(LEFT), buff=0.3)
        self.wait(1)

        new_circle = Circle(radius=3).set_color(BLUE)
        self.play(Create(new_circle))
        self.wait(1)
        new_roots = [roots[0], roots[2], roots[4]]
        new_arrows = VGroup(*[
            Arrow(start=ORIGIN, end=3 * root, buff=0).set_color(WHITE)
            for root in new_roots
        ])
        self.play(FadeIn(new_arrows))
        self.wait(1)
        new_dots = VGroup(*[
            Dot(point=3 * root, color=GREEN).scale(2)
            for root in new_roots
        ])
        self.play(FadeOut(new_arrows), run_time=0.2)
        self.play(FadeIn(new_dots), run_time=0.2)
        self.wait(1)
        new_labels_omegas = VGroup(*[
            MathTex(fr"\omega_6^{{{i*2}}}").scale(0.8).next_to(3 * root, RIGHT)
            for i, root in enumerate(new_roots)
        ])
        self.play(FadeIn(new_labels_omegas))
        self.wait(1)
        
        second_roots = VGroup(*[new_dots, new_labels_omegas, new_circle])
        self.play(second_roots.animate.to_edge(RIGHT), buff=0.3)
        self.wait(1)

        self.play(first_roots.animate.scale(0.6).to_corner(UL), buff=0.3)
        self.wait(1)
        self.play(second_roots.animate.scale(0.6).to_corner(UR), buff=0.3)
        self.wait(1)

        third_circle = Circle(radius=1.5).set_color(PURPLE)
        third_arros = VGroup(*[
            Arrow(start=ORIGIN, end=1.5 * root, buff=0).set_color(WHITE)
            for root in roots
        ]).move_to(third_circle.get_center(), ORIGIN)

        third_circle.to_edge(DOWN)
        third_arros.to_edge(DOWN)
        self.play(Create(third_circle))
        self.wait(1)

        # vectors in latex including the unitary roots
        v1 = Matrix([
            [r"\omega_6^{0}"],
            [r"\omega_6^{1}"],
            [r"\omega_6^{2}"],
            [r"\omega_6^{3}"],
            [r"\omega_6^{4}"],
            [r"\omega_6^{5}"]
        ]).next_to(first_roots, RIGHT)
        
        v2 = Matrix([
            [r"\overline{\omega_6^{0}}"],
            [r"\overline{\omega_6^{2}}"],
            [r"\overline{\omega_6^{4}}"],
            [r"\overline{\omega_6^{0}}"],
            [r"\overline{\omega_6^{2}}"],
            [r"\overline{\omega_6^{4}}"]
        ]).next_to(second_roots, LEFT)
        self.play(Create(v1))
        self.play(Create(v2))
        self.wait(1)

        # now term by term the dot product
        t0 = VGroup(*[v1.get_rows()[0].copy(), MathTex(r"\cdot"), v2.get_rows()[0].copy()]).arrange(RIGHT)
        t1 = VGroup(*[v1.get_rows()[1].copy(), MathTex(r"\cdot"), v2.get_rows()[1].copy()]).arrange(RIGHT)
        t2 = VGroup(*[v1.get_rows()[2].copy(), MathTex(r"\cdot"), v2.get_rows()[2].copy()]).arrange(RIGHT)
        t3 = VGroup(*[v1.get_rows()[3].copy(), MathTex(r"\cdot"), v2.get_rows()[3].copy()]).arrange(RIGHT)
        t4 = VGroup(*[v1.get_rows()[4].copy(), MathTex(r"\cdot"), v2.get_rows()[4].copy()]).arrange(RIGHT)
        t5 = VGroup(*[v1.get_rows()[5].copy(), MathTex(r"\cdot"), v2.get_rows()[5].copy()]).arrange(RIGHT)
        colors = [YELLOW, BLUE, RED, GREEN, PURPLE, ORANGE]
        products = VGroup(*[t0, t1, t2, t3, t4, t5]).scale(0.7).arrange(DOWN).to_edge(UP)
        for c, p, a in zip(colors, products, third_arros):
            p.set_color(c)
            a.set_color(c)
        self.play(Create(products))
        self.wait(1)

        self.play(Transform(t0, third_arros[0]))
        self.play(Transform(t1, third_arros[5]))
        self.play(Transform(t2, third_arros[4]))
        self.play(Transform(t3, third_arros[3]))
        self.play(Transform(t4, third_arros[2]))
        self.play(Transform(t5, third_arros[1]))
        self.wait(1)

