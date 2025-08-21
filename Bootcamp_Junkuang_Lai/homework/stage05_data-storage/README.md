I collected a monthly NVDA dataset covering 2021–2025.

To ensure the saved data was correct, I reloaded both the CSV and Parquet files and compared them with the original DataFrame. During this validation, I found that the date column in the Parquet file was not automatically recognized as a datetime type, which caused a data type mismatch in my validation function.

To fix this, I modified the Parquet saving process to explicitly convert the date column to the datetime data type before saving.

I also created utility functions for reading and writing DataFrames. These functions make it easier to handle both CSV and Parquet files, so I don’t have to manually specify the file type each time.

The code mainly focuses on handling data types and is straightforward. I didn’t add extra error checks because my environment is already set up and I didn’t encounter any issues. If any problems do occur, they are usually easy to spot. I plan to add any required dependencies to requirements.txt in the future.
