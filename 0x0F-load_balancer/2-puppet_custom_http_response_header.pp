# add redirection and error page
exec { 'add_header':
  command  => 'apt-get -y update;
  apt-get -y install nginx;
  sed -i \'/server_name _;/a \\n\tadd_header X-Served-By $hostname;\' /etc/nginx/sites-available/default;
  service nginx restart;',
  provider => shell,
}
