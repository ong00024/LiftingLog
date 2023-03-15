# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import dearpygui.dearpygui as dpg
import functions

dpg.create_context()
dpg.create_viewport(title='Lifting Log', width=360, height=720)

def new_work():
    functions.new_workout()

def view_work():
    functions.view_workouts()

with dpg.window(label="Select Task",width=360, height=120):
    title_card = dpg.add_text("LiftingLog - Workout Tracker")
    create_workout_button = dpg.add_button(label="Enter New Workout", callback=new_work)
    view_workout_button = dpg.add_button(label="View Old Workouts", callback=view_work)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


