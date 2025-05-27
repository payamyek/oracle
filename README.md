# Oracle - Life Expectancy Predictor

Oracle takes in personal attributes like age and gender to magically (using science and extensive research) determine a person's life expectancy. The methods we use to determine these lovely estimates are explained in the subsequent sections.

## Data Sources

We use publicly available data provided by [Stats Canada](https://www150.statcan.gc.ca/n1/en/catalogue/84-537-X) and reference the most up-to-date lifetable.

> [!NOTE]
> Lifetables essentially predict how long a person is expected to live, based on current mortality rates for different age groups. These tables provide age-specific probabilities of death, life expectancy, and survival rates, allowing us to estimate the average remaining years of life for individuals at various ages.

If you are interested how we extract this data using Pandas, you can view the commited [Jupyter notebook](https://github.com/payamyek/oracle/blob/13ecbd2ccf9c50e2eff7dcba799a527559c6a273/notebooks/life_table.ipynb). We essentially take this precomputed Excel life table and load them into our Python runtime as a Pandas Dataframe.

## Research

- Smoking (https://onlinelibrary.wiley.com/doi/10.1111/add.16757)

## Tools

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- Postgres
- Poetry
- Docker
