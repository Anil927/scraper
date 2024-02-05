import pandas as pd


class DataCollection:
    def __init__(self):
        self.df = pd.DataFrame(columns=["Country_Name", "Company_Name", "Product_Name", "ProductURL", "ImageURL", "Raw_Category", "Category", "Currency", "Price", "Description", "Gold_Colour", "Weight", "Gold_Purity", "Diamond_Colour", "Diamond_Clarity", "Diamond_Pieces", "Diamond_Weight", "Ratings", "RatingCounts"])

    def add_row(self, new_row):
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)

    def get_df(self, name):       
        # export to csv
        self.df.to_csv(f"{name}.csv", index=False)
