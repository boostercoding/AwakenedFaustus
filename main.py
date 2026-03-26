import tkinter
from tkinter import ttk

window = tkinter.Tk() # Root window for everything else. The widget that contains all the other widgets
window.title("Find Better Price")

frame = tkinter.Frame(window)
frame.pack()

# Saving chaos per divine, amount per chaos, and amount per divine
price_frame = tkinter.LabelFrame(frame, text="Price")
price_frame.grid(row=0, column=0, padx=20, pady=10)


chaos_to_divine_label = tkinter.Label(price_frame, text="Chaos per Divine")
chaos_to_divine_label.grid(row=0, column=0)
amount_per_chaos_label = tkinter.Label(price_frame, text="Amount per Chaos")
amount_per_chaos_label.grid(row=0, column=1)
amount_per_divine_label = tkinter.Label(price_frame, text="Amount per Divine")
amount_per_divine_label.grid(row=0, column=2)

chaos_to_divine_entry = tkinter.Entry(price_frame)
amount_per_chaos_entry = tkinter.Entry(price_frame)
amount_per_divine_entry = tkinter.Entry(price_frame)
chaos_to_divine_entry.grid(row=1, column=0)
amount_per_chaos_entry.grid(row=1, column=1)
amount_per_divine_entry.grid(row=1, column=2)

item_amount_label = tkinter.Label(price_frame, text="Amount Buying")
item_amount_spinbox = tkinter.Spinbox(price_frame, from_=1, to=5000)
item_amount_label.grid(row=0, column=3)
item_amount_spinbox.grid(row=1, column=3)

# Hopefully our eyes wont die after these 2 neat lines
for widget in price_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)
    
# Frame for the math
math_frame = tkinter.LabelFrame(frame, text="Math")
math_frame.grid(row=1, column=0, padx=20, pady=10)

result_label = tkinter.Label(math_frame, text="Enter values and click Calculate")
result_label.pack(padx=10, pady=10)

# ----------------- LOGIC -----------------
def calculate_better_price():
    try:
        chaos_per_divine = float(chaos_to_divine_entry.get())
        items_per_chaos = float(amount_per_chaos_entry.get())
        items_per_divine = float(amount_per_divine_entry.get())
        quantity = int(item_amount_spinbox.get())

        # Convert ratios to cost per item
        chaos_per_item = 1 / items_per_chaos
        divine_per_item = 1 / items_per_divine

        # Total costs
        total_chaos = chaos_per_item * quantity
        total_divine = divine_per_item * quantity
        total_divine_in_chaos = total_divine * chaos_per_divine
        
        # Split divine cost into divines + chaos remainder
        whole_divines = int(total_divine)
        remaining_divine = total_divine - whole_divines
        remaining_chaos = remaining_divine * chaos_per_divine

        if total_chaos < total_divine_in_chaos:
            result = "Cheaper to buy with CHAOS"
        elif total_chaos > total_divine_in_chaos:
            result = "Cheaper to buy with DIVINE"
        else:
            result = "Both cost the same"

        result_label.config(
    text=(
        f"Total Chaos Cost: {total_chaos:.2f} chaos\n\n"
        f"Total Divine Cost:\n"
        f"  {total_divine:.5f} divine\n"
        f"  ({total_divine_in_chaos:.2f} chaos)\n"
        f"  {whole_divines} div + {remaining_chaos:.0f} chaos\n\n"
        f"{result}"
    )
)

    except (ValueError, ZeroDivisionError):
        messagebox.showerror("Input Error", "Please enter valid, non-zero values.")
        
calculate_button = tkinter.Button(
    math_frame, text="Calculate", command=calculate_better_price
)
calculate_button.pack(pady=10)

window.mainloop() # An infinite loop that runs as long as the application is open. Stops when the application is closed.
