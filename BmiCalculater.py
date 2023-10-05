import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert height to meters
        bmi = weight / (height ** 2)
        result_label.config(text=f"Your BMI: {bmi:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid values for weight and height.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and pack widgets
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Height (cm):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
