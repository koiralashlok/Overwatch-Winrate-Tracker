resource "aws_ssm_parameter" "backend_url" {
  name  = var.ssm_backend_url_key
  type  = "String"
  value = aws_instance.backend[0].public_ip
  overwrite = true
}

resource "aws_ssm_parameter" "debug_mode" {
  name  = var.ssm_debug_mode_key
  type  = "String"
  value = false
  overwrite = true
}