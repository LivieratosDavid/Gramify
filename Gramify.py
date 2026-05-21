import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox

g = 9.81

# ---------------- MAIN WINDOW ----------------
window = tk.Tk()
window.title("Motion Simulator")
window.geometry("500x600")
window.resizable(False, False)

# ---------------- VARIABLES ----------------
motion_var = tk.StringVar(value="Linear Motion")
diagram_var = tk.StringVar(value="x-t")


# ---------------- FUNCTIONS ----------------
def update_diagrams(*args):
    motion = motion_var.get()

    if motion == "Linear Motion":
        diagram_menu["values"] = ["x-t", "v-t"]
        angle_label.place_forget()
        angle_entry.place_forget()
        height_label.place_forget()
        height_entry.place_forget()
        acceleration_label.place_forget()
        acceleration_entry.place_forget()

    elif motion == "Accelerated Motion":
        diagram_menu["values"] = ["x-t", "v-t"]
        acceleration_label.place(x=250, y=320, anchor="center")
        acceleration_entry.place(x=250, y=345, anchor="center")
        angle_label.place_forget()
        angle_entry.place_forget()
        height_label.place_forget()
        height_entry.place_forget()

    elif motion == "Projectile Motion":
        diagram_menu["values"] = ["x-t", "y-t", "x-y"]
        angle_label.place(x=250, y=320, anchor="center")
        angle_entry.place(x=250, y=345, anchor="center")
        height_label.place(x=250, y=375, anchor="center")
        height_entry.place(x=250, y=400, anchor="center")
        acceleration_label.place_forget()
        acceleration_entry.place_forget()

    diagram_var.set(diagram_menu["values"][0])


def simulate():
    try:
        motion = motion_var.get()
        t_max = float(time_entry.get())
        v0 = float(velocity_entry.get())
        diagram = diagram_var.get()
        m = float(mass_entry.get())
        t = np.linspace(0, t_max, 200)

        # ---------------- LINEAR MOTION ----------------
        if motion == "Linear Motion":
            x = v0 * t
            v = np.full_like(t, v0)
            dK = 0
            U = 0


            if diagram == "x-t":
                y_data, ylabel, title = x, "Distance (m)", "Linear Motion: x-t"
            else:
                y_data, ylabel, title = v, "Velocity (m/s)", "Linear Motion: v-t"

            plt.figure(figsize=(8, 5))
            plt.plot(t, y_data, color="red", linewidth=3)
            plt.title(title)
            plt.xlabel("Time (s)")
            plt.ylabel(ylabel)
            plt.figtext(0.15, 0.02, f"U={U} J", fontsize=9, color = "red")
            plt.figtext(0.02, 0.02, f"ΔK = {dK} J", fontsize=9, color="darkred")
            plt.grid(True)
            plt.show()

        # ---------------- ACCELERATED MOTION ----------------
        elif motion == "Accelerated Motion":
            a = float(acceleration_entry.get())
            x = v0 * t + 0.5 * a * t**2
            v = v0 + a * t
            K_init = 1/2 * m * v0**2
            K_final = 1/2 * m * v[-1]**2
            d_K = K_final - K_init
            U = 0


            if diagram == "x-t":
                y_data, ylabel, title = x, "Distance (m)", "Accelerated Motion: x-t"
            else:
                y_data, ylabel, title = v, "Velocity (m/s)", "Accelerated Motion: v-t"

            plt.figure(figsize=(8, 5))
            plt.plot(t, y_data, color="red", linewidth=3)
            plt.title(title)
            plt.xlabel("Time (s)")
            plt.ylabel(ylabel)
            plt.grid(True)
            plt.figtext(0.15, 0.02, f"U={U}", fontsize=9, color = "red")
            plt.figtext(0.02, 0.02, f"ΔK = {d_K:.2f} J", fontsize=9, color="darkred")
            plt.show()

        # ---------------- PROJECTILE MOTION ----------------
        elif motion == "Projectile Motion":
        # -------------- MATH ------------------- 
            theta = float(angle_entry.get())
            h0 = float(height_entry.get())
            angle = np.radians(theta)
            vx = v0 * np.cos(angle)        # ← must be before y
            vy = v0 * np.sin(angle)        # ← must be before y
            x = vx * t
            y = np.maximum(h0 + vy * t - 0.5 * g * t**2, 0)

            landing_index = np.where(y == 0)[0]   # ← cutoff before t_flight
            if len(landing_index) > 0:
                cutoff = landing_index[0]
                x = x[:cutoff]
                y = y[:cutoff]

            t_flight = t[len(y)-1]         # ← after cutoff
            vy_final = vy - g * t_flight
            v_final = np.sqrt(vx**2 + vy_final**2)
            K_init = 1/2 * m * v0**2
            K_final = 1/2 * m * v_final**2
            d_K = K_final - K_init
            U_start = m * g * h0
            U_final = 0
            dU = U_start - U_final
        # ----------- DIAGRAMS -----------
            if diagram == "x-t":
                plt.figure(figsize=(8, 5))
                plt.plot(t, x, color="red", linewidth=3)
                plt.title("Projectile Motion: x-t")
                plt.xlabel("Time (s)")
                plt.ylabel("Horizontal Distance (m)")
                plt.figtext(0.15, 0.02, f"ΔU={dU} J", fontsize=9, color = "red")
                plt.figtext(0.02, 0.02, f"ΔK = {d_K:.2f} J", fontsize=9, color="darkred")
                plt.grid(True)
                plt.show()

            elif diagram == "y-t":
                plt.figure(figsize=(8, 5))
                plt.plot(t, y, color="red", linewidth=3)
                plt.title("Projectile Motion: y-t")
                plt.xlabel("Time (s)")
                plt.ylabel("Vertical Distance (m)")
                plt.figtext(0.15, 0.02, f"U={dU} J", fontsize=9, color = "red")
                plt.figtext(0.02, 0.02, f"ΔK = {d_K:.2f} J", fontsize=9, color="darkred")
                plt.grid(True)
                plt.show()

            else:
                plt.figure(figsize=(8, 5))
                plt.plot(x, y, color="red", linewidth=3)
                plt.title("Projectile Trajectory (x-y)")
                plt.xlabel("Horizontal Distance (m)")
                plt.ylabel("Vertical Distance (m)")
                plt.grid(True)
                plt.figtext(0.15, 0.02, f"U={dU} J", fontsize=9, color = "red")
                plt.figtext(0.02, 0.02, f"ΔK = {d_K:.2f} J", fontsize=9, color="darkred")
                plt.show()

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


