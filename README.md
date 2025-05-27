# Oracle - Life Expectancy Predictor

Oracle takes in personal attributes like age and gender to magically (using science and extensive research) determine a person's life expectancy. The methods we use to determine these lovely estimates are explained in the subsequent sections. 

## Tools

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- Postgres
- Poetry
- Pytest

## Data Sources

We use the publicly available data provided by the [Stats Canada](https://www150.statcan.gc.ca/n1/en/catalogue/84-537-X) and use the most up-to-date lifetables. Lifetables essentially predict how long a person is expected to live, based on current mortality rates for different age groups. These tables provide age-specific probabilities of death, life expectancy, and survival rates, allowing us to estimate the average remaining years of life for individuals at various ages. 

# Research

- Smoking (https://onlinelibrary.wiley.com/doi/10.1111/add.16757)
