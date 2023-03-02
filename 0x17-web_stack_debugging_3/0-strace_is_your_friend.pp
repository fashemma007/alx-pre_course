# identify bug using strace
$doc_root = '/var/www/html'
$file_to_edit = '/var/www/html/wp-settings.php'

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
#replace line containing "phpp" with "php"
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
