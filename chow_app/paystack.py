import requests

paystack_api_key = "sk_test_86b1a0b2ba176915fedc133ec4b8e78bc9656079"

paystack_endpoint = "https://api.paystack.co/transaction/initialize"

# Set the transaction parameters
amount = 10000 # Amount in kobo
email = "user@example.com"

# Set the request headers
headers = {
    "Authorization": f"Bearer {paystack_api_key}",
    "Content-Type": "application/json"
}

# Set the request data
data = {
    "amount": amount,
    "email": email
}

# Send the request to the Paystack API
response = requests.post(paystack_endpoint, json=data, headers=headers)

# Extract the payment URL from the response
payment_url = response.json()["data"]["authorization_url"]
