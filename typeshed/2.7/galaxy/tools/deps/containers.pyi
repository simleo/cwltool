# Stubs for galaxy.tools.deps.containers (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .container_resolvers.explicit import ExplicitContainerResolver as ExplicitContainerResolver
from .container_resolvers.mulled import BuildMulledContainerResolver as BuildMulledContainerResolver, CachedMulledContainerResolver as CachedMulledContainerResolver, MulledContainerResolver as MulledContainerResolver
from .requirements import ContainerDescription as ContainerDescription
from .requirements import DEFAULT_CONTAINER_RESOLVE_DEPENDENCIES as DEFAULT_CONTAINER_RESOLVE_DEPENDENCIES, DEFAULT_CONTAINER_SHELL as DEFAULT_CONTAINER_SHELL
from ..deps import docker_util as docker_util

log = ...  # type: Any
DOCKER_CONTAINER_TYPE = ...  # type: str
DEFAULT_CONTAINER_TYPE = ...  # type: Any
ALL_CONTAINER_TYPES = ...  # type: Any
LOAD_CACHED_IMAGE_COMMAND_TEMPLATE = ...  # type: str

class ContainerFinder:
    app_info = ...  # type: Any
    container_registry = ...  # type: Any
    def __init__(self, app_info) -> None: ...
    def find_container(self, tool_info, destination_info, job_info): ...

class NullContainerFinder:
    def find_container(self, tool_info, destination_info, job_info): ...

class ContainerRegistry:
    resolver_classes = ...  # type: Any
    enable_beta_mulled_containers = ...  # type: Any
    app_info = ...  # type: Any
    container_resolvers = ...  # type: Any
    def __init__(self, app_info) -> None: ...
    def find_best_container_description(self, enabled_container_types, tool_info): ...

class AppInfo:
    galaxy_root_dir = ...  # type: Any
    default_file_path = ...  # type: Any
    outputs_to_working_directory = ...  # type: Any
    container_image_cache_path = ...  # type: Any
    library_import_dir = ...  # type: Any
    enable_beta_mulled_containers = ...  # type: Any
    containers_resolvers_config_file = ...  # type: Any
    involucro_path = ...  # type: Any
    involucro_auto_init = ...  # type: Any
    def __init__(self, galaxy_root_dir: Optional[Any] = ..., default_file_path: Optional[Any] = ..., outputs_to_working_directory: bool = ..., container_image_cache_path: Optional[Any] = ..., library_import_dir: Optional[Any] = ..., enable_beta_mulled_containers: bool = ..., containers_resolvers_config_file: Optional[Any] = ..., involucro_path: Optional[Any] = ..., involucro_auto_init: bool = ...) -> None: ...

class ToolInfo:
    container_descriptions = ...  # type: Any
    requirements = ...  # type: Any
    env_pass_through = ...  # type: Any
    def __init__(self, container_descriptions: Any = ..., requirements: Any = ...) -> None: ...

class JobInfo:
    working_directory = ...  # type: Any
    job_directory = ...  # type: Any
    tool_directory = ...  # type: Any
    job_directory_type = ...  # type: Any
    def __init__(self, working_directory, tool_directory, job_directory, job_directory_type) -> None: ...

class Container:
    __metaclass__ = ...  # type: Any
    container_id = ...  # type: Any
    app_info = ...  # type: Any
    tool_info = ...  # type: Any
    destination_info = ...  # type: Any
    job_info = ...  # type: Any
    container_description = ...  # type: Any
    def __init__(self, container_id, app_info, tool_info, destination_info, job_info, container_description) -> None: ...
    @property
    def resolve_dependencies(self): ...
    @property
    def shell(self): ...
    def containerize_command(self, command): ...

class DockerContainer(Container):
    def containerize_command(self, command): ...

def docker_cache_path(cache_directory, container_id): ...

CONTAINER_CLASSES = ...  # type: Any

class NullContainer:
    def __init__(self) -> None: ...
    def __nonzero__(self): ...

NULL_CONTAINER = ...  # type: Any