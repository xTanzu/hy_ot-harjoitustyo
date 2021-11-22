from dbaos.user_dbao import User_DBAO

def main():
    db = User_DBAO()
    result = db.find_user_by_username("tanzu")
    print(result)

main()