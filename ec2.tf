provider "aws" {
  region = "us-east-1" # Change to your preferred AWS region
}

resource "aws_security_group" "flask_sg" {
  name        = "flask_security_group"
  description = "Security group for Flask API EC2 instance"

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Allowing public access to Flask API
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Allowing SSH access
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Allowing HTTP traffic
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Allowing HTTPS traffic
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"] # Allow all outbound traffic
  }
}

resource "aws_instance" "flask_ec2" {
  ami             = "ami-04b4f1a9cf54c11d0" # Change to the latest Amazon Linux AMI or your preferred AMI
  instance_type   = "t2.micro"
  security_groups = [aws_security_group.flask_sg.name]

  tags = {
    Name = "Flask-API-Server"
  }
}
