variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-west-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "ssm_backend_url_key" {
  description = "SSM parameter name for backend URL"
  type        = string
  default     = "/ow_winrate_tracker/backend_url"
  sensitive   = true
}

variable "ssm_debug_mode_key" {
  description = "SSM parameter name for debug mode"
  type        = string
  default     = false
}

variable "ssh_key_name" {
  description = "SSH key name"
  type        = string
  sensitive   = true
}

data "aws_instances" "running_instances" {
  instance_state_names = ["running"]
}

data "aws_ssm_parameter" "ami_id" {
  name = "/ec2/ami"
}

data "aws_security_group" "existing_sg" {
  filter {
    name   = "group-name"
    values = ["OverwatchWinrateTracker"]
  }
}
