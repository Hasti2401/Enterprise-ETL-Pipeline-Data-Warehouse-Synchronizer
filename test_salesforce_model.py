from src.models.salesforce import SalesforceContact


salesforce_data = {
    "Id": "003ABC",
    "FirstName": "John",
    "LastName": "Smith",
    "Email": "john@example.com"
}


contact = SalesforceContact(**salesforce_data)

print("Salesforce contact:")
print(contact)

print("\nAs dictionary:")
print(contact.model_dump())