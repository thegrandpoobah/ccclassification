# Household Budgeting Tool

This is a set of tools that we use to classify the transactions in our household bank and credit card statements. It essentially does 3 things:

1. It reads in Bank Account and Credit Card statements formatted in LibreOffice Calc workbooks (with multiple sheets) and categorizes the individual transactions based on a trained model that I've built up based on manually classifying 3 months of my statements.
2. It constructs a spend cube visualization of the data in the statements in a Jupyter Notebook.
3. It compares monthly spending to an allocated monthly budget.

## Classification

To use the classification model, you will have to follow 4 basic steps

1. Input your credit card and bank account statements into a LibreOffice Calc workbook formatted in the template format [provided in the repository](statement.template.ods).
2. Manually categorize a subset of your statements into a training file. I found that categorizing around 400 transactions was enough to get a decent classification rate.
3. Use the `train.py` file to train the classification model (e.g. `python train.py training.ods`)
4. Use the `classify.py` file to categorize the rest (e.g. `python classify.py 2019.ods`)

The classification tool is far from perfect, but I found verifying and correcting the auto-categorizations to be easier than categorizing everything manually.

## Analysis

## 
