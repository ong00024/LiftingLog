import dearpygui.dearpygui as dpg
import sqlite3 as sq


def new_workout():
    with dpg.window(label="new workout",width=360, height=640, pos=[0,120]):
        dpg.add_input_text(label="Title", hint="Workout of the day")
        dpg.add_input_text(label="Exercise 1", hint="First Exercise...", width=150)
        dpg.add_input_int(label="Sets", width=100)
        dpg.add_input_int(label="Reps", width=100)
        dpg.add_input_float(label="Weight", width=100)
        dpg.add_input_text(label="Exercise 2", hint="Second Exercise...", width=150)
        dpg.add_input_int(label="Sets", width=100)
        dpg.add_input_int(label="Reps", width=100)
        dpg.add_input_float(label="Weight", width=100)
        dpg.add_input_text(label="Exercise 3", hint="Third Exercise...", width=150)
        dpg.add_input_int(label="Sets", width=100)
        dpg.add_input_int(label="Reps", width=100)
        dpg.add_input_float(label="Weight", width=100)
        dpg.add_button(label="save", callback=save_data)

def save_data(sender, app_data):
    print("saving...")
def view_workouts():
    print("Viewing old workouts...")