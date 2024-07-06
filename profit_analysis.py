import tkinter as tk

def max_subarray_sum(arr, low, high):
    # Base case: if the array has only one element
    if low == high:
        return low, high, arr[low], arr[low]

    # Recursive case: divide the array into two halves
    mid = (low + high) // 2

    # Find the maximum sum subarrays in the left and right halves
    left_low, left_high, left_sum, left_max = max_subarray_sum(arr, low, mid)
    right_low, right_high, right_sum, right_max = max_subarray_sum(arr, mid + 1, high)

    # Find the maximum sum subarray crossing the midpoint
    cross_low, cross_high, cross_sum = find_crossing_subarray(arr, low, mid, high)

    # Compare the three sums to find the overall maximum
    if left_max >= right_max and left_max >= cross_sum:
        return left_low, left_high, left_sum, left_max
    elif right_max >= left_max and right_max >= cross_sum:
        return right_low, right_high, right_sum, right_max
    else:
        return cross_low, cross_high, cross_sum, cross_sum

def find_crossing_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    max_left = mid
    total = 0

    # Find the maximum sum subarray on the left of the midpoint
    for i in range(mid, low - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
            max_left = i

    right_sum = float('-inf')
    max_right = mid + 1
    total = 0

    # Find the maximum sum subarray on the right of the midpoint
    for i in range(mid + 1, high + 1):
        total += arr[i]
        if total > right_sum:
            right_sum = total
            max_right = i

    return max_left, max_right, left_sum + right_sum

def show_result():
    try:
        monthly_income = [float(x) for x in income_entry.get().split(",")]
        start_month, end_month, max_sum, _ = max_subarray_sum(monthly_income, 0, len(monthly_income) - 1)

        result_text = (
            f"Monthly Income: {monthly_income}\n"
            f"Most profitable period: Month {start_month + 1} to Month {end_month + 1}\n"
            f"Maximum Income: {max_sum:.2f}"
        )

        result_label.config(text=result_text)
    except ValueError:
        result_label.config(text="Error: Please enter valid numerical values.")

# Create the main window
root = tk.Tk()
root.title("Profit Analysis")

# Create and pack widgets
info_label = tk.Label(root, text="Enter monthly incomes (comma-separated):")
info_label.pack(pady=10)

income_entry = tk.Entry(root, width=30)
income_entry.pack(pady=10)

analyze_button = tk.Button(root, text="Analyze Profit", command=show_result)
analyze_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
