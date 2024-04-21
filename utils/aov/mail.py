def findmail(username, database):
    try:
        encoding='utf-8'
        with open(database, 'r', encoding=encoding) as file:
            for line in file:
                line = line.strip()
                if line.startswith(username + ":"):
                    data = line.split(':')
                    if len(data) >= 4:
                        return data[1]
                    else:
                        print(f"Line format is incorrect for line: {line}") 
                        #format is gamertag:email
                        return None
            print(f"Username '{username}' not found in the file.")
            status = 'None found, you can ask staff to run a manual search!'
            return status
    except FileNotFoundError:
        print(f"Database File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    

