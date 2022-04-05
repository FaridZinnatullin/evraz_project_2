from typing import List, Optional
import datetime
import attr


@attr.dataclass
class Issue:
    id: Optional[int] = None
    action: Optional[str] = None
    object_type: Optional[str] = None
    object_id: Optional[int] = None
    # created_datetime: datetime.datetime = datetime.datetime.now()

