daily_sales=[
    1,2,4,5,1,3,2,32,43,12,54,76,43,86,43,12,65,327,43,874,75
]

total_cup=sum(sales for sales in daily_sales if sales>10)
print(total_cup)