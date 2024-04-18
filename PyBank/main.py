import csv

# constants
CSV_PATH = "./Resources/budget_data.csv"
OUTPUT_PATH = "./analysis/pybank.txt"

# read file
with open(CSV_PATH) as file:
    csv_reader = csv.reader(file, delimiter=',')

    # header
    # Date,Profit/Losses
    csv_header = next(csv_reader)

    # data
    total_months = 0
    net_profit_loss = 0
    prev_profit_loss = 0
    profit_loss_deltas = []
    profit_loss_deltas_dates = []

    for idx, row in enumerate(csv_reader):
        # total months
        total_months+=1
        # total profit loss
        net_profit_loss+=int(row[1])
        # profit loss deltas
        curr_profit_loss = int(row[1])
        if idx != 0:
            profit_loss_deltas.append( curr_profit_loss - prev_profit_loss )
            profit_loss_deltas_dates.append(row[0])
        prev_profit_loss = int(row[1])


# results
profit_loss_delta_max = max(profit_loss_deltas)
profit_loss_delta_max_idx = profit_loss_deltas.index(profit_loss_delta_max)
profit_loss_delta_min = min(profit_loss_deltas)
profit_loss_delta_min_idx = profit_loss_deltas.index(profit_loss_delta_min)

# console
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${round(sum(profit_loss_deltas)/len(profit_loss_deltas), 2)}")
print(f"Greatest Increase in Profits: {profit_loss_deltas_dates[profit_loss_delta_max_idx]} (${profit_loss_delta_max})")
print(f"Greatest Decrease in Profits: {profit_loss_deltas_dates[profit_loss_delta_min_idx]} (${profit_loss_delta_min})")

# file
with open(OUTPUT_PATH, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_profit_loss}\n")
    file.write(f"Average Change: ${round(sum(profit_loss_deltas)/len(profit_loss_deltas), 2)}\n")
    file.write(f"Greatest Increase in Profits: {profit_loss_deltas_dates[profit_loss_delta_max_idx]} (${profit_loss_delta_max})\n")
    file.write(f"Greatest Decrease in Profits: {profit_loss_deltas_dates[profit_loss_delta_min_idx]} (${profit_loss_delta_min})\n")
