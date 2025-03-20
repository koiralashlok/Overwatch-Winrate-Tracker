output "backend_public_ip" {
  value = aws_instance.backend[0].public_ip
}

output "backend_ssm_url" {
  sensitive = true
  value     = aws_ssm_parameter.backend_url.value
}
