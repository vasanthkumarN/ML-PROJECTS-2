provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "itsm_ml_app" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  key_name      = var.key_name
  security_groups = [aws_security_group.itsm_sg.name]
  user_data = file("init-script.sh")
}
