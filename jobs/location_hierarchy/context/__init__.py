from nautobot.extras.jobs import IPNetworkVar
from nautobot.dcim.models import Location
from nautobot.ipam.models import Prefix

from nautobot_design_builder.context import Context
from nautobot_design_builder.errors import DesignValidationError

from netaddr import IPNetwork


class LocationHierarchyContext(Context):
    """Render context for Regions and nested Country"""

    region_name: str
    country_name: str
    region_prefix: IPNetwork
    country_prefix: IPNetwork

    def _validate_region(self):
        try:
            Location.objects.filter(name__iexact=self.region_name).exists()
            raise DesignValidationError(f"Region '{self.region_name}' already exists.")
        except Location.DoesNotExist:
            return

    def _validate_country(self):
        try:
            Location.objects.filter(name__iexact=self.country_name).exists()
            raise DesignValidationError(f"Country '{self.country_name}' already exists.")
        except Location.DoesNotExist:
            return
    
    def _validate_prefix(self):
        try:
            Prefix.objects.filter(prefix=self.region_prefix).exists()
            raise DesignValidationError(f"Prefix {self.region_prefix} already exists.")
        except Prefix.DoesNotExist:
            return 
