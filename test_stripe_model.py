from src.models.stripe import StripeCustomer


stripe_data = {
    "id": "cus_001",
    "name": "John Smith",
    "email": "john@example.com"
}


customer = StripeCustomer(**stripe_data)

print("Stripe customer:")
print(customer)

print("\nAs dictionary:")
print(customer.model_dump())