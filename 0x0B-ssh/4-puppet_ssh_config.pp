# Modify client config file
include stdlib

file_line {
  'off_password_auth':
    # makes sure the file is available
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => '    PasswordAuthentication no'
  ;
  'Declare identity file':
    # makes sure the file is available
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => '    IdentityFile ~/.ssh/school'
}
