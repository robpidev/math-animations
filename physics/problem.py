from manim import * 

class TablonProblema(Scene):
    def construct(self):
        # Config
        SCALE = 1.2  # 1 unidad = 1 metro
        
        # Titulo
        titulo = Text("Problema del tablón y el muchacho", font_size=36)
        self.play(Write(titulo))
        self.wait(1)
        self.play(FadeOut(titulo))

        # Dibujar el suelo
        suelo = Line(LEFT*7, RIGHT*7, color=GRAY).shift(DOWN*2)
        self.play(Create(suelo))

        # Dibujar el tablon
        tablon = Rectangle(width=6*SCALE, height=0.3, fill_opacity=1, color=GREEN)
        tablon.shift(DOWN*1.8)
        marcas = VGroup(*[Line(UP*0.15, DOWN*0.15).move_to(tablon.get_left() + RIGHT*i*SCALE) 
                          for i in range(7)])
        self.play(Create(tablon), Create(marcas))
        
        # Etiquetas del tablon
        etiqueta_6m = Text("6 m", font_size=24).next_to(tablon, UP)
        punto_P = Dot(tablon.get_right(), color=YELLOW)
        label_P = Text("P").scale(0.7).next_to(punto_P, UP)
        self.play(Write(etiqueta_6m), Create(punto_P), Write(label_P))

        # Crear el muchacho como un circulo + cabeza
        muchacho = VGroup(
            Circle(radius=0.15, color=BLUE, fill_opacity=1),
            Circle(radius=0.08, color=GRAY, fill_opacity=1).shift(UP*0.2)
        ).move_to(tablon.get_left() + RIGHT*1*SCALE + UP*0.3)
        
        etiqueta_m = MathTex("m_m").scale(0.8).next_to(muchacho, UP)
        self.play(FadeIn(muchacho), Write(etiqueta_m))
        
        # Datos iniciales
        datos = VGroup(
            Text("Datos:", font_size=28),
            MathTex("L = 6\\,\\text{m}"),
            MathTex("m_t = \\frac{2}{3} m_m"),
            Text("Superficie lisa → sin fuerzas externas")
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        
        self.play(Write(datos))
        self.wait(2)

        # Paso 1: Mostrar fuerzas
        paso1 = Text("Paso 1: Fuerzas internas acción-reacción", font_size=28).to_edge(UP)
        self.play(Transform(datos, paso1))
        
        fuerza_m_t = Arrow(muchacho.get_bottom(), DOWN*0.5, color=RED)
        fuerza_t_m = Arrow(tablon.get_center() + UP*0.15, UP*0.5, color=RED)
        txt_F = MathTex("F").scale(0.8)
        txt_F1 = txt_F.copy().next_to(fuerza_m_t, RIGHT)
        txt_F2 = txt_F.copy().next_to(fuerza_t_m, RIGHT)
        
        self.play(GrowArrow(fuerza_m_t), GrowArrow(fuerza_t_m), Write(txt_F1), Write(txt_F2))
        self.wait(1)

        # Paso 2: Ecuaciones de Newton
        paso2 = Text("Paso 2: 2ª Ley de Newton", font_size=28).to_edge(UP)
        eq1 = MathTex("F = m_m a_m").shift(UP*0.5)
        eq2 = MathTex("F = m_t a_t = \\frac{2}{3}m_m a").shift(DOWN*0.5)
        
        self.play(Transform(datos, paso2), FadeOut(fuerza_m_t, fuerza_t_m, txt_F1, txt_F2))
        self.play(Write(eq1), Write(eq2))
        self.wait(2)
        
        # Paso 3: Relación de aceleraciones
        paso3 = Text("Paso 3: Relacionar aceleraciones", font_size=28).to_edge(UP)
        eq3 = MathTex("a_m = \\frac{2}{3}a").shift(UP*0.5)
        eq4 = MathTex("a_{m/t} = a_m + a = \\frac{5}{3}a").shift(DOWN*0.5)
        
        self.play(Transform(datos, paso3), FadeOut(eq1, eq2))
        self.play(Write(eq3), Write(eq4))
        self.wait(2)

        # Animacion del movimiento
        paso4 = Text("Paso 4: Animación del movimiento", font_size=28).to_edge(UP)
        self.play(Transform(datos, paso4), FadeOut(eq3, eq4))
        
        # Mover tablon 3m a la izquierda, muchacho 2m a la derecha respecto al suelo
        tablon_target = tablon.copy().shift(LEFT*3*SCALE)
        marcas_target = marcas.copy().shift(LEFT*3*SCALE)
        muchacho_target = muchacho.copy().shift(RIGHT*2*SCALE)
        
        # Flechas de desplazamiento
        flecha_tablon = Arrow(tablon.get_center(), tablon_target.get_center(), color=ORANGE)
        flecha_muchacho = Arrow(muchacho.get_center(), muchacho_target.get_center(), color=GREEN)
        txt_3m = Text("3 m", color=ORANGE).scale(0.7).next_to(flecha_tablon, DOWN)
        txt_2m = Text("2 m", color=GREEN).scale(0.7).next_to(flecha_muchacho, UP)
        
        self.play(GrowArrow(flecha_tablon), GrowArrow(flecha_muchacho), 
                  Write(txt_3m), Write(txt_2m))
        
        self.play(
            Transform(tablon, tablon_target),
            Transform(marcas, marcas_target),
            Transform(muchacho, muchacho_target),
            run_time=3
        )
        
        # Paso 5: Resultado
        paso5 = Text("Paso 5: Resultado", font_size=28).to_edge(UP)
        resultado = MathTex("x_m = 2\\,\\text{m}", color=GREEN).scale(1.5)
        
        self.play(Transform(datos, paso5))
        self.play(Write(resultado))
        self.wait(3)
        
        self.play(FadeOut(*self.mobjects))
