from src.api_extractor import APIExtractor


def main():
    print("=" * 50)
    print("ETL API INTEGRATION")
    print("=" * 50)

    try:
        extractor = APIExtractor()

        # Fetch data from API
        users = extractor.fetch_users()

        # Display number of records
        print(f"\nRecords extracted: {len(users)}")

        # Display sample records
        print("\nSample records:")

        for user in users[:5]:
            print(user.model_dump())

        print("\nAPI extraction completed successfully.")

    except Exception as error:
        print(f"\nAPI extraction failed: {error}")


if __name__ == "__main__":
    main()
