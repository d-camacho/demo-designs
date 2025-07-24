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

    
    def validate(self):
            self._validate_region()
            self._validate_country()
            self._validate_prefix()

    def _validate_region(self):
        if Location.objects.filter(name__iexact=self.region_name).exists():
            raise DesignValidationError(f"Region '{self.region_name}' already exists.")

    def _validate_country(self):
        if Location.objects.filter(name__iexact=self.country_name).exist():
            raise DesignValidationError(f"Country '{self.country_name}' already exists.")
    
    def _validate_prefix(self):
        if Prefix.objects.filter(prefix=self.region_prefix).exists():
            raise DesignValidationError(f"Prefix {self.region_prefix} already exists.")
