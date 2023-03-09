# Change /etc/default/nginx file to increase limit
# current nginx request open files

exec {'nginx limit':
  command => "sed -i 's/15/15000/' /etc/default/nginx ",
  path    => '/usr/bin/:/usr/local/bin/:/bin/'
}
exec {'restart nginx':
  command => 'sudo service nginx restart',
  path    => '/usr/bin/:/usr/local/bin/:/bin/',
  require => Exec['nginx limit']
}
