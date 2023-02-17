# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Lifting Log', width=600, height=300)

with dpg.window(label="Select Task"):
    dpg.add_text("LiftingLog - Workout Tracker")
    dpg.add_button(label="Enter New Workout")
    dpg.add_button(label="View Old Workouts")
#    dpg.add_input_text(label="string", default_value="Quick brown fox")
#    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
