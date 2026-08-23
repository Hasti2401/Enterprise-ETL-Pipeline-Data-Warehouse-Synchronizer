from src.config.settings import settings

print("Stripe key loaded:", bool(settings.stripe_api_key))
print("Salesforce token loaded:", bool(settings.salesforce_access_token))
print("Salesforce URL:", settings.salesforce_instance_url)