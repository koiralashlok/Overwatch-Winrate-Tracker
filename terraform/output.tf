output "backend_public_ip" {
  value = aws_instance.backend[0].public_ip
}
