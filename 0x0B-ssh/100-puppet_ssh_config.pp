#client ssh comfiguration file with ssh
file {'~/.ssh/config':
  content=> 'Host *\n      PasswordAuthentication no\n      IdentityFile ~/.ssh/school",
}
