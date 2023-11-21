library(reticulate)
system("python C:/Users/storl/miniconda3/envs/torenv/GetStockDataFromYahoo.py --symbol ABT --date_range 3mo --interval 1d --db_file C:/Users/storl/miniconda3/envs/torenv/Stocks.db")
?source_python()
