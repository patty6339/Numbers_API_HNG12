provider "aws" {
  region = "us-east-1" # Change to your preferred AWS region
}

# Create a key pair for SSH access
resource "aws_key_pair" "flask_key" {
  key_name   = "flask-key-pair"          # Name of the key pair
  public_key = file("~/.ssh/id_rsa.pub") # Path to your public key file
}

# Create a security group for the Flask API EC2 instance
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

# Create the EC2 instance
resource "aws_instance" "flask_ec2" {
  ami             = "ami-04b4f1a9cf54c11d0" # Ubuntu 20.04 LTS AMI in us-east-1 (change as needed)
  instance_type   = "t2.micro"
  security_groups = [aws_security_group.flask_sg.name]
  key_name        = aws_key_pair.flask_key.key_name # Associate the key pair with the instance

  tags = {
    Name = "Flask-API-Server"
  }
}

# Output the public IP of the instance
output "instance_public_ip" {
  value = aws_instance.flask_ec2.public_ip
}