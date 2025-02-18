"""Config flow."""
from homeassistant import config_entries

from .const import DOMAIN


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle the configuration steps."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handlde the user initiated configuration step."""
        await self.async_set_unique_id("ha_registry")
        return self.async_create_entry(title="Home Assistant Registry", data={})
