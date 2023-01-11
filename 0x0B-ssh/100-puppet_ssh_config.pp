# Install puppet standard libs
exec {'install_lib':
  path    => '/usr/bin/',
  command => 'puppet module install puppetlabs-stdlib'
}

# make sure the file is available
file {'/etc/ssh/ssh_config':
      ensure  => present
}
# import stdlib
include stdlib
file_line {'off_password_auth':
    path    => '/etc/ssh/ssh_config',
    line    => '    PasswordAuthentication no',
    require => Exec['install_lib']
}

file_line {'Declare identity file':
    path    => '/etc/ssh/ssh_config',
    line    => '    IdentityFile ~/.ssh/school',
    require => Exec['install_lib']
}
