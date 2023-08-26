#client ssh comfiguration file with ssh
file {'~/.ssh/config':
  content=> 'Host *      
      PasswordAuthentication no
      IdentityFile ~/.ssh/school',
}
