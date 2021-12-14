bill = float(input("Enter the bill to be paid($): "))
split_among = int(input("Split the bill among: "))
tip = int(input("Enter the percent of tip: "))
percent_tip = tip/100
tip_amount = bill*percent_tip
total_amount = tip_amount + bill
tip_calculate = total_amount/split_among
final_tip = '%.2f'% tip_calculate
print(f"Total tip you need to pay is: {final_tip}") 