from nautobot.extras.jobs import IPNetworkVar
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
        """Ensure region and country don't already exist."""
        # Check region
        try:
            region = Location.objects.get(name__iexact=self.region_name, location_type__name="Region")
            raise DesignValidationError(f"A region already exists with the name '{self.region_name}'.")
        except Location.DoesNotExist:
            pass

        # Check country under the region
        try:
            country = Location.objects.get(
                name__iexact=self.country_name.strip(),
                location_type__name="Country",
                parent__name__iexact=self.region_name,
            )
            raise DesignValidationError(f"A country named '{self.country_name}' already exists under region '{self.region_name}'.")
        except Location.DoesNotExist:
            pass

