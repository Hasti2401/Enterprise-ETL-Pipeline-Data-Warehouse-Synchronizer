from src.models.unified import UnifiedCustomer


customer = UnifiedCustomer(
    source="stripe",
    source_id="cus_001",
    full_name="John Smith",
    email="john@example.com"
)

print(customer)
print(customer.model_dump())