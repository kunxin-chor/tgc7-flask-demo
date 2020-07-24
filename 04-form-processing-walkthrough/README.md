# Form Processing Practise

## Q1: Check age
Create a route `/ask` that will display a form to ask for the user's age.

In the `POST` version of the route, the code will determine if age is above 21. If so, 
return the string "You are able to vote" or else display "Try again in 5 years time".

## Q2: BMI
Create a route `/bmi` that will display two textfields, one for the weight (in kg) and one for the height (in metres). 

In the POST versin of the route, display the user's BMI.

## Q3: Currency Search

Use a route to display two textboxes and ask the user to enter two currency symbol.

In the POST version of the route, use the https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo API to
retrieve and display the exchange rate.

You need to provide your own api key.