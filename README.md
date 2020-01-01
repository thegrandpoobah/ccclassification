# Household Budgeting Tool

This is a set of tools that we use to classify the transactions in our household bank and credit card statements. It essentially does 3 things:

1. It reads in Bank Account and Credit Card statements formatted in LibreOffice Calc workbooks (with multiple sheets) and categorizes the individual transactions based on a trained model that I've built up based on manually classifying 3 months of my statements.
2. It constructs a spend cube visualization of the data in the statements in a Jupyter Notebook.
3. It compares monthly spending to an allocated monthly budget.

## To get started

Probably the easiest way to get started is by using the [Anaconda](https://www.anaconda.com/) distribution of Python and Jupyter Notebook. Install Anaconda as a first step.

Clone this repository and load the dependencies: `pip install -r requirements.txt`

## Classification

To use the classification model, you will have to follow 4 basic steps

1. Input your credit card and bank account statements into a LibreOffice Calc workbook formatted in the template format [provided in the repository](statement.template.ods).
2. Manually categorize a subset of your statements into a training file. I found that categorizing around 400 transactions was enough to get a decent classification rate.
3. Use the `train.py` file to train the classification model (e.g. `python train.py training.ods`)
4. Use the `classify.py` file to categorize the rest (e.g. `python classify.py 2019.ods`)

The classification tool is far from perfect, but I found verifying and correcting the auto-categorizations to be easier than categorizing everything manually.

## Analysis

Once all the transactions have been classified, you can create a taxonomy of the spend categories. Again, there is [a template provided in the repository](taxonomy.template.json) that you can use as a starting point. But in short, each spend category that you have assigned to your transactions, needs a classification in the JSON file like so:

```js
"id": { /* should match up to a transaction category */
  "name": "Human Readable Category Name", /* what will be displayed in the Jupyter Notebook */
  "parent": "parent_category_id", /* each category can have a parent category if you want to create a hierarchical spend cube */
  "spend": true, /* should this category type be considered spending.. defaults to true, but things like automatic deposits from paystubs or health benefits should be false */
}
```

Once this taxonomy is created, you can use the [provided Jupyter Notebook](analyze.ipynb) to look over your spending across three axis:

1. Month by Month spending across all categories
2. Categorized Spending across the entire time period (i.e. hierarchical spending cube)
3. Spend Breakdown

Just change the files where the Jupyter Notebook is pulling its data from to match the files you have created and go from there.

## Budgeting

You can optionally specify a per month budget for each spend category and the analysis notebook will compute a rolling budget for each month. The budget amount is specified in cents.

```js
"id": { /* should match up to a transaction category */
  "name": "Human Readable Category Name", /* what will be displayed in the Jupyter Notebook */
  "parent": "parent_category_id", /* each category can have a parent category if you want to create a hierarchical spend cube */
  "spend": true, /* should this category type be considered spending.. defaults to true, but things like automatic deposits from paystubs or health benefits should be false */
  "budget": 50000 /* the monthly budget allocated to this category. The number is specified in pennies.
}
```
