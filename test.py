import requests
import json

def create_user(dni, name):
    # API endpoint URL
    url = "http://localhost:8000/api/users/"
    
    # Request payload
    payload = {
        "dni": dni,
        "name": name
    }
    
    # Headers specifying JSON content
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        # Make POST request
        response = requests.post(url, json=payload, headers=headers)
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse and return response
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error creating user: {e}")
        return None

def main():
    # Example usage
    result = create_user("12345", "John Doe")
    
    if result:
        print("User created successfully:")
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
