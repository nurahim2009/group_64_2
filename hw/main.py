import flet as ft
from db import main_db

def main(page: ft.Page):
    page.title = "ToDo List"
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column(spacing=20)

    def view_tasks(task_id, task_text):
        task_field = ft.TextField(read_only=True, value=task_text, expand=True)
        row_container = ft.Row()

        def enable_edit(_):
            task_field.read_only = not task_field.read_only
            task_field.border_color = "blue" if not task_field.read_only else None
            page.update() 

        def save_task(_):
            main_db.update_task(task_id=task_id, new_task=task_field.value)
            task_field.read_only = True
            task_field.border_color = None
            page.update()

        def delete_task(_):
            main_db.delete_task(task_id) 
            task_list.controls.remove(row_container)
            page.update()
            print(f"Задача {task_id} удалена")

        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=enable_edit)
        save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=save_task)
        delete_button = ft.IconButton(
            icon=ft.Icons.DELETE_FOREVER, 
            icon_color=ft.Colors.RED_ACCENT, 
            on_click=delete_task
        )

        row_container.controls = [
            task_field,
            edit_button,
            save_button,
            delete_button
        ]
        return row_container

    def add_task_db(_):
        if task_input.value:
            task_text = task_input.value
            task_id = main_db.add_task(task=task_text)
            task_list.controls.append(view_tasks(task_id=task_id, task_text=task_text))
            task_input.value = "" 
            page.update()

    task_input = ft.TextField(label="Введите задачу", expand=True, on_submit=add_task_db)
    add_task_button = ft.ElevatedButton("ADD", on_click=add_task_db, icon=ft.Icons.ADD)

    main_object = ft.Row([task_input, add_task_button])

    page.add(main_object, task_list)

if __name__ == "__main__":
    main_db.init_db()
    ft.app(target=main)