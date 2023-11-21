from YahooAPI import YahooAPI
import pandas as pd

def main():
  api = YahooAPI("PLTR", date_range="5d", interval="1d")
  data = api.get_stock_data()

  # Create and print a pandas dataframe
  df = pd.DataFrame(data)

  print(df)
  print(type(df))

  
  
if __name__ == "__main__":
  main()

