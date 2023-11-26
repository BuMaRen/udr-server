from subprocess import call

def modify_ftp():
    vsftpd_conf = '/etc/vsftpd.conf'
    content = ''
    with open(vsftpd_conf) as fd:
        content = fd.read(1024*10)
        content = content.replace('#write1_enable=YES', 'write_enable=YES')
        content = content.replace('#anon_upload_enable=YES', 'anon_upload_enable=YES')
        content = content.strip()
    with open(vsftpd_conf, '+w') as fd:
        fd.write(content)

def modify_sftp():
    sshd_config = '/etc/ssh/sshd_config'
    content = ''
    with open(sshd_config) as fd:
        content = fd.read(1024*10)
        content = content.replace('#Port 22', 'Port 22')
        content = content.replace('#AddressFamily any', 'AddressFamily any')
        content = content.replace('#PasswordAuthentication yes', 'PasswordAuthentication yes')
        content = content.strip()
    with open(sshd_config, '+w') as fd:
        fd.write(content)

modify_ftp()
modify_sftp()
print('restart ftp result', call('systemctl restart vsftpd.service', shell=True))
print('restart sftp result', call('/usr/sbin/sshd -D &', shell=True))