output "managed_identity_ids" {
  value       = { for k, v in azurerm_user_assigned_identity.sp : k => v.id }
  description = "Map of app IDs to managed identity IDs."
}

output "managed_identity_names" {
  value       = { for k, v in azurerm_user_assigned_identity.sp : k => v.name }
  description = "Map of app IDs to managed identity names."
}

