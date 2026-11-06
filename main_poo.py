import flet as ft


class Contador(ft.Column):
    """Control personalizado: guarda el valor y responde a los eventos."""

    def __init__(self):
        super().__init__(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.valor = 0
        self.texto = ft.Text(str(self.valor), size=60)
        self.boton_sumar = ft.ElevatedButton("Sumar 1", on_click=self.incrementar)
        self.boton_reiniciar = ft.OutlinedButton("Reiniciar", on_click=self.reiniciar)
        self.controls = [
            self.texto,
            ft.Row(
                [self.boton_sumar, self.boton_reiniciar],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ]

    def incrementar(self, e):
        self.valor += 1
        self._actualizar_vista()

    def reiniciar(self, e):
        self.valor = 0
        self._actualizar_vista()

    def _actualizar_vista(self):
        self.texto.value = str(self.valor)
        self.update()


def main(page: ft.Page):
    page.title = "Contador POO con Flet"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(Contador())


ft.app(target=main)
