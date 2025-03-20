resource "aws_instance" "backend" {
  count         = 1
  ami           = data.aws_ssm_parameter.ami_id.value
  instance_type = var.instance_type

  tags = {
    Name = "Backend-EC2"
  }

  lifecycle {
    create_before_destroy = true
  }

  vpc_security_group_ids = [data.aws_security_group.existing_sg.id]
  key_name               = var.ssh_key_name
}
