from manim import Scene
from manim import Text, MathTex, Tex
from manim import SurroundingRectangle
from manim import Write, Create, VGroup
from manim import Transform
from manim import FadeOut
# from manim import NumberPlane
from manim import Arrow
from manim import DOWN, LEFT
from manim import GREEN, RED, PURPLE_A


class Logic(Scene):
    def construct(self):

        # self.add(NumberPlane().set_opacity(0.5))
        self.wait()
        self.logo()
        self.intro()
        self.types()
        self.compuestas()
        self.conditionals()
        self.biconditionals()
        self.notation()

    def intro(self):

        # Title
        title = Text("¿Qué es una proposición?")
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.set_y(3.5).set_x(-2))

        # prop
        prop = Text("Es una expresión que se puede aseverar sin" +
                    "\nambigüdad y se puede contrastar con la realidad",
                    line_spacing=1)
        prop.scale(0.7).set_y(2)
        self.play(Write(prop), run_time=3)
        self.wait()
        rect = SurroundingRectangle(prop[24:32])
        self.play(Create(rect))
        asev = prop[24:32].copy().set_y(-1.5).set_x(-5)
        self.play(Transform(prop[24:32].copy(), asev), FadeOut(rect))

        v = Text("Verdad (V)", color=GREEN).set_y(-1).set_x(-1.2).scale(0.6)
        f = Text("Falso (F)", color=RED).set_y(-2).scale(0.6).set_x(-1.2)
        av = Arrow([-3.8, -1.5, 0], [-2.2, -1, 0])
        af = Arrow([-3.8, -1.5, 0], [-2.2, -2, 0])

        self.play(Create(av))
        self.play(Write(v))
        self.play(Create(af))
        self.play(Write(f))

        # Ejemplos
        ejem = Text("Ejemplos: ").scale(0.8)
        ej1 = MathTex(r"1.\quad 1 + 2 = 4", r"\quad(F)")
        ej2 = Text("2. Un cubo tiene 6 lados (V)").scale(0.6)
        ej3 = Text("3. Dios existe.").scale(0.6)
        ej4 = Text("4. La tarde está muy triste.").scale(0.6)
        ej5 = Text("5. ¡Que te vaya muy bien!").scale(0.6)
        ej6 = MathTex(r"6. \quad x^2 + y^2 = 4^2")
        ej7 = Text("7. ¿Cómo estas?").scale(0.6)

        eG = VGroup(ejem, ej1, ej2, ej3, ej4, ej5, ej6, ej7).arrange(
                DOWN, aligned_edge=LEFT).set_x(3.5).set_y(-1.5).scale(0.8)

        self.play(Write(ejem))
        self.wait()
        self.play(Write(ej1[0]))
        self.wait()
        self.play(Write(ej1[1].set_color(RED)))
        self.wait()
        self.play(Write(ej2[:-3]))
        self.wait()
        self.play(Write(ej2[-3:].set_color(GREEN)))
        self.wait()

        for i in range(3, 8):
            mo = eG[i]
            self.play(Write(mo))
            self.play(mo.animate.set_color(RED))
            self.wait()

        self.clear()
        self.wait()

    def logo(self):
        name = Text("ROB")
        pi = MathTex(r"\pi").scale(2.5)

        self.play(Write(name))
        self.play(Transform(name, pi))
        self.play(FadeOut(name))
        self.wait()

    def types(self):
        self.next_section(skip_animations=False)
        title = Text("Tipos de Proposiciones").scale(0.9)
        self.play(Write(title))
        self.play(title.animate.move_to([-2.8, 3.5, 0]))

        # Enunciados abiertos
        self.next_section(skip_animations=False)
        tea = Text("0. Enunciados abiertos:").scale(0.7).set_color(PURPLE_A)
        ej1 = MathTex("1 + x < 8")
        sol1 = MathTex(r"\text{si }x = 0 \Rightarrow 1 + 0 = 1 < 8",
                       r"\quad (V)")
        sol2 = MathTex(r"\text{si }x = 8 \Rightarrow 1 + 8 = 9 < 8",
                       r"\quad (F)")

        ea = VGroup(tea,
                    ej1,
                    sol1,
                    sol2).arrange(DOWN, aligned_edge=LEFT).scale(0.9)
        ea.move_to([-3.5, 1.5, 0])
        self.play(Write(tea))
        self.wait(0.5)
        self.play(Write(ej1))
        self.wait(0.5)
        self.play(Write(sol1[0]), run_time=3)
        self.wait(0.5)
        self.play(Write(sol1[1].set_color(GREEN)))
        self.wait(0.5)
        self.play(Write(sol2[0]), run_time=3)
        self.wait(0.5)
        self.play(Write(sol2[1].set_color(RED)))
        self.wait()

        # Porposiciones simples
        self.next_section(skip_animations=False)
        tps = Text("1. Simples o atómicas: ").scale(0.7).set_color(PURPLE_A)
        ej1 = Text("(a) Juan tiene 12 años.").scale(0.6)
        ej2 = Text("(b) El número 73 es primo.").scale(0.6)
        ej3 = Text("(c) Elizabeth baila.").scale(0.6)
        ps = VGroup(tps,
                    ej1,
                    ej2,
                    ej3).arrange(DOWN, aligned_edge=LEFT).scale(0.9)
        ps.move_to([3, 1.5, 0])
        for mo in ps:
            self.play(Write(mo))
            self.wait(0.5)

        # Proposiciones predicativas
        self.next_section(skip_animations=False)
        tpp = Text("1.1 Predicativas:").scale(0.7).set_color(PURPLE_A)
        ej1 = Text("(a) Juan come una manzana.").scale(0.6)
        ej2 = Text("(b) María es matemática.").scale(0.6)
        ej3 = Text("(c) La guitarra es mía.").scale(0.6)

        pp = VGroup(
                tpp,
                ej1,
                ej2,
                ej3).arrange(DOWN, aligned_edge=LEFT).scale(0.9)
        pp.move_to([-3.6, -1.7, 0])
        for mo in pp:
            self.play(Write(mo))
            self.wait(0.5)

        self.play(pp[3].animate.set_color(RED))
        self.wait()

        # Proposiciones Relacionales
        self.next_section(skip_animations=False)
        tpr = Text("1.2 Relacionales:").scale(0.7).set_color(PURPLE_A)
        ej1 = Text("(a) Juan y María son hermanos.").scale(0.6)
        ej2 = MathTex(r"(b) \quad 3 > 2.")
        ej3 = Text("(c) 3 es igual 8.").scale(0.6)

        pr = VGroup(
                tpr,
                ej1,
                ej2,
                ej3).arrange(DOWN, aligned_edge=LEFT).scale(0.9)
        pr.move_to([3.5, -1.7, 0])
        for mo in pr:
            self.play(Write(mo))
            self.wait(0.5)

        self.wait()
        self.play(FadeOut(ea, ps, pp, pr, title))

    def part_animate(self, vg: VGroup):
        for mo in vg:
            self.play(Write(mo[:4]))
            self.wait(0.5)
            r1 = SurroundingRectangle(mo[1])
            self.play(Create(r1))
            self.play(Write(mo[-3]))
            r2 = SurroundingRectangle(mo[2])
            self.play(Transform(r1, r2))
            self.play(Write(mo[-2]))
            r2 = SurroundingRectangle(mo[3])
            self.play(Transform(r1, r2))
            self.play(Write(mo[-1]))
            self.play(FadeOut(r1))
            self.wait()


    def compuestas(self):
        self.wait()
        notation = Text("Notación de Proposiciones simples")
        self.play(Write(notation))
        self.play(notation.animate.move_to([0, 3, 0]))

        self.next_section(skip_animations=False)
        sg = VGroup(
                Text("p = Elizabeth baila."),
                Text("r = Juan y María son hermanos."),
                Text("q = 2 es mayor que 8."),
                ).arrange(DOWN, aligned_edge=LEFT)

        for s in sg:
            self.play(Write(s[2:]))

        self.wait()
        for s in sg:
            self.play(Write(s[0:2]))
            self.wait(0.5)

        self.play(FadeOut(sg, notation))

        self.next_section(skip_animations=False)
        title = Text("2. Proposiciones compuestas").scale(0.8)
        self.play(Write(title))
        self.wait()
        self.play(title.animate.move_to([-2.5, 3.5, 0]))

        # Proposiciones Adjuntivas
        self.next_section(skip_animations=False)
        pa = VGroup(
                Tex("2.1 Adjuntivas ",
                    r"(... y ..., $\wedge$)").set_color(PURPLE_A),
                Tex("(a) ", "$2 > 8$ ", "y ", "$4 = 5$.",
                    r"$\quad(p$ ", r"$\wedge$ ", r"$q)$"),
                Tex("(b) ", "Mary canta ", "y ", "baila.",
                    r"$\quad(r$ ", r"$\wedge$ ", r"$s)$"),
                Tex("(c) ", "Canto ", "mientras ", "camino.",
                    r"$\quad(t$ ", r"$\wedge$ ", r"$u)$"),
                Tex(
                    "Otros:",
                    " asimismo, pero, ademas, sin embargo, también,"
                    ).scale(0.6),
                Tex(
                    "no obstante,",
                    " incluso, etc.").scale(0.6)
                ).arrange(DOWN, aligned_edge=LEFT).scale(0.8)

        pa.move_to([-3.6, 1.5, 0])

        self.play(Write(pa[0]))
        self.part_animate(pa[1:4])

        for mo in pa[4:]:
            self.play(Write(mo[0]))
            self.wait(0.5)
            self.play(Write(mo[1]))
            self.wait(0.5)

        # Proposiciones Disyuntivas débiles
        self.next_section(skip_animations=False)
        pdd = VGroup(
                Tex("2.2 Disyuntivas débiles",
                    r" (... o ..., $\vee$)").set_color(PURPLE_A),
                Tex("(a) ", "$2 > 8$ ", "o ", "$4 = 5.$",
                    r"$\quad(p$ ", r"$\vee$ ", r"$q)$"),
                Tex("(b) ", "Mary canta ", "o ", "baila.",
                    r"$\quad(r$ ", r"$\vee$ ", r"$s)$"),
                Tex("(c) ", "Escucho música ", "o ", "juego.",
                    r"$\quad(t$ ", r"$\vee$ ", r"$u)$"),
                ).arrange(DOWN, aligned_edge=LEFT).scale(0.8)
        pdd.move_to([-3.6, -1.7, 0])

        self.play(Write(pdd[0]))
        self.wait(0.5)
        self.part_animate(pdd[1:])

        # Proposiciones Disyuntivas fuertes
        self.next_section(skip_animations=False)
        pdf = VGroup(
                Tex("2.3 Disyuntivas fuertes ",
                    "(O ... o ...", r"$\nleftrightarrow$)").set_color(PURPLE_A),
                Tex("(a) ", "$2 > 8$ ", "o ", "$2 < 8$.",
                    r"$\quad(p$ ", r"$\nleftrightarrow$ ", r"$q)$"),
                Tex("(b) ", "O cantas ", "o ", "bailas.",
                    r"$\quad(u$ ", r"$\nleftrightarrow$ ", r"$v)$"),
                Tex("(c) ", "Yo corro ", "o ", "camino.",
                    r"$\quad(s$ ", r"$\nleftrightarrow$ ", r"$t)$"),
                ).arrange(DOWN, aligned_edge=LEFT).scale(0.8)
        pdf.move_to([3.6, 1.9, 0])
        self.play(Write(pdf[0]))
        self.part_animate(pdf[1:])
       
        # Proposiciones Negativas
        self.next_section(skip_animations=False)
        pn = VGroup(
                Tex("2.3 Negativas",
                    r" (no ... , $\neg$)").set_color(PURPLE_A),
                Tex("(a) ", "No ", "hay vida en marte.",
                    r"$\quad(\neg$ ",  "$p)$"),
                Tex("(b) ", "Es falso que ", "2 = 5.",
                    r"$\quad(\neg$ ",  "$q)$"),
                Tex("(c) ", "No ocurre que ", "juego.",
                    r"$\quad(\neg$ ",  "$r)$"),
                ).arrange(DOWN, aligned_edge=LEFT).scale(0.8)
        pn.move_to([3.5, -1.7, 0])

        self.play(Write(pn[0]))
        for mo in pn[1:]:
            self.play(Write(mo[:3]))
            r1 = SurroundingRectangle(mo[1])
            self.play(Create(r1))
            self.play(Write(mo[-2]))
            r2 = SurroundingRectangle(mo[2])
            self.play(Transform(r1, r2))
            self.play(Write(mo[-1]))
            self.play(FadeOut(r1))
            self.wait(0.5)

        self.wait()
        self.play(FadeOut(pa, pdd, pdf, pn))

    def conditionals(self):
        self.wait()

        # Proposiciones conditionals
        self.next_section(skip_animations=False)
        pc = VGroup(
                Tex("2.3 Condicionales",
                    r" (Si [antecedente] entonces [consecuente], $\to$)").scale(1.2).set_color(PURPLE_A),
                Tex("(a) Si corres entonces llegas rápido.",
                    r"\quad ($p \to q$)"),
                Tex("(b) Si ", "$9 > 8$", ", ", "$9 > 7$", r"$\quad(u \to v)$"),
                Tex("(c) Si ", r"$ax^2 + bx + x = 0$", " entonces ",
                    r"$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.",
                    r"$\quad (s \to t)$"),
                Tex("drakenfor"),
                Tex("2.3.1 Forma especial",
                     r" ([consecuente] porque [antecedente], ", r"$\leftarrow$)").scale(1.1).set_color(PURPLE_A),
                Tex("(a) ", "Aprobé ",  "porque ", "estudié. ",
                    r"$\quad(p \leftarrow q)\quad$", r"o $\quad(q \to p)$"),
                Tex("(b) ", "0.5 es racional ", "ya que ", "0.5 = 1/2.",
                    r"$\quad(r \leftarrow s)\quad$", r" o $\quad(s \to r)$"),
                Tex("(c) ", "Llegué temprano ", "dado que ", "vine corriendo.",
                    r"$\quad(m \leftarrow n)\quad$", r" o $\quad(n \to m)$"),
                ).arrange(DOWN, aligned_edge=LEFT).scale(0.8)

        self.play(Write(pc[0][0]))
        self.wait(0.5)
        self.play(Write(pc[0][1]))
        self.wait(0.5)
        self.play(Write(pc[1][0]))
       
       # Ejem 1
        self.next_section(skip_animations=False)
        r1 = SurroundingRectangle(pc[1][0][3:11])
        self.play(Create(r1))
        self.play(Write(pc[1][1][0:2]))
        r2 = SurroundingRectangle(pc[1][0][11:-14])
        self.play(Transform(r1, r2))
        self.play(Write(pc[1][1][2]))
        r2 = SurroundingRectangle(pc[1][0][-14:-1])
        self.play(Transform(r1, r2))
        self.play(Write(pc[1][1][3:]))
        self.play(FadeOut(r1))

        # Ejem2
        self.next_section(skip_animations=False)
        self.play(Write(pc[2][:-1]))
        r1 = SurroundingRectangle(pc[2][1])
        self.play(Create(r1))
        self.play(Write(pc[2][-1][:2]))
        self.play(Write(pc[2][-1][2]))
        r2 = SurroundingRectangle(pc[2][3])
        self.play(Transform(r1, r2))
        self.play(Write(pc[2][-1][3:]))
        self.play(FadeOut(r1))
        
        # Ejem3
        self.next_section(skip_animations=False)
        self.play(Write(pc[3][:-1]), run_time = 3)
        r1 = SurroundingRectangle(pc[3][1])
        self.play(Create(r1))
        self.play(Write(pc[3][-1][:2]))
        r2 = SurroundingRectangle(pc[3][2])
        self.play(Transform(r1, r2))
        self.play(Write(pc[3][-1][2]))
        r2 = SurroundingRectangle(pc[3][3])
        self.play(Transform(r1, r2))
        self.play(Write(pc[3][-1][3:]))
        self.play(FadeOut(r1))

        # Formas especiales
        self.next_section(skip_animations=False)
        self.play(Write(pc[5][0]))
        self.wait(0.5)
        self.play(Write(pc[5][1]), run_time=3)
        self.wait(0.5)
        self.play(Write(pc[5][2]))
        self.wait()

        for i in range(6, 9):
            mo = pc[i]
            self.play(Write(mo[:-2]))
            r1 = SurroundingRectangle(mo[1])
            self.play(Create(r1))
            self.play(Write(mo[-2][:2]))
            r2 = SurroundingRectangle(mo[2])
            self.play(Transform(r1, r2))
            self.play(Write(mo[-2][2]))
            r2 = SurroundingRectangle(mo[3])
            self.play(Transform(r1, r2))
            self.play(Write(mo[-2][3:]))
            self.play(FadeOut(r1))
            self.wait(0.5)
            self.play(Write(mo[-1]))
            self.wait()

        self.play(FadeOut(pc))


        # biconditionals
    def biconditionals(self):
        self.wait()
        pb = VGroup(
                Tex("2.4 Bicondicionales ", "(... si y solo si ..., ",
                    r"$\leftrightarrow)$").scale(1.2).set_color(PURPLE_A),
                Tex("(a) ", "Juan baila ", "si y solo si ", "Mary canta.",
                    r"$\quad(p$", r" $\leftrightarrow$ ", r"$q)$"),
                Tex(r"$\Rightarrow$ ", "Si Juan baila entonces Mary canta ", r"y\\",
                    r"si Mary canta entonces Juan baila.\\",
                    r"$(p \rightarrow q)$", r" $\wedge$ ", r"$(q \rightarrow p)$"),
                Tex("h"),
                Tex("(b) ", r"$n$ es primo ", "si y solo si ", 
                    r"$n$ tiene 2 divisores",
                    r"$\quad(s$", r" $\leftrightarrow$ ", r"$t)$"),
                Tex(r"$\Rightarrow$ ", "Si $n$ es primo entonces tiene 2 divisores ",
                    r"y\\", r"Si $n$ tiene 2 divisores entonces es primo.\\",
                    r"$(s \rightarrow t)$", r" $\wedge$ ", r"$(t \rightarrow s)$")
                ).arrange(DOWN, aligned_edge=LEFT).move_to([0, -0.25, 0])

        self.next_section(skip_animations=False)
        self.play(Write(pb[0][0]))
        self.wait(0.5)
        self.play(Write(pb[0][1]))
        self.wait(0.5)
        self.play(Write(pb[0][2]))
        self.wait()

        self.next_section(skip_animations=False)
        for i in range(1, 6):

            if len(pb[i]) < 2:
                continue

            self.play(Write(pb[i][0:4]), run_time=6)
            self.wait(0.5)
            r1 = SurroundingRectangle(pb[i][1])
            self.play(Create(r1))
            self.play(Write(pb[i][-3]))
            r2 = SurroundingRectangle(pb[i][2])
            self.play(Transform(r1, r2))
            self.play(Write(pb[i][-2]))
            r2 = SurroundingRectangle(pb[i][3])
            self.play(Transform(r1, r2))
            self.play(Write(pb[i][-1]))
            self.play(FadeOut(r1))
            self.wait()

        self.play(FadeOut(pb))

    def notation(self):
        self.wait()
        title = Text("Notatación\nde Proposiciones compuestas.").scale(0.8)
        self.play(Write(title))
        self.play(title.animate.move_to([0, 2.4, 0]))

        vg = VGroup(
                MathTex(r"A\equiv", r"p\wedge q"),
                MathTex(r"B\equiv", r"p\leftrightarrow q"),
                MathTex(r"C\equiv", r"(p \wedge q) \leftrightarrow (p \vee q)")
                ).arrange(DOWN, aligned_edge=LEFT).scale(1.3)

        for mo in vg:
            self.play(Write(mo[1]))
            self.wait(0.5)
            self.play(Write(mo[0]))
            

        self.wait()
        self.play(FadeOut(title, vg))

