resource "azurerm_user_assigned_identity" "sp" {
  name                = local.sp_name
  location            = local.submission.region
  resource_group_name = var.resource_group_name
}

terraform {
  required_version = ">= 1.0.0"
}

locals {
  submission = jsondecode(file("../../submissions/90f491e1-4af9-42e0-955e-34ce21e1ca38.json"))
  sp_name = "sp-${replace(local.submission.platform, " ", "")}-${replace(local.submission.app_name, " ", "")}-${replace(local.submission.environment, " ", "" )}"
}

output "app_name" {
  value = local.submission.app_name
}
