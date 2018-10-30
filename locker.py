import os, secrets, string, recognize

# generate password for encryption
def generate_password():
    alphabet = string.ascii_letters + string.digits
    # create password with 20 symbols
    passwd = ''.join(secrets.choice(alphabet) for i in range(20))
    return passwd

# write password to file
def write_file(passwd):
    os.system('touch pass.txt')
    with open('pass.txt', 'w') as text_file:
        text_file.write(passwd)
        text_file.close()

# read password from file
def read_file():
    with open('pass.txt', 'r') as file:
        data = file.read().replace('\n', '')
    return data

# decode zip file
def decode(filename, passwd):
    ans = int(input('Do you have "unzip" package? [1] you have [2] you do not have (we will install it) \n > '))
    if ans == 1:
        pass
    elif ans == 2:
        print('Enter SUDO password to download "unzip".')
        os.system('sudo apt install unzip')

    os.system('unzip -P {} {}.zip'.format(passwd, filename))
    os.system('rm -r {}.zip'.format(filename))

def encode(filename, passwd):
    ans = int(input('Do you have "zip" package? [1] you have [2] you do not have (we will install it) \n > '))
    if ans == 1:
        pass
    elif ans == 2:
        print('Enter SUDO password to download "zip".')
        os.system('sudo apt install zip')

    # zip folder
    os.system('zip -P {} -r {} {}'.format(passwd, filename, filename))
    # remove unzipped folder
    os.system('rm -r {}'.format(filename))

    print('"{}.zip" is created.'.format(filename))

def run(ans):
    if ans == 1:
        com = input('Enter folder name to protect or "create NEW_FOLDER_NAME" to create new\n > ')

        # if you want to create new folder
        if 'create' in com:
            com = com.split(' ')[1]
            os.system('mkdir {}'.format(com))

        # if directory does not exist
        if not os.path.isdir(com):
            print('Directory "{}" does not exist. EXIT.'.format(com))
            exit(0)

        passwd = ''

        # get image to decode folder later
        if recognize.get_image():
            print('Thank you, continue encoding.')
            # generate password
            passwd = generate_password()

            write_file(passwd)
        else:
            print('Bad image. Can not find face.')
            exit(0)

        # encode folder
        encode(com, passwd)
    elif ans == 2:
        filename = input('Enter .zip file name\n > ')
        if recognize.recognize():
            decode(filename, read_file())

def main():
    ans = int(input('What do you want? [1] encrypt folder, [2] decrypt\n > '))
    run(ans)


if __name__ == '__main__':
    main()