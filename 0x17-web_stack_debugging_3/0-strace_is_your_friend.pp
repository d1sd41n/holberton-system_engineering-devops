# fixing apache bug
exec { 'fix_bug':
  command => '/usr/bin/env sed -i "s/phpp/php/g" /var/www/html/wp-settings.php':,
 }
