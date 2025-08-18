provider "azurerm" {
  features {}
  subscription_id = var.subscription_id
}

provider "azuread" {
  # Add provider configuration here if needed
}
