import requests

def get_pr_details(repo, pr_number, token):
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
    headers = {"Authorization": f"token {token}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        pr = response.json()
        print(f"Title: {pr['title']}")
        print(f"Author: {pr['user']['login']}")
        print(f"State: {pr['state']}")
        print(f"Created At: {pr['created_at']}")
    else:
        print(f"Failed to fetch PR details: {response.status_code}")

if __name__ == "__main__":
    repo = input("Enter repo (user/repo): ")
    pr_number = input("Enter PR number: ")
    token = input("Enter GitHub token: ")
    get_pr_details(repo, pr_number, token)