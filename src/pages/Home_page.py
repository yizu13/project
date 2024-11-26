import flet as ft


def main_button(page):
    def button_clicked(e):
        b.data += 1
        t.value = f"Button clicked {b.data} time(s)"
        t.update()  # Ensure UI updates

    # Create the button and text
    b = ft.ElevatedButton("Button with 'click' event", on_click=button_clicked, data=0)
    t = ft.Text("Button clicked 0 time(s)")

    # Add controls to the page
    page.add(b, t)