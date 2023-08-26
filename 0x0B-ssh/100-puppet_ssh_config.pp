#config management for ssh config
include stdlib

file_line {'ensure password authentication == no':
  ensure  => present,
  path    => '/root/.ssh/config',
  line    => '      PasswordAuthentication no',
  replace => true,
}

file_line {'check identity file':
  ensure  => present,
  path    => '/root/.ssh/config',
  line    => '      IdentityFile ~/.ssh/school',
  replace => true,
}
