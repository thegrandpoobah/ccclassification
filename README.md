# classification

This is a quick tool that I use to classify the transactions in my bank and credit card statements.
It reads in LibreOffice Calc format workbooks (with multiple spreadsheets) and categorizes the individual
transactions based on a trained model that I've built up based on manually classifying 3 months of my
statements.

To use, you will have to follow 4 basic steps

1. your credit card statements from your bank in the template format provided by this application
2. manually categorize a subset of your statements into a training file
3. use the `train.py` file to train the model
4. use the `classify.py` file to categorize the rest

The tool is far from perfect, but it cuts down the categorization time of a statement greatly (and it was fun to build).
