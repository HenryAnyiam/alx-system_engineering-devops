#client ssh comfiguration file with ssh
file {'/root/.ssh/config':
  ensure  => file,
  mode    => '0600',
  content => 'Host *      
      PasswordAuthentication no
      IdentityFile ~/.ssh/school
',
}
