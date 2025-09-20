import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


# data section
data = pd.read_csv('./house_price_regression_dataset.csv')

features_house = data[["Square_Footage", "Num_Bedrooms", "Num_Bathrooms",
                       "Year_Built", "Lot_Size", "Garage_Size", "Neighborhood_Quality"]]
price = data["House_Price"]


reg = LinearRegression()
reg.fit(features_house, price)

predict_values = reg.predict(features_house)


# ui section
root = ttk.Window(title='Multiple Linear Regression')
root.geometry("960x500")
root.resizable(False, False)

# main frame
main_frame = ttk.Frame(root)
main_frame.pack(expand=True, fill='both', padx=10, pady=10)

# top frame for predictions
predict_frame = ttk.Frame(main_frame, bootstyle="light")
predict_frame.pack(side='top', fill='both', expand=True, padx=5, pady=5)

# bottom frame for correlation
correlation_frame = ttk.Frame(main_frame)
correlation_frame.pack(side='bottom', fill='x', padx=5, pady=5)


# correlation output entry (just for display)
correlation_output = ttk.Text(correlation_frame)
correlation_output.pack(fill='x', padx=5, pady=5)


columns = ("Square_Footage", "Num_Bedrooms", "Num_Bathrooms", "Year_Built",
           "Lot_Size", "Garage_Size", "Neighborhood_Quality", "House_Price")
tree = ttk.Treeview(predict_frame, columns=columns,
                    show='headings', bootstyle='primary')
tree.pack(fill='both', expand=True, padx=10, pady=10)

tree.heading('Square_Footage', text="Square_Footage")
tree.heading('Num_Bedrooms', text="Num_Bedrooms")
tree.heading('Num_Bathrooms', text="Num_Bathrooms")
tree.heading('Year_Built', text="Year_Built")
tree.heading('Lot_Size', text="Lot_Size")
tree.heading('Garage_Size', text="Garage_Size")
tree.heading('Neighborhood_Quality', text="Neighborhood_Quality")
tree.heading('House_Price', text="House_Price")


tree.column("Square_Footage", width=100, anchor="center")
tree.column("Num_Bedrooms", width=100, anchor="center")
tree.column("Num_Bathrooms", width=100, anchor="center")
tree.column("Year_Built", width=110, anchor="center")
tree.column("Lot_Size", width=110, anchor="center")
tree.column("Garage_Size", width=100, anchor="center")
tree.column("Neighborhood_Quality", width=130, anchor="center")
tree.column("House_Price", width=120, anchor="center")


# Combine data
combined_data = features_house.copy()
combined_data["House_Price"] = price  # add new row to dataframe


for _, row in combined_data.iterrows():
    tree.insert(
        "", END,
        values=(
            row["Square_Footage"],
            row["Num_Bedrooms"],
            row["Num_Bathrooms"],
            row["Year_Built"],
            row["Lot_Size"],
            row["Garage_Size"],
            row["Neighborhood_Quality"],
            row["House_Price"],
        )
    )


# show result
print(f'Coefficient : {reg.coef_}')
print(f'Intercept : {reg.intercept_}')
# print(f'Predict value : {predict_values}')
print(f'R^2 : {reg.score(features_house , price)}')


features = ["Square_Footage", "Num_Bedrooms", "Num_Bathrooms",
            "Year_Built", "Lot_Size", "Garage_Size", "Neighborhood_Quality"]


max_correlation = 0
max_feature = None
for feature in features:
    correlation = data[feature].corr(data["House_Price"])
    if max_correlation <= correlation:
        max_correlation = correlation
        max_feature = feature
    correlation_output.insert(
        "1.0", f'Correlation between {feature} and House_Price : {correlation:.3f}\n\n')
    # print(f'Correlation between {feature} and House_Price : {correlation:.3f}')
# print(f'Max Correlation {max_feature} : {max_correlation} ')
correlation_output.insert(
        "1.0", f'Max Correlation {max_feature} : {max_correlation} \n\n')
correlation_output.config(state='disabled')

root.mainloop()
