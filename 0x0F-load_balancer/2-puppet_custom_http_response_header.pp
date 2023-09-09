# add redirection and error page
exec { 'add_header';
  command      => 'sudo apt-get -y update;
  sudo apt-get -y  install nginx;
  sudo sed -i '/server_name _;/a \\n\tadd_header X-Served-By $hostname;' /etc/nginx/sites-available/default;
  sudo service nginx restart;',
  provider     => shell,
  refresh only => true,
}
