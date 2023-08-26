#config management for ssh config
include stdlib

file_line {'Turn off passwd auth':
  ensure  => present,
  path    => '/root/ssh/config',
  line    => '      PasswordAuthentication no',
  replace => true,
}

file_line {'Declare identity file':
  ensure  => present,
  path    => '/root/ssh/config',
  line    => '      IdentityFile ~/.ssh/school',
  replace => true,
}
