# Install nginx web server and configure using puppet
include stdlib

$redirect = "
      location ~/redirect_me {
                              return 301 https://github.com/fashemma007;
                              }
"

# Update apt repositories
exec { 'Update apt library':
  command => 'sudo apt update',
  path    => '/usr/bin/'
}

# Install nginx
package { 'nginx':
  ensure   => 'installed',
}

# Configure nginx and add redirection rule
file_line { 'Add redirect line':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'server_name _;',
  line   => $redirect,
}

# Set index.html content
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Restart nginx service
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
