import requests
import time

def check_subdomain_status(subdomain):

    try:
        response = requests.get(f"http://{subdomain}*.com")
        if response.status_code == 200:
            return 'UP'
        else:
            return 'DOWN'
    except requests.ConnectionError:
        return 'DOWN'

def display_status_table(subdomains):

    print("{:<20} {:<10}".format("Subdomain", "Status"))
    print("-" * 30)
    for subdomain in subdomains:
        status = check_subdomain_status(subdomain)
        print("{:<20} {:<10}".format(subdomain, status))

def main():

    subdomains = ['awesomeweb', 'mysite', 'demo']  # Add your subdomains here
    while True:
        display_status_table(subdomains)
        time.sleep(60)  # Sleep for 60 seconds before checking again

if __name__ == "__main__":
    main()
