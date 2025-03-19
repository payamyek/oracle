# Oracle

Life expectancy predictor.

## API Key Validation

1. Extract from request headers `X-API-KEY` and `X-CLIENT-ID`
2. Get all matching databases row from `ApiKey` table using `X-CLIENT-ID`
3. Loop through all matches and see if there is match hashed api key
4. Compare the request's referer header and the db referer value for equality
5. If all good, allow request to go ahead
