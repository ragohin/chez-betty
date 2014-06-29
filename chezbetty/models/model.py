import datetime
from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    Float,
    Text,
    Enum,
    DateTime,
    ForeignKey,
    Boolean
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    validates,
    relationship,
    object_session,
    hybrid_attribute
    )
    
from sqlalchemy.sql.expression import or_

from zope.sqlalchemy import ZopeTransactionExtension

from .history_meta import Versioned, versioned_session

DBSession = versioned_session(scoped_session(sessionmaker(extension=ZopeTransactionExtension())))
Base = declarative_base()
