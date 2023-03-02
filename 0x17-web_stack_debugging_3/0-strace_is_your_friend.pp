# identify bug using strace
$doc_root = '/var/www/html'

file { $doc_root:
  ensure => 'directory',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0644'
}

file { "${doc_root}/index.html":
        ensure  => 'present',
        path    => '/var/www/html/index.html',
        content => '<h1>Bug Fixed by fash the great</h1>',
        require => File[$doc_root]
}
