#!/bin/bash

echo '127.0.0.1 elastic.planex.com' >> /etc/hosts
echo '127.0.0.1 mattermost.planex.com' >> /etc/hosts

apt-get install haproxy -y

sudo service haproxy stop

if [[ -f /vagrant/haproxy.cfg ]]; then
	cp /vagrant/haproxy.cfg /etc/haproxy/haproxy.cfg
fi

service haproxy start