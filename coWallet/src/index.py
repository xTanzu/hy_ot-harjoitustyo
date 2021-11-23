from repositories.user_repository import User_Repository

def main():
    repo = User_Repository()
    result = repo.insert_new_user("tanzu92", "Hitman69!", "Taneli", "Härkönen")
    print(f"insert success: {result}")
    exists = repo.username_exists("tanzu92")
    print(f"exists: {exists}")
    repo.get_user_by_username("tanzu92")

main()