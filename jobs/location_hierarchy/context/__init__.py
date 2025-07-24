
from nautobot.dcim.models import Location

from nautobot_design_builder.context import Context
from nautobot_design_builder.errors import DesignValidationError

from netaddr import IPNetwork


class LocationHierarchyContext(Context):
    """Render context for Regions and nested Country"""

    region_name: str
    country_name: str
    region_prefix: IPNetwork
    country_prefix: IPNetwork
    

    def validate_new_region_and_country(self):
        """Ensure region and country do not already exist."""
        # Check for existing top-level region; no parent
        try:
            Location.objects.get(name__iexact=self.region_name.strip(), location_type__name="Region")
            raise DesignValidationError(f"A region with the name '{self.region_name}' already exists.")
        except Location.DoesNotExist:
            pass

        # Check country under the region
        try:
            Location.objects.get(
                name__iexact=self.country_name.strip(),
                location_type__name="Country",
                parent__name__iexact=self.region_name.strip(),
            )
            raise DesignValidationError(f"A country named '{self.country_name}' already exists under region '{self.region_name}'.")
        except Location.DoesNotExist:
            pass

