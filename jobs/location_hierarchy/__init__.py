from nautobot.apps.jobs import register_jobs, IPNetworkVar, StringVar

from nautobot_design_builder.design_job import DesignJob

from .context import LocationHierarchyContext

class LocationHierarchyDesign(DesignJob):
    """Creates a hierarchy of location so users can nest new sites under."""
    
    region_name = StringVar(
        label="Region",
        description="Parent Region i.e. Americas, Europe, etc.",
    )
    country_name = StringVar(
        label="Country",
        description="Country where sites are located.",
    )
    region_prefix=IPNetworkVar(min_prefix_length=8, max_prefix_length=16)
    country_prefix=IPNetworkVar(max_prefix_length=8, max_prefix_lenth=16)
    has_sensitive_variables = False

    class Meta:
        """Pulls information from different files to render design."""
        
        name = "Location Hierarchy Design"
        commit_default = False
        description = "Creates nested location structure with assigned prefix."
        design_file = "designs/hierarchy_design.yaml.j2"
        context_class = LocationHierarchyContext
        nautobot_version = ">=2"

name = "Demo Designs"
register_jobs(LocationHierarchyDesign)