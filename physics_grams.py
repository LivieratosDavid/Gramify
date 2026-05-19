import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

print(" _____ ____  ____  _      _      _  ________  _
/  __//  __\/  _ \/ \__/|/ \__/|/ \/    /\  \//
| |  _|  \/|| / \|| |\/||| |\/||| ||  __\ \  / 
| |_//|    /| |-||| |  ||| |  ||| || |    / /  
\____\\_/\_\\_/ \|\_/  \|\_/  \|\_/\_/   /_/   
                                               ")
question = int(input("What motion? (1 - Linear Motion, 2 - Accelerated Motion, 3 - Projectile Motion): "))
window = tk.Tk()

g = 9.81

#--Projectile Motion--
def projectile_motion():
    t_max = int(input("Put the max time of the motion: "))
    t = np.linspace(0, t_max, 100)

    v0 = int(input("Put your initial velocity: "))
    theta = int(input("Angle of shooting:"))
    diagram = input("What diagram do you want? (x-t OR y-t): ")

    angle = np.radians(theta)

    vx = v0 * np.cos(angle)
    vy = v0 * np.sin(angle)

    x = v0*t
    y = vy * t - 0.5 * g * t**2

    y = np.maximum(y, 0)
   
    if diagram == "x-t":
        plt.figure(figsize=(8, 5))
        plt.plot(t, x)
        plt.plot(t, x, linewidth=3)
        plt.plot(t, x, color="red")
        plt.title("Horizontal Motion")
        plt.ylabel("Distance (m)")
        plt.xlabel("Time (s)")
        plt.grid(True)

    elif diagram == "y-t":
        plt.figure(figsize=(8, 5))
        plt.plot(t, y)
        plt.plot(t, y, linewidth=3)
        plt.plot(t, y, color="red")
        plt.title("Motion")
        plt.ylabel("Vertical Distance (m/s)")
        plt.xlabel("Time (s)")
        plt.grid(True)

    else:
        print("Oops!")

    plt.show()
#--Accelerated Motion--
def accelerated_motion():
    t_max = int(input("Put the max time of the motion: "))
    t = np.linspace(0, t_max, 100)

    v0 = int(input("Put your initial velocity: "))
    a = int(input("Put your acceleration (constant): "))
    diagram = input("What diagram do you want? (x-t OR v-t): ")

    x = v0 * t + 0.5 * a * t**2
    v = v0 + a * t

    if diagram == "x-t":
        plt.figure(figsize=(8, 5))
        plt.plot(t, x)
        plt.plot(t, x, linewidth=3)
        plt.plot(t, x, color="red")
        plt.title("Motion")
        plt.ylabel("Distance (m)")
        plt.xlabel("Time (s)")
        plt.grid(True)

    elif diagram == "v-t":
        plt.figure(figsize=(8, 5))
        plt.plot(t, v)
        plt.plot(t, v, linewidth=3)
        plt.plot(t, v, color="red")
        plt.title("Motion")
        plt.ylabel("Velocity (m/s)")
        plt.xlabel("Time (s)")
        plt.grid(True)

    else:
        print("Oops!")

    plt.show()
#--Linear Motion--
def linear_motion():
    t_max = int(input("Put the max time of the motion: "))
    t = np.linspace(0, t_max, 100)

    v0 = int(input("Put your initial velocity: "))
    diagram = input("What diagram do you want? (x-t OR v-t): ")

    x = v0 * t
    v = np.full_like(t, v0)

    if diagram == "x-t":
        plt.figure(figsize=(8, 5))
        plt.plot(t, x)
        plt.plot(t, x, linewidth=3)
        plt.plot(t, x, color="red")
        plt.title("Motion")
        plt.ylabel("Distance (m)")
        plt.xlabel("Time (s)")
        plt.grid(True)

    elif diagram == "v-t":
        plt.figure(figsize=(8, 5))
        plt.plot(t, v)
        plt.plot(t, v, linewidth=3)
        plt.plot(t, v, color="red")
        plt.title("Motion")
        plt.ylabel("Velocity (m/s)")
        plt.xlabel("Time (s)")
        plt.grid(True)

    else:
        print("Oops!")

    plt.show()

if question == 1:
    linear_motion()

elif question == 2:
    accelerated_motion()

elif question == 3:
    projectile_motion()

else:
    print("Invalid option")