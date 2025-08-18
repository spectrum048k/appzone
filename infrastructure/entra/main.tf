locals {
  config_files = fileset(var.config_dir, "*.json")
  apps = [for f in local.config_files : jsondecode(file("${var.config_dir}/${f}"))]
}

resource "azurerm_user_assigned_identity" "sp" {
  for_each = {
    for app in local.apps :
    "${replace(app.platform, " ", "")}_${replace(app.app_name, " ", "")}_${replace(app.environment, " ", "" )}" => app
  }
  name                = "sp-${replace(each.value.platform, " ", "")}-${replace(each.value.app_name, " ", "")}-${replace(each.value.environment, " ", "")}" 
  location            = each.value.region
  resource_group_name = var.resource_group_name
  tags = {
    deployment = "terraform"
  }
}