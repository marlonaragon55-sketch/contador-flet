import flet as ft


def main(page: ft.Page):
    page.title = "Contador con Flet"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    contador = ft.Text(value="0", size=60)

    def incrementar(e):
        contador.value = str(int(contador.value) + 1)
        page.update()

    boton = ft.ElevatedButton("Sumar 1", on_click=incrementar)
    page.add(contador, boton)


ft.app(target=main)
