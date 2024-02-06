""" This module is used to store the data in a pandas dataframe and export it to a csv file. """

import pandas as pd


class DataCollection:
    """ Data Collection class to store the data in a pandas dataframe and export it to a csv file. """

    def __init__(self):
        self.df = pd.DataFrame(columns=["Country_Name", "Company_Name", "Product_Name", "ProductURL", "ImageURL", "Raw_Category", "Category", "Currency", "Price", "Description", "Gold_Colour", "Weight", "Gold_Purity", "Diamond_Colour", "Diamond_Clarity", "Diamond_Pieces", "Diamond_Weight", "Ratings", "RatingCounts"])

    def add_row(self, new_row: dict) -> None:
        """Method to add a new row to the dataframe. 

        Args:
            new_row: The new row to be added to the dataframe.
        """
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)

    def get_df(self, name: str) -> None:       
        """Method to export the dataframe to a csv file.
        
        Args:
            name: The name of the csv file.
        """
        # export to csv
        self.df.to_csv(f"{name}.csv", index=False)
