import math

og_stock_price = 15.30
og_money_spent = 1000
new_stock_price = 380


number_of_stocks_bought = math.floor(og_money_spent / og_stock_price)

og_value_owned = og_stock_price * number_of_stocks_bought

current_value_owned = (number_of_stocks_bought * new_stock_price)

percent_gain = (current_value_owned - og_value_owned) / og_value_owned

display_og_stock_price = '${:,.2f}'.format(og_stock_price)
display_og_money_spent = '${:,.2f}'.format(og_money_spent)
display_og_value_owned = '${:,.2f}'.format(og_value_owned)
display_new_stock_price = '${:,.2f}'.format(new_stock_price)
display_current_value_owned = '${:,.2f}'.format(current_value_owned)
display_percent_gain = '{:.2%}'.format(percent_gain)

print('Original stock price: ' + display_og_stock_price)
print('Spent: ' + display_og_money_spent)
print('Quantity of stocks bought: ' + str(number_of_stocks_bought))
print('Original stock amount net worth: ' + display_og_value_owned)
print('Current  stock amount net worth: ' + display_current_value_owned)
print('The value has increased: ' + display_percent_gain)

print('\n\n')

spent = 11762.64
cur_value_2026 = 18991.46
now_gain_per = (cur_value_2026 - spent) / spent
print(now_gain_per)
gain_per = '{:.2%}'.format(now_gain_per)
print(gain_per)

"""
show_og_value_owned = '${:,.2f}'.format(og_value_owned)

                    '${:,.2f}' string
                        $   Currency
                        :,  Thousands comma separater
                        .2f Show 2 decimal places
                    
                        .format(variable) method

display_percent_gain = '{:.2f}%'.format(percent_gain)
                    '{:.2%}' Show percent value with 2 decimal places

Rounding up 
(math.ceil(2.3)) 
    3
Rounding Down
(math.floor(2.3))
    2  

og_stock_price = 15.30
og_money_spent = 1000
new_stock_price = 380  
"""