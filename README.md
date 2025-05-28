# Oracle - Life Expectancy Predictor

Oracle takes in personal attributes like age and gender to magically (using science and extensive research) determine a person's life expectancy. The methods we use to determine these lovely estimates are explained in the subsequent sections.

## Data Sources

We use public data provided by [Stats Canada](https://www150.statcan.gc.ca/n1/en/catalogue/84-537-X) and reference the most up-to-date lifetable.

> [!NOTE]
> Lifetables essentially predict how long a person is expected to live, based on current mortality rates for different age groups. These tables provide age-specific probabilities of death, life expectancy, and survival rates, allowing us to estimate the average remaining years of life for individuals at various ages.

If you are interested how we extract this data using Pandas, you can view the commited [Jupyter notebook](https://github.com/payamyek/oracle/blob/13ecbd2ccf9c50e2eff7dcba799a527559c6a273/notebooks/life_table.ipynb). We essentially take this pre-computed Excel life table and load them into our Python runtime as a Pandas Dataframe.

## Prediction Service

The prediction service is the heart of the system, it makes the predictions ...

With a simple input as such:

```json
{
  "date_of_birth": "2000-04-18",
  "sex": "M",
  "country_code": "CA",
  "smoking_start_date": "2010-04-19",
  "smoking_daily_frequency": 2
}
```

The predictor will output:

```json
{
  "date_of_birth": "2000-04-18",
  "components": [
    {
      "type": "LIFE_TABLE",
      "adjustment": 80.41
    },
    {
      "type": "SMOKING",
      "adjustment": -0.3569482496194825
    }
  ],
  "age": 25,
  "life_expectancy": 80.05305175038052,
  "date_of_death": "2080-04-17",
  "milliseconds_till_death": 1732143131211
}
```

Essentially, it's saying that I'm expected to die on April 17, 2080. The `components` block explains how it got the final result which is the `life_expectancy` scalar value. I lost `0.35` years off my life for smoking 2 cigars starting from the age of 10 (obviously this data is not real ...)

If you are interested in the API specification, please checkout the [API documentation](https://oracle-production.up.railway.app/docs#/).

## Tools

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- Postgres
- Poetry
- Docker

## Research

- Smoking (https://onlinelibrary.wiley.com/doi/10.1111/add.16757)
