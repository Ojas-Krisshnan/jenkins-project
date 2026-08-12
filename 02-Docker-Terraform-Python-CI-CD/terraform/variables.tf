variable "aws_region" {
  description = "The AWS region to deploy infrastructure in"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Target deployment environment (e.g. dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "app_name" {
  description = "Name of the application"
  type        = string
  default     = "devops-assignment3-app"
}

variable "container_port" {
  description = "Port exposed by the FastAPI container"
  type        = number
  default     = 8000
}

variable "instance_type" {
  description = "EC2 instance type for application hosting"
  type        = string
  default     = "t3.micro"
}
