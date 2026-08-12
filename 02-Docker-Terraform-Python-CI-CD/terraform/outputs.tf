output "environment" {
  description = "Deployed environment name"
  value       = var.environment
}

output "app_name" {
  description = "Application identifier"
  value       = var.app_name
}

output "security_group_id" {
  description = "ID of the created application security group"
  value       = aws_security_group.app_sg.id
}

output "application_endpoint" {
  description = "Constructed public health check endpoint URL"
  value       = "http://${aws_instance.web.public_ip}:${var.container_port}/health"
}

output "instance_public_ip" {
  description = "Public IP address of the provisioned EC2 instance"
  value       = aws_instance.web.public_ip
}
