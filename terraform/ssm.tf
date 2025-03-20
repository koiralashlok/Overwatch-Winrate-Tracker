resource "aws_ssm_parameter" "backend_url" {
  name  = var.ssm_backend_url_key
  type  = "String"
  value = aws_instance.backend[0].public_ip
}
