import subprocess
import platform
import locale


def exec_linux():
    cmd = 'ls /etc/NetworkManager/system-connections'
    wifi_ssids = subprocess.run(cmd, capture_output=True, shell=True)
    list_ssids = wifi_ssids.stdout.decode().split('\n')

    list_cmds = list()

    for i in list_ssids:
        if i != '':
            list_cmds.append(f' "/etc/NetworkManager/system-connections/{i}"')

    cat_cmds = 'sudo cat ' + ' '.join(list_cmds) + ' | grep psk='

    print(
        'Requires sudo permission to read the wifi passwords, '
        + 'if you want you can see the command, [Y]', end=' ')
    if input().lower() == 'y':
        print(f'\n{cat_cmds}\n')

    passwords = subprocess.run(cat_cmds, capture_output=True, shell=True)

    psks = passwords.stdout.decode().split('\n')

    if len(psks) != len(list_cmds):
        print('\nInvalid password!\n')
        return 0

    print('\n    List of Wifi SSIDs with passwords\n')
    for i in zip(list_ssids, psks):
        print(f'\t{i[0]} : {i[1][4:]}')


def exec_windows():
    default_lang = locale.getdefaultlocale()[0]

    KEYWORDS = {
        "fr_FR": ['profil tous les utilisateurs', 'Contenu'],
        "en_GB": ['all user profile', 'Key Content'],
        "en_US": ['all user profile', 'Key Content'],
        "en_IN": ['all user profile', 'Key Content']
    }

    wifi_ssids = subprocess.run(
        'netsh wlan show profile',
        capture_output=True,
        shell=True
    )
    list_ssids = [
        i.strip().lower() for i in wifi_ssids.stdout.decode("ISO-8859-1")
        .split('\r\n')
    ]

    cmds = list()

    for ssid in list_ssids:
        if ssid.startswith(KEYWORDS[default_lang][0]):
            cmds.append(ssid.split(':')[1].strip())

    output = list()
    for cmd in cmds:
        cat_cmd = f'netsh wlan show profile "{cmd}" key=clear'
        cat_cmd = subprocess.run(cat_cmd, capture_output=True, shell=True)
        out = cat_cmd.stdout.decode("ISO-8859-1").split('\r\n')
        for key in out:
            if key.strip().startswith(KEYWORDS[default_lang][1]):
                temp_key = key.split(': ')
                if len(temp_key) == 2:
                    output.append((cmd, temp_key[1]))
                    break
                else:
                    output.append((cmd, ''))
                    break

    print('\n    List of Wifi SSIDs with passwords\n')
    for i in output:
        print(f'\t{i[0]} : {i[1]}')


if __name__ == '__main__':
    current_platform = platform.system().lower()
    if current_platform == 'linux':
        exec_linux()
    elif current_platform == 'windows':
        exec_windows()
    else:
        print('Apologies, only supports Linux and Windows')
