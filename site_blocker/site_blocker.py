# function for adding a site to the hosts file
def add_domain():
    domain_name = input("Enter the domain of the website to block:")
    with open("c:/Windows/System32/drivers/etc/hosts", "a") as fileHandler:
        fileHandler.write('127.0.0.1 {}'.format(domain_name) + '\n')


# function for removing the domains from the host file
def remove_all_domains():
    all_domains_list = input("Enter the domains to remove separated by space:")
    all_domains = all_domains_list.split(" ")
    with open("c:/Windows/System32/drivers/etc/hosts", 'r+') as f:
        file_contents = f.readlines()
        for each_domain in all_domains:
            for each_line in file_contents:
                if each_domain.strip(" ") in each_line.strip("\n").split(" "):
                    file_contents.pop(file_contents.index(each_line))
                else:
                    pass
        f.seek(0)
        f.truncate()
        f.writelines(file_contents)
        print("All requested sites have been unblocked")


try:
    choice = int(input("Enter 1 to block and 2 to remove a blocked site:"))
    if choice == 1:
        add_domain()
    elif choice == 2:
        remove_all_domains()
    else:
        print("Wrong Choice")
except Exception:
    print("Not a valid choice")
