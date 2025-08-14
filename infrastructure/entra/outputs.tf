output "sp_name" {
  value = local.sp_name
}

output "managed_identity_id" {
  value = azurerm_user_assigned_identity.sp.id
}
