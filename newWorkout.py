import dearpygui.dearpygui as dpg

item_table = []

# builts the context window
dpg.create_context()
dpg.create_viewport(title="invengo", width=600, height=600)


# outputs the data from the inputs and callbacks
def reg(sender):
    print(dpg.get_value(sender))
    item_table.append(dpg.get_value(sender))


def new_workout():
    with dpg.window(label="new workout",width=360, height=240):
        dpg.add_input_text(label="Title", hint="Workout of the day")
        dpg.add_input_text(label="ExerciseA", hint="First Exercise...", width=100)
        dpg.add_input_int(label="sets", width=100)
        dpg.add_input_int(label="reps", width=100)
        dpg.add_input_int(label="Weight", width=100)

def lel(sender):
    with dpg.window(label="Select Task", width=300, height=300):
        dpg.add_text("LiftingLog - Workout Tracker")
        dpg.add_button(label="Enter New Workout", callback=new_workout)
        dpg.add_button(label="View Old Workouts")



# builts the datainputs
with dpg.window(tag="PW"):
    item_name = dpg.add_input_text(label="input text", hint="something here...",
                                   callback=reg, on_enter=True)
    item_amount = dpg.add_combo(label="Item Amount", default_value=1, items=(1, 2, 3, "four"), callback=reg)
    check_button = dpg.add_button(label="CLICK ME", callback=lel)
dpg.set_item_callback(item_name, reg)

# debugging
print(dpg.get_value(item_name))

# start the modul
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("PW", True)
dpg.start_dearpygui()
dpg.destroy_context()

# debugging
print(item_table)