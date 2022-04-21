from tkinter import *
from functools import partial
import subprocess
main_window = Tk()

def load_main_window():
    title = Label(main_window, text="DTLS simulator", font=("", 20))
    subtitle = Label(main_window, text="!Add Description!")
    title.pack()
    subtitle.pack()
    run_sim_parallel_btn = Button(text="Run Simulation", width=15, height=3,command=run_sim_on_click)
    run_sim_parallel_btn.pack()
    run_quick_sim_btn = Button(text="Quick Simulation", width=15, height=3,command=run_sim_on_click)
    run_quick_sim_btn.pack()


def select_main_options():
    sec_choise = StringVar()
    sec_choise.set("Choose from list:")
    types_list = [1,2,3]
    sec_manu = OptionMenu(main_window, sec_choise, *types_list)
    sec_manu.pack()

def clean_selection():
    for widgets in main_window.winfo_children():
        widgets.destroy()

def run_sim_on_click():
    sim_path = 'src/simulation_V1.0.1.py'
    subprocess.call(f"python3 {sim_path}", shell=True)


load_main_window()
#select_main_options()
main_window.mainloop()