def generate_unique_usernames(usernames):
    username_count = {}
    result = []

    for username in usernames:
        if username not in username_count:
            username_count[username] = 0
            result.append(username)
        else:
            while True:
                new_username = f"{username}{username_count[username]}"
                if new_username not in username_count:
                    result.append(new_username)
                    username_count[new_username] = 0
                    break
                username_count[username] += 1
            username_count[username] += 1
    
    return result

# Example usage:
# usernames = ['ls8150', 'ls8152', 'ls8150', 'ls8151', 'ls8150', 'ls8152', 'ls815', 'ls815', 'ls8150', 'ls8153']
# usernames=['aezakmi','aezakmi1','aezakmi1','aezakmi']
usernames=['ab','ab','ab','ab']
print(generate_unique_usernames(usernames))
# output:
# ['ls8150', 'ls8152', 'ls81500', 'ls8151', 'ls81501', 'ls81520', 'ls815', 'ls8153', 'ls81502', 'ls81530']
# ['aezakmi', 'aezakmi1', 'aezakmi10', 'aezakmi0']