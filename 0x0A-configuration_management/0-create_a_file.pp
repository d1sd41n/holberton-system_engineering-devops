# creates a new conf file

file { '/tmp/holberton':
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  ensure  => 'file',
  content => 'I love Puppet'
}
