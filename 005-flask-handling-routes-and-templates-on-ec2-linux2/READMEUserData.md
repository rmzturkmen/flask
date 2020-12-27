UserData:
Fn::Base64:
!Sub |
#! /bin/bash
yum update -y
yum install python3 -y
pip3 install flask
wget https://raw.githubusercontent.com/rmzturkmen/Clarusway-aws-devops-workshop/master/python/hands-on/flask-02-handling-routes-and-templates-on-ec2-linux2/app.py
mkdir templates
cd templates
wget https://raw.githubusercontent.com/rmzturkmen/Clarusway-aws-devops-workshop/master/python/hands-on/flask-02-handling-routes-and-templates-on-ec2-linux2/templates/evens.html
wget https://raw.githubusercontent.com/rmzturkmen/Clarusway-aws-devops-workshop/master/python/hands-on/flask-02-handling-routes-and-templates-on-ec2-linux2/templates/index.html
wget https://raw.githubusercontent.com/rmzturkmen/Clarusway-aws-devops-workshop/master/python/hands-on/flask-02-handling-routes-and-templates-on-ec2-linux2/templates/greet.html
wget https://raw.githubusercontent.com/rmzturkmen/Clarusway-aws-devops-workshop/master/python/hands-on/flask-02-handling-routes-and-templates-on-ec2-linux2/templates/list100.html
cd ..
python3 app.py
