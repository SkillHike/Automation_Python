import tkinter as tk
import random
import time
import sched

# Define the list of exercises
exercises = ['Stretch your arms', 'Do squats', 'Take a walk', 'Do lunges', 'Stretch your back']


# Define the pop-up window
def show_popup():
    # Choose a random exercise from the list
    exercise = random.choice(exercises)

    # Create the pop-up window
    popup = tk.Tk()
    popup.geometry('200x100')
    popup.title('Exercise Reminder')

    # Add the exercise label to the pop-up window
    exercise_label = tk.Label(popup, text=exercise)
    exercise_label.pack(pady=1)

    # Add the snooze button to the pop-up window
    snooze_button = tk.Button(popup, text='Snooze', command=popup.destroy)
    snooze_button.pack()

    # Display the pop-up window
    popup.mainloop()


# Define the scheduler to show the pop-up every 15 minutes
s = sched.scheduler(time.time, time.sleep)


def show_popup_interval():
    show_popup()
    s.enter(15, 1, show_popup_interval, ())


# Start the scheduler
s.enter(0, 2, show_popup_interval, ())
s.run()
