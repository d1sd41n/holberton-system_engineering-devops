# Sky is the limit, let's bring that limit higher

exec {'fix--for-nginx':
    command => "sed -i 's/15/1000/g' /etc/default/nginx",
    path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}

exec {'arestart-nginx':
    command => 'service nginx restart',
    path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}

