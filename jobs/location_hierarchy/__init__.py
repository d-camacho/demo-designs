from nautobot.apps.jobs import register_jobs, IPNetworkVar, StringVar, ObjectVar

from nautobot_design_builder.design_job import DesignJob

from .context import LocationHierarchyContext

from nautobot.dcim.models import LocationType, Location

class LocationHierarchyDesign(DesignJob):
    """Creates a hierarchy of locations so users can nest new sites under."""

    region_type = ObjectVar(
        model=LocationType
    )
    region_name = StringVar(
        label="Region",
        description="Parent Region (e.g., Americas, Europe, etc.)",
    )
    country_name = StringVar(
        label="Country",
        description="Country where sites will be located (e.g., United States)",
    )
    region_prefix = IPNetworkVar(
        label="Region Prefix",
        min_prefix_length=8,
        max_prefix_length=16,
        description="Top-level container prefix (e.g., 10.0.0.0/8)",
    )
    country_prefix = IPNetworkVar(
        label="Country Prefix",
        min_prefix_length=8,
        max_prefix_length=16,
        description="Child container prefix for the country (e.g., 10.1.0.0/12)",
    )
    has_sensitive_variables = False

    class Meta:
        """Pulls information from different files to render design."""
        
        name = "Location Hierarchy Design"
        commit_default = False
        description = "Creates nested location structure with assigned container prefix."
        design_file = "designs/hierarchy_design.yaml.j2"
        context_class = LocationHierarchyContext
        nautobot_version = ">=2"

name = "Builder Designs"
register_jobs(LocationHierarchyDesign)