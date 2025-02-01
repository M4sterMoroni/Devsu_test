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
        # Test connection first
        requests.get(url.rstrip('/'))
        
        # Make POST request
        response = requests.post(url, json=payload, headers=headers)
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse and return response
        return response.json()
    
    except requests.exceptions.ConnectionError:
        print("Error: No se puede conectar al servidor. Por favor, verifica que:")
        print("1. El servidor está ejecutándose")
        print("2. La URL es correcta (http://localhost:8000)")
        print("3. El puerto 8000 está disponible y no bloqueado")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error creating user: {e}")
        if hasattr(e.response, 'text'):
            print(f"Error details: {e.response.text}")
        return None

def main():
    # Example usage
    result = create_user("4321", "Carlos Monterroso") 
    
    if result:
        print("User created successfully:")
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