# ---------------- WIDGETS ----------------

# Title
title_label = tk.Label(window, text="Physics Motion Simulator", font=("Arial", 18, "bold"))
title_label.place(x=250, y=25, anchor="center")

# Motion type
motion_label = tk.Label(window, text="Select Motion Type:")
motion_label.place(x=250, y=70, anchor="center")
motion_menu = ttk.Combobox(window, textvariable=motion_var,
                           values=["Linear Motion", "Accelerated Motion", "Projectile Motion"],
                           state="readonly")
motion_menu.place(x=250, y=95, anchor="center")

# Max time
time_label = tk.Label(window, text="Maximum Time (s):")
time_label.place(x=250, y=140, anchor="center")
time_entry = tk.Entry(window)
time_entry.place(x=250, y=165, anchor="center")

# Mass Entry
mass_label = tk.Label(window, text="Mass (kg):")
mass_entry = tk.Entry(window)
mass_label.place(x=250, y=265, anchor="center")
mass_entry.place(x=250, y=290, anchor="center")

# Initial velocity
velocity_label = tk.Label(window, text="Initial Velocity (m/s):")
velocity_label.place(x=250, y=205, anchor="center")
velocity_entry = tk.Entry(window)
velocity_entry.place(x=250, y=230, anchor="center")

# Mass
mass_label.place(x=250, y=265, anchor="center")
mass_entry.place(x=250, y=290, anchor="center")

# Acceleration (hidden by default, shown for Accelerated Motion)
acceleration_label = tk.Label(window, text="Acceleration (m/s²):")
acceleration_entry = tk.Entry(window)

# Angle (hidden by default, shown for Projectile Motion)
angle_label = tk.Label(window, text="Launch Angle (degrees):")
angle_entry = tk.Entry(window)

# Height (hidden by default, shown for Projectile Motion)
height_label = tk.Label(window, text="Initial Height (m):")
height_entry = tk.Entry(window)

# Diagram selection — pushed down to make room for angle + height
diagram_label = tk.Label(window, text="Select Diagram:")
diagram_label.place(x=250, y=440, anchor="center")
diagram_menu = ttk.Combobox(window, textvariable=diagram_var,
                            values=["x-t", "v-t"], state="readonly")
diagram_menu.place(x=250, y=465, anchor="center")

# Simulate button
simulate_button = tk.Button(window, text="Run Simulation",
                            font=("Arial", 12, "bold"), bg="lightblue",
                            command=simulate)
simulate_button.place(x=250, y=560, anchor="center")

# ---------------- START ----------------
motion_var.trace_add("write", update_diagrams)
update_diagrams()
window.mainloop()
