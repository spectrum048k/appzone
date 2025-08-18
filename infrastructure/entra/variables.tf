variable "subscription_id" {
  description = "The Azure subscription ID to use for the provider."
  type        = string
}

variable "resource_group_name" {
  description = "The name of the resource group in which to create the managed identity."
  type        = string
  default     = "rg-managed-identities"
}

variable "config_dir" {
  description = "The path to the config directory containing JSON files."
  type        = string
  default     = "../../config"
}
